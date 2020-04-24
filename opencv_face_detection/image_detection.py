import cv2, time
import numpy as np
video = cv2.VideoCapture(0)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, 500)
video.set(cv2.CAP_PROP_FRAME_WIDTH, 750)
face_detection_cascade = cv2.CascadeClassifier('./opencv_haarcascade_data/haarcascade_frontalface_default.xml')
person_list=[]
while True:
	check, frame = video.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#gray = cv2.GaussianBlur(gray,(21,21),0)

	faces_detected = face_detection_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
	for (x, y, w, h) in faces_detected:
		cv2.rectangle(frame, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=2)
	# Fliping the image as said in question
	print(faces_detected.shape)
	face_count = str(len(faces_detected))
	person_list.append(face_count)
	person_list = list(set(person_list))
	frame_flip = cv2.flip(frame,1)

	# Combining the two different image frames in one window
	# combined_window = np.hstack([frame,frame_flip])

	# Displaying the single window
	# cv2.imshow("Combined videos ",combined_window)
	cv2.imshow("Frame", frame_flip)
	key = cv2.waitKey(1)
	if key == ord("q"):
		break
	if not check:
		break
print(max(person_list))
video.release()
cv2.destroyAllWindows()