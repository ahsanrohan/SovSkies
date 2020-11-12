import pyglet
from physicalObject import *
from resources import *


class Bullet(PhysicalObject):
    """Bullets fired by the player"""

    def __init__(self,image, bullet_x, bullet_y, bullet_damage , **kwargs):
        super().__init__(img = image, x= bullet_x, y = bullet_y, **kwargs)

        # Bullets shouldn't stick around forever
        pyglet.clock.schedule_once(self.die, 1.5)
        self.damage = bullet_damage
        # Flag as a bullet
        self.is_bullet = True
        self.die_on_impact = True
    # def update(self, dt):
    #     if self.dead == True:
    #         print("hi")

    def die(self, dt):
        #print("bullet is dead")
        self.dead = True
        self.visible = False
        #self.delete()