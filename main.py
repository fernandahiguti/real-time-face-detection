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

