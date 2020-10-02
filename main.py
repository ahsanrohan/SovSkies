import pyglet
from playerPlaneHandler import planes
import mapHandler


def start():
    window = pyglet.window.Window(1800, 1000, resizable=True)

    level_batch = pyglet.graphics.Batch()
    start_screen_batch = pyglet.graphics.Batch()
    live_batch = start_screen_batch
    # setting layering
    plane_layer = pyglet.graphics.OrderedGroup(0)
    maps_layer = pyglet.graphics.OrderedGroup(-2)
    buttons_layer = pyglet.graphics.OrderedGroup(-1)

    planeNumber = 1

    # adding images to batches
    test = pyglet.sprite.Sprite(planes[planeNumber].planeImg, batch=level_batch, group=plane_layer)
    start_map = pyglet.sprite.Sprite(mapHandler.start_map.map_Image, batch=start_screen_batch, group=maps_layer)
    temp_image = pyglet.image.load('start_button.png')
    temp = pyglet.sprite.Sprite(temp_image, x=900-(temp_image.width/2), batch=start_screen_batch, group=buttons_layer)


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
        if 739 < x < 1060 and y < 320:
            nonlocal live_batch
            live_batch = level_batch
            print('going to level')
            window.clear()
            print(level_batch)



    @window.event
    def on_draw():
        window.clear()
        live_batch.draw()

    pyglet.app.run()


if __name__ == '__main__':
    start()
