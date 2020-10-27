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

start_button = pyglet.resource.image("start_button.png")
center_image(start_button)

quit_button = pyglet.resource.image("quit_button.png")
center_image(quit_button)

exit_button = pyglet.resource.image("exit_button.png")
center_image(exit_button)

exit_button = pyglet.resource.image("exit_button.png")
center_image(exit_button)

start_map = pyglet.resource.image("placeholdermap.jpg")

level_map = pyglet.resource.image("level_background.png")

level_map = pyglet.resource.image("level_background.png")
center_image(level_map)

sov_logo = pyglet.resource.image("SovLogo.png")
center_image(sov_logo)

end_image = pyglet.resource.image("end_game.jpg")
center_image(end_image)

enemy_plane = pyglet.resource.image("enemyPlane1.png")
center_image(enemy_plane)

sov_logo_image = pyglet.resource.image("SovLogo.png")
center_image(sov_logo_image)

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


# The engine flame should not be centered on the ship. Rather, it should be shown 
# behind it. To achieve this effect, we just set the anchor point outside the
# image bounds.
#engine_image = pyglet.resource.image("engine_flame.png")
#engine_image.anchor_x = engine_image.width * 1.5
#engine_image.anchor_y = engine_image.height / 2

# Load the bullet sound _without_ streaming so we can play it more than once at a time
#bullet_sound = pyglet.resource.media("bullet.wav", streaming=False)