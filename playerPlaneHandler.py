from playerPlane import PlayerPlane
from resources import *


class PlayerPlaneHandler():
    def __init__(self, *args, **kwargs):
        self.activePlane = 0
        self.plane1 = PlayerPlane(1200, 50, plane_1, [50, -50], **kwargs)
        self.plane2 = PlayerPlane(2000, 80, plane_2, [0], **kwargs)
        self.plane1.visible = False
        self.plane2.visible = False
        self.planes = [self.plane1, self.plane2]
        self.planes[self.activePlane].visible = True

    def getActivePlane(self):
        return self.planes[self.activePlane]

    def setActivePlane(self, num, currPlane):
        self.planes[self.activePlane].visible = False
        self.activePlane = num
        self.planes[self.activePlane].x = currPlane.x
        self.planes[self.activePlane].y = currPlane.y
        self.planes[self.activePlane].visible = True

    def getAllPlanes(self):
        return self.planes
