from playerPlane import PlayerPlane
from resources import *


class PlayerPlaneHandler():
    def __init__(self, *args, **kwargs):
        self.activePlane = 1
        self.planes = []
        self.planes.append(PlayerPlane("lightning", 1200, 50, plane_1, [50, -50], **kwargs))
        self.planes.append(PlayerPlane("oldy", 2000, 80, plane_2, [0], **kwargs))
        # self.plane1 = PlayerPlane(1200, 50, plane_1, [50, -50], **kwargs)
        #self.plane2 = PlayerPlane(2000, 80, plane_2, [0], **kwargs)
        # self.planes = [self.plane1, self.plane2]
        self.planes[self.activePlane].visible = True

    def getActivePlane(self):
        return self.planes[self.activePlane]

    def setActivePlane(self, num, currPlane):
        if self.planes[num].user_owns == True:
            self.planes[self.activePlane].visible = False
            self.activePlane = num
            self.planes[self.activePlane].x = currPlane.x
            self.planes[self.activePlane].y = currPlane.y
            self.planes[self.activePlane].visible = True
        else:
            print ("player does not own")

    def getAllPlanes(self):
        return self.planes
