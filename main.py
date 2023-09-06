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

