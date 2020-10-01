import pyglet
from playerPlaneHandler import planes

def start():
    window = pyglet.window.Window(600, 600)
    batch = pyglet.graphics.Batch()
    background = pyglet.graphics.OrderedGroup(0)

    planeNumber = 1
    testImg = planes[planeNumber].planeImg

    test = pyglet.sprite.Sprite(testImg, batch=batch, group=background)

    @window.event
    def on_mouse_motion(x, y, dx, dy):
        window.clear()
        test.x = x
        test.y = y

    @window.event
    def on_draw():
        batch.draw()

    pyglet.app.run()


if __name__ == '__main__':
    start()

