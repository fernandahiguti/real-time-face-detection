# Real-time Face Detection

This project demonstrates real-time face detection using OpenCV in Python. It captures video from your webcam, detects faces in the video feed, overlays a logo on the video, and adds a timestamp with the local timezone. You can also capture and save individual frames with a timestamp.

## Prerequisites

Before running the project, ensure you have the following dependencies installed:

- Python 3.x
- OpenCV (cv2)
- NumPy (np)

You can install OpenCV and NumPy using pip:

```
pip install opencv-python numpy
```

## Getting Started

1. **Clone the Repository**:

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/fernandahiguti/real-time-face-detection.git
   ```

2. **Download the Cascade Classifier File**:

   Download the `haarcascade_frontalface_default.xml` file from the OpenCV GitHub repository [here](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml) and place it in the same directory as your Python script.

3. **Run the Application**:

   Run the Python script to start real-time face detection:

   ```bash
   python main.py
   ```

   - Press 'q' to exit the application.
   - Press 'c' to capture and save the current frame with a timestamp in the output folder.

## Configuration

- You can customize the logo used for overlay by replacing the `your_logo.png` file in the script's directory with your desired logo image.

## Output

Captured images with timestamps will be saved in the `face-detection-captures` directory in the script's directory.

## Acknowledgments

- The `haarcascade_frontalface_default.xml` file used for face detection is from the OpenCV GitHub repository.

## License

This project is licensed under the MIT License.
