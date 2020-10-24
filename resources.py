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


# The engine flame should not be centered on the ship. Rather, it should be shown 
# behind it. To achieve this effect, we just set the anchor point outside the
# image bounds.
#engine_image = pyglet.resource.image("engine_flame.png")
#engine_image.anchor_x = engine_image.width * 1.5
#engine_image.anchor_y = engine_image.height / 2

# Load the bullet sound _without_ streaming so we can play it more than once at a time
#bullet_sound = pyglet.resource.media("bullet.wav", streaming=False)