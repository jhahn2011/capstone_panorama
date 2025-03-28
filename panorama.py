import cv2
import time

# 웹캠 인덱스 설정 (본인 환
# 경에 맞게 수정)
camera_indices = [1, 2, 3, 4]
captures = []

# 각 웹캠 연결 시도
for index in camera_indices:
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        print(f"웹캠 {index}을(를) 열 수 없습니다.")
        exit()
    captures.append(cap)

# Stitcher 객체 생성
stitcher = cv2.Stitcher.create()

while True:
    images = []
    for cap in captures:
        ret, frame = cap.read()
        if not ret:
            print("프레임을 읽을 수 없습니다.")
            break
        # 필요하다면 프레임 크기 조정
        frame = cv2.resize(frame, (640, 480))
        images.append(frame)

    if len(images) == len(camera_indices):
        # 이미지 스티칭 수행
        status, stitched_image = stitcher.stitch(images)

        if status == cv2.STITCHER_OK:
            # 파노라마 이미지 표시
            cv2.imshow("Panorama", stitched_image)
        elif status == cv2.STITCHER_ERR_NEED_MORE_IMGS:
            print("파노라마 생성을 위해 더 많은 이미지가 필요합니다.")
        elif status == cv2.STITCHER_ERR_HOMOGRAPHY_EST_FAIL:
            print("호모그래피 추정 실패.")
        elif status == cv2.STITCHER_ERR_CAMERA_PARAMS_ADJUST_FAIL:
            print("카메라 파라미터 조정 실패.")
        else:
            print(f"스티칭 실패. 상태 코드: {status}")

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 웹캠 리소스 해제
for cap in captures:
    cap.release()
cv2.destroyAllWindows()