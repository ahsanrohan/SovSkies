import pyglet
import math
import physicalObject, resources

class Enemy(physicalObject.PhysicalObject):
    def __init__ (self, image, health, *args, **kwargs):
        super(Enemy, self).__init__(image, *args, **kwargs)
        self.health = health
        self.kwargs = kwargs
        self.movement = kwargs.get('movement', 'move_not')
        self.orientation = True
        self.is_enemy = True

    def move_not(self):
        #default don't move
        pass
        #test
    def update(self, dt):
        if (self.health <= 0):
            self.dead = True
            self.visible = False
            self.reacts_to_bullets = False
        super(Enemy, self).update(dt)

    def collides_with(self, other_object):
        return super(Enemy, self).collides_with(other_object)

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
        

# enemy
        '''
        test_enemy.velocity_x = 5
        test_enemy.y = 700
        '''
        # sine wave
        '''
        test_enemy.velocity_x = 4
        test_enemy.velocity_y = 100 * math.sin(0.001 * test_enemy.x)
        '''

        # parabola
        '''
        test_enemy.velocity_x = 4
        test_enemy.velocity_y = -0.001 * test_enemy.x * 2
        '''

        # log
        '''
        test_enemy.velocity_x = 4
        test_enemy.y = 800
        test_enemy.velocity_y = 40/(0.01 * test_enemy.x + 1 ) 
        '''

        #circle
        '''
        test_enemy.velocity_y = math.cos(test_enemy.y)
        test_enemy.velocity_x = math.sin(test_enemy.x)
        '''
        