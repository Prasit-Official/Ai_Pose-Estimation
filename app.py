import cv2
import time

from realtime.camera import Camera
from pose.detector import PoseDetector
from pose.extractor import PoseExtractor
from pose.angles import AngleCalculator
from realtime.overlay import Overlay
from pose.utils import PoseUtils


def main():

    camera = Camera()
    detector = PoseDetector()
    extractor = PoseExtractor()
    angles = AngleCalculator()
    overlay = Overlay()
    utils = PoseUtils()

    prev_time = time.time()

    while True:

        frame = camera.read()

        if frame is None:
            break

        h, w = frame.shape[:2]

        # -------------------------
        # 1. Pose Detection
        # -------------------------
        annotated, result = detector.detect(frame)

        # -------------------------
        # 2. Extract Keypoints
        # -------------------------
        persons = extractor.get_keypoints(result)

        if persons is None or len(persons) == 0:

            overlay.draw_text(frame, "No person detected", 20, 60)
            cv2.imshow("AI Lifting Risk Detection", frame)

            if cv2.waitKey(1) == 27:
                break
            continue

        joints = persons[0]

        # -------------------------
        # 3. Validate Pose
        # -------------------------
        if not utils.is_valid_joints(joints):

            overlay.draw_text(frame, "Low confidence pose", 20, 60, (0, 255, 255))
            cv2.imshow("AI Lifting Risk Detection", frame)

            if cv2.waitKey(1) == 27:
                break
            continue

        # -------------------------
        # 4. Calculate Angles
        # -------------------------
        angle_data = angles.calculate_all(joints)

        # -------------------------
        # 5. Simple Risk Logic (Baseline)
        # -------------------------
        back = angle_data["back"]
        knee = min(angle_data["left_knee"], angle_data["right_knee"])

        if back > 60 or knee > 160:
            risk = "DANGER"
        elif back > 40:
            risk = "WARNING"
        else:
            risk = "SAFE"

        # -------------------------
        # 6. Draw Pose (from YOLO output)
        # -------------------------
        frame = annotated

        # -------------------------
        # 7. Overlay Information
        # -------------------------
        overlay.draw_risk_box(frame, risk)
        overlay.draw_angles(frame, angle_data)

        # -------------------------
        # 8. FPS Calculation
        # -------------------------
        curr_time = time.time()
        fps = 1 / (curr_time - prev_time + 1e-6)
        prev_time = curr_time

        overlay.draw_fps(frame, fps)

        # -------------------------
        # 9. Show Frame
        # -------------------------
        cv2.imshow("AI Lifting Risk Detection", frame)

        if cv2.waitKey(1) == 27:
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()