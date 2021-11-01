import cv2

video = cv2.VideoCapture("output.mp4")

while video.isOpened():

    ret, frame = video.read()

    cv2.imshow("Preview", frame)

    if cv2.waitKey() & 0xFFF == ord('q'):
        break

video.release()
