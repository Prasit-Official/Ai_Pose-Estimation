"""
==========================================
Camera Module
==========================================
"""

import cv2
import config


class Camera:

    def __init__(self):

        self.cap = cv2.VideoCapture(config.CAMERA_ID)

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, config.FRAME_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, config.FRAME_HEIGHT)
        self.cap.set(cv2.CAP_PROP_FPS, config.FPS)

        if not self.cap.isOpened():
            raise RuntimeError("Cannot open camera")

    def read(self):

        ret, frame = self.cap.read()

        if not ret:
            return None

        return frame

    def release(self):

        self.cap.release()

    def is_opened(self):

        return self.cap.isOpened()

    def get_size(self):

        width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        return width, height

    def get_fps(self):

        fps = self.cap.get(cv2.CAP_PROP_FPS)

        return fps