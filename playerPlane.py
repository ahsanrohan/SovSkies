import pyglet
import math
from bullet import *
from physicalObject import *
from resources import *


class PlayerPlane(PhysicalObject):

    #def __init__(self,name, moveSpeed, health, image, shoot_speed, collision_damage, special_ability, arr, **kwargs):

    def __init__(self,name, moveSpeed, health, image, planeNum, shoot_speed, collision_damage, special_ability, arr, **kwargs):

        super().__init__(img = image, **kwargs)
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
        self.scale = 0.7

        self.shoot_speed = shoot_speed
        self.could_shoot = True
        

        self.has_special_ability = True
        self.special_ability = special_ability
        self.special_ability_shoot_speed = .7
        self.special_ability_shoot_duration = .175
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

        self.is_player = True
        self.planeNum = planeNum
        if (planeNum == 3):
            self.rotorRadius = self.image.width * 0.35 * self.scale * 2
            self.collisionRadius = self.image.width * 0.35 * self.scale
            self.damage = 5
            self.rotorDamage = 0.2
        else:
            self.rotorRadius = 1
            self.collisionRadius = self.image.width * 0.35 * self.scale
            self.damage = 5

        if (planeNum == 4):
            self.heal = True
            self.regen = 1
        else:
            self.regen = 0
            self.heal = False


        self.blue_progress_circle = pyglet.image.Animation.from_image_sequence(self.blue_progress_circle_images, duration=self.special_ability_shoot_speed, loop=False)
    
    def get_can_heal(self):
        return self.heal
    
    def getImage(self):
        return self.planeImg

    def get_name(self):
        return self.name

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

            # Note: pyglet's rotation attributes are in "negative degrees"
            if (ydiff > 0):
                angle_radians = -math.radians(math.degrees(math.atan(xdiff/ydiff)) + 270)
            else:
                angle_radians = math.radians(-(math.degrees(math.atan(xdiff/ydiff)) + 90))
            
            angle_radians = -math.radians(270)
            #print(self.shootVec)
            # Create a new bullet just in front of the player
            if self.name == "helicopter":
                ship_radius = 171
            else: 
                ship_radius = self.planeImg.width / 2
            for shootSlot in self.shootVec:
                bullet_x = self.x + shootSlot #* ship_radius #+ math.cos(angle_radians) * ship_radius
                bullet_y = self.y #* ship_radius #+ math.sin(angle_radians) * ship_radius

                new_bullet = Bullet(bullet, bullet_x , bullet_y , self.bullet_damage, batch = self.batch, group=self.group)

                #new_bullet = Bullet(bullet_x, bullet_y + 5, batch = self.batch)


            # Give it some speed
                bullet_vx = 0 #math.cos(angle_radians) * self.bullet_speed
                bullet_vy = self.bullet_speed #math.sin(angle_radians) * self.bullet_speed
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
                    new_bullet = Bullet(laser, self.x, self.y +500, self.special_bullet_damage, batch = self.batch, group=self.group)
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
                    pyglet.clock.schedule_once(self.revert_fire_rate_increase, self.special_ability_shoot_duration * 8,  self.shoot_speed)
                    self.shoot_speed = self.shoot_speed/100
                    self.progress_circle = pyglet.image.Animation.from_image_sequence(self.progress_circle_images, duration=self.shoot_speed, loop=False)
                    print("fire_rate_increse")
                if self.special_ability == "raming":
                    print("raming")

    def add_upgrades(self, upgrades):
        for upgrade in upgrades:
            if upgrade[0] == "improved_movespeed":
                self.moveSpeed = self.moveSpeed * 1.5
            elif upgrade[0] == "improved_bullet_damage":
                self.bullet_damage == self.bullet_damage * 1.5
            elif upgrade[0] == "shorter_special_charge_time":
                self.special_ability_shoot_speed = self.special_ability_shoot_speed * .5
            elif upgrade[0] == "improved_fire_rate":
                self.shoot_speed = self.shoot_speed * .5;
            elif upgrade[0] == "increased_special_damage":
                self.special_bullet_damage = self.special_bullet_damage * 1.5
            elif upgrade[0] == "increase_dodge_bullets":
                print("6")
            elif upgrade[0] == "improved_bullet_damage":
                self.bullet_damage = self.bullet_damage * 1.5
            elif upgrade[0] == "bomb":
                print("8")
            elif upgrade[0] == "improved_bomb_damage":
                print("9")
            elif upgrade[0] == "improved_bomb_fire_rate":
                print("10")
            elif upgrade[0] == "triples_fire_rate":
                print("11")
            elif upgrade[0] == "improved_collision_damage":
                print("12")
            elif upgrade[0] == "improved_health":
                self.health = self.health * 1.5
            elif upgrade[0] == "improved_movement_speed":
                print("14")
            elif upgrade[0] == "increase_special_time":
                self.special_ability_shoot_duration = self.special_ability_shoot_duration * 1.5
            elif upgrade[0] == "increased_damage_to_closer_enemies":
                print("17")
            elif upgrade[0] == "improved_regen_rate":
                print("18")
            elif upgrade[0] == "regenerate_self":
                print("19")
            elif upgrade[0] == "revive_planes_full_health":
                print("20")
            elif upgrade[0] == "shorter_special_charge_time":
                print("21")
            elif upgrade[0] == "revives_all_planes":
                print("22")
                

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

