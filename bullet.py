import pyglet
from PhysicalObject import *
from resources import *


class Bullet(PhysicalObject):
    """Bullets fired by the player"""

    def __init__(self, bullet_x, bullet_y , **kwargs):
        super().__init__(img = bullet, x= bullet_x, y = bullet_y, **kwargs)

        # Bullets shouldn't stick around forever
        pyglet.clock.schedule_once(self.die, 0.5)

        # Flag as a bullet
        self.is_bullet = True

    def die(self, dt):
        self.dead = True