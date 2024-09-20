import cv2

video = cv2.VideoCapture("src/video.mp4")

nr_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
fps = video.get(cv2.CAP_PROP_FPS)

timestamp = input('Enter timestamp in hh:mm:ss format: ')

# timestamp = '00:00:02.75'
timestamp_list = timestamp.split(':')
hh, mm, ss = timestamp_list
timestamp_list_floats = [float(i) for i in timestamp_list]

hours, minuts, seconds = timestamp_list_floats

frame_nr = hours * 3600 * fps + minuts * 60 *  fps + seconds * fps

video.set(1, frame_nr)
success, frame = video.read()
cv2.imwrite(f'Frame at {hh}:{mm}:{ss}.jpg', frame)