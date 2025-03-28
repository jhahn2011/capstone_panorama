import cv2

def check_webcams(max_index=10):
    """
    지정된 최대 인덱스까지 연결된 웹캠을 확인하고 인덱스와 연결 여부를 출력합니다.
    """
    for i in range(max_index):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"인덱스 {i}: 웹캠 연결됨")
            cap.release()
    else:
        print(f"인덱스 {i}: 웹캠 연결 안됨")

if __name__ == "__main__":
    check_webcams()