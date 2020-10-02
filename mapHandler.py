import pyglet


class mapImage:
    def __init__(self, image):
        self.map_Image = pyglet.image.load(image)

    def get_image(self):
        return self.map_Image

    def get_texture(self):
        return self.map_Image


start_map = mapImage('placeholdermap.jpg')
