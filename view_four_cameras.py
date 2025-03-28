import cv2

# 사용할 웹캠 인덱스 (본인 환경에 맞게 수정)
camera_indices = [1, 2, 3, 4]  # 예시: 실제 확인한 인덱스로 변경하세요

captures = []
window_names = []

for index in camera_indices:
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        print(f"웹캠 {index}을(를) 열 수 없습니다.")
    else:
        captures.append(cap)
        window_names.append(f"Camera {index}")

while True:
    for i in range(len(captures)):
        ret, frame = captures[i].read()
        if ret:
            cv2.imshow(window_names[i], frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 웹캠 리소스 해제
for cap in captures:
    cap.release()
cv2.destroyAllWindows()