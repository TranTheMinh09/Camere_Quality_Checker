import cv2
import numpy as np

def calculate_sharpness(frame):
    """
    Tính độ nét ảnh bằng phương pháp Laplacian.
    Trả về: giá trị phương sai càng cao càng rõ nét.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    sharpness = laplacian.var()
    return sharpness
