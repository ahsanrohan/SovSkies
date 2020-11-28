import pyglet
import math
from bullet import *
from physicalObject import *
from resources import *
import random


class PlayerPlane(PhysicalObject):

    # def __init__(self,name, moveSpeed, health, image, shoot_speed, collision_damage, special_ability, arr, **kwargs):

    def __init__(self, name, moveSpeed, health, image, planeNum, shoot_speed, collision_damage, special_ability, arr, **kwargs):

        super().__init__(img=image, **kwargs)
        # def __init__(self, *args, **kwargs):
        self.name = name
        self.user_owns = True
        self.moveSpeed = moveSpeed
        self.health = health
        self.maxHealth = health
        self.planeImg = image
        self.bullet_speed = 10
        self.bullet_damage = 10
        self.special_bullet_damage = 10
        self.new_objects = []
        self.shootVec = arr
        self.visible = False

        self.collision_damage = collision_damage
        self.laser = ""
        self.damageable = True

        self.wrap = False
        self.bind = True
        # Player should not collide with own bullets
        self.reacts_to_bullets = False
        self.reacts_to_enemy_bullets = True
        self.scale = .7

        self.shootSpeedUp = 2
        self.shoot_speed = shoot_speed
        self.could_shoot = True

        self.has_special_ability = True
        self.special_ability = special_ability
        self.special_ability_shoot_speed = .7
        self.special_ability_shoot_duration = 0.25
        self.could_shoot_special_ability = True
        self.special_ability_time_multiplier = 8
        self.specialInvulnerableTime = 3
        self.dodgeChange = 0
        #if self.name == "damage_plane":
        #    self.bombShot = True
        #    self.bombDamage = self.bullet_damage * 1.5
        #    self.bombRate = 5
        #else:
        self.bombShot = False
        self.bombDamage = 0
        self.bombRate = 0
        self.bombCounter = 0

        self.progress_circle_images = [progress_circle_0,
                                       progress_circle_1,
                                       progress_circle_2,
                                       progress_circle_3,
                                       progress_circle_4,
                                       progress_circle_5,
                                       progress_circle_6,
                                       progress_circle_7,
                                       progress_circle_8]

        self.progress_circle = pyglet.image.Animation.from_image_sequence(self.progress_circle_images, duration=self.shoot_speed,
                                                                          loop=False)

        self.blue_progress_circle_images = [blue_progress_circle_0,
                                            blue_progress_circle_1,
                                            blue_progress_circle_2,
                                            blue_progress_circle_3,
                                            blue_progress_circle_4,
                                            blue_progress_circle_5,
                                            blue_progress_circle_6,
                                            blue_progress_circle_7,
                                            blue_progress_circle_8]

        if(self.name == "helicopter"):
            self.get_width = 300 #345
            self.get_height = 300 #345
        else:
            self.get_width = self.image.width
            self.get_height = self.image.height

        self.is_player = True
        self.planeNum = planeNum
        if (self.name == "helicopter"):
            self.rotorRadius = 345 * 0.35 * self.scale * 2
            self.collisionRadius = 300 * 0.35 * self.scale
            self.damage = 5
            self.rotorDamage = 0.5
        else:
            self.rotorRadius = 1
            self.collisionRadius = self.image.width * 0.35 * self.scale
            self.damage = 5

        if (self.name == "support_plane"):
            self.heal = True
            self.regen = 1
            self.canRevive = True
            self.revivePercentage = 0.5
            self.revAll = False
            self.revRecharge = 30
        else:
            self.regen = 0
            self.heal = False
            self.canRevive = False
            self.revivePercentage = 0
            self.revAll = False
            self.revRecharge = 999

        self.selfHeal = False
        self.blue_progress_circle = pyglet.image.Animation.from_image_sequence(self.blue_progress_circle_images,
                                                                               duration=self.special_ability_shoot_speed, loop=False)

    def get_width(self):
        return self.get_width
    def get_height(self):
        return self.get_height

    def get_can_heal(self):
        return self.heal

    def getImage(self):
        return self.planeImg

    def get_name(self):
        return self.name

    def enableShoot(self, dt):
        self.could_shoot = True

    def enableRevive(self, dt):
        self.canRevive = True

    def enableSpecialAbilityShoot(self, dt):
        self.could_shoot_special_ability = True

    def revert_fire_rate_increase(self, dt, previous_rate):
        self.shoot_speed = previous_rate
        self.progress_circle = pyglet.image.Animation.from_image_sequence(self.progress_circle_images, duration=self.shoot_speed,
                                                                          loop=False)

    def fire(self, mouse_x, mouse_y):

        if (self.could_shoot):
            self.could_shoot = False
            pyglet.clock.schedule_once(self.enableShoot, self.shoot_speed * 8)
            progress_circle_sprite = pyglet.sprite.Sprite(self.progress_circle, x=61, y=61,
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

            # Note: pyglet's rotation attributes are in "negative degrees"
            if (ydiff > 0):
                angle_radians = -math.radians(math.degrees(math.atan(xdiff / ydiff)) + 270)
            elif(ydiff< 0):
                angle_radians = math.radians(-(math.degrees(math.atan(xdiff / ydiff)) + 90))
            else:
                angle_radians = math.radians(-(math.degrees(math.atan(0)) + 90))

            angle_radians = -math.radians(270)
            angle_radians = -math.radians(270)
            # print(self.shootVec)
            # Create a new bullet just in front of the player
            if self.name == "helicopter":
                ship_radius = 171
            else:
                ship_radius = self.planeImg.width / 2
            for shootSlot in self.shootVec:
                bullet_x = self.x + shootSlot  # * ship_radius #+ math.cos(angle_radians) * ship_radius
                bullet_y = self.y  # * ship_radius #+ math.sin(angle_radians) * ship_radius

                new_bullet = Bullet(bullet, bullet_x, bullet_y, self.bullet_damage, batch=self.batch, group=self.group)

                # new_bullet = Bullet(bullet_x, bullet_y + 5, batch = self.batch)

                # Give it some speed
                bullet_vx = 0  # math.cos(angle_radians) * self.bullet_speed
                bullet_vy = self.bullet_speed  # math.sin(angle_radians) * self.bullet_speed
                new_bullet.velocity_x, new_bullet.velocity_y = bullet_vx, bullet_vy
                new_bullet.wrap = False
                # Add it to the list of objects to be added to the game_objects list
                self.new_objects.append(new_bullet)
            # play bullet
            if (self.bombShot == True and self.bombCounter % self.bombRate == 0):
                new_bomb = Bullet(bomb, self.x, self.y + 30, self.bullet_damage, batch=self.batch,
                                  group=self.group)
                bullet_vx = 0  # math.cos(angle_radians) * self.bullet_speed
                bullet_vy = self.bullet_speed
                new_bomb.velocity_x, new_bomb.velocity_y = bullet_vx, bullet_vy
                new_bomb.wrap = False
                # Add it to the list of objects to be added to the game_objects list
                self.new_objects.append(new_bomb)
                self.bombCounter += 1
            else:
                self.bombCounter += 1

            if len(self.shootVec) == 1:
                bullet_sound.play()
            elif len(self.shootVec) == 2:
                two_bullets.play()


    def specialAbilityFire(self, mouse_x, mouse_y):
        if self.has_special_ability:
            if (self.could_shoot_special_ability):
                self.could_shoot_special_ability = False
                pyglet.clock.schedule_once(self.enableSpecialAbilityShoot, self.special_ability_shoot_speed * self.special_ability_time_multiplier)

                progress_circle_sprite = pyglet.sprite.Sprite(self.blue_progress_circle, x=61, y=61,
                                                              batch=self.batch,
                                                              group=self.group)
                print(self.special_ability)
                if self.special_ability == "laser":
                    print("laser")
                    new_bullet = Bullet(laser, self.x, self.y + 500, self.special_bullet_damage, batch=self.batch, group=self.group)
                    #new_bullet.color = (255, 85, 66)
                    angle_radians = -math.radians(270)
                    bullet_vx = math.cos(angle_radians) * 0
                    bullet_vy = math.sin(angle_radians) * 0
                    new_bullet.velocity_x, new_bullet.velocity_y = bullet_vx, bullet_vy
                    new_bullet.wrap = False
                    new_bullet.die_on_impact = False
                    self.laser = new_bullet
                    self.new_objects.append(new_bullet)
                if self.special_ability == "fire_rate_increase":
                    print("fire_rate_increase")
                    pyglet.clock.schedule_once(self.revert_fire_rate_increase, self.special_ability_shoot_duration * 8, self.shoot_speed)
                    self.shoot_speed = self.shoot_speed / self.shootSpeedUp
                    self.progress_circle = pyglet.image.Animation.from_image_sequence(self.progress_circle_images,
                                                                                      duration=self.shoot_speed, loop=False)
                    print("fire_rate_increase")
                if self.special_ability == "ramming":
                    self.color = (255, 50, 50) #Need revisiting
                    self.damageable = False
                    pyglet.clock.unschedule(self.revert_damageable)
                    pyglet.clock.schedule_once(self.revert_damageable, self.specialInvulnerableTime)
                    pyglet.clock.schedule_once(self.revert_color, self.specialInvulnerableTime)
                    print("ramming")
                if self.special_ability == "revive":
                    self.canRevive = True
                    print("revived")
                #if self.special_ability == "revive" and deadPlaneNum != -1:

                    #print("deadplaneNUm")
                    #print(deadPlaneNum)

                    #print("revive")

    def add_upgrades(self, upgrades):
        for upgrade in upgrades:
            if upgrade[0] == "improved_movespeed":
                self.moveSpeed = self.moveSpeed * 1.5
            elif upgrade[0] == "improved_bullet_damage":
                self.bullet_damage = self.bullet_damage * 1.5
            elif upgrade[0] == "shorter_special_charge_time":
                self.special_ability_shoot_speed = self.special_ability_shoot_speed * .5
            elif upgrade[0] == "improved_fire_rate":
                self.shoot_speed = self.shoot_speed * .5
            elif upgrade[0] == "increased_special_damage":
                self.special_bullet_damage = self.special_bullet_damage * 1.5
            elif upgrade[0] == "increase_dodge_bullets":
                self.dodgeChange = 0.3
            elif upgrade[0] == "improved_bullet_damage":
                self.bullet_damage = self.bullet_damage * 1.5
            elif upgrade[0] == "bomb":
                self.bombShot = True
                self.bombDamage = self.bullet_damage * 1.5
                self.bombRate = 5
            elif upgrade[0] == "improved_bomb_damage":
                self.bombDamage = self.bullet_damage * 2
            elif upgrade[0] == "improved_bomb_fire_rate":
                self.bombRate = 3
            elif upgrade[0] == "triples_fire_rate":
                self.shootSpeedUp = 3
            elif upgrade[0] == "improved_collision_damage":
                self.rotorDamage = self.rotorDamage * 2
            elif upgrade[0] == "improved_health":
                self.health = self.health * 1.5
                self.maxHealth = self.maxHealth * 1.5
            elif upgrade[0] == "improved_movement_speed":
                self.moveSpeed = self.moveSpeed * 1.5
            elif upgrade[0] == "increase_special_time":
                self.specialInvulnerableTime += 3
                #self.special_ability_shoot_duration = self.special_ability_shoot_duration * 1.5
            elif upgrade[0] == "increased_damage_to_closer_enemies":
                self.rotorRadius = self.rotorRadius * 1.5
                self.rotorDamage = self.rotorDamage * 1.5
            elif upgrade[0] == "improved_regen_rate":
                self.regen += 1
            elif upgrade[0] == "regenerate_self":
                self.selfHeal = True
            elif upgrade[0] == "revive_planes_full_health":
                self.revivePercentage = 1
            elif upgrade[0] == "shorter_special_charge_time":
                self.special_ability_time_multiplier -= 2
            elif upgrade[0] == "revives_all_planes":
                self.revAll = True

    def collides_with(self, other_object):

        return super(PlayerPlane, self).collides_with(other_object)

    def handle_collision_with(self, other_object):
        self.damageable = False
        pyglet.clock.schedule_once(self.revert_damageable, 0.5)
        if (self.dodgeChange > 0):
            randomNum = random.randrange(1, 10)
            if randomNum <= 10 * self.dodgeChange:
                self.color = (150, 150, 200)
                pyglet.clock.schedule_once(self.revert_color, 0.25)
                return

        super(PlayerPlane, self).handle_collision_with(other_object)

    def revert_damageable(self, dt):
        self.damageable = True

    # def update(self):
    # if (self.health <= 0):
    # print('plane die')
    # self.dead = True
    # self.destroyed = True
    # self.visible = False
    # self.reacts_to_bullets = False
