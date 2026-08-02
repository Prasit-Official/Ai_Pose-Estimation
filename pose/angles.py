"""
==========================================
Joint Angle Calculation
==========================================
"""

import numpy as np


class AngleCalculator:

    def __init__(self):
        pass

    @staticmethod
    def calculate_angle(a, b, c):
        """
        Calculate angle ABC
        """

        a = np.array(a)
        b = np.array(b)
        c = np.array(c)

        ba = a - b
        bc = c - b

        cosine = np.dot(ba, bc) / (
            np.linalg.norm(ba) * np.linalg.norm(bc) + 1e-6
        )

        cosine = np.clip(cosine, -1.0, 1.0)

        angle = np.degrees(np.arccos(cosine))

        return angle

    @staticmethod
    def point(joints, index):

        return (
            joints[index]["x"],
            joints[index]["y"]
        )

    def knee_angle_left(self, joints):

        hip = self.point(joints, 11)
        knee = self.point(joints, 13)
        ankle = self.point(joints, 15)

        return self.calculate_angle(
            hip,
            knee,
            ankle
        )

    def knee_angle_right(self, joints):

        hip = self.point(joints, 12)
        knee = self.point(joints, 14)
        ankle = self.point(joints, 16)

        return self.calculate_angle(
            hip,
            knee,
            ankle
        )

    def elbow_angle_left(self, joints):

        shoulder = self.point(joints, 5)
        elbow = self.point(joints, 7)
        wrist = self.point(joints, 9)

        return self.calculate_angle(
            shoulder,
            elbow,
            wrist
        )

    def elbow_angle_right(self, joints):

        shoulder = self.point(joints, 6)
        elbow = self.point(joints, 8)
        wrist = self.point(joints, 10)

        return self.calculate_angle(
            shoulder,
            elbow,
            wrist
        )

    def hip_angle_left(self, joints):

        shoulder = self.point(joints, 5)
        hip = self.point(joints, 11)
        knee = self.point(joints, 13)

        return self.calculate_angle(
            shoulder,
            hip,
            knee
        )

    def hip_angle_right(self, joints):

        shoulder = self.point(joints, 6)
        hip = self.point(joints, 12)
        knee = self.point(joints, 14)

        return self.calculate_angle(
            shoulder,
            hip,
            knee
        )

    def back_angle(self, joints):
        """
        Estimate trunk inclination relative to vertical.
        Returns 0° when upright and increases as the trunk leans.
        """

        ls = np.array(self.point(joints, 5))
        rs = np.array(self.point(joints, 6))
        lh = np.array(self.point(joints, 11))
        rh = np.array(self.point(joints, 12))

        shoulder_mid = (ls + rs) / 2
        hip_mid = (lh + rh) / 2

        trunk = shoulder_mid - hip_mid

        vertical = np.array([0.0, -1.0])

        cosine = np.dot(trunk, vertical) / (
            np.linalg.norm(trunk) * np.linalg.norm(vertical) + 1e-6
        )

        cosine = np.clip(cosine, -1.0, 1.0)

        return np.degrees(np.arccos(cosine))

    def calculate_all(self, joints):

        return {

            "back": self.back_angle(joints),

            "left_knee": self.knee_angle_left(joints),

            "right_knee": self.knee_angle_right(joints),

            "left_elbow": self.elbow_angle_left(joints),

            "right_elbow": self.elbow_angle_right(joints),

            "left_hip": self.hip_angle_left(joints),

            "right_hip": self.hip_angle_right(joints)

        }