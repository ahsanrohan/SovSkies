import pyglet

class playerPlane():

    def __init__ (self, moveSpeed, health, image):
        self.moveSpeed: moveSpeed
        self.health: health
        self.planeImg = pyglet.image.load(image)

    def getImage(self):
        return self.planeImg
