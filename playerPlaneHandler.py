from playerPlane import PlayerPlane
from resources import *


class PlayerPlaneHandler():
    def __init__(self,ownedPlanes, *args, **kwargs):
        self.activePlane = 0

        #self.planes = []
        #for plane in ownedPlanes:
        #    if plane[0] == "fast_plane":
        #        self.planes.append(PlayerPlane("fast_plane", 2000, 30, plane_2, 0.1, 10, "laser",  [0], **kwargs))
        #    if plane[0] == "damage_plane":
        #        self.planes.append(PlayerPlane("damage_plane", 1200, 50, plane_1, 0.1, 10, "fire_rate_increase",  [50, -50], **kwargs))
        #    if plane[0] == "speedy":
        #        self.planes.append(PlayerPlane("helicopter", 1600, 40, plane_2, 0.1, 40, "raming", [0], **kwargs))
        #    if plane[0] == "yourMom":
        #        self.planes.append(PlayerPlane("support_plane", 1200, 80, plane_2,0.1, 20, "revive", [0], **kwargs))

        self.prevPlane = 1
        self.planes = []

        helicopter =   [helicopter_0,
            helicopter_1,
            helicopter_2,
            helicopter_3,
            helicopter_4
        ]
        helicopter_animation = pyglet.image.Animation.from_image_sequence(helicopter, duration= .1, loop=True)
        for plane in ownedPlanes:
            if plane[0] == "fast_plane":
                self.planes.append(PlayerPlane("fast_plane", 2000, 30, plane_2, 1, 0.1, 10, "laser",  [0], **kwargs))
            if plane[0] == "damage_plane":
                self.planes.append(PlayerPlane("damage_plane", 1200, 50, plane_1, 2, 0.1, 10, "fire_rate_increase",  [50, -50], **kwargs))
            if plane[0] == "helicopter":
                self.planes.append(PlayerPlane("helicopter", 1600, 40, helicopter_animation, 3, 0.1, 40, "raming", [0], **kwargs))
            if plane[0] == "support_plane":
                self.planes.append(PlayerPlane("support_plane", 1200, 80, plane_2, 40.1, 20, "revive", [0], **kwargs))
        # self.plane1 = PlayerPlane(1200, 50, plane_1, [50, -50], **kwargs)
        #self.plane2 = PlayerPlane(2000, 80, plane_2, [0], **kwargs)
        # self.planes = [self.plane1, self.plane2]
        self.planes[self.activePlane].visible = True

    def getActivePlane(self):
        return self.planes[self.activePlane]

    def getPlaneByNum(self, number):
        for plane in self.planes:
            if plane.planeNum == number:
                return plane

    def setActivePlane(self, num, currPlane):
        if (len(self.planes) > num):
            if self.getActivePlane().dead == False:
                self.prevPlane = self.activePlane
            if (self.planes[num].dead == False):
                self.planes[self.activePlane].visible = False
                self.activePlane = num
                self.planes[self.activePlane].x = currPlane.x
                self.planes[self.activePlane].y = currPlane.y
                self.planes[self.activePlane].visible = True
            else:
                print('dead plane')
        else:
            print ("player does not own")

    def getAllPlanes(self):
        return self.planes
