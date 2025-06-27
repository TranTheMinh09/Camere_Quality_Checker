import cv2
import os
import time
from datetime import datetime

from camera.quality_check import calculate_sharpness, calculate_brightness
from camera.utils import get_next_image_index

# 🔧 Ngưỡng đánh giá
sharpness_threshold = 120
brightness_low = 50
brightness_high = 200
capture_interval = 3  # Giây giữa mỗi lần chụp


def open_camera_with_sharpness():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera.")
        return

    last_capture_time = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)

        sharpness = calculate_sharpness(frame)
        brightness = calculate_brightness(frame)

        cv2.putText(frame, f"Sharpness: {sharpness:.2f}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        if sharpness < sharpness_threshold:
            sharp_status = "BLURRY IMAGE"
            sharp_color = (0, 0, 255)
        else:
            sharp_status = "SHARP IMAGE"
            sharp_color = (0, 255, 0)

        cv2.putText(frame, sharp_status, (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, sharp_color, 2)

        cv2.putText(frame, f"Brightness: {brightness:.2f}", (10, 110),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

        if brightness < brightness_low:
            bright_status = "TOO DARK"
            bright_color = (0, 0, 255)
        elif brightness > brightness_high:
            bright_status = "TOO BRIGHT"
            bright_color = (0, 0, 255)
        else:
            bright_status = "BRIGHTNESS OK"
            bright_color = (0, 255, 0)

        cv2.putText(frame, bright_status, (10, 150),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, bright_color, 2)

        cv2.putText(frame, "Press Q or ESC to exit",
                    (10, frame.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (180, 180, 180), 1)

        cv2.imshow("Camera Quality Checker", frame)

        current_time = time.time()
        if (
            sharpness >= sharpness_threshold
            and brightness_low <= brightness <= brightness_high
            and current_time - last_capture_time > capture_interval
        ):
            if not os.path.exists("captured"):
                os.makedirs("captured")

            index = get_next_image_index()
            filename = f"captured/image_{index:03d}.jpg"
            cv2.imwrite(filename, frame)
            print(f"[✔] Saved: {filename}")
            last_capture_time = current_time

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q") or key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    open_camera_with_sharpness()
