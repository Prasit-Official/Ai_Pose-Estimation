import numpy as np


class PoseExtractor:

    def __init__(self):
        pass

    def get_keypoints(self, result):

        if result.keypoints is None:
            return None

        xy = result.keypoints.xy.cpu().numpy()

        conf = result.keypoints.conf.cpu().numpy()

        persons = []

        for person_xy, person_conf in zip(xy, conf):

            joints = []

            for (x, y), c in zip(person_xy, person_conf):

                joints.append({
                    "x": float(x),
                    "y": float(y),
                    "confidence": float(c)
                })

            persons.append(joints)

        return persons

    def flatten(self, joints):

        feature = []

        for p in joints:

            feature.append(p["x"])
            feature.append(p["y"])
            feature.append(p["confidence"])

        return np.array(feature, dtype=np.float32)