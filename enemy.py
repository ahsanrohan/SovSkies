import pyglet
import math
import physicalObject, resources

class Enemy(physicalObject.PhysicalObject):
    def __init__ (self, image, health, velocity_x=0.0, velocity_y=0.0, *args, **kwargs):
        super().__init__(image, *args, **kwargs)
        self.health = health
        self.movement = {}
        self.orientation = True
        self.wrap = False
        self.is_enemy = True
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.t = 0

    def move_not(self):
        #default don't move
        pass

    def update(self, dt):
        if (self.health <= 0):
            self.dead = True
            self.visible = False
            self.reacts_to_bullets = False
        getattr(self, self.movement.get('name'))()
        self.t += 1
        super(Enemy, self).update(dt)

    def collides_with(self, other_object):
        return super(Enemy, self).collides_with(other_object)

    def handle_collision_with(self, other_object):
        super(Enemy, self).handle_collision_with(other_object)
    

    def move_ellipse(self):
        a = self.movement.get('a',5)
        b = self.movement.get('b',5)
        speed = self.movement.get('speed', 1)
        #self.x = a*math.cos(.01 * self.t) + self.x
        #self.y = b*math.sin(.01 * self.t) + self.y
        self.velocity_x = speed*a*math.sin(.01 * speed * self.t)
        self.velocity_y = speed*b*math.cos(.01 * speed * self.t)

    def move_sinusoid(self):
        speed = self.movement.get('speed', 1)
        self.velocity_x = speed
        a = self.movement.get('a', 1)
        b = self.movement.get('b', 0.01)
        self.velocity_y = a * math.sin(0.01 * self.t)
    
    def move_parabola(self):
        speed = self.movement.get('speed', 1)
        a = self.movement.get('a', 1)
        self.velocity_x = speed
        self.velocity_y = -0.001*a*speed*self.t   

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
        
