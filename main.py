# import pyglet
# from playerPlaneHandler import planes
# from pyglet.gl import *
# from resources import *
# from level import level
# from menu import menu
    
# #sets up the window
# window = pyglet.window.Window(1800, 1000, resizable=True)

# live_batch = pyglet.graphics.Batch()

# def init():
#     menu(live_batch)

# @game_window.event
# def on_draw():
#     window.clear()
#     live_batch.draw()

# if __name__ == '__main__':
#     # Starts up
#     init()

#     #updates the game 60 times per second
#     pyglet.clock.schedule_interval(update, 1/60.0)

#     pyglet.app.run()


















from playerplanehandler import planes
from pyglet.gl import *
from resources import *
from playerplane import *
import math
import pyglet

window = pyglet.window.Window(1800, 1000, resizable=True)
maps_layer = pyglet.graphics.OrderedGroup(-2)
buttons_layer = pyglet.graphics.OrderedGroup(-1)

def init():
    menu()

def menu():
    start_screen_batch = pyglet.graphics.Batch()

    live_batch = start_screen_batch


    #start_map = pyglet.sprite.Sprite(mapHandler.start_map.map_Image, batch=start_screen_batch, group=maps_layer)
    temp_image = pyglet.image.load('./resources/start_button.png')

    temp = pyglet.sprite.Sprite(temp_image, x=900-(temp_image.width/2), batch=start_screen_batch, group=buttons_layer)
    temp_start_map = pyglet.sprite.Sprite(start_map, batch=start_screen_batch, group=maps_layer)
    temp = pyglet.sprite.Sprite(start_button, x=900, y=start_button.anchor_y, batch=start_screen_batch,
                                group=buttons_layer)

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        
        if 739 < x < 1060 and y < 320:
            inGame = True
            nonlocal live_batch
            #live_batch = level_batch
            print('going to level')
            window.clear()
            #print(level_batch)
            start()

    @window.event
    def on_draw():
        window.clear()
        live_batch.draw()
    
    pyglet.app.run()



def start():
    level_batch = pyglet.graphics.Batch()
    mouse_x = 1
    mouse_y = 1
    
    # setting layering
    plane_layer = pyglet.graphics.OrderedGroup(0)

    game_objects = []
    planeNumber = 1

    plane1 = PlayerPlane(50, 50, plane_1, batch=level_batch)
    plane2 = PlayerPlane(20, 80, plane_2, batch=level_batch)
    plane2.visible = False
    plane1.visible = False
    planes = [plane1, plane2]

    # for plane in planes:
    #     game_objects += [planes]
        # adding images to batches
    #test = PhysicalObject(planes[planeNumber].planeImg, batch=level_batch, group=plane_layer)
    #test = PlayerPlane(50, 50, plane_1, batch=level_batch, group=plane_layer)
    #test = PhysicalObject(planes[planeNumber].planeImg, batch=level_batch, group=plane_layer)
    test = planes[planeNumber]
    game_objects += [test]

    #temp_exit_button = pyglet.sprite.Sprite(exit_button, x=1800 - exit_button.anchor_x, y=1000 - exit_button.anchor_y,
    #                                        batch=level_batch)

    level_map_object = PhysicalObject(level_map,x=900, batch=level_batch, group=maps_layer)
    game_objects += [level_map_object]
    level_map_object.velocity_y = -1

    # adding images to batches
    # test = pyglet.sprite.Sprite(planes[planeNumber].planeImg, batch=level_batch, group=plane_layer)

    bullet_image = pyglet.image.load('./resources/bullet1.png')

    bullet_batch = pyglet.graphics.Batch()
    bullet_sprites = []

    @window.event
    def on_mouse_motion(x, y, dx, dy):
        nonlocal mouse_x
        nonlocal mouse_y
        mouse_x = x
        mouse_y = y

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
        print("click")
        planes[planeNumber].fire()
        #bullet_sprites.append(pyglet.sprite.Sprite(bullet_image, x, y, batch = bullet_batch))

    @window.event
    def on_draw():
        window.clear()
        level_batch.draw()
        #bullet_batch.update(y = y + 2)

    def update(dt):
        vector_x = mouse_x - test.x
        vector_y = mouse_y - test.y
        magnitude_velocity = math.sqrt(vector_x ** 2 + vector_y ** 2)

        unit_x = vector_x / magnitude_velocity
        unit_y = vector_y / magnitude_velocity

        test.velocity_x = unit_x
        test.velocity_y = unit_y

        to_add = []
        for obj in game_objects:
            obj.update(1)

            to_add.extend(obj.new_objects)
            obj.new_objects = []

         # Add new objects to the list
        game_objects.extend(to_add)

    pyglet.clock.schedule_interval(update, 1 / 120.0)

    pyglet.app.run()


if __name__ == '__main__':
    init()