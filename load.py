import pyglet
import copy
from . import enemy, resources

#def enemies(enemywave object, batch=None):
def enemy_wave(num_enemies, image, health, spawn_x, spawn_y, batch=None, **kwargs):
    #load a custom wave of enemies
    enemies = []
    for i in range(num_enemies):
        new_enemy = Enemy(plane_1, health, x=spawn_x, y=spawn_x, **kwargs) 
        #example enemy initiliazation => enemy =  Enemy(plane_1, 50, 50, 50, movement = 'move_ellipse', a = 5, b = 2)
        enemies.append(new_enemy)
    return enemies

#list of tuples of num of planes and kwargs for plane movement
level_1 = [(5,{'movement' = 'move_ellipse', 'a': 5, 'b' = 2}), ]
enemies = [Enemy(plane_1, 50, x=50, y=50, movement = 'move_ellipse', a = 5, b = 2)  for i in range(5)]


'''
def player_lives(num_icons, batch=None):
    """Generate sprites for player life icons"""
    player_lives = []
    for i in range(num_icons):
        new_sprite = pyglet.sprite.Sprite(img=resources.player_image,
                                          x=785 - i * 30, y=585,
                                          batch=batch)
        new_sprite.scale = 0.5
        player_lives.append(new_sprite)
    return player_lives


def asteroids(num_asteroids, player_position, batch=None):
    """Generate asteroid objects with random positions and velocities, not close to the player"""
    asteroids = []
    for i in range(num_asteroids):
        asteroid_x, asteroid_y = player_position
        while util.distance((asteroid_x, asteroid_y), player_position) < 100:
            asteroid_x = random.randint(0, 800)
            asteroid_y = random.randint(0, 600)
        new_asteroid = asteroid.Asteroid(x=asteroid_x, y=asteroid_y, batch=batch)
        new_asteroid.rotation = random.randint(0, 360)
        new_asteroid.velocity_x, new_asteroid.velocity_y = random.random() * 40, random.random() * 40
        asteroids.append(new_asteroid)
    return asteroids
'''