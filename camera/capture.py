import cv2

def open_camera():
    # Mở webcam mặc định
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Không thể mở camera.")
        return

    print("Camera đang chạy... Nhấn 'q' để thoát.")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Không đọc được khung hình.")
            break

        cv2.imshow("", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
