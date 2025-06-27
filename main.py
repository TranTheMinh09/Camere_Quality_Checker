import cv2
from camera.quality_check import calculate_sharpness, calculate_brightness

# 🔧 Ngưỡng đánh giá
sharpness_threshold = 120
brightness_low = 50
brightness_high = 200

def open_camera_with_sharpness():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)

        # Tính độ nét và độ sáng
        sharpness = calculate_sharpness(frame)
        brightness = calculate_brightness(frame)

        # 🔹 Hiển thị chỉ số độ nét
        sharpness_text = f"Sharpness: {sharpness:.2f}"
        cv2.putText(frame, sharpness_text, (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        # 🔹 Cảnh báo độ nét
        if sharpness < sharpness_threshold:
            sharpness_status = "⚠ BLURRY IMAGE"
            sharpness_color = (0, 0, 255)  # Red
        else:
            sharpness_status = "✅ SHARP IMAGE"
            sharpness_color = (0, 255, 0)  # Green

        cv2.putText(frame, sharpness_status, (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, sharpness_color, 2)

        # 🔹 Hiển thị độ sáng
        brightness_text = f"Brightness: {brightness:.2f}"
        cv2.putText(frame, brightness_text, (10, 110),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)

        # 🔹 Cảnh báo độ sáng
        if brightness < brightness_low:
            brightness_status = "TOO DARK"
            brightness_color = (0, 0, 255)
        elif brightness > brightness_high:
            brightness_status = "⚠ TOO BRIGHT"
            brightness_color = (0, 0, 255)
        else:
            brightness_status = "BRIGHTNESS OK"
            brightness_color = (0, 255, 0)

        cv2.putText(frame, brightness_status, (10, 150),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, brightness_color, 2)

        # Hiển thị ảnh
        cv2.imshow("Camera Quality Checker", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    open_camera_with_sharpness()
