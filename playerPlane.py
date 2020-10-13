import pyglet
import math
from bullet import *
from physicalobject import *
from resources import *


class PlayerPlane(PhysicalObject):
    def __init__(self, moveSpeed, health, image, **kwargs):
        super().__init__(img = image, **kwargs)
   # def __init__(self, *args, **kwargs):
        self.moveSpeed: moveSpeed
        self.health: health
        self.planeImg = image
        self.bullet_speed = 700.0
        self.new_objects = []

        # Player should not collide with own bullets
        self.reacts_to_bullets = False

    def getImage(self):
        return self.planeImg

    def fire(self):
            print("FIRE")
            print(self.x)
            # Note: pyglet's rotation attributes are in "negative degrees"
            angle_radians = -math.radians(0)

            # Create a new bullet just in front of the player
            ship_radius = self.planeImg.width / 2
            bullet_x = self.x #+ math.cos(angle_radians) * ship_radius
            bullet_y = self.y #+ math.sin(angle_radians) * ship_radius
            new_bullet = Bullet(bullet_x, bullet_y, batch = self.batch)

            # Give it some speed
            bullet_vx = math.cos(angle_radians) * self.bullet_speed
            bullet_vy = math.sin(angle_radians) * self.bullet_speed
            new_bullet.velocity_x, new_bullet.velocity_y = bullet_vx, bullet_vy

            # Add it to the list of objects to be added to the game_objects list
            self.new_objects.append(new_bullet)
