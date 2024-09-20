import cv2

video = cv2.VideoCapture("src/video.mp4")
success, frame = (video.read())

count = 1
while success:
    cv2.imwrite(f'images_count/{count}.jpg', frame)
    success, frame = video.read()
    count += 1
