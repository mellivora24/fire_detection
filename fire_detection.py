import cv2
from PyQt5 import QtCore, QtGui
from ultralytics import YOLO

class Fire_smoke_detection(QtCore.QThread):
    model = YOLO('predict.pt')
    cam = cv2.VideoCapture(0)
    color_imageUpdate = QtCore.pyqtSignal(QtGui.QImage)
    gray_imageUpdate = QtCore.pyqtSignal(QtGui.QImage)

    def fire_dectect(self, picSRC):
        pass
    def smoke_detect(self, picSRC):s
        pass

    def run(self):
        self.ThreadActive = True
        while self.ThreadActive:
            ret, frame = self.cam.read()
            frame = cv2.flip(frame, 1)
            if ret:
                results = self.model(frame)
                try:
                    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    annotated_frame = results[0].plot()
                    annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)

                    color_QtFormat = QtGui.QImage(image.data, image.shape[1], image.shape[0],
                                                  QtGui.QImage.Format_RGB888)
                    detect_img = QtGui.QImage(annotated_frame.data, annotated_frame.shape[1], annotated_frame.shape[0], QtGui.QImage.Format_RGB888)

                    color_QtFormat = color_QtFormat.scaled(553, 333, QtCore.Qt.KeepAspectRatio)
                    hsv_QtFormat = detect_img.scaled(553, 333, QtCore.Qt.KeepAspectRatio)

                    self.color_imageUpdate.emit(color_QtFormat)
                    self.gray_imageUpdate.emit(hsv_QtFormat)
                except:
                    print("Crash when processing images.")
    def stop(self):
        self.ThreadActive = False
        if hasattr(self, 'cam'):
            self.cam.release()
        self.quit()


if __name__=="__main__":
    print("This module must call as library.")
