from copy import deepcopy
from pybotics.kinematics.kinematic_pair import KinematicPair
from pybotics.kinematics.mdh_link import MDHLink


class RevoluteMDHLink(MDHLink):
    def __init__(self, alpha, a, theta, d) -> None:
        super().__init__(alpha, a, theta, d)
        self._kinematic_pair = KinematicPair.REVOLUTE

    def displace(self, position=0):
        vector = deepcopy(self.vector)
        vector[2] += position
        return vector
