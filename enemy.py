import pyglet
import math
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

    def move_not(self):
        #default don't move
        pass

    def update(self, dt):
        if (self.health <= 0):
            self.dead = True
            self.destroyed = True
            self.visible = False
            self.reacts_to_bullets = False
        elif (self.y <= 100 or self.y >= 900):
            self.canFire = False
        elif (self.x <= 0 or self.x >= 1400):
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

    def fire_target(self, target_x, target_y):
        speed = self.fire_type.get('speed', 10)
        if (not self.dead):
            xdiff = target_x - self.x
            ydiff = target_y - self.y
            magnitude_velocity = math.sqrt(xdiff ** 2 + ydiff ** 2)
            unit_x = xdiff / magnitude_velocity
            unit_y = ydiff / magnitude_velocity

            bullet_x = self.x #* ship_radius #+ math.cos(angle_radians) * ship_radius
            bullet_y = self.y #* ship_radius #+ math.sin(angle_radians) * ship_radius
            new_bullet = Bullet(bullet_x, bullet_y + 5, batch = self.batch)
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

    def cone(self):
        bullets = self.fire_type.get('count', 3)
        spread = self.fire_type.get('spread', 30) #degrees
        for bullet in range(-int(bullets/2),int(bullets/2)):
            self.rotation += int(spread/bullets * bullet)
            print(self.velocity_x, self.velocity_y)
            self.fire_target(self.x + self.velocity_x + 0.01, self.y + self.velocity_y + 0.01)

    def multi(self): pass

