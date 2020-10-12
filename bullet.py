import pyglet
from physicalobject import *
from resources import *


class Bullet(PhysicalObject):
    """Bullets fired by the player"""

    def __init__(self, *args, **kwargs):
        super(Bullet, self).__init__(img=bullet, *args, **kwargs)

        # Bullets shouldn't stick around forever
        pyglet.clock.schedule_once(self.die, 0.5)

        # Flag as a bullet
        self.is_bullet = True

    def die(self, dt):
        self.dead = True