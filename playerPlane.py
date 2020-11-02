import pyglet
import math
from bullet import *
from physicalObject import *
from resources import *


class PlayerPlane(PhysicalObject):
    def __init__(self,name, moveSpeed, health, image, shoot_speed, special_ability, arr, **kwargs):
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
        

        self.has_special_ability = True
        self.special_ability = special_ability
        self.special_ability_shoot_speed = .2
        self.could_shoot_special_ability = True

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
        
        self.blue_progress_circle_images =   [blue_progress_circle_0,
                    blue_progress_circle_1,
                    blue_progress_circle_2,
                    blue_progress_circle_3,
                    blue_progress_circle_4,
                    blue_progress_circle_5,
                    blue_progress_circle_6,
                    blue_progress_circle_7,
                    blue_progress_circle_8]

        self.blue_progress_circle = pyglet.image.Animation.from_image_sequence(self.blue_progress_circle_images, duration=self.special_ability_shoot_speed, loop=False)
    def getImage(self):
        return self.planeImg


    def enableShoot(self, dt):
        self.could_shoot = True

    def enableSpecialAbilityShoot(self, dt):
        self.could_shoot_special_ability = True

    def revert_fire_rate_increase(self, dt, previous_rate):
        self.shoot_speed = previous_rate
        self.progress_circle = pyglet.image.Animation.from_image_sequence(self.progress_circle_images, duration=self.shoot_speed, loop=False)

    def fire(self, mouse_x, mouse_y):

        if(self.could_shoot):
            
            self.could_shoot = False
            pyglet.clock.schedule_once(self.enableShoot, self.shoot_speed * 8)
            progress_circle_sprite = pyglet.sprite.Sprite(self.progress_circle, x = 61, y = 61,
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
                new_bullet = Bullet(bullet, bullet_x, bullet_y, batch = self.batch, group=self.group)

            # Give it some speed
                bullet_vx = math.cos(angle_radians) * self.bullet_speed
                bullet_vy = math.sin(angle_radians) * self.bullet_speed
                new_bullet.velocity_x, new_bullet.velocity_y = bullet_vx, bullet_vy
                new_bullet.wrap = False
            # Add it to the list of objects to be added to the game_objects list
                self.new_objects.append(new_bullet)
    
    def specialAbilityFire(self, mouse_x, mouse_y):
        if self.has_special_ability:
            if(self.could_shoot_special_ability):
                self.could_shoot_special_ability = False
                pyglet.clock.schedule_once(self.enableSpecialAbilityShoot, self.special_ability_shoot_speed * 8)

                progress_circle_sprite = pyglet.sprite.Sprite(self.blue_progress_circle, x = 61, y = 61,
                                        batch=self.batch,
                                        group=self.group)
                print(self.special_ability)
                if self.special_ability == "laser":
                    print("laser")
                    new_bullet = Bullet(laser, self.x, self.y, batch = self.batch, group=self.group)
                    angle_radians = -math.radians(270)
                    bullet_vx = math.cos(angle_radians) * 0
                    bullet_vy = math.sin(angle_radians) * 0
                    new_bullet.velocity_x, new_bullet.velocity_y = bullet_vx, bullet_vy
                    new_bullet.wrap = False
                    self.new_objects.append(new_bullet)
                if self.special_ability == "fire_rate_increase":
                    print("got here")
                    pyglet.clock.schedule_once(self.revert_fire_rate_increase, self.special_ability_shoot_speed * 2,  self.shoot_speed)
                    self.shoot_speed = self.shoot_speed/10
                    self.progress_circle = pyglet.image.Animation.from_image_sequence(self.progress_circle_images, duration=self.shoot_speed, loop=False)
                    print("fire_rate_increse")
                if self.special_ability == "raming":
                    print("raming")


        


