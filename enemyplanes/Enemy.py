import pyglet
import math

class Enemy():
    def __init__ (self, health, image, x, y, dt = 1/60, t = 0, rotation = 0, **kwargs):
        self.health = health
        self.img = pyglet.image.load(image)
        self.x = x
        self.y = y
        self.t = t
        self.dt = 1/60
        self.rotation = rotation
        self.kwargs = kwargs
        self.movement = kwargs.get('movement', 'move_not')

    def get_image(self):
        return self.img

    def get_position(self):
        return self.x, self.y

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def move_not(self):
        #default don't move
        pass
        

    def move_ellipse(self):
        a = self.kwargs.get('a',1)
        b = self.kwargs.get('b',1)
        self.x = a*math.cos(self.dt * self.t) + self.x
        self.y = b*math.sin(self.dt * self.t) + self.y
        self.t += 1

    def move_straight(self):
        direction = self.kwargs.get('direction').lower()
        print(self.x, self.y)
        if not direction:
            raise Exception('no direction specified in moveStraight')
        if direction == "up":
            self.x += 1
        if direction == "down":
            self.x = self.t
        if direction == "left":
            self.y = self.t
        if direction == "right":
            self.y = self.t
        
        