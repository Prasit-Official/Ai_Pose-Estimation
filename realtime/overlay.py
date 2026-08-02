"""
==========================================
Overlay Drawing Module
==========================================
"""

import cv2
import config


class Overlay:

    def __init__(self):
        pass

    def draw_text(self, frame, text, x, y, color=(255, 255, 255)):

        cv2.putText(
            frame,
            text,
            (x, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            config.FONT_SCALE,
            color,
            config.LINE_THICKNESS,
            cv2.LINE_AA
        )

    def draw_risk_box(self, frame, risk_level):

        if risk_level == "SAFE":
            color = config.SAFE_COLOR

        elif risk_level == "WARNING":
            color = config.WARNING_COLOR

        else:
            color = config.DANGER_COLOR

        h, w = frame.shape[:2]

        cv2.rectangle(frame, (10, 10), (w - 10, h - 10), color, 3)

        self.draw_text(frame, f"RISK: {risk_level}", 20, 40, color)

    def draw_angles(self, frame, angles):

        y = 80

        for key, value in angles.items():

            text = f"{key}: {value:.1f} deg"

            self.draw_text(frame, text, 20, y)

            y += 30

    def draw_fps(self, frame, fps):

        self.draw_text(frame, f"FPS: {fps:.1f}", 20, frame.shape[0] - 20)