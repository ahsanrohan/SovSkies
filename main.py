import pyglet


def start():
    window = pyglet.window.Window(600, 600)

    @window.event
    def on_draw():
        window.clear()

    pyglet.app.run()


if __name__ == '__main__':
    start()
