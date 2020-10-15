import pyglet
import math
import physicalObject, resources

class Enemy(physicalObject.PhysicalObject):
    def __init__ (self, image, health, *args, **kwargs):
        super(Enemy, self).__init__(image, *args, **kwargs)
        self.health = health
        self.kwargs = kwargs
        self.movement = kwargs.get('movement', 'move_not')

    def move_not(self):
        #default don't move
        pass
    '''
    def update(self, dt):
        super(Enemy, self).update(dt)
    '''

    
    def handle_collision_with(self, other_object):
        super(Enemy, self).handle_collision_with(other_object)
    

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
        
        