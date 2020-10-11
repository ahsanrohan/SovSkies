import pyglet
from playerPlaneHandler import planes
from pyglet.gl import *
from resources import *
from PhysicalObject import *


def start():
    window = pyglet.window.Window(1800, 1000, resizable=True)
    glEnable(GL_BLEND)  # transparency
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)  # transparency

    level_batch = pyglet.graphics.Batch()
    start_screen_batch = pyglet.graphics.Batch()
    live_batch = start_screen_batch
    # setting layering
    plane_layer = pyglet.graphics.OrderedGroup(-1)
    maps_layer = pyglet.graphics.OrderedGroup(-2)
    buttons_layer = pyglet.graphics.OrderedGroup(0)

    #organizing objects
    game_objects = []

    planeNumber = 1

    # adding images to batches
    test = pyglet.sprite.Sprite(planes[planeNumber].planeImg, batch=level_batch, group=plane_layer)
    temp_exit_button = pyglet.sprite.Sprite(exit_button, x=1800 - exit_button.anchor_x, y=1000 - exit_button.anchor_y,
                                            batch=level_batch,
                                            group=buttons_layer)
    temp_start_map = pyglet.sprite.Sprite(start_map, batch=start_screen_batch, group=maps_layer)
    temp = pyglet.sprite.Sprite(start_button, x=900, y=start_button.anchor_y, batch=start_screen_batch,
                                group=buttons_layer)


    level_map_object = PhysicalObject(start_map, batch=level_batch, group=maps_layer)
    game_objects += [level_map_object]
    level_map_object.velocity_y = -1

    @window.event
    def on_mouse_motion(x, y, dx, dy):
        window.clear()
        test.x = x
        test.y = y

    # key press event
    @window.event
    def on_key_press(symbol, modifier):
        # key "1" get press +
        if symbol == pyglet.window.key._1:
            planeNumber = 1
            test.image = planes[planeNumber].planeImg
        if symbol == pyglet.window.key._2:
            planeNumber = 0
            test.image = planes[planeNumber].planeImg

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        nonlocal live_batch

        if live_batch == start_screen_batch:  # checking if we are in a start screen currently
            if 739 < x < 1060 and y < 320:
                live_batch = level_batch
                window.clear()
        else:
            if (1800 - exit_button.width) < x < 1800 and y > (1000 - exit_button.height):
                live_batch = start_screen_batch
                window.clear()

    @window.event
    def on_draw():
        window.clear()
        live_batch.draw()

    def update(dt):
        for obj in game_objects:
            obj.update(1)

    pyglet.clock.schedule_interval(update, 1 / 120.0)

    pyglet.app.run()


if __name__ == '__main__':
    start()
