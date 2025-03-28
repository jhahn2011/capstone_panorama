import cv2

def view_camera(index):
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        print(f"웹캠 {index}을(를) 열 수 없습니다.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print(f"웹캠 {index}에서 프레임을 읽을 수 없습니다.")
            break

        cv2.imshow(f"Camera {index}", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # 확인하고 싶은 웹캠 인덱스를 여기에 입력하세요
    camera_index_to_view = 4
    view_camera(camera_index_to_view)