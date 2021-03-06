import pyglet
import math
import random
from bullet import *
import physicalObject, resources

class Enemy(physicalObject.PhysicalObject):
    def __init__ (self, image, health, velocity_x=0.0, velocity_y=0.0, *args, **kwargs):
        super().__init__(image, *args, **kwargs)
        self.health = health
        self.movement = {}
        self.fire_type = {}
        self.orientation = True
        self.wrap = False
        self.is_enemy = True
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.t = 0
        self.destroyed = False
        self.damage = 5 #collision damage
        self.scale = 0.7
        self.reacts_to_enemy_bullets = False
        self.canFire = False
        self.collisionRadius = self.image.width * 0.5 * self.scale
        self.boss = False

    def move_not(self):
        #default don't move
        pass

    def update(self, dt):
        if (self.health <= 0):
            self.dead = True
            self.destroyed = True
            self.visible = False
            self.reacts_to_bullets = False
        elif (self.y <= 100 or self.y >= 1200):
            self.canFire = False
        elif (self.x <= 0 or self.x >= 1900):
            self.canFire = False
        else:
            self.canFire = True

        getattr(self, self.movement.get('name'))()
        self.t += 1
        super(Enemy, self).update(dt)

    def collides_with(self, other_object):
        return super(Enemy, self).collides_with(other_object)

    def handle_collision_with(self, other_object):
        super(Enemy, self).handle_collision_with(other_object)

    def collides_with_rotor(self, other_object):
        collision_distance = self.collisionRadius \
                             + other_object.rotorRadius

        actual_distance = math.sqrt((self.position[0] - other_object.position[0]) ** 2 +
                                    (self.position[1] - other_object.position[1]) ** 2)
        return (actual_distance <= collision_distance)

    def boss_collision(self, other_obj):
        hitbox = [self.x - self.image.width/4, self.y-self.image.height/4, self.image.width/2, self.image.height/2]

        if (other_obj.x >= hitbox[0] and other_obj.x <= hitbox[2] + hitbox[0]):
            if (other_obj.y >= hitbox[1] and other_obj.y <= hitbox[3] + hitbox[1]):
                return True
        return False

    def boss_collision_radius(self, other_obj, radius):
        hitbox = [self.x - self.image.width/4, self.y-self.image.height/4, self.image.width/2, self.image.height/2]

        if (other_obj.x + radius >= hitbox[0] and other_obj.x - radius <= hitbox[2] + hitbox[0]):
            if (other_obj.y + radius >= hitbox[1] and other_obj.y - radius <= hitbox[3] + hitbox[1]):
                return True
        return False

    def move_ellipse(self):
        a = self.movement.get('a',5)
        b = self.movement.get('b',5)
        speed = self.movement.get('speed', 1)
        #self.x = a*math.cos(.01 * self.t) + self.x
        #self.y = b*math.sin(.01 * self.t) + self.y
        self.velocity_x = speed*a*math.sin(.01 * speed * self.t)
        self.velocity_y = speed*b*math.cos(.01 * speed * self.t)

    def move_sinusoid(self):
        speed = self.movement.get('speed', 1)
        self.velocity_x = speed
        a = self.movement.get('a', 1)
        b = self.movement.get('b', 0.01)
        self.velocity_y = a * math.sin(0.01 * self.t)
    
    def move_parabola(self):
        speed = self.movement.get('speed', 1)
        a = self.movement.get('a', 1)
        self.velocity_x = speed
        self.velocity_y = -0.001*a*speed*self.t

    def move_down(self):
        speed = self.movement.get('speed', 1)
        #self.x = self.movement.get('pos', 1)
        self.velocity_x = 0
        self.velocity_y = speed

    def move_down_follow(self):
        speed = self.movement.get('speed', 1)
        self.velocity_x = 0
        self.velocity_y = -10 * speed
        self.rotation = 90


    def stop_at(self):
        speed = self.movement.get('speed', 1)
        target_x = self.movement.get('x', 500)
        target_y = self.movement.get('y', 900)
        self.orientation = False
        self.rotation = 180
        if self.x <= target_x or self.y <= target_y:
            self.velocity_x = 0
            self.velocity_y = 0

    #fire bullet to a targetted x,y
    def fire_target(self, target_x, target_y):
        speed = self.fire_type.get('speed', 10)
        xdiff = target_x - self.x
        ydiff = target_y - self.y
        magnitude_velocity = math.sqrt(xdiff ** 2 + ydiff ** 2)
        unit_x = xdiff / magnitude_velocity
        unit_y = ydiff / magnitude_velocity

        bullet_x = self.x #* ship_radius #+ math.cos(angle_radians) * ship_radius
        bullet_y = self.y #* ship_radius #+ math.sin(angle_radians) * ship_radius
        new_bullet = Bullet(bullet, bullet_x, bullet_y + 5, 5, False,  batch=self.batch, group=self.group)
        new_bullet.color = (255, 5, 5)
        new_bullet.is_enemyBullet = True
        # Give it some speed
        bullet_vx = unit_x * speed #math.cos(angle_radians) * self.bullet_speed
        bullet_vy = unit_y * speed #self.bullet_speed #math.sin(angle_radians) * self.bullet_speed
        new_bullet.velocity_x, new_bullet.velocity_y = bullet_vx, bullet_vy
        new_bullet.wrap = False
        # Add it to the list of objects to be added to the game_objects list
        self.new_objects.append(new_bullet)


    def target_plane(self, plane):
        self.fire_target(plane.x, plane.y)

    def down(self):
        self.fire_target(self.x, self.y-1)

    def straight(self):
        offset = self.fire_type.get('offset', 0) #degrees
        bullet_angle = self.fire_type.get('bullet_rotation', 90 - self.rotation) + offset
        speed = self.fire_type.get('speed', 10)
        new_bullet = Bullet(bullet, self.x, self.y, 5, False, batch=self.batch, group=self.group)
        new_bullet.is_enemyBullet = True
        new_bullet.color = (255, 5, 5)
        new_bullet.velocity_x, new_bullet.velocity_y = speed*math.cos(math.radians(bullet_angle)), speed*math.sin(math.radians(bullet_angle))
        self.new_objects.append(new_bullet)

    def cone(self):
        bullets = self.fire_type.get('count', 3)
        spread = self.fire_type.get('spread', 9) #degrees
        for bullet in range(-int(bullets/2), int(bullets/2) + 1):
            self.fire_type['bullet_rotation'] = 90 - self.rotation + int(spread/bullets * bullet)
            self.straight()

    def rand(self):
        spread = self.fire_type.get('spread', 30) #range of random
        rand = random.randint(-spread//2, spread//2)
        self.fire_type['bullet_rotation'] = 90 - self.rotation + rand
        self.straight()

    def burst(self):
        #cone with 360 degree spread, offset so that enemy isnt shooting directly in front of itself
        count = self.fire_type.get('count', 3)
        self.fire_type['spread'] = 360
        self.fire_type['offset'] = 360/count/2
        self.cone()

    def spiral(self):
        count = self.fire_type.get('count', 3)
        self.fire_type['spread'] = 360
        spiral_speed = self.fire_type.get('spiral_speed', 5)
        if 'offset' in self.fire_type:
            self.fire_type['offset'] += spiral_speed
        else:
            self.fire_type['offset'] = 0
        self.cone()
