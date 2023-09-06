import cv2
import numpy as np
import os
from datetime import datetime
import pytz
import tzlocal

def load_logo(logo_path):
    if os.path.exists(logo_path):
        logo = cv2.imread(logo_path, cv2.IMREAD_UNCHANGED)
        logo = cv2.resize(logo, (36, 36))
        return logo
    else:
        return create_placeholder_logo()

def create_placeholder_logo():
    logo = np.ones((36, 36, 4), dtype=np.uint8) * 192 
    return logo

def add_margin(image, margin):
    if image.shape[2] == 4:
        return np.zeros((image.shape[0] + 2 * margin, image.shape[1] + 2 * margin, 4), dtype=np.uint8)
    else:
        return np.zeros((image.shape[0] + 2 * margin, image.shape[1] + 2 * margin, 3), dtype=np.uint8)

def capture_and_save(frame, output_folder):
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    file_name = os.path.join(output_folder, f'captured_image_{timestamp}.png')
    cv2.imwrite(file_name, frame)
    print(f'Image saved as {file_name}')

def add_datetime_overlay(frame, margin=10):
    local_timezone = tzlocal.get_localzone()
    current_time = datetime.now(local_timezone).strftime('%Y-%m-%d %H:%M:%S')

    datetime_text = f'{current_time} {local_timezone}'

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.5
    font_color = (255, 255, 255) 
    thickness = 1
    text_size = cv2.getTextSize(datetime_text, font, font_scale, thickness)[0]
    text_x = frame.shape[1] - text_size[0] - margin
    text_y = frame.shape[0] - margin
    cv2.putText(frame, datetime_text, (text_x, text_y), font, font_scale, font_color, thickness)

def main():
    face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    logo = load_logo('your_logo.png')  # Replace 'your_logo.png' with your logo's filename
    margin = 10

    script_dir = os.path.dirname(os.path.abspath(__file__))  
    output_folder = os.path.join(script_dir, 'face-detection-captures')  

    os.makedirs(output_folder, exist_ok=True)

    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        logo_x = margin
        logo_y = margin

        alpha_channel = None
        if logo.shape[2] == 4:
            alpha_channel = logo[:, :, 3]

        for c in range(0, 3):
            frame[logo_y:logo_y + logo.shape[0], logo_x:logo_x + logo.shape[1], c] = \
                frame[logo_y:logo_y + logo.shape[0], logo_x:logo_x + logo.shape[1], c] * \
                (1 - alpha_channel / 255.0) + logo[:, :, c] * (alpha_channel / 255.0) if alpha_channel is not None else logo[:, :, c]

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 0)

        add_datetime_overlay(frame, margin)

        cv2.imshow('Video Face Detection', frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('c'):
            capture_and_save(frame, output_folder)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()