import pyglet
from physicalObject import *
from resources import *


class Bullet(PhysicalObject):

    def __init__(self, bullet_x, bullet_y , **kwargs):
        super().__init__(img = bullet, x= bullet_x, y = bullet_y, **kwargs)

        # Bullets shouldn't stick around forever
        self.life_time = 2.5
        pyglet.clock.schedule_once(self.die, self.life_time)
        self.damage = 10
        # Flag as a bullet
        self.is_bullet = True
        self.is_enemyBullet = False
        self.wrap = False
        self.decceleration = 0

    '''
    def update(self, dt):
        if self.dead == True:
            print("hi")

    def deccelerate(self):
        bullet_rotation = 90 - self.rotation
        new_bullet.velocity_x -= self.decceleration*math.cos(math.radians(bullet_rotation))
        new_bullet.velocity_y -= self.decceleration*math.sin(math.radians(bullet_rotation))
    '''
    def die(self, dt):
        #print("bullet is dead")
        self.dead = True
        self.visible = False
        #self.delete()