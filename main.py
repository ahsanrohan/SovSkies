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








from playerplanehandler import *
from pyglet.gl import *
from resources import *
from physicalobject import *
import math
import pyglet

window = pyglet.window.Window(1800, 1000, resizable=True)
maps_layer = pyglet.graphics.OrderedGroup(-2)
buttons_layer = pyglet.graphics.OrderedGroup(-1)

#this is where values are initialized 
def init():
    menu()

#menu funtion
def menu():
    start_screen_batch = pyglet.graphics.Batch()

    live_batch = start_screen_batch


    #start_map = pyglet.sprite.Sprite(mapHandler.start_map.map_Image, batch=start_screen_batch, group=maps_layer)
    temp_image = pyglet.image.load('./resources/start_button.png')

    temp = pyglet.sprite.Sprite(temp_image, x=900-(temp_image.width/2), batch=start_screen_batch, group=buttons_layer)
    temp_start_map = pyglet.sprite.Sprite(start_map, batch=start_screen_batch, group=maps_layer)
    temp = pyglet.sprite.Sprite(start_button, x=900, y=start_button.anchor_y, batch=start_screen_batch, group=buttons_layer)

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


#Game function
def start():
    level_batch = pyglet.graphics.Batch()
    mouse_x = 1
    mouse_y = 1
    
    # setting layering
    plane_layer = pyglet.graphics.OrderedGroup(0)

    # these objects will be updated every tick
    game_objects = []

    #initializing plane handler which holds all the planes
    planeHandler = PlayerPlaneHandler(batch=level_batch, group=plane_layer)
    game_objects += planeHandler.getAllPlanes();

    #initializing the background
    level_map_object = PhysicalObject(level_map, x=900, batch=level_batch, group=maps_layer)
    game_objects += [level_map_object]
    level_map_object.velocity_y = -1

    @window.event
    def on_mouse_motion(x, y, dx, dy):
        nonlocal mouse_x
        nonlocal mouse_y
        mouse_x = x
        mouse_y = y

    # key press event
    @window.event
    def on_key_press(symbol, modifier):
        if symbol == pyglet.window.key._1:
            planeHandler.setActivePlane(1)
        if symbol == pyglet.window.key._2:
            planeHandler.setActivePlane(0)

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        if (button == 1):
            planeHandler.getActivePlane().fire(mouse_x, mouse_y)

    @window.event
    def on_draw():
        window.clear()
        level_batch.draw()

    def update(dt):
        vector_x = mouse_x - planeHandler.getActivePlane().x
        vector_y = mouse_y - planeHandler.getActivePlane().y
        magnitude_velocity = math.sqrt(vector_x ** 2 + vector_y ** 2)
        if (magnitude_velocity > 200 and planeHandler.getActivePlane().x <= 1800 and planeHandler.getActivePlane().x >= 0):
            unit_x = vector_x / magnitude_velocity
            unit_y = vector_y / magnitude_velocity

            planeHandler.getActivePlane().velocity_x = unit_x * planeHandler.getActivePlane().moveSpeed * dt * 0.8
            planeHandler.getActivePlane().velocity_y = unit_y * planeHandler.getActivePlane().moveSpeed * dt * 0.8
        elif (magnitude_velocity > 20 and magnitude_velocity < 200 and planeHandler.getActivePlane().x <= 1800 and planeHandler.getActivePlane().x >= 0):
            unit_x = vector_x / magnitude_velocity
            unit_y = vector_y / magnitude_velocity

            planeHandler.getActivePlane().velocity_x = unit_x * planeHandler.getActivePlane().moveSpeed * dt
            planeHandler.getActivePlane().velocity_y = unit_y * planeHandler.getActivePlane().moveSpeed * dt
        else:
            planeHandler.getActivePlane().velocity_x = 0
            planeHandler.getActivePlane().velocity_y = 0
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