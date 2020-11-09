from playerPlane import PlayerPlane
from resources import *


class PlayerPlaneHandler():
    def __init__(self,ownedPlanes, *args, **kwargs):
        self.activePlane = 0
        self.planes = []
        for plane in ownedPlanes:
            if plane[0] == "fast_plane":
                self.planes.append(PlayerPlane("fast_plane", 2000, 30, plane_2, 0.1, 10, "laser",  [0], **kwargs))
            if plane[0] == "damage_plane":
                self.planes.append(PlayerPlane("damage_plane", 1200, 50, plane_1, 0.1, 10, "fire_rate_increase",  [50, -50], **kwargs))
            if plane[0] == "speedy":
                self.planes.append(PlayerPlane("helicopter", 1600, 40, plane_2, 0.1, 40, "raming", [0], **kwargs))
            if plane[0] == "yourMom":
                self.planes.append(PlayerPlane("support_plane", 1200, 80, plane_2,0.1, 20, "revive", [0], **kwargs))
        # self.plane1 = PlayerPlane(1200, 50, plane_1, [50, -50], **kwargs)
        #self.plane2 = PlayerPlane(2000, 80, plane_2, [0], **kwargs)
        # self.planes = [self.plane1, self.plane2]
        self.planes[self.activePlane].visible = True

    def getActivePlane(self):
        return self.planes[self.activePlane]

    def setActivePlane(self, num, currPlane):
        if len(self.planes) > num:
            self.planes[self.activePlane].visible = False
            self.activePlane = num
            self.planes[self.activePlane].x = currPlane.x
            self.planes[self.activePlane].y = currPlane.y
            self.planes[self.activePlane].visible = True
        else:
            print ("player does not own")

    def getAllPlanes(self):
        return self.planes
