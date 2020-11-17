from playerPlaneHandler import *
from pyglet.gl import *
from resources import *
from physicalObject import *
from enemy import *
import math
import pyglet
from longTermData import *
import json

#createGame()


window = pyglet.window.Window(fullscreen=True)
windowWidth = window.width
windowHeight = window.height
maps_layer = pyglet.graphics.OrderedGroup(-2)
buttons_layer = pyglet.graphics.OrderedGroup(-1)

playerName = "Peyton"
# this is where values are initialized
def init():
    #createPlayer("Peyton")
    #createPlayerPlanes("Peyton", "oldy")

    getPlayerPlanes(playerName)
    menu()


# menu funtion
def menu():
    start_screen_batch = pyglet.graphics.Batch()
    live_batch = start_screen_batch

    start_map_sprite = pyglet.sprite.Sprite(start_map, batch=start_screen_batch, group=maps_layer)
    start_button_sprite = pyglet.sprite.Sprite(start_button, x=windowWidth/2, y = windowHeight/4, batch=start_screen_batch,
                                               group=buttons_layer)
    sov_logo_sprite = pyglet.sprite.Sprite(sov_logo_image, x=windowWidth/2, y = windowHeight*3/4, batch=start_screen_batch,
                                           group=buttons_layer)

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        if windowWidth/2 -150 < x < (windowWidth/2)+150 and windowHeight/4 -50 < y < windowHeight/4 + 50:
            inGame = True
            nonlocal live_batch
            # live_batch = level_batch
            window.clear()
            # print(level_batch)
            start()

    @window.event
    def on_draw():
        window.clear()
        live_batch.draw()

    pyglet.app.run()


def end_screen(dt):
    end_screen_batch = pyglet.graphics.Batch()

    # start_map = pyglet.sprite.Sprite(mapHandler.start_map.map_Image, batch=start_screen_batch, group=maps_layer)
    end_sprite = pyglet.sprite.Sprite(end_image, x=windowWidth/2, y = windowHeight*3/4, batch=end_screen_batch,
                                      group=maps_layer)

    quit_button_sprite = pyglet.sprite.Sprite(quit_button, x=windowWidth/2, y=start_button.anchor_y + 150, batch=end_screen_batch,
                                               group=buttons_layer)  

    start_button_sprite = pyglet.sprite.Sprite(start_button, x=windowWidth/2, y=start_button.anchor_y, batch=end_screen_batch,
                                               group=buttons_layer)

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        if windowWidth/2 -150 < x < (windowWidth/2)+150 and y < 100:
            window.clear()
            # print(level_batch)
            start()

        if windowWidth/2 -150 < x < (windowWidth/2)+150 and 150 < y < 250:
            closeConnection()
            window.close()
            # print(level_batch)

    @window.event
    def on_draw():
        window.clear()
        end_screen_batch.draw()

    pyglet.app.run()


# Game function
def start():
    level_batch = pyglet.graphics.Batch()
    mouse_x = 1
    mouse_y = 1
    # setting layering
    plane_layer = pyglet.graphics.OrderedGroup(0)

    # these objects will be updated every tick
    game_objects = []
    enemies = []

    # Score Handling
    score_obj = {'score': 0, 'target_score': 20}
    label = pyglet.text.Label('Score: ' + str(score_obj['score']),
                              font_name='Times New Roman',
                              font_size=24, group=buttons_layer,
                              x=window.width - 200, y=window.height // 2, batch=level_batch)


    # initializing plane handler which holds all the planes
    planeHandler = PlayerPlaneHandler(getPlayerPlanes(playerName), batch=level_batch, group=plane_layer)
    game_objects += planeHandler.getAllPlanes()

    health = pyglet.text.Label('Health: ' + str(planeHandler.getActivePlane().health),
                               font_name='Times New Roman',
                               font_size=24, group=buttons_layer,
                               x=window.width - 200, y=(window.height // 2) - 50, batch=level_batch)

    # load level data
    level_filepath = 'resources/level_scripts.json'
    level_number = 2 #hardcoded level
    with open(level_filepath) as f:
        level = json.load(f)[level_number]

    # functions to add enemy objects to game objects
    def enemy_fire(dt, enemy, name):
        if(enemy.canFire and not enemy.dead):
            if( enemy.fire_type and name == 'target_plane'):
                enemy.target_plane(planeHandler.getActivePlane())
            else:
                getattr(enemy, name)()

    def enemy_fire_list(dt, enemy, fire_type):
        curr_time = 0
        for fire in fire_type:
            new_enemy.fire_type = fire
            for i in range(int(fire['duration']//fire['interval'])):
                pyglet.clock.schedule_once(enemy_fire, curr_time, enemy=new_enemy, name=fire['name'])
                curr_time += fire['interval']

    def add_enemy(dt, enemy):
        game_objects.append(enemy)
        enemies.append(enemy)
        enemy.visible = True
        if(enemy.x == -500):
            enemy.x = planeHandler.getActivePlane().x

    #read level data
    for wave in level:
        for enemy_count in range(wave['enemy_count']):
            img = eval('resources.' + wave['enemy_obj']['img'])
            hp = wave['enemy_obj']['hp']
            new_enemy = Enemy(img, hp, batch=level_batch, group=plane_layer, **wave['enemy_obj']['kwargs'])
            new_enemy.movement = wave.get('movement', {"name": 'move_not'})
            fire_type = wave.get('fire')
            new_enemy.x += enemy_count*wave.get('spawn_dx', 0)
            new_enemy.y += enemy_count*wave.get('spawn_dy', 0)
            new_enemy.visible = False
            if (new_enemy.movement['name'] == 'move_down_follow'):
                new_enemy.x = -500 #outside value to check for plane follow
            if type(fire_type) is list:
                new_enemy.canFire = True
                repeat_fire_interval = sum([f['duration'] for f in fire_type])
                pyglet.clock.schedule_interval(enemy_fire_list, repeat_fire_interval, enemy=new_enemy, fire_type=fire_type)
            elif (fire_type):
                new_enemy.fire_type = fire_type
                new_enemy.canFire = True
                pyglet.clock.schedule_interval(enemy_fire, new_enemy.fire_type['interval'], enemy=new_enemy, name=new_enemy.fire_type['name'])
                #pyglet.clock.schedule_interval(new_enemy.enemyFire,
                                          #wave['fire']['interval'], planeHandler.getActivePlane())
            pyglet.clock.schedule_once(add_enemy, delay=wave['spawn_time']+enemy_count*wave['interval'], enemy = new_enemy)
    

    #initialize wave
    

    # initializing the background
    level_map_object = PhysicalObject(level_map, x=windowWidth/2, batch=level_batch, group=maps_layer)
    game_objects.append(level_map_object)
    level_map_object.velocity_y = -1

    # initialize the exit button
    exit_button_sprite = pyglet.sprite.Sprite(exit_button, x= windowWidth - exit_button.anchor_x, y= windowHeight - exit_button.anchor_y,
                                              batch=level_batch,
                                              group=buttons_layer)

    def mouse_location_update(x, y):
        nonlocal mouse_x
        nonlocal mouse_y
        mouse_x = x
        mouse_y = y

    @window.event
    def on_mouse_motion(x, y, dx, dy):
        mouse_location_update(x, y)

    # key press event
    @window.event
    def on_key_press(symbol, modifier):
        currPlane = planeHandler.getActivePlane()
        if symbol == pyglet.window.key._1:
            # planeHandler.getActivePlane(1).x = currPlane.x
            planeHandler.setActivePlane(0, currPlane)
        if symbol == pyglet.window.key._2:
            # planeHandler.getActivePlane(0).x = currPlane.x
            planeHandler.setActivePlane(1, currPlane)
        if symbol == pyglet.window.key._3:
            # planeHandler.getActivePlane(0).x = currPlane.x
            planeHandler.setActivePlane(2, currPlane)
        if symbol == pyglet.window.key._4:
            # planeHandler.getActivePlane(0).x = currPlane.x
            planeHandler.setActivePlane(3, currPlane)

    @window.event
    def on_mouse_drag(x, y, dx, dy, button, modifiers):
        mouse_location_update(x, y)

    @window.event
    def on_mouse_press(x, y, button, modifiers):

        if (windowWidth - exit_button.width) < x < windowWidth and y > (windowHeight - exit_button.height):  # clicking X button
            end_screen(0)
            window.clear()
        if (button == 1):
            planeHandler.getActivePlane().fire(mouse_x, mouse_y)
        # print(game_objects)

    @window.event
    def on_draw():
        window.clear()
        level_batch.draw()
        circle = pyglet.shapes.Circle(planeHandler.getActivePlane().x, planeHandler.getActivePlane().y,
                                      planeHandler.getActivePlane().collisionRadius, color=(50, 225, 30), batch=level_batch)
        circle.opacity = 100

        #rotorCircle = pyglet.shapes.Circle(planeHandler.getActivePlane().x, planeHandler.getActivePlane().y,
        #                             planeHandler.getActivePlane().rotorRadius, color=(255, 255, 255), batch=level_batch)

        #rotorCircle.opacity = 100

        circle.draw()
        #rotorCircle.draw()

    def checkEnd():
        planes = planeHandler.getAllPlanes()
        currentPlane = planeHandler.getActivePlane()
        if(planes[planeHandler.prevPlane].dead == False):
            pyglet.clock.schedule_once(switchDeadPlane, num=planeHandler.prevPlane, currPlane=currentPlane, delay=0.1)
        else:
            pyglet.clock.schedule_once(end_screen, 0.4)

    def switchDeadPlane(dt, num, currPlane):
        planeHandler.setActivePlane(num, currPlane)

    def regeneratePlane(dt, selfHeal):
        low = 2.0
        planeNum = 0
        if (planeHandler.getActivePlane().planeNum == 4):
            for plane in planeHandler.getAllPlanes():
                if (plane.health / plane.maxHealth) < low:
                    low = plane.health / plane.maxHealth
                    planeNum = plane.planeNum
            if (low < 1):
                planeHandler.getPlaneByNum(planeNum).health += planeHandler.getPlaneByNum(4).regen

        elif (planeHandler.getActivePlane().planeNum != 4 and selfHeal == True
              and planeHandler.getPlaneByNum(4).health < planeHandler.getPlaneByNum(4).maxHealth):
            planeHandler.getPlaneByNum(4).health += planeHandler.getPlaneByNum(4).regen

        planeHandler.getPlaneByNum(4).heal = True

    def handle_move(dt):

        # player plane
        vector_x = mouse_x - planeHandler.getActivePlane().x
        vector_y = mouse_y - planeHandler.getActivePlane().y
        magnitude_velocity = math.sqrt(vector_x ** 2 + vector_y ** 2)
        if (
                magnitude_velocity > 200 and planeHandler.getActivePlane().x <= 1800 and planeHandler.getActivePlane().x >= 0):
            unit_x = vector_x / magnitude_velocity
            unit_y = vector_y / magnitude_velocity

            planeHandler.getActivePlane().velocity_x = unit_x * planeHandler.getActivePlane().moveSpeed * dt * 0.8
            planeHandler.getActivePlane().velocity_y = unit_y * planeHandler.getActivePlane().moveSpeed * dt * 0.8
        elif (
                magnitude_velocity > 20 and magnitude_velocity < 200 and planeHandler.getActivePlane().x <= 1800 and planeHandler.getActivePlane().x >= 0):
            unit_x = vector_x / magnitude_velocity
            unit_y = vector_y / magnitude_velocity

            planeHandler.getActivePlane().velocity_x = unit_x * planeHandler.getActivePlane().moveSpeed * dt
            planeHandler.getActivePlane().velocity_y = unit_y * planeHandler.getActivePlane().moveSpeed * dt
        else:
            planeHandler.getActivePlane().velocity_x = 0
            planeHandler.getActivePlane().velocity_y = 0

    def checkCollision():
        for obj in game_objects:
            if (obj.dead == True):
                if obj.is_enemy == True and obj.destroyed == True:
                    enemies.remove(obj)
                    score_obj['score'] += 1
                    label.text = 'Score: '+ str(score_obj['score'])

                    print(score_obj)
                    if score_obj['score'] >= score_obj['target_score']:  # change this to change the required score to win
                        pyglet.clock.schedule_once(end_screen, 1)
                        print("game end")

                game_objects.remove(obj)

            if (obj.is_enemy):
                if(planeHandler.getActivePlane().planeNum == 3):
                    if (obj.collides_with_rotor(planeHandler.getActivePlane())):
                        obj.health -= planeHandler.getActivePlane().rotorDamage
                        obj.color = (255, 100, 100)
                        pyglet.clock.schedule_once(obj.revert_color, 0.1)

                if(obj.collides_with(planeHandler.getActivePlane()) and planeHandler.getActivePlane().damageable == True):
                    planeHandler.getActivePlane().handle_collision_with(obj)

            if (obj.is_bullet):
                if (obj.is_enemyBullet):
                    if (planeHandler.getActivePlane().collides_with(obj) == True and planeHandler.getActivePlane().damageable == True):
                        planeHandler.getActivePlane().handle_collision_with(obj)
                else:
                    for enemyObj in enemies:
                        if (enemyObj.collides_with(obj) == True):
                            enemyObj.handle_collision_with(obj)

    def checkHeal():
        if (planeHandler.getPlaneByNum(4).heal == True):
            pyglet.clock.schedule_once(regeneratePlane, 1, False)
            planeHandler.getPlaneByNum(4).heal = False

    def update(dt):
        handle_move(dt)
        #checkCollision()
        if (planeHandler.getActivePlane().health <= 0):
            planeHandler.getActivePlane().dead = True
            checkEnd()
        checkHeal()

        to_add = []
        for obj in game_objects:
            obj.update(1)
    
            to_add.extend(obj.new_objects)
            obj.new_objects = []

        # Add new objects to the list
        game_objects.extend(to_add)

        health.text = 'Health: ' + str(planeHandler.getActivePlane().health)

    pyglet.clock.schedule_interval(update, 1 / 120.0)

    pyglet.app.run()


if __name__ == '__main__':
    init()
