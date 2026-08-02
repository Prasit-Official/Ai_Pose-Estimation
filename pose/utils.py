"""
==========================================
Pose Utilities
==========================================
"""

import numpy as np


class PoseUtils:

    def __init__(self):
        pass

    @staticmethod
    def is_valid_joints(joints, min_conf=0.3):
        """
        ตรวจสอบว่าคนนี้ pose ใช้ได้ไหม
        """

        if joints is None:
            return False

        if len(joints) < 17:
            return False

        valid_points = 0

        for j in joints:
            if j["confidence"] >= min_conf:
                valid_points += 1

        return valid_points >= 10

    @staticmethod
    def get_midpoint(p1, p2):
        """
        จุดกึ่งกลาง
        """

        return (
            (p1[0] + p2[0]) / 2,
            (p1[1] + p2[1]) / 2
        )

    @staticmethod
    def euclidean_distance(p1, p2):
        """
        ระยะทาง 2 จุด
        """

        return float(np.linalg.norm(np.array(p1) - np.array(p2)))

    @staticmethod
    def normalize_keypoints(joints, width, height):
        """
        normalize ค่าให้อยู่ 0–1
        """

        normalized = []

        for j in joints:

            normalized.append({
                "x": j["x"] / width,
                "y": j["y"] / height,
                "confidence": j["confidence"]
            })

        return normalized