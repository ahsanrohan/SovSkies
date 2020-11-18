import pyglet
from EnemyHandler import enemy1

window = pyglet.window.Window(600, 600)
batch = pyglet.graphics.Batch()
background = pyglet.graphics.OrderedGroup(0)

testImg = enemy1.img
testImg.rotation = 120

test = pyglet.sprite.Sprite(testImg, x = enemy1.get_x(), y = enemy1.get_y(), batch=batch, group=background)

@window.event
def on_draw():
    window.clear()
    batch.draw()

def update(dt):
    getattr(enemy1, enemy1.movement)()
    test.update(x=enemy1.x, y=enemy1.y)



if __name__ == "__main__":
    # Update the game 120 times per second
    pyglet.clock.schedule_interval(update, 1 / 60.0)

    # Tell pyglet to do its thing
    pyglet.app.run()
