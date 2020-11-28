import pyglet


def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2


# Tell pyglet where to find the resources
pyglet.resource.path = ['resources']
pyglet.resource.reindex()

# Load the three main resources and get them to draw centered
bullet = pyglet.resource.image("bullet1.png")
center_image(bullet)

plane_1 = pyglet.resource.image("planeTest1.png")
center_image(plane_1)

plane_2 = pyglet.resource.image("planeTest2.png")
center_image(plane_2)

helicopter_0 = pyglet.resource.image('helicopter1.png')
center_image(helicopter_0)
helicopter_1 = pyglet.resource.image('helicopter2.png')
center_image(helicopter_1)
helicopter_2 = pyglet.resource.image('helicopter3.png')
center_image(helicopter_2)
helicopter_3 = pyglet.resource.image('helicopter4.png')
center_image(helicopter_3)
helicopter_4 = pyglet.resource.image('helicopter5.png')
center_image(helicopter_4)

start_button = pyglet.resource.image("start.png")
center_image(start_button)

quit_button = pyglet.resource.image("quit.png")
center_image(quit_button)

exit_button = pyglet.resource.image("exit.png")
center_image(exit_button)

x_button = pyglet.resource.image("exit_button.png")
center_image(x_button)

levels_button = pyglet.resource.image("levels.png")
center_image(levels_button)

store_button = pyglet.resource.image("shop.png")
center_image(store_button)

resume_button = pyglet.resource.image("Resume.png")
center_image(resume_button)

menu_button = pyglet.resource.image("menu.png")
center_image(menu_button)

plane1_button = pyglet.resource.image("plane1.png")
center_image(plane1_button)

plane2_button = pyglet.resource.image("plane2.png")
center_image(plane2_button)

plane3_button = pyglet.resource.image("plane3.png")
center_image(plane3_button)

plane4_button = pyglet.resource.image("plane4.png")
center_image(plane4_button)


start_map = pyglet.resource.image("placeholdermap.jpg")
center_image(start_map)

#level_map = pyglet.resource.image("gainesville_background.png")
#level_map = pyglet.resource.image("water_background.png")
level_map = pyglet.resource.image("road_background.png")
#level_map = pyglet.resource.image("level_background.png")
center_image(level_map)

sov_logo = pyglet.resource.image("SovLogo.png")
center_image(sov_logo)

end_image = pyglet.resource.image("end_game.jpg")
center_image(end_image)

enemy_plane = pyglet.resource.image("enemyPlane1.png")
center_image(enemy_plane)

enemy_plane_1 = pyglet.resource.image("enemyPlane1.png")
center_image(enemy_plane_1)

enemy_plane_2 = pyglet.resource.image("enemyPlane2.png")
center_image(enemy_plane_2)

enemy_plane_3 = pyglet.resource.image("enemyPlane3.png")
center_image(enemy_plane_3)

enemy_plane_4 = pyglet.resource.image("enemyPlane4.png")
center_image(enemy_plane_4)
enemy_plane_4.height *= 1.4
enemy_plane_4.width *= 1.4

enemy_plane_5 = pyglet.resource.image("enemyPlane5.png")
center_image(enemy_plane_5)
enemy_plane_5.height *= 1.4
enemy_plane_5.width *= 1.4

enemy_plane_6 = pyglet.resource.image("enemyPlane6.png")
center_image(enemy_plane_6)

enemy_boss = pyglet.resource.image("boss1.png")
enemy_boss.height *= 2
enemy_boss.width *= 2
center_image(enemy_boss)

enemy_boss_2 = pyglet.resource.image("boss2.png")
enemy_boss_2.height *= 4
enemy_boss_2.width *= 4
center_image(enemy_boss_2)

sov_logo_image = pyglet.resource.image("SovLogo.png")
center_image(sov_logo_image)


laser = pyglet.resource.image("laser.png")
center_image(laser)

blue_progress_circle_8 = pyglet.resource.image('progressCircle8.png')
center_image(blue_progress_circle_8)
blue_progress_circle_7 = pyglet.resource.image('blueprogressCircle7.png')
center_image(blue_progress_circle_7)
blue_progress_circle_6 = pyglet.resource.image('blueprogressCircle6.png')
center_image(blue_progress_circle_6)
blue_progress_circle_5 = pyglet.resource.image('blueprogressCircle5.png')
center_image(blue_progress_circle_5)
blue_progress_circle_4 = pyglet.resource.image('blueprogressCircle4.png')
center_image(blue_progress_circle_4)
blue_progress_circle_3 = pyglet.resource.image('blueprogressCircle3.png')
center_image(blue_progress_circle_3)
blue_progress_circle_2 = pyglet.resource.image('blueprogressCircle2.png')
center_image(blue_progress_circle_2)
blue_progress_circle_1 = pyglet.resource.image('blueprogressCircle1.png')
center_image(blue_progress_circle_1)
blue_progress_circle_0 = pyglet.resource.image('blueprogressCircle0.png')
center_image(blue_progress_circle_0)

progress_circle_8 = pyglet.resource.image('progressCircle8.png')
center_image(progress_circle_8)
progress_circle_7 = pyglet.resource.image('progressCircle7.png')
center_image(progress_circle_7)
progress_circle_6 = pyglet.resource.image('progressCircle6.png')
center_image(progress_circle_6)
progress_circle_5 = pyglet.resource.image('progressCircle5.png')
center_image(progress_circle_5)
progress_circle_4 = pyglet.resource.image('progressCircle4.png')
center_image(progress_circle_4)
progress_circle_3 = pyglet.resource.image('progressCircle3.png')
center_image(progress_circle_3)
progress_circle_2 = pyglet.resource.image('progressCircle2.png')
center_image(progress_circle_2)
progress_circle_1 = pyglet.resource.image('progressCircle1.png')
center_image(progress_circle_1)
progress_circle_0 = pyglet.resource.image('progressCircle0.png')
center_image(progress_circle_0)



healthbar_0 = pyglet.resource.image('health0.png')
center_image(healthbar_0)
healthbar_1 = pyglet.resource.image('health1.png')
center_image(healthbar_1)
healthbar_2 = pyglet.resource.image('health2.png')
center_image(healthbar_2)
healthbar_3 = pyglet.resource.image('health3.png')
center_image(healthbar_3)
healthbar_4 = pyglet.resource.image('health4.png')
center_image(healthbar_4)
healthbar_5 = pyglet.resource.image('health5.png')
center_image(healthbar_5)
healthbar_6 = pyglet.resource.image('health6.png')
center_image(healthbar_6)
healthbar_7 = pyglet.resource.image('health7.png')
center_image(healthbar_7)

bomb = pyglet.resource.image('Bomb.png')
center_image(bomb)

lock_icon = pyglet.resource.image("lock.png")
center_image(lock_icon)

bullet_sound = pyglet.resource.media('Pop_Final.wav', streaming=False)
two_bullets = pyglet.resource.media('Double_Pop_2.wav', streaming=False)
laser = pyglet.resource.media('laser.wav', streaming=False)
fortunate_son = pyglet.resource.media('fortunate.wav')
immigrant = pyglet.resource.media('immigrant.wav')
kicks = pyglet.resource.media('kicks.wav')
purple_haze = pyglet.resource.media('purple_haze.wav')
background_music = pyglet.resource.media('background_music.wav')

# shop icons
move_speed_icon = pyglet.resource.image('move_speed.png')
center_image(move_speed_icon)
damage_icon = pyglet.resource.image('damage.png')
center_image(damage_icon)
charge_time_icon = pyglet.resource.image('charge_time.png')
center_image(charge_time_icon)
fire_rate = pyglet.resource.image('fire_rate.png')
center_image(fire_rate)
laser_damage_icon = pyglet.resource.image('laser_damage.png')
center_image(laser_damage_icon)
dodge_icon = pyglet.resource.image('dodge.png')
center_image(dodge_icon)
health_up_icon = pyglet.resource.image('repair_kit.png')
center_image(health_up_icon)
duration_icon = pyglet.resource.image('duration.png')
center_image(duration_icon)
ramming_icon = pyglet.resource.image('ramming.jpg')
center_image(ramming_icon)
prox_damage_icon = pyglet.resource.image('prox_damage.png')
center_image(prox_damage_icon)
bomb_icon = pyglet.resource.image('bomb_shop.png')
center_image(bomb_icon)
triple_icon = pyglet.resource.image('triple.jpg')
center_image(triple_icon)
regen_icon = pyglet.resource.image('regen.png')
center_image(regen_icon)
self_regen_icon = pyglet.resource.image('self_regen.png')
center_image(self_regen_icon)
revive_icon = pyglet.resource.image('revive.png')
center_image(revive_icon)
revive_all_icon = pyglet.resource.image('revive_all.png')
center_image(revive_all_icon)

store_map = start_map
center_image(store_map)


# The engine flame should not be centered on the ship. Rather, it should be shown 
# behind it. To achieve this effect, we just set the anchor point outside the
# image bounds.
#engine_image = pyglet.resource.image("engine_flame.png")
#engine_image.anchor_x = engine_image.width * 1.5
#engine_image.anchor_y = engine_image.height / 2

# Load the bullet sound _without_ streaming so we can play it more than once at a time
#bullet_sound = pyglet.resource.media("bullet.wav", streaming=False)