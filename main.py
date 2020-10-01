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
    
    # key press event     
    @window.event 
    def on_key_press(symbol, modifier): 
        # key "1" get press 
        if symbol == pyglet.window.key._1: 
            planeNumber = 1
            test.image = planes[planeNumber].planeImg
        if symbol == pyglet.window.key._2:
            planeNumber = 0
            test.image = planes[planeNumber].planeImg

    @window.event
    def on_draw():
        batch.draw()

    pyglet.app.run()


if __name__ == '__main__':
    start()

