import sys
import cv2
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import Slot, QTimer
from PySide2.QtGui import QImage, QPixmap
from gui.faceDetectionUI import Ui_MainWindow


class MainAppWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.webcam_frame = None
        self.processed_webcam_frame = None
        self.face_detection_enabled = False
        # Load the haarcascade classifier file for face detection
        self.face_detection_cascade = cv2.CascadeClassifier(
            './opencv_haarcascade_data/haarcascade_frontalface_default.xml')
        self.timer = QTimer(self)
        self.startWebcamButton.clicked.connect(self.start_webcam_clicked)
        self.stopWebcamButton.clicked.connect(self.stop_webcam_clicked)
        self.faceDetectionButton.setCheckable(True)
        self.faceDetectionButton.toggled.connect(self.face_detection_clicked)
        # Connect the timeout signal from the QTimer instance to a slot.
        self.timer.timeout.connect(self.update_webcam_frame)

    @Slot()
    def face_detection_clicked(self, button_status):
        if button_status:
            self.faceDetectionButton.setText('Stop Face Detection')
            self.face_detection_enabled = True
        else:
            self.faceDetectionButton.setText('Start Face Detection')
            self.face_detection_enabled = False

    @Slot()
    def update_webcam_frame(self):
        '''
        Updates the webcam frame every time the timeout signal of the QTimer instance is called.
        Checks whether the QPushButton instance for Face Detection is clicked to implement or stop
        the Face Detection on the webcam feed.
        '''
        ret, self.webcam_frame = self.capture.read()
        self.webcam_frame = cv2.flip(self.webcam_frame, 1)
        self.processed_webcam_frame = self.webcam_frame.copy()
        if self.face_detection_enabled:
            self.webcam_face_detection()
            self.display_webcam_feed()
        else:
            self.display_webcam_feed()

    def webcam_face_detection(self):
        '''
        Applies the opencv haarcascade classifier to detect faces within a frame from webcam video feed.
        :param webcam_frame: A frame from the wecam video feed.
        '''
        grayscale_frame = cv2.cvtColor(self.processed_webcam_frame, cv2.COLOR_BGR2GRAY)
        faces_detected = self.face_detection_cascade.detectMultiScale(grayscale_frame, scaleFactor=1.3, minNeighbors=5)
        for (x, y, w, h) in faces_detected:
            cv2.rectangle(self.processed_webcam_frame, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=2)

    def display_webcam_feed(self):
        '''
        Displays the frame in the QLabel instance.
        '''
        frame_format = None
        if 3 <= len(self.processed_webcam_frame.shape) <= 4:
            if len(self.processed_webcam_frame.shape) == 4:
                frame_format = QImage.Format_RGBA8888
            if len(self.processed_webcam_frame.shape) == 3:
                frame_format = QImage.Format_RGB888
        if len(self.processed_webcam_frame.shape) == 2:
            frame_format = QImage.Format_Grayscale8

        output_webcam_frame = QImage(self.processed_webcam_frame,
                                     self.processed_webcam_frame.shape[1],
                                     self.processed_webcam_frame.shape[0],
                                     self.processed_webcam_frame.strides[0],
                                     frame_format)
        output_webcam_frame = output_webcam_frame.rgbSwapped()
        self.webcamFeedLabel.setPixmap(QPixmap.fromImage(output_webcam_frame))
        self.webcamFeedLabel.setScaledContents(True)

    @Slot()
    def start_webcam_clicked(self):
        '''
        Starts the default webcam and update the webcam frame.
        '''
        self.capture = cv2.VideoCapture(0)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 526)
        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 782)
        # Starts the QTimer instance with specific interval.
        self.timer.start(5)

    @Slot()
    def stop_webcam_clicked(self):
        '''
        Stops the QTimer instance and releases the webcam instance that was being used.
        '''
        self.timer.stop()
        self.capture.release()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainAppWindow = MainAppWindow()
    mainAppWindow.show()
    sys.exit(app.exec_())
