import pyglet
import math
from bullet import *
from physicalObject import *
from resources import *


class PlayerPlane(PhysicalObject):
    def __init__(self,name, moveSpeed, health, image, shoot_speed, arr, **kwargs):
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

        self.wrap = False
        self.bind = True
        # Player should not collide with own bullets
        self.reacts_to_bullets = False
        self.scale = 0.7
        self.shoot_speed = shoot_speed
        self.could_shoot = True

        self.progress_circle_images =   [progress_circle_0,
                    progress_circle_1,
                    progress_circle_2,
                    progress_circle_3,
                    progress_circle_4,
                    progress_circle_5,
                    progress_circle_6,
                    progress_circle_7,
                    progress_circle_8]

        self.progress_circle = pyglet.image.Animation.from_image_sequence(self.progress_circle_images, duration=self.shoot_speed, loop=False)

    def getImage(self):
        return self.planeImg


    def enableShoot(self, dt):
        self.could_shoot = True

    def fire(self, mouse_x, mouse_y):

        if(self.could_shoot):
            
            self.could_shoot = False
            pyglet.clock.schedule_once(self.enableShoot, self.shoot_speed * 8)
            progress_circle_sprite = pyglet.sprite.Sprite(self.progress_circle, x = 50, y = 50,
                                                    batch=self.batch,
                                                    group=self.group)

            # print("mosue x is: " + str(mouse_x))
            # print("mouse y is: " + str(mouse_y))
            # print("plane x is: " + str(self.x))
            # print("plane y is: " + str(self.y))
            # print("diff x is: " +str(mouse_x - self.x))
            xdiff = mouse_x - self.x
            # print("diff y is: " +str(mouse_y - self.y))
            ydiff = mouse_y - self.y

            print("math: " + str(- (180-math.radians(math.degrees(math.atan(xdiff/ydiff)) + 270))))
            # print("FIRE")
            # print(self.x)
            # print(self.moveSpeed)
            # Note: pyglet's rotation attributes are in "negative degrees"
            if (ydiff > 0):
                angle_radians = -math.radians(math.degrees(math.atan(xdiff/ydiff)) + 270)
            else:
                angle_radians = math.radians(-(math.degrees(math.atan(xdiff/ydiff)) + 90))
            
            angle_radians = -math.radians(270)
            #print(self.shootVec)
            # Create a new bullet just in front of the player
            ship_radius = self.planeImg.width / 2
            for shootSlot in self.shootVec:
                bullet_x = self.x + shootSlot #* ship_radius #+ math.cos(angle_radians) * ship_radius
                bullet_y = self.y #* ship_radius #+ math.sin(angle_radians) * ship_radius
                new_bullet = Bullet(bullet_x, bullet_y, batch = self.batch, group=self.group)

            # Give it some speed
                bullet_vx = math.cos(angle_radians) * self.bullet_speed
                bullet_vy = math.sin(angle_radians) * self.bullet_speed
                new_bullet.velocity_x, new_bullet.velocity_y = bullet_vx, bullet_vy
                new_bullet.wrap = False
            # Add it to the list of objects to be added to the game_objects list
                self.new_objects.append(new_bullet)


