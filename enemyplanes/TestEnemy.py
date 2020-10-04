import pyglet
from enemyHandler import enemy1

window = pyglet.window.Window(600, 600)
batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)

testImg = enemy1.img
testImg.rotation = 120

test = pyglet.sprite.Sprite(testImg, x = enemy1.getx(), y = enemy1.gety(), batch=batch, group=background)

def on_draw():
    window.clear()
    batch.draw()

def update(dt):
    getattr(enemy1, enemy1.movement)()




if __name__ == "__main__":
    # Update the game 120 times per second
    pyglet.clock.schedule_interval(update, 1 / 60.0)

    # Tell pyglet to do its thing
    pyglet.app.run()
