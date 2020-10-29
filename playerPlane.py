import pyglet
import math
from bullet import *
from physicalObject import *
from resources import *


class PlayerPlane(PhysicalObject):
    def __init__(self,name, moveSpeed, health, image, arr, **kwargs):
        super().__init__(img = image, **kwargs)
   # def __init__(self, *args, **kwargs):
        self.name = name
        self.user_owns = True
        self.moveSpeed = moveSpeed
        self.health = health
        self.planeImg = image
        self.bullet_speed = 10
        self.new_objects = []
        self.shootVec = arr
        self.visible = False
        self.damageable = True

        self.wrap = False
        self.bind = True
        # Player should not collide with own bullets
        self.reacts_to_bullets = False
        self.reacts_to_enemy_bullets = True
        self.scale = 0.7

    def getImage(self):
        return self.planeImg

    def fire(self, mouse_x, mouse_y):
            xdiff = mouse_x - self.x
            # print("diff y is: " +str(mouse_y - self.y))
            ydiff = mouse_y - self.y

            # Note: pyglet's rotation attributes are in "negative degrees"
            if (ydiff > 0):
                angle_radians = -math.radians(math.degrees(math.atan(xdiff/ydiff)) + 270)
            else:
                angle_radians = math.radians(-(math.degrees(math.atan(xdiff/ydiff)) + 90))
            #print(self.shootVec)
            # Create a new bullet just in front of the player
            ship_radius = self.planeImg.width / 2
            for shootSlot in self.shootVec:
                bullet_x = self.x + shootSlot #* ship_radius #+ math.cos(angle_radians) * ship_radius
                bullet_y = self.y #* ship_radius #+ math.sin(angle_radians) * ship_radius
                new_bullet = Bullet(bullet_x, bullet_y + 5, batch = self.batch)

            # Give it some speed
                bullet_vx = 0 #math.cos(angle_radians) * self.bullet_speed
                bullet_vy = self.bullet_speed #math.sin(angle_radians) * self.bullet_speed
                new_bullet.velocity_x, new_bullet.velocity_y = bullet_vx, bullet_vy
                new_bullet.wrap = False
            # Add it to the list of objects to be added to the game_objects list
                self.new_objects.append(new_bullet)

    def collides_with(self, other_object):

        return super(PlayerPlane, self).collides_with(other_object)

    def handle_collision_with(self, other_object):
        self.damageable = False
        pyglet.clock.schedule_once(self.revert_damageable, 0.5)
        super(PlayerPlane, self).handle_collision_with(other_object)

    def revert_damageable(self, dt):
        self.damageable = True

    #def update(self):
        #if (self.health <= 0):
            #print('plane die')
            #self.dead = True
            #self.destroyed = True
            #self.visible = False
            #self.reacts_to_bullets = False
