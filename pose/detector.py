from ultralytics import YOLO

import config


class PoseDetector:

    def __init__(self):

        self.model = YOLO(str(config.YOLO_MODEL))

    def detect(self, frame):

        results = self.model.predict(
            frame,
            conf=config.POSE_CONFIDENCE,
            iou=config.POSE_IOU,
            verbose=False
        )

        annotated = results[0].plot()

        return annotated, results[0]