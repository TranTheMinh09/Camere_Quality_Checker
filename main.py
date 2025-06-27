import cv2
from camera.quality_check import calculate_sharpness

# 🔧 Ngưỡng sharpness để đánh giá mờ / nét
sharpness_threshold = 120

def open_camera_with_sharpness():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Không thể mở camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)

        sharpness = calculate_sharpness(frame)

        # Hiển thị chỉ số độ nét
        text = f"Sharpness: {sharpness:.2f}"
        cv2.putText(frame, text, (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        # ⚠️ Cảnh báo mờ / nét
        if sharpness < sharpness_threshold:
            status = "BLURRY IMAGE"
            color = (0, 0, 255)  # đỏ
        else:
            status = "SHARP IMAGE"
            color = (0, 255, 0)  # xanh

        cv2.putText(frame, status, (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        cv2.imshow("Camera - Sharpness", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    open_camera_with_sharpness()
