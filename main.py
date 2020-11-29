from playerPlaneHandler import *
from pyglet.gl import *
from resources import *
from physicalObject import *
from enemy import *
import math
import pyglet
from longTermData import *
import json
import ctypes

user32 = ctypes.windll.user32

# createGame()
mode = "hi"
quitCheck = False
time = 0
finalTime = 0

set_fullscreen = True
if user32.GetSystemMetrics(0) > 1920:
    set_width = 1920
    set_fullscreen = False
else:
    set_width = user32.GetSystemMetrics(0)
if user32.GetSystemMetrics(1) > 1080:
    set_height = 1080
    set_fullscreen = False
else:
    set_height = user32.GetSystemMetrics(1)

if set_fullscreen == True:
    window = pyglet.window.Window(fullscreen=set_fullscreen)
else:
    window = pyglet.window.Window(fullscreen=set_fullscreen, width=set_width,
    height=set_height)

windowWidth = window.width
windowHeight = window.height
maps_layer = pyglet.graphics.OrderedGroup(-4)
buttons_layer = pyglet.graphics.OrderedGroup(-3)
icon_layer = pyglet.graphics.OrderedGroup(-2)
label_layer = pyglet.graphics.OrderedGroup(-1)
player = pyglet.media.Player()

playerName = "Peyton"


@window.event
def on_close():
    global mode
    mode = "end"


def modeCheck():
    while (mode != "end"):
        # change_volume(0)
        print(mode)
        if (mode == "menu"):
            bullet_sound.play()
            # print(mode)
            menu()
        if (mode == "game"):
            bullet_sound.play()
            # print(mode)
            start()
        if (mode == "store"):
            bullet_sound.play()
            # print(mode)
            store_menu()
        if (mode == "level"):
            bullet_sound.play()
            # print(mode)
            level_menu()
        if (mode == "quit"):
            bullet_sound.play()
            # quitCheck = False
            # print(mode)
            # window.clear()
            for element in dir():
                if element[0:2] != "__":
                    del globals()[element]
            print(dir())
            end_screen()
    bullet_sound.play()
    for element in dir():
        if element[0:2] != "__":
            del globals()[element]
    
    closeConnection()
    # print(dir())


def create_square(batch, x, y, x2, y2, width=20):
    line_left = pyglet.shapes.Line(x, y, x, y2,
                                   color=(0, 0, 0), width=width, batch=batch, group=buttons_layer)
    line_bottom = pyglet.shapes.Line(x - width / 2, y, x2 + width / 2, y,
                                     color=(0, 0, 0), width=width, batch=batch, group=buttons_layer)
    line_top = pyglet.shapes.Line(x - width / 2, y2, x2 + width / 2, y2,
                                  color=(0, 0, 0), width=width, batch=batch, group=buttons_layer)
    line_right = pyglet.shapes.Line(x2, y, x2, y2,
                                    color=(0, 0, 0), width=width, batch=batch, group=buttons_layer)
    return [line_left, line_bottom, line_top, line_right]


# this is where values are initialized
def init():
    # deleteLevels("Peyton")
    # dropLevel()
    # createLevelTable()
    # createLevel("Peyton", 1)
    # createLevel("Peyton", 2)
    # createLevel("Peyton", 3)
    # createLevel("Peyton", 4)
    # createLevel("Peyton", 5)
    # createLevel("Peyton", 6)
    # deletePlayer()
    # createPlayer("Peyton")
    print("database planes: ")
    printPlayerPlanes()
    print("database Levels: ")
    printLevels()

    # dropUpgrades()
    # createPlaneUpgradeTable()
    print("database upgrades: ")
    printAllPlayerPlanesUpgrades()

    deletePlanes("Peyton")
    deleteUpgrades("Peyton")
    createPlayerPlanes("Peyton", "fast_plane")
    createPlayerPlanes("Peyton", "damage_plane")
    # createPlayerPlanes("Peyton", "helicopter")
    # createPlayerPlanes("Peyton", "support_plane")
    
    # updatePlayerCash(100, "Peyton")
    #updatePlayerGamesPlayed("Peyton")
    #updatePlayerLevel(13, "Peyton")
    #updateLevelComplete(1,2, 30, "Peyton")
    print("this is the player")
    printAllPlayer()
    print("these are the levels")
    printLevels()
    global mode
    mode = "menu"

    getPlayerPlanes(playerName)
    modeCheck()
    # menu()


def shop_upgrade(plane_choice_shopping, batch, description):
    upgrade_box_array = []
    icon_array = []
    text = ""
    if plane_choice_shopping == 1:
        text = "Speedy: This plane is fast and has a steady rate of fire." #fast plane
        # Tier 1
        upgrade_box_array += create_square(batch, x=windowWidth / 3 - 50,
                                           y=windowHeight / 3 - 50,
                                           x2=windowWidth / 3 + 50, y2=windowHeight / 3 + 50)
        icon_array += [pyglet.sprite.Sprite(move_speed_icon, x=windowWidth / 3,
                                            y=2 * windowHeight / 3, batch=batch, group=icon_layer)]
        upgrade_box_array += create_square(batch, x=windowWidth / 3 - 50,
                                           y=2 * windowHeight / 3 - 50,
                                           x2=windowWidth / 3 + 50,
                                           y2=2 * windowHeight / 3 + 50)
        icon_array += [pyglet.sprite.Sprite(damage_icon, x=windowWidth / 3,
                                            y=windowHeight / 3, batch=batch, group=icon_layer)]
        # Tier 2
        upgrade_box_array += create_square(batch, x=windowWidth / 2 - 50,
                                           y=windowHeight / 3 - 50,
                                           x2=windowWidth / 2 + 50, y2=windowHeight / 3 + 50)
        icon_array += [pyglet.sprite.Sprite(charge_time_icon, x=windowWidth / 2,
                                            y=2 * windowHeight / 3, batch=batch, group=icon_layer)]

        upgrade_box_array += create_square(batch, x=windowWidth / 2 - 50,
                                           y=2 * windowHeight / 3 - 50,
                                           x2=windowWidth / 2 + 50,
                                           y2=2 * windowHeight / 3 + 50)

        icon_array += [pyglet.sprite.Sprite(fire_rate, x=windowWidth / 2,
                                            y=windowHeight / 3, batch=batch, group=icon_layer)]

        # Tier 3
        upgrade_box_array += create_square(batch, x=2 * windowWidth / 3 - 50,
                                           x2=2 * windowWidth / 3 + 50,
                                           y=2 * windowHeight / 3 - 50,
                                           y2=2 * windowHeight / 3 + 50)
        icon_array += [pyglet.sprite.Sprite(dodge_icon, x=2 * windowWidth / 3,
                                            y=windowHeight / 3, batch=batch, group=icon_layer)]

        upgrade_box_array += create_square(batch, x=2 * windowWidth / 3 - 50,
                                           x2=2 * windowWidth / 3 + 50,
                                           y=windowHeight / 3 - 50,
                                           y2=windowHeight / 3 + 50)
        icon_array += [pyglet.sprite.Sprite(laser_damage_icon, x=2 * windowWidth / 3,
                                            y=2 * windowHeight / 3, batch=batch, group=icon_layer)]

        # Connections
        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 3 + 50, x2=windowWidth / 2 - 50,
                                           y=windowHeight / 3, y2=windowHeight / 3)
        upgrade_box_array += create_square(batch, x=windowWidth / 3 + 50,
                                           x2=windowWidth / 2 - 50,
                                           y=2 * windowHeight / 3, y2=2 * windowHeight / 3)
        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 2 + 50, x2=2 * windowWidth / 3 - 50,
                                           y=2 * windowHeight / 3, y2=2 * windowHeight / 3)
        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 2 + 50, x2=2 * windowWidth / 3 - 50,
                                           y=windowHeight / 3, y2=windowHeight / 3)
        for upgrades in  getPlayerPlanesUpgradesIcon("Peyton", "fast_plane"):
            icon_array[upgrades[0]].color = (255, 5, 5)
        
    elif plane_choice_shopping == 2:
        text = "Big Chungus: This plane is slow but has the highest rate of fire. The special ability increase fire rate." #Damage Plane
        # Tier 1
        upgrade_box_array = create_square(batch, x=windowWidth / 3 - 50,
                                          y=windowHeight / 3 - 50,
                                          x2=windowWidth / 3 + 50, y2=windowHeight / 3 + 50)
        icon_array += [pyglet.sprite.Sprite(bomb_icon, x=windowWidth / 3,
                                            y=windowHeight / 3, batch=batch, group=icon_layer)]
        upgrade_box_array += create_square(batch, x=windowWidth / 3 - 50,
                                           y=2 * windowHeight / 3 - 50,
                                           x2=windowWidth / 3 + 50,
                                           y2=2 * windowHeight / 3 + 50)
        icon_array += [pyglet.sprite.Sprite(damage_icon, x=windowWidth / 3,
                                            y=2 * windowHeight / 3, batch=batch, group=icon_layer)]
        # Tier 2
        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 2 - 50, x2=windowWidth / 2 + 50,
                                           y=windowHeight / 2 + 50, y2=windowHeight / 2 - 50)
        icon_array += [pyglet.sprite.Sprite(damage_icon, x=windowWidth / 2,
                                            y=windowHeight / 2, batch=batch, group=icon_layer)]

        # Tier 3
        upgrade_box_array += create_square(batch,
                                           x=2 * windowWidth / 3 - 50,
                                           x2=2 * windowWidth / 3 + 50,
                                           y=windowHeight / 3 - 50, y2=windowHeight / 3 + 50)
        icon_array += [pyglet.sprite.Sprite(triple_icon, x=2 * windowWidth / 3,
                                            y=windowHeight / 3, batch=batch, group=icon_layer)]
        upgrade_box_array += create_square(batch,
                                           x=2 * windowWidth / 3 - 50,
                                           x2=2 * windowWidth / 3 + 50,
                                           y=2 * windowHeight / 3 - 50,
                                           y2=2 * windowHeight / 3 + 50)
        icon_array += [pyglet.sprite.Sprite(fire_rate, x=2 * windowWidth / 3,
                                            y=2 * windowHeight / 3, batch=batch, group=icon_layer)]

        # Connections 1
        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 3 + 50, x2=windowWidth / 2,
                                           y=windowHeight / 3, y2=windowHeight / 3)
        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 3 + 50, x2=windowWidth / 2,
                                           y=2 * windowHeight / 3, y2=2 * windowHeight / 3)

        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 2, x2=windowWidth / 2,
                                           y=2 * windowHeight / 3, y2=windowHeight / 2 + 50)
        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 2, x2=windowWidth / 2,
                                           y=windowHeight / 3, y2=windowHeight / 2 - 50)
        # Connections 2
        upgrade_box_array += create_square(batch,
                                           x=2 * windowWidth / 3, x2=2 * windowWidth / 3,
                                           y=windowHeight / 2, y2=windowHeight / 3 + 50)
        upgrade_box_array += create_square(batch,
                                           x=2 * windowWidth / 3, x2=2 * windowWidth / 3,
                                           y=windowHeight / 2, y2=2 * windowHeight / 3 - 50)
        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 2 + 50, x2=2 * windowWidth / 3,
                                           y=windowHeight / 2, y2=windowHeight / 2)
        for upgrades in  getPlayerPlanesUpgradesIcon("Peyton", "damage_plane"):
            icon_array[upgrades[0]].color = (255, 5, 5)
    elif plane_choice_shopping == 3:
        text = "Heli: The helicopter damages planes around it. The special ability shortly increases the rotor damage and grants invincibility." #helicopter
        # Tier 1
        upgrade_box_array += create_square(batch, x=windowWidth / 3 - 50,
                                           y=windowHeight / 3 - 50,
                                           x2=windowWidth / 3 + 50, y2=windowHeight / 3 + 50)

        icon_array += [pyglet.sprite.Sprite(ramming_icon, x=windowWidth / 3,
                                            y=windowHeight / 3, batch=batch, group=icon_layer)]

        upgrade_box_array += create_square(batch, x=windowWidth / 3 - 50,
                                           y=2 * windowHeight / 3 - 50,
                                           x2=windowWidth / 3 + 50,
                                           y2=2 * windowHeight / 3 + 50)

        icon_array += [pyglet.sprite.Sprite(health_up_icon, x=windowWidth / 3,
                                            y=2 * windowHeight / 3, batch=batch, group=icon_layer)]
        # Tier 2
        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 2 - 50, x2=windowWidth / 2 + 50,
                                           y=2 * windowHeight / 3 + 50,
                                           y2=2 * windowHeight / 3 - 50)
        icon_array += [pyglet.sprite.Sprite(move_speed_icon, x=windowWidth / 2,
                                            y=windowHeight / 3, batch=batch, group=icon_layer)]
        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 2 - 50, x2=windowWidth / 2 + 50,
                                           y=windowHeight / 3 + 50, y2=windowHeight / 3 - 50)
        icon_array += [pyglet.sprite.Sprite(duration_icon, x=windowWidth / 2,
                                            y=2 * windowHeight / 3, batch=batch, group=icon_layer)]

        # Tier 3
        upgrade_box_array += create_square(batch,
                                           x=2 * windowWidth / 3 - 50,
                                           x2=2 * windowWidth / 3 + 50,
                                           y=windowHeight / 3 - 50, y2=windowHeight / 3 + 50)
        icon_array += [pyglet.sprite.Sprite(prox_damage_icon, x=2 * windowWidth / 3,
                                            y=windowHeight / 3, batch=batch, group=icon_layer)]
        upgrade_box_array += create_square(batch,
                                           x=2 * windowWidth / 3 - 50,
                                           x2=2 * windowWidth / 3 + 50,
                                           y=2 * windowHeight / 3 - 50,
                                           y2=2 * windowHeight / 3 + 50)
        icon_array += [pyglet.sprite.Sprite(laser_damage_icon, x=2 * windowWidth / 3,
                                            y=2 * windowHeight / 3, batch=batch, group=icon_layer)]

        # Connections
        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 3 + 50, x2=windowWidth / 2 - 50,
                                           y=windowHeight / 3, y2=windowHeight / 3)
        upgrade_box_array += create_square(batch, x=windowWidth / 3 + 50,
                                           x2=windowWidth / 2 - 50,
                                           y=2 * windowHeight / 3, y2=2 * windowHeight / 3)
        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 2 + 50, x2=2 * windowWidth / 3 - 50,
                                           y=2 * windowHeight / 3, y2=2 * windowHeight / 3)
        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 2 + 50, x2=2 * windowWidth / 3 - 50,
                                           y=windowHeight / 3, y2=windowHeight / 3)
        for upgrades in  getPlayerPlanesUpgradesIcon("Peyton", "helicopter"):
            icon_array[upgrades[0]].color = (255, 5, 5)
    elif plane_choice_shopping == 4:
        text = "Medic: This plane is slow and bulky. It slowly regenerates the worst health plane. The special ability revives destroyed planes."
        # Tier 1
        upgrade_box_array += create_square(batch, x=windowWidth / 3 - 50,
                                           y=windowHeight / 3 - 50,
                                           x2=windowWidth / 3 + 50, y2=windowHeight / 3 + 50)
        icon_array += [pyglet.sprite.Sprite(self_regen_icon, x=windowWidth / 3,
                                            y=windowHeight / 3, batch=batch, group=icon_layer)]
        upgrade_box_array += create_square(batch, x=windowWidth / 3 - 50,
                                           y=2 * windowHeight / 3 - 50,
                                           x2=windowWidth / 3 + 50,
                                           y2=2 * windowHeight / 3 + 50)
        icon_array += [pyglet.sprite.Sprite(regen_icon, x=windowWidth / 3,
                                            y=2 * windowHeight / 3, batch=batch, group=icon_layer)]

        # Tier 2
        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 2 - 50, x2=windowWidth / 2 + 50,
                                           y=windowHeight / 2 + 50, y2=windowHeight / 2 - 50)
        icon_array += [pyglet.sprite.Sprite(revive_icon, x=windowWidth / 2,
                                            y=windowHeight / 2, batch=batch, group=icon_layer)]
        # Tier 3
        upgrade_box_array += create_square(batch,
                                           x=2 * windowWidth / 3 - 50,
                                           x2=2 * windowWidth / 3 + 50,
                                           y=windowHeight / 3 - 50, y2=windowHeight / 3 + 50)
        icon_array += [pyglet.sprite.Sprite(revive_all_icon, x=2 * windowWidth / 3,
                                            y=windowHeight / 3, batch=batch, group=icon_layer)]
        upgrade_box_array += create_square(batch,
                                           x=2 * windowWidth / 3 - 50,
                                           x2=2 * windowWidth / 3 + 50,
                                           y=2 * windowHeight / 3 - 50,
                                           y2=2 * windowHeight / 3 + 50)

        icon_array += [pyglet.sprite.Sprite(charge_time_icon, x=2 * windowWidth / 3,
                                            y=2 * windowHeight / 3, batch=batch, group=icon_layer)]

        # Connections 1
        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 3 + 50, x2=windowWidth / 2,
                                           y=windowHeight / 3, y2=windowHeight / 3)
        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 3 + 50, x2=windowWidth / 2,
                                           y=2 * windowHeight / 3, y2=2 * windowHeight / 3)

        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 2, x2=windowWidth / 2,
                                           y=2 * windowHeight / 3, y2=windowHeight / 2 + 50)
        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 2, x2=windowWidth / 2,
                                           y=windowHeight / 3, y2=windowHeight / 2 - 50)
        # Connections 2
        upgrade_box_array += create_square(batch,
                                           x=2 * windowWidth / 3, x2=2 * windowWidth / 3,
                                           y=windowHeight / 2, y2=windowHeight / 3 + 50)
        upgrade_box_array += create_square(batch,
                                           x=2 * windowWidth / 3, x2=2 * windowWidth / 3,
                                           y=windowHeight / 2, y2=2 * windowHeight / 3 - 50)
        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 2 + 50, x2=2 * windowWidth / 3,
                                           y=windowHeight / 2, y2=windowHeight / 2)
        for upgrades in getPlayerPlanesUpgradesIcon("Peyton", "support_plane"):
            icon_array[upgrades[0]].color = (255, 5, 5)

    
    
    # if plane_choice_shopping == 1:
    #     planeName = "fast_plane"
    # elif plane_choice_shopping == 2:
    #     planeNmae = "damage_plane"
    # elif plane_choice_shopping == 3:
    #     planeName = "helicopter"
    # else:
    #     planeName = "support_plane"
    description.text = text
    description.x = windowWidth / 2 - description.content_width/2


    return [upgrade_box_array, icon_array]


# menu function
def menu():
    # Sound
    player.next_source()
    player.queue(background_music)
    player.play()

    # Graphics
    start_screen_batch = pyglet.graphics.Batch()

    start_map_sprite = pyglet.sprite.Sprite(start_map, x=windowWidth / 2, y=windowHeight / 2,
                                            batch=start_screen_batch,
                                            group=maps_layer)
    start_map_sprite.scale_x = windowWidth / start_map_sprite.width
    start_map_sprite.scale_y = windowHeight / start_map_sprite.height
    start_button_sprite = pyglet.sprite.Sprite(start_button, x= 2*windowWidth / 13, y=windowHeight / 4,
                                               batch=start_screen_batch,
                                               group=buttons_layer)
    store_button_sprite = pyglet.sprite.Sprite(store_button, x=8 * windowWidth / 13,
                                               y=windowHeight / 4,
                                               batch=start_screen_batch,
                                               group=buttons_layer)

    levels_button_sprite = pyglet.sprite.Sprite(levels_button, x=5 * windowWidth / 13,
                                                y=windowHeight / 4,
                                                batch=start_screen_batch,
                                                group=buttons_layer)
    exit_button_sprite = pyglet.sprite.Sprite(exit_button, x=11 * windowWidth / 13,
                                                y=windowHeight / 4,
                                                batch=start_screen_batch,
                                                group=buttons_layer)

    # level_select_square = create_square(start_screen_batch, x=windowWidth / 2 - 200,
    #                                     y=windowHeight / 4 - 40,
    #                                     x2=windowWidth / 2 + 200, y2=windowHeight / 4 + 40, width=2)

    # plane_1_label = pyglet.text.Label('Level Select', color=(0, 0, 0, 255),
    #                                   font_name='Times New Roman',
    #                                   font_size=50, group=buttons_layer,
    #                                   x=window.width / 2, y=windowHeight / 4 - 20,
    #                                   batch=start_screen_batch)
    # plane_1_label.x = plane_1_label.x - plane_1_label.content_width / 2

    sov_logo_sprite = pyglet.sprite.Sprite(sov_logo_image, x=windowWidth / 2,
                                           y=windowHeight * 3 / 4,
                                           batch=start_screen_batch,
                                           group=buttons_layer)

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        global mode
        if 2*windowWidth / 13 - 150 < x < (2* windowWidth / 13) + 150 and  (
                windowHeight / 4 - 50 < y < windowHeight / 4 + 50):  # start game
            inGame = True
            # live_batch = level_batch
            window.clear()
            # print(level_batch)
            mode = "game"
            pyglet.app.exit()
            # return
            # start()
        elif ((8 * windowWidth / 13 - 150) < x < (8 * windowWidth / 13) + 150) and (
                windowHeight / 4 - 50 < y < windowHeight / 4 + 50):  # goto store
            window.clear()
            mode = "store"
            pyglet.app.exit()
            # return
            # store_menu()
        elif ((5*windowWidth / 13 - 200) < x < (5*windowWidth / 13 + 200)) and (
                windowHeight / 4 - 40 < y < windowHeight / 4 + 40):  # goto store
            window.clear()
            mode = "level"
            pyglet.app.exit()
        elif ((11*windowWidth / 13 - 200) < x < (11*windowWidth / 13 + 200)) and (
                windowHeight / 4 - 40 < y < windowHeight / 4 + 40):  # goto store
            window.clear()
            mode = "end"
            pyglet.app.exit()
            # return
            # level_menu()

    # return

    @window.event
    def on_draw():
        window.clear()
        start_screen_batch.draw()

    pyglet.app.run()


def level_menu():
    player.next_source()
    player.queue(kicks)
    player.play()
    levels_array = getLevels(playerName)

    level_menu_batch = pyglet.graphics.Batch()
    text_layer = pyglet.graphics.OrderedGroup(0)
    check_layer = pyglet.graphics.OrderedGroup(1)

    def level_button(number, stars, completed=0):
        shape = pyglet.shapes.Circle(window.width * ((number - 1) % 3) / 3 + window.width / 6,
                                     (window.height / (1 + ((number - 1) // 3)) * 1 / 2) + 1 / 8 * window.height,
                                     100, color=(237, 177, 47),
                                     batch=level_menu_batch, group=buttons_layer)
        text = pyglet.text.Label(str(number), font_name='Comic Sans', font_size=100, group=text_layer,
                                 x=shape.x, y=shape.y, batch=level_menu_batch)
        text.x = text.x - (text.content_width / 2)
        text.y = text.y - (text.content_height / 3)
        if completed == 1:
            completed = check_off(number)
        return [shape, text, stars, completed]

    def show_stars(number, stars):
        text_stars = pyglet.text.Label("Stars: " + str(stars), font_name='Comic Sans', font_size=50, group=text_layer,
                                       x=(window.width * ((number - 1) % 3) / 3 + window.width / 6) - 100,
                                       y=(window.height / (1 + ((number - 1) // 3)) * 1 / 2) + 1 / 8 * window.height + 50,
                                       batch=level_menu_batch)
        return [text_stars]

    def check_off(number):
        strike_1 = pyglet.shapes.Line(window.width * ((number - 1) % 3) / 3 + window.width / 6,
                                      (window.height / (1 + ((number - 1) // 3)) * 1 / 2) + 1 / 8 * window.height - 95,
                                      window.width * ((number - 1) % 3) / 3 + window.width / 6 - 95,
                                      (window.height / (1 + ((number - 1) // 3)) * 1 / 2) + 1 / 8 * window.height,
                                      color=(0, 255, 0), width=10, batch=level_menu_batch, group=check_layer)
        strike_2 = pyglet.shapes.Line(window.width * ((number - 1) % 3) / 3 + window.width / 6,
                                      (window.height / (1 + ((number - 1) // 3)) * 1 / 2) + 1 / 8 * window.height - 95,
                                      window.width * ((number - 1) % 3) / 3 + window.width / 6 + 125,
                                      (window.height / (1 + ((number - 1) // 3)) * 1 / 2) + 1 / 8 * window.height + 100,
                                      color=(0, 255, 0), width=10, batch=level_menu_batch, group=check_layer)
        return [strike_1, strike_2]

    def lock_off(number):

        lock_sprite = pyglet.sprite.Sprite(lock_icon, x=(window.width * ((number - 1) % 3) / 3 + window.width / 6),
                                           y=(window.height / (1 + ((number - 1) // 3)) * 1 / 2) + 1 / 8 * window.height,
                                           batch=level_menu_batch,
                                           group=check_layer)
        return lock_sprite

    store_label = pyglet.text.Label('Level Selection',
                                    font_name='Times New Roman',
                                    font_size=50, group=buttons_layer,
                                    x=window.width / 2, y=window.height // 1.1,
                                    batch=level_menu_batch)
    store_label.x = store_label.x - store_label.content_width / 2
    level_map_sprite = pyglet.sprite.Sprite(start_map, batch=level_menu_batch, x=windowWidth / 2,
                                            y=windowHeight / 2, group=maps_layer)
    level_map_sprite.scale_x = windowWidth / level_map_sprite.width
    level_map_sprite.scale_y = windowHeight / level_map_sprite.height
    exit_button_sprite = pyglet.sprite.Sprite(x_button, x=windowWidth - x_button.anchor_x,
                                              y=windowHeight - x_button.anchor_y,
                                              batch=level_menu_batch,
                                              group=buttons_layer)

    stars_text = []
    level_1 = level_button(1, stars=levels_array[0][1], completed=levels_array[0][3])
    level_2 = level_button(2, stars=levels_array[1][1], completed=levels_array[1][3])
    level_3 = level_button(3, stars=levels_array[2][1], completed=levels_array[2][3])
    level_4 = level_button(4, stars=levels_array[3][1], completed=levels_array[3][3])
    level_5 = level_button(5, stars=levels_array[4][1], completed=levels_array[4][3])
    level_6 = level_button(6, stars=0)
    locks = []

    for i in range(len(levels_array)-1):
        if levels_array[i][4] != 1:
            locks += [lock_off(i + 2)]

    @window.event
    def on_draw():
        window.clear()
        level_menu_batch.draw()

    @window.event
    def on_mouse_motion(x, y, dx, dy):
        nonlocal stars_text
        for temp in stars_text:
            temp.delete()
        if level_1[0].x - 100 < x < level_1[0].x + 100 and level_1[0].y - 100 < y < level_1[0].y + 100:
            stars_text += show_stars(1, level_1[2])
        elif level_2[0].x - 100 < x < level_2[0].x + 100 and level_2[0].y - 100 < y < level_2[0].y + 100:
            stars_text += show_stars(2, level_2[2])
        elif level_3[0].x - 100 < x < level_3[0].x + 100 and level_3[0].y - 100 < y < level_3[0].y + 100:
            stars_text += show_stars(3, level_3[2])
        elif level_4[0].x - 100 < x < level_4[0].x + 100 and level_4[0].y - 100 < y < level_4[0].y + 100:
            stars_text += show_stars(4, level_4[2])
        elif level_5[0].x - 100 < x < level_5[0].x + 100 and level_5[0].y - 100 < y < level_5[0].y + 100:
            stars_text += show_stars(5, level_5[2])
        # level 6 doesnt have stars as it is the last level
        elif level_6[0].x - 100 < x < level_6[0].x + 100 and level_6[0].y - 100 < y < level_6[0].y + 100:
            stars_text += show_stars(6, level_6[2])

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        global mode
        global time
        if (windowWidth - x_button.width) < x < windowWidth and y > (
                windowHeight - x_button.height):  # clicking X button
            mode = "menu"
            pyglet.app.exit()
            # menu()
        elif level_1[0].x - 100 < x < level_1[0].x + 100 and level_1[0].y - 100 < y < level_1[0].y + 100:
            mode = "game"
            time = 0
            start(0)
        elif level_2[0].x - 100 < x < level_2[0].x + 100 and level_2[0].y - 100 < y < level_2[0].y + 100:
            mode = "game"
            time = 0
            start(1)
        elif level_3[0].x - 100 < x < level_3[0].x + 100 and level_3[0].y - 100 < y < level_3[0].y + 100:
            mode = "game"
            time = 0
            start(2)
        elif level_4[0].x - 100 < x < level_4[0].x + 100 and level_4[0].y - 100 < y < level_4[0].y + 100:
            mode = "game"
            time = 0
            start(3)
        elif level_5[0].x - 100 < x < level_5[0].x + 100 and level_5[0].y - 100 < y < level_5[0].y + 100:
            mode = "game"
            time = 0
            start(4)
        elif level_6[0].x - 100 < x < level_6[0].x + 100 and level_6[0].y - 100 < y < level_6[0].y + 100:
            mode = "game"
            time = 0
            start(5)

    def update(dt):
        level_menu_batch.draw()

    pyglet.clock.schedule_interval(update, 1 / 120.0)
    pyglet.app.run()


def store_menu():
    def item_buy(item):
        if (getPlayerCash("Peyton")[0][0] >= 3):
            if item[0] == 1:
                # print(item[1])
                if item[1] == 1 and len(getPlayerPlaneUpgrades("Peyton", "improved_movespeed", "fast_plane")) == 0:
                    createPlayerPlaneUpgrades("Peyton", "improved_movespeed", "fast_plane", 0)
                elif item[1] == 3 and len(getPlayerPlaneUpgrades("Peyton", "improved_bullet_damage", "fast_plane")) == 0:
                    createPlayerPlaneUpgrades("Peyton", "improved_bullet_damage", "fast_plane", 1)
                elif item[1] == 4 and len(getPlayerPlaneUpgrades("Peyton", "shorter_special_charge_time", "fast_plane")) == 0:
                    createPlayerPlaneUpgrades("Peyton", "shorter_special_charge_time", "fast_plane" , 2)
                elif item[1] == 6 and len(getPlayerPlaneUpgrades("Peyton", "improved_fire_rate", "fast_plane")) == 0:
                    createPlayerPlaneUpgrades("Peyton", "improved_fire_rate", "fast_plane" ,3)
                elif item[1] == 7 and len(getPlayerPlaneUpgrades("Peyton",
                                                                 "increased_special_damage", "fast_plane")) == 0:
                    createPlayerPlaneUpgrades("Peyton", "increased_special_damage", "fast_plane" ,4 )
                elif item[1] == 9 and len(getPlayerPlaneUpgrades("Peyton",
                                                                 "increase_dodge_bullets", "fast_plane")) == 0:
                    createPlayerPlaneUpgrades("Peyton", "increase_dodge_bullets", "fast_plane" ,5)
            elif item[0] == 2 :
                if item[1] == 1 and len(getPlayerPlaneUpgrades("Peyton", "improved_bullet_damage", "damage_plane")) == 0:
                    createPlayerPlaneUpgrades("Peyton", "improved_bullet_damage", "damage_plane", 0)
                elif item[1] == 3 and len(getPlayerPlaneUpgrades("Peyton", "bomb", "damage_plane")) == 0:
                    createPlayerPlaneUpgrades("Peyton", "bomb", "damage_plane" , 1)
                elif item[1] == 5 and len(getPlayerPlaneUpgrades("Peyton", "improved_bomb_damage", "damage_plane")) == 0:
                    createPlayerPlaneUpgrades("Peyton", "improved_bomb_damage", "damage_plane", 2)
                elif item[1] == 7 and len(getPlayerPlaneUpgrades("Peyton", "improved_bomb_fire_rate", "damage_plane")) == 0:
                    createPlayerPlaneUpgrades("Peyton", "improved_bomb_fire_rate", "damage_plane",3)
                elif item[1] == 9 and len(getPlayerPlaneUpgrades("Peyton", "triples_fire_rate", "damage_plane")) == 0:
                    createPlayerPlaneUpgrades("Peyton", "triples_fire_rate", "damage_plane", 4)
            elif item[0] == 3:
                if item[1] == 1 and len(getPlayerPlaneUpgrades("Peyton", "improved_collision_damage", "helicopter")) == 0:
                    createPlayerPlaneUpgrades("Peyton", "improved_collision_damage", "helicopter", 0)
                elif item[1] == 3 and len(getPlayerPlaneUpgrades("Peyton", "improved_health", "helicopter")) == 0:
                    createPlayerPlaneUpgrades("Peyton", "improved_health", "helicopter", 1)
                elif item[1] == 4 and len(getPlayerPlaneUpgrades("Peyton",
                                                                 "improved_movement_speed", "helicopter")) == 0:
                    createPlayerPlaneUpgrades("Peyton", "improved_movement_speed", "helicopter", 2)
                elif item[1] == 6 and len(getPlayerPlaneUpgrades("Peyton",
                                                                 "increase_special_time", "helicopter")) == 0:
                    createPlayerPlaneUpgrades("Peyton", "increase_special_time", "helicopter",3 )
                elif item[1] == 7 and len(getPlayerPlaneUpgrades("Peyton",
                                                                 "increased_special_damage", "helicopter")) == 0:
                    createPlayerPlaneUpgrades("Peyton", "increased_special_damage", "helicopter",4 )
                elif item[1] == 9 and len(getPlayerPlaneUpgrades("Peyton",
                                                                 "increased_damage_to_closer_enemies", "helicopter")) == 0:
                    createPlayerPlaneUpgrades("Peyton", "increased_damage_to_closer_enemies", "helicopter", 5)
            elif item[0] == 4:
                if item[1] == 1 and len(getPlayerPlaneUpgrades("Peyton", "improved_regen_rate", "support_plane")) == 0:
                    createPlayerPlaneUpgrades("Peyton", "improved_regen_rate", "support_plane", 0)
                elif item[1] == 3 and len(getPlayerPlaneUpgrades("Peyton", "regenerate_self", "support_plane")) == 0:
                    createPlayerPlaneUpgrades("Peyton", "regenerate_self", "support_plane", 1)
                elif item[1] == 5 and len(getPlayerPlaneUpgrades("Peyton", "revive_planes_full_health", "support_plane")) == 0:
                    createPlayerPlaneUpgrades("Peyton", "revive_planes_full_health", "support_plane", 2)
                elif item[1] == 7 and len(getPlayerPlaneUpgrades("Peyton", "shorter_special_charge_time", "support_plane")) == 0:
                    createPlayerPlaneUpgrades("Peyton", "shorter_special_charge_time", "support_plane", 3)
                elif item[1] == 9 and len(getPlayerPlaneUpgrades("Peyton", "revives_all_planes", "support_plane")) == 0:
                    createPlayerPlaneUpgrades("Peyton", "revives_all_planes", "support_plane", 4)
            Cash_Available_label.text = str(getPlayerCash("Peyton")[0][0])

    def get_upgrade_text(plane, item, text_color=(255, 255, 255, 255)):

        if plane == 1:
            if item == 1:
                store_label = pyglet.text.Label('Increased Movement Speed',
                                                font_name='Times New Roman',
                                                font_size=50, group=label_layer,
                                                x=windowWidth / 3, y=2 * windowHeight / 3+55,
                                                batch=store_menu_batch, color=text_color)
                store_label.x = store_label.x - store_label.content_width / 2
                return [store_label]
            elif item == 3:
                store_label = pyglet.text.Label('Increased Bullet Damage',
                                                font_name='Times New Roman',
                                                font_size=50, group=label_layer,
                                                x=windowWidth / 3, y=windowHeight / 3+55,
                                                batch=store_menu_batch, color=text_color)
                store_label.x = store_label.x - store_label.content_width / 2
                return [store_label]
            elif item == 4:
                store_label = pyglet.text.Label('Decreased Special Cooldown',
                                                font_name='Times New Roman',
                                                font_size=50, group=label_layer,
                                                x=windowWidth / 2, y=2 * windowHeight / 3+55,
                                                batch=store_menu_batch, color=text_color)
                store_label.x = store_label.x - store_label.content_width / 2
                return [store_label]
            elif item == 6:
                store_label = pyglet.text.Label('Increased Fire Rate',
                                                font_name='Times New Roman',
                                                font_size=50, group=label_layer,
                                                x=windowWidth / 2, y=windowHeight / 3+55,
                                                batch=store_menu_batch, color=text_color)
                store_label.x = store_label.x - store_label.content_width / 2
                return [store_label]
            elif item == 7:
                store_label = pyglet.text.Label('Increased Special Damage',
                                                font_name='Times New Roman',
                                                font_size=50, group=label_layer,
                                                x=2*windowWidth / 3, y=2 * windowHeight / 3+55,
                                                batch=store_menu_batch, color=text_color)
                store_label.x = store_label.x - store_label.content_width / 2
                return [store_label]
            elif item == 9:
                store_label = pyglet.text.Label('Chance to Dodge Bullets',
                                                font_name='Times New Roman',
                                                font_size=50, group=label_layer,
                                                x=2*windowWidth / 3, y=windowHeight / 3+55,
                                                batch=store_menu_batch, color=text_color)
                store_label.x = store_label.x - store_label.content_width / 2
                return [store_label]
        elif plane == 2:
            if item == 1:
                store_label = pyglet.text.Label('Increased Bullet Damage', font_name='Times New Roman', font_size=50, group=label_layer,
                                                x=windowWidth / 3, y=2 * windowHeight / 3+55, batch=store_menu_batch, color=text_color)
                store_label.x = store_label.x - store_label.content_width / 2
                return [store_label]
            elif item == 3:
                store_label = pyglet.text.Label('Added Bombs Every 5 Shots',
                                                font_name='Times New Roman',
                                                font_size=50, group=label_layer,
                                                x=windowWidth / 3, y=windowHeight / 3+55,
                                                batch=store_menu_batch, color=text_color)
                store_label.x = store_label.x - store_label.content_width / 2
                return [store_label]
            elif item == 5:
                store_label = pyglet.text.Label('Bombs Do More Damage',
                                                font_name='Times New Roman',
                                                font_size=50, group=label_layer,
                                                x=windowWidth / 2, y=windowHeight / 2+55,
                                                batch=store_menu_batch, color=text_color)
                store_label.x = store_label.x - store_label.content_width / 2
                return [store_label]
            elif item == 7:
                store_label = pyglet.text.Label('Increased Bomb Fire Rate',
                                                font_name='Times New Roman',
                                                font_size=50, group=label_layer,
                                                x=2*windowWidth / 3, y=2 * windowHeight / 3+55,
                                                batch=store_menu_batch, color=text_color)
                store_label.x = store_label.x - store_label.content_width / 2
                return [store_label]
            elif item == 9:
                store_label = pyglet.text.Label('Tripled Fire Rate',
                                                font_name='Times New Roman',
                                                font_size=50, group=label_layer,
                                                x=2*windowWidth / 3, y=windowHeight / 3+55,
                                                batch=store_menu_batch, color=text_color)
                store_label.x = store_label.x - store_label.content_width / 2
                return [store_label]
        elif plane == 3:
            if item == 1:
                store_label = pyglet.text.Label('Increased Collision Damage',
                                                font_name='Times New Roman',
                                                font_size=50, group=label_layer,
                                                x=windowWidth / 3, y=2 * windowHeight / 3+55,
                                                batch=store_menu_batch, color=text_color)
                store_label.x = store_label.x - store_label.content_width / 2
                return [store_label]
            elif item == 3:
                store_label = pyglet.text.Label('Increased Health',
                                                font_name='Times New Roman',
                                                font_size=50, group=label_layer,
                                                x=windowWidth / 3, y=windowHeight / 3+55,
                                                batch=store_menu_batch, color=text_color)
                store_label.x = store_label.x - store_label.content_width / 2
                return [store_label]
            elif item == 4:
                store_label = pyglet.text.Label('Increased Movement Speed',
                                                font_name='Times New Roman',
                                                font_size=50, group=label_layer,
                                                x=windowWidth / 2, y=2 * windowHeight / 3+55,
                                                batch=store_menu_batch, color=text_color)
                store_label.x = store_label.x - store_label.content_width / 2
                return [store_label]
            elif item == 6:
                store_label = pyglet.text.Label('Increased Special Duration',
                                                font_name='Times New Roman',
                                                font_size=50, group=label_layer,
                                                x=windowWidth / 2, y=windowHeight / 3+55,
                                                batch=store_menu_batch, color=text_color)
                store_label.x = store_label.x - store_label.content_width / 2
                return [store_label]
            elif item == 7:
                store_label = pyglet.text.Label('Increased Special Damage',
                                                font_name='Times New Roman',
                                                font_size=50, group=label_layer,
                                                x=2 * windowWidth / 3, y=2 * windowHeight / 3+55,
                                                batch=store_menu_batch, color=text_color)
                store_label.x = store_label.x - store_label.content_width / 2
                return [store_label]
            elif item == 9:
                store_label = pyglet.text.Label('Increased Damage to Close Enemies',
                                                font_name='Times New Roman',
                                                font_size=50, group=label_layer,
                                                x=2 * windowWidth / 3, y=windowHeight / 3+55,
                                                batch=store_menu_batch, color=text_color)
                store_label.x = store_label.x - store_label.content_width / 2
                return [store_label]
        elif plane == 4:
            if item == 1:
                store_label = pyglet.text.Label('Improved Regeneration',
                                                font_name='Times New Roman',
                                                font_size=50, group=label_layer,
                                                x=windowWidth / 3, y=2 * windowHeight / 3+55,
                                                batch=store_menu_batch, color=text_color)
                store_label.x = store_label.x - store_label.content_width / 2
                return [store_label]
            elif item == 3:
                store_label = pyglet.text.Label('Self Regenerating',
                                                font_name='Times New Roman',
                                                font_size=50, group=label_layer,
                                                x=windowWidth / 3, y=windowHeight / 3+55,
                                                batch=store_menu_batch, color=text_color)
                store_label.x = store_label.x - store_label.content_width / 2
                return [store_label]
            elif item == 5:
                store_label = pyglet.text.Label('Revives Planes With Full HP',
                                                font_name='Times New Roman',
                                                font_size=50, group=label_layer,
                                                x=windowWidth / 2, y=windowHeight / 2+55,
                                                batch=store_menu_batch, color=text_color)
                store_label.x = store_label.x - store_label.content_width / 2
                return [store_label]
            elif item == 7:
                store_label = pyglet.text.Label('Increased Special Damage',
                                                font_name='Times New Roman',
                                                font_size=50, group=label_layer,
                                                x=2 * windowWidth / 3, y=2 * windowHeight / 3+55,
                                                batch=store_menu_batch, color=text_color)
                store_label.x = store_label.x - store_label.content_width / 2
                return [store_label]
            elif item == 9:
                store_label = pyglet.text.Label('Revives All Planes At Once',
                                                font_name='Times New Roman',
                                                font_size=50, group=label_layer,
                                                x=2 * windowWidth / 3, y=windowHeight / 3+55,
                                                batch=store_menu_batch, color=text_color)
                store_label.x = store_label.x - store_label.content_width / 2
                return [store_label]
        return []

    player.next_source()
    player.queue(fortunate_son)
    player.play()

    store_menu_batch = pyglet.graphics.Batch()
    store_menu_sprite = pyglet.sprite.Sprite(store_map, x=windowWidth / 2, y=windowHeight / 2,
                                             batch=store_menu_batch,
                                             group=maps_layer)
    store_menu_sprite.scale_x = windowWidth / store_menu_sprite.width
    store_menu_sprite.scale_y = windowHeight / store_menu_sprite.height
    store_label = pyglet.text.Label('S T O R E',
                                    font_name='Times New Roman',
                                    font_size=50, group=buttons_layer,
                                    x=window.width / 2, y=window.height // 1.1,
                                    batch=store_menu_batch)
    store_label.x = store_label.x - store_label.content_width / 2
    Cash_Available_label = pyglet.text.Label( str(getPlayerCash("Peyton")[0][0]),
                                    font_name='Times New Roman',
                                    font_size=50, group=buttons_layer,
                                    x= 10, y=window.height // 1.1,
                                    batch=store_menu_batch)

    # plane_square_1 = create_square(store_menu_batch, x=windowWidth / 4 - 100, y=windowHeight * 0.80,
    #                                x2=windowWidth / 4 + 100, y2=windowHeight * 0.85, width=2)
    plane_1_label = pyglet.sprite.Sprite(plane1_button, group=buttons_layer,
                                         x=window.width / 8, y=window.height * 0.82,
                                         batch=store_menu_batch)
    # plane_1_label = pyglet.text.Label('P L A N E 1', color=(0, 0, 255, 255),
    #                                   font_name='Times New Roman',
    #                                   font_size=20, group=buttons_layer,
    #                                   x=window.width / 4, y=window.height * 0.82,
    #                                   batch=store_menu_batch)
    # plane_1_label.x = plane_1_label.x - plane_1_label.content_width / 2
    plane_2_label = pyglet.sprite.Sprite(plane2_button, group=buttons_layer,
                                         x=window.width * 3 / 8, y=window.height * 0.82,
                                         batch=store_menu_batch)
    plane_3_label = pyglet.sprite.Sprite(plane3_button, group=buttons_layer,
                                         x=window.width * 5 / 8, y=window.height * 0.82,
                                         batch=store_menu_batch)
    plane_4_label = pyglet.sprite.Sprite(plane4_button, group=buttons_layer,
                                         x=window.width * 7 / 8, y=window.height * 0.82,
                                         batch=store_menu_batch)

    exit_button_sprite = pyglet.sprite.Sprite(x_button, x=windowWidth - x_button.anchor_x,
                                              y=windowHeight - x_button.anchor_y,
                                              batch=store_menu_batch,
                                              group=buttons_layer)
    plane_choice_shopping = 1
    description = pyglet.text.Label("", font_name='Comic Sans', font_size=40,
                                 x=windowWidth / 2, y=50, batch=store_menu_batch, group=buttons_layer)
    description.color = (0, 0, 0, 255)
    temp_upgrades = shop_upgrade(plane_choice_shopping, store_menu_batch, description)
    store_menu_batch.draw()

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        global mode
        nonlocal temp_upgrades, plane_choice_shopping
        if windowWidth / 3 - 50 < x < windowWidth / 3 + 50 and windowHeight / 3 - 50 < y < windowHeight / 3 + 50:  # bottom left
            item_buy([plane_choice_shopping, 3])
        elif windowWidth / 3 - 50 < x < windowWidth / 3 + 50 and 2 * windowHeight / 3 - 50 < y < 2 * windowHeight / 3 + 50:  # top left
            item_buy([plane_choice_shopping, 1])
        elif windowWidth / 3 - 50 < x < windowWidth / 3 + 50 and windowHeight / 2 - 50 < y < windowHeight / 2 + 50:  # middle left
            item_buy([plane_choice_shopping, 2])
        elif windowWidth / 2 - 50 < x < windowWidth / 2 + 50 and 2 * windowHeight / 3 - 50 < y < 2 * windowHeight / 3 + 50:  # top middle
            item_buy([plane_choice_shopping, 4])
        elif windowWidth / 2 - 50 < x < windowWidth / 2 + 50 and windowHeight / 2 - 50 < y < windowHeight / 2 + 50:  # middle middle
            item_buy([plane_choice_shopping, 5])
        elif windowWidth / 2 - 50 < x < windowWidth / 2 + 50 and windowHeight / 3 - 50 < y < windowHeight / 3 + 50:  # bottom left
            item_buy([plane_choice_shopping, 6])
        elif 2 * windowWidth / 3 - 50 < x < 2 * windowWidth / 3 + 50 and 2 * windowHeight / 3 - 50 < y < 2 * windowHeight / 3 + 50:  # top right
            item_buy([plane_choice_shopping, 7])
        elif 2 * windowWidth / 3 - 50 < x < 2 * windowWidth / 3 + 50 and windowHeight / 2 - 50 < y < windowHeight / 2 + 50:  # middle right
            item_buy([plane_choice_shopping, 8])
        elif 2 * windowWidth / 3 - 50 < x < 2 * windowWidth / 3 + 50 and windowHeight / 3 - 50 < y < windowHeight / 3 + 50:  # bottom right
            item_buy([plane_choice_shopping, 9])

        elif windowWidth / 8 - 100 < x < windowWidth / 8 + 100 and windowHeight * 0.80 < y < windowHeight * 0.85:  # swap plane 1
            plane_choice_shopping = 1
            bullet_sound.play()
            temp_upgrades = shop_upgrade(1, store_menu_batch, description)
            
            # print("plane choice change to 1")
        elif windowWidth * 3 / 8 - 100 < x < windowWidth * 3 / 8 + 100 and windowHeight * 0.80 < y < windowHeight * 0.85:  # swap plane 2
            plane_choice_shopping = 2
            bullet_sound.play()
            temp_upgrades = shop_upgrade(2, store_menu_batch, description)

        elif windowWidth * 5 / 8 - 100 < x < windowWidth * 5 / 8 + 100 and windowHeight * 0.80 < y < windowHeight * 0.85:  # swap plane 3
            plane_choice_shopping = 3
            bullet_sound.play()
            temp_upgrades = shop_upgrade(3, store_menu_batch, description)

        elif windowWidth * 7 / 8 - 100 < x < windowWidth * 7 / 8 + 100 and windowHeight * 0.80 < y < windowHeight * 0.85:  # swap plane 3
            plane_choice_shopping = 4
            bullet_sound.play()
            temp_upgrades = shop_upgrade(4, store_menu_batch, description)

        elif (windowWidth - x_button.width) < x < windowWidth and y > (
                windowHeight - x_button.height):  # clicking X button
            mode = "menu"
            pyglet.app.exit()

    upgrade_text = []

    @window.event
    def on_mouse_motion(x, y, dx, dy):
        nonlocal upgrade_text
        for temp in upgrade_text:
            temp.delete()
        if windowWidth / 3 - 50 < x < windowWidth / 3 + 50 and windowHeight / 3 - 50 < y < windowHeight / 3 + 50:  # bottom left
            upgrade_text = get_upgrade_text(plane=plane_choice_shopping, item=3)
        elif windowWidth / 3 - 50 < x < windowWidth / 3 + 50 and 2 * windowHeight / 3 - 50 < y < 2 * windowHeight / 3 + 50:  # top left
            upgrade_text = get_upgrade_text(plane=plane_choice_shopping, item=1)
        elif windowWidth / 3 - 50 < x < windowWidth / 3 + 50 and windowHeight / 2 - 50 < y < windowHeight / 2 + 50:  # middle left
            upgrade_text = get_upgrade_text(plane=plane_choice_shopping, item=2)
        elif windowWidth / 2 - 50 < x < windowWidth / 2 + 50 and 2 * windowHeight / 3 - 50 < y < 2 * windowHeight / 3 + 50:  # top middle
            upgrade_text = get_upgrade_text(plane=plane_choice_shopping, item=4)
        elif windowWidth / 2 - 50 < x < windowWidth / 2 + 50 and windowHeight / 2 - 50 < y < windowHeight / 2 + 50:  # middle middle
            upgrade_text = get_upgrade_text(plane=plane_choice_shopping, item=5)
        elif windowWidth / 2 - 50 < x < windowWidth / 2 + 50 and windowHeight / 3 - 50 < y < windowHeight / 3 + 50:  # bottom left
            upgrade_text = get_upgrade_text(plane=plane_choice_shopping, item=6)
        elif 2 * windowWidth / 3 - 50 < x < 2 * windowWidth / 3 + 50 and 2 * windowHeight / 3 - 50 < y < 2 * windowHeight / 3 + 50:  # top right
            upgrade_text = get_upgrade_text(plane=plane_choice_shopping, item=7)
        elif 2 * windowWidth / 3 - 50 < x < 2 * windowWidth / 3 + 50 and windowHeight / 2 - 50 < y < windowHeight / 2 + 50:  # middle right
            upgrade_text = get_upgrade_text(plane=plane_choice_shopping, item=8)
        elif 2 * windowWidth / 3 - 50 < x < 2 * windowWidth / 3 + 50 and windowHeight / 3 - 50 < y < windowHeight / 3 + 50:  # bottom right
            upgrade_text = get_upgrade_text(plane=plane_choice_shopping, item=9)

    @window.event
    def on_draw():
        window.clear()
        store_menu_batch.draw()

    def update(dt):
        window.clear()
        store_menu_batch.draw()

    pyglet.clock.schedule_interval(update, 1 / 120.0)

    pyglet.app.run()


def end_screen():
    end_screen_batch = pyglet.graphics.Batch()
    # del game_objects
    # enemies = []
    # start_map = pyglet.sprite.Sprite(mapHandler.start_map.map_Image, batch=start_screen_batch,
    # group=maps_layer)
    end_sprite = pyglet.sprite.Sprite(end_image, x=windowWidth / 2, y=windowHeight * 3 / 4,
                                      batch=end_screen_batch,
                                      group=maps_layer)

    quit_button_sprite = pyglet.sprite.Sprite(quit_button, x=windowWidth / 2,
                                              y=start_button.anchor_y + 150,
                                              batch=end_screen_batch,
                                              group=buttons_layer)

    start_button_sprite = pyglet.sprite.Sprite(start_button, x=windowWidth / 2,
                                               y=start_button.anchor_y,
                                               batch=end_screen_batch,
                                               group=buttons_layer)

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        global mode
        global quitCheck
        global time
        if windowWidth / 2 - 150 < x < (windowWidth / 2) + 150 and y < 100:
            window.clear()
            # print(level_batch)
            mode = "game"
            quitCheck = False
            pyglet.app.exit()
            # start()

        if windowWidth / 2 - 150 < x < (windowWidth / 2) + 150 and 150 < y < 250:
            window.clear()
            mode = "menu"
            quitCheck = False
            time = 0
            pyglet.app.exit()
            # closeConnection()
            # window.close()
            # print(level_batch)

    @window.event
    def on_draw():
        window.clear()
        end_screen_batch.draw()

    pyglet.app.run()


paused = False


# Game function
def start(level_number=0):
    global mode
    global paused
    global finalTime
    level_batch = pyglet.graphics.Batch()
    paused_batch = pyglet.graphics.Batch()
    mouse_x = 1
    mouse_y = 1
    # setting layering
    plane_layer = pyglet.graphics.OrderedGroup(0)

    # these objects will be updated every tick
    game_objects = []
    enemies = []

    # load level data
    level_filepath = 'resources/level_scripts.json'

    with open(level_filepath) as f:
        level = json.load(f)[level_number]

    with open(level_filepath) as f:
        scores = json.load(f)[6]

    # Score Handling
    score_obj = {'score': 0, 'target_score': scores[level_number]['total_score']}
    #label = pyglet.text.Label('Score: ' + str(score_obj['score']),
    #                          font_name='Times New Roman',
    #                          font_size=24, group=buttons_layer,
    #                          x=window.width - 200, y=window.height // 2, batch=level_batch)

    # initializing plane handler which holds all the planes
    planeHandler = PlayerPlaneHandler(getPlayerPlanes(playerName), batch=level_batch,
                                      group=plane_layer)
    # createPlayerPlaneUpgrades("Peyton", "support_plane", "improved_movespeed")
    for i in planeHandler.getAllPlanes():
        i.add_upgrades(getPlayerPlanesUpgrades("Peyton", i.get_name()))
    game_objects += planeHandler.getAllPlanes()

    #health = pyglet.text.Label('Health: ' + str(planeHandler.getActivePlane().health),
    #                           font_name='Times New Roman',
    #                           font_size=24, group=buttons_layer,
    #                           x=window.width - 200, y=(window.height // 2) - 50, batch=level_batch)

    pause_button_sprite = pyglet.sprite.Sprite(resume_button, x=windowWidth / 2, y=windowHeight / 4,
                                               batch=paused_batch)
    quit_button_sprite = pyglet.sprite.Sprite(quit_button, x=windowWidth / 2, y=windowHeight * 2 / 4,
                                              batch=paused_batch)

    count = 0
    planeIcons = []
    healthBarIcons = []
    # print("peyton")
    # print(len(planeHandler.getAllPlanes()))
    for i in planeHandler.getAllPlanes():
        # print(count)
        planeIcons.append(pyglet.sprite.Sprite(i.getImage(), x=windowWidth - 30,
                                               y=windowHeight / 2 - 100 * count,
                                               batch=level_batch,
                                               group=buttons_layer))
        planeIcons[count].scale = i.get_width / windowWidth
        healthBarIcons.append(pyglet.sprite.Sprite(healthbar_7, x=windowWidth - 30,
                                                   y=windowHeight / 2 - 50 - 100 * count,
                                                   batch=level_batch,
                                                   group=buttons_layer))
        # planeIcons[count].scale_y = windowHeight / i.get_height
        count += 1

    # planeTest = pyglet.sprite.Sprite(planeHandler.getActivePlane().getImage(), x=windowWidth/2,
    #                                         y=windowHeight/2 - 200,
    #                                         batch=level_batch,
    #                                         group=buttons_layer)

    # HerePeyton

    # functions to add enemy objects to game objects
    def enemy_fire(dt, enemy, name):
        if (enemy.canFire and not enemy.dead):
            if (enemy.fire_type and name == 'target_plane'):
                enemy.target_plane(planeHandler.getActivePlane())
            else:
                getattr(enemy, name)()

    def enemy_fire_list(dt, enemy, fire_type):
        curr_time = 0
        for fire in fire_type:
            new_enemy.fire_type = fire
            for i in range(int(fire['duration'] // fire['interval'])):
                pyglet.clock.schedule_once(enemy_fire, curr_time, enemy=new_enemy, name=fire['name'])
                curr_time += fire['interval']

    def add_enemy(dt, enemy):
        game_objects.append(enemy)
        enemies.append(enemy)
        enemy.visible = True
        if (enemy.x == -500):
            enemy.x = planeHandler.getActivePlane().x

    # read level data
    for wave in level:
        for enemy_count in range(wave['enemy_count']):
            img = eval('resources.' + wave['enemy_obj']['img'])
            hp = wave['enemy_obj']['hp']
            new_enemy = Enemy(img, hp, batch=level_batch, group=plane_layer, **wave['enemy_obj']['kwargs'])
            if (wave['enemy_obj']['img'] == "enemy_boss"):
                new_enemy.boss = True
            new_enemy.movement = wave.get('movement', {"name": 'move_not'})
            fire_type = wave.get('fire')
            new_enemy.x += enemy_count * wave.get('spawn_dx', 0)
            new_enemy.y += enemy_count * wave.get('spawn_dy', 0)
            new_enemy.visible = False
            if (new_enemy.movement['name'] == 'move_down_follow'):
                new_enemy.x = -500  # outside value to check for plane follow
            if type(fire_type) is list:
                new_enemy.canFire = True
                repeat_fire_interval = sum([f['duration'] for f in fire_type])
                pyglet.clock.schedule_interval(enemy_fire_list, repeat_fire_interval, enemy=new_enemy, fire_type=fire_type)
            elif (fire_type):
                new_enemy.fire_type = fire_type
                new_enemy.canFire = True
                pyglet.clock.schedule_interval(enemy_fire, new_enemy.fire_type['interval'], enemy=new_enemy,
                                               name=new_enemy.fire_type['name'])
                # pyglet.clock.schedule_interval(new_enemy.enemyFire,
                # wave['fire']['interval'], planeHandler.getActivePlane())
            pyglet.clock.schedule_once(add_enemy, delay=wave['spawn_time'] + enemy_count * wave['interval'], enemy=new_enemy)

    # initialize wave
    # finalTime = level[-1]['spawn_time'] + (level[-1]['enemy_count'] * level[-1]['interval']) + 5
    finalTime = scores[level_number]['end_time']
    # testTime = scores[level_number]
    print(finalTime)
    # initializing the background
    level_map_object = PhysicalObject(level_map, x=windowWidth / 2, batch=level_batch,
                                      group=maps_layer)
    level_map_object.level_map_height = windowHeight
    level_map_object.y = level_map_object.height / 2
    level_map_object.scale_x = windowWidth / level_map_object.width
    # level_map_object.wrap = False
    # level_map_object.bind = False
    game_objects.append(level_map_object)
    level_map_object.velocity_y = -1

    # initialize the exit button
    # exit_button_sprite = pyglet.sprite.Sprite(x_button, x=windowWidth - x_button.anchor_x,
    #                                           y=windowHeight - x_button.anchor_y,
    #                                           batch=level_batch,
    #                                           group=buttons_layer)

    def mouse_location_update(x, y):
        nonlocal mouse_x
        nonlocal mouse_y
        mouse_x = x
        mouse_y = y

    @window.event
    def on_mouse_motion(x, y, dx, dy):
        if paused == False:
            mouse_location_update(x, y)

    # key press event
    @window.event
    def on_key_press(symbol, modifier):
        global paused
        if symbol == pyglet.window.key.P:
            paused = not paused
        elif paused == False:
            currPlane = planeHandler.getActivePlane()
            if symbol == pyglet.window.key._1:
                # planeHandler.getActivePlane(1).x = currPlane.x
                planeHandler.setActivePlane(0, currPlane)
            if symbol == pyglet.window.key._2:
                # planeHandler.getActivePlane(0).x = currPlane.x
                if (planeHandler.getActivePlane().name == "fast_plane"):
                    for obj in game_objects:
                        if obj.is_bullet:
                            if obj.is_laser:
                                obj.dead = True
                                obj.visible = False
                planeHandler.setActivePlane(1, currPlane)
            if symbol == pyglet.window.key._3:
                # planeHandler.getActivePlane(0).x = currPlane.x
                if (planeHandler.getActivePlane().name == "fast_plane"):
                    for obj in game_objects:
                        if obj.is_bullet:
                            if obj.is_laser:
                                obj.dead = True
                                obj.visible = False
                planeHandler.setActivePlane(2, currPlane)
            if symbol == pyglet.window.key._4:
                # planeHandler.getActivePlane(0).x = currPlane.x
                if (planeHandler.getActivePlane().name == "fast_plane"):
                    for obj in game_objects:
                        if obj.is_bullet:
                            if obj.is_laser:
                                obj.dead = True
                                obj.visible = False
                planeHandler.setActivePlane(3, currPlane)
            if symbol == pyglet.window.key.E:
                planeHandler.autoFire = not planeHandler.autoFire
        
                #print("e pressed")

    @window.event
    def on_mouse_drag(x, y, dx, dy, button, modifiers):
        if paused == False:
            mouse_location_update(x, y)

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        global mode
        global quitCheck
        global paused
        if paused == False:
            # if (windowWidth - x_button.width) < x < windowWidth and y > (
            #         windowHeight - x_button.height):  # clicking X button
            #     # for obj in game_objects:
            #     #        game_objects.remove(obj)
            #     # for enemy in enemies:
            #     #    enemies.remove(enemy)
            #     # del game_objects
            #     # del enemies
            #     # mode = "quit"
            #     paused = not paused
            # pyglet.app.exit()
            # end_screen(0)
            # window.clear()

            if (button == 1):
                planeHandler.getActivePlane().fire(mouse_x, mouse_y)
            if (button == 4):
                if (len(planeHandler.deadPlaneNum) != 0 and planeHandler.getActivePlane().planeNum == 4
                        and planeHandler.getActivePlane().canRevive == True):
                    revivePlane()
                elif (planeHandler.getActivePlane().planeNum != 4):
                    planeHandler.getActivePlane().specialAbilityFire(mouse_x, mouse_y)
        else:
            if windowWidth / 2 - 150 < x < (
                    windowWidth / 2) + 150 and windowHeight * 2 / 4 - 50 < y < windowHeight * 2 / 4 + 50:  # quitButton
                paused = False
                mode = "menu"
                quitCheck = False
                all_dead = False
                all_dead = False
                for plane in planeHandler.getAllPlanes():
                    plane.health = plane.maxHealth
                    plane.dead = False
                for obj in game_objects:
                    game_objects.remove(obj)
                for enemy in enemies:
                    enemies.remove(enemy)
                obj.update(1)
                pyglet.app.exit()
            # live_batch = level_batch
            # print(level_batch)
            if windowWidth / 2 - 150 < x < (
                    windowWidth / 2) + 150 and windowHeight / 4 - 50 < y < windowHeight / 4 + 50:  # ResumeButtons
                paused = False

        # print(game_objects)

    @window.event
    def on_draw():
        global quitCheck
        global mode
        global time
        global finalTime
        if quitCheck == True:
            # print ("this is running IDK")
            mode = "quit"
            # planeHandler.autoFire = False
            quitCheck = False
            all_dead = False
            all_dead = False
            for plane in planeHandler.getAllPlanes():
                plane.health = plane.maxHealth
                plane.dead = False
            for obj in game_objects:
                game_objects.remove(obj)
            for enemy in enemies:
                enemies.remove(enemy)
            # print(dir())
            # obj.update(1)
            # window.clear()
            pyglet.clock.unschedule(add_enemy)
            pyglet.clock.unschedule(enemy_fire)
            pyglet.clock.unschedule(update)

            currPercent = score_obj['score']/score_obj['target_score']
            if (currPercent >= 0.7):
                starVal = 10
            elif (currPercent >= 0.6):
                starVal = 8
            elif (currPercent >= 0.5):
                starVal = 6
            elif (currPercent >= 0.4):
                starVal = 4
            else:
                starVal = 0

            if (currPercent >= 0.4):
                if (level_number == 0 and len(getPlayerPlane("Peyton", "helicopter")) == 0):
                    createPlayerPlanes("Peyton", "helicopter")
                    print("got here")
                if (level_number == 2 and len(getPlayerPlane("Peyton", "support_plane")) == 0):
                    createPlayerPlanes("Peyton", "support_plane")
            #print(currPercent)
            # return
            time = 0
            updateLevelComplete(level_number +1, starVal, score_obj['score'], "Peyton")
            pyglet.app.exit()
        if paused == False:
            window.clear()
            level_batch.draw()
            #circle = pyglet.shapes.Circle(planeHandler.getActivePlane().x, planeHandler.getActivePlane().y,
            #                              planeHandler.getActivePlane().collisionRadius, color=(50, 225, 30), batch=level_batch)
            #circle.opacity = 100

            # rotorCircle = pyglet.shapes.Circle(planeHandler.getActivePlane().x, planeHandler.getActivePlane().y,
            #                             planeHandler.getActivePlane().rotorRadius, color=(255, 255, 255), batch=level_batch)

            # rotorCircle.opacity = 100
            #for enemy in enemies:
            #    if enemy.boss == True and enemy.dead == False:
            #        rectangle = pyglet.shapes.Rectangle(enemy.x - enemy.image.width / 4, enemy.y - enemy.image.height / 4,
            #                                            enemy.image.width / 2, enemy.image.height / 2,
            #                                            color=(50, 225, 30), batch=level_batch)
            #        rectangle.opacity = 100
            #        rectangle.draw()

            # circle.draw()
            # rotorCircle.draw()
        else:
            window.clear()
            paused_batch.draw()

    def checkEnd():
        # global mode
        global quitCheck
        currentPlane = planeHandler.getActivePlane()
        planeTemp = -1
        for plane in planeHandler.getAllPlanes():
            if (plane.dead == False):
                planeTemp = plane.planeNum
                break
        if (planeTemp != -1):
            quitCheck = False
            pyglet.clock.schedule_once(switchDeadPlane, num=planeTemp - 1, currPlane=currentPlane, delay=0.1)  # planeHandler.prevPlane
        else:
            # print('bug here?')
            # print(dir())
            quitCheck = True

            # planeHandler.autoFire = False

    def revivePlane():
        suppPlane = planeHandler.getActivePlane()
        suppPlane.canRevive = False
        suppPlane.specialAbilityFire(mouse_x, mouse_y)
        # pyglet.clock.schedule_once(suppPlane.enableSpecialAbilityShoot, suppPlane.special_ability_shoot_speed * suppPlane.special_ability_time_multiplier)
        if (suppPlane.revAll == True):
            while (len(planeHandler.deadPlaneNum) > 0):
                currPlane = planeHandler.getPlaneByNum(planeHandler.deadPlaneNum.pop(0))
                currPlane.dead = False
                currPlane.health = math.ceil(currPlane.maxHealth * planeHandler.getActivePlane().revivePercentage)
                game_objects.append(currPlane)
        else:
            currPlane = planeHandler.getPlaneByNum(planeHandler.deadPlaneNum.pop(0))
            currPlane.dead = False
            currPlane.health = math.ceil(currPlane.maxHealth * planeHandler.getActivePlane().revivePercentage)
            game_objects.append(currPlane)
        # print(game_objects)

    def switchDeadPlane(dt, num, currPlane):
        if (planeHandler.getActivePlane().name == "fast_plane"):
            for obj in game_objects:
                if obj.is_bullet:
                    if obj.is_laser:
                        obj.dead = True
                        obj.visible = False

        if (planeHandler.getActivePlane().health <= 0):
            planeHandler.deadPlaneNum.append(planeHandler.getActivePlane().planeNum)
        planeHandler.setActivePlane(num, currPlane)

    def regeneratePlane(dt, selfHeal):
        low = 2.0
        planeNum = 0
        if (planeHandler.getActivePlane().planeNum == 4):
            for plane in planeHandler.getAllPlanes():
                if ((plane.health / plane.maxHealth) < low) and plane.dead == False:
                    low = plane.health / plane.maxHealth
                    planeNum = plane.planeNum
            if (low < 1):
                planeHandler.getPlaneByNum(planeNum).health += planeHandler.getPlaneByNum(4).regen

        elif (planeHandler.getActivePlane().planeNum != 4 and planeHandler.getPlaneByNum(4).selfHeal == True
              and planeHandler.getPlaneByNum(4).health < planeHandler.getPlaneByNum(4).maxHealth):
            planeHandler.getPlaneByNum(4).health += planeHandler.getPlaneByNum(4).regen

        planeHandler.getPlaneByNum(4).heal = True

    def handle_move(dt):

        # player plane
        vector_x = mouse_x - planeHandler.getActivePlane().x
        vector_y = mouse_y - planeHandler.getActivePlane().y
        magnitude_velocity = math.sqrt(vector_x ** 2 + vector_y ** 2)
        if (
                magnitude_velocity >= 200 and planeHandler.getActivePlane().x <= user32.GetSystemMetrics(
            0) and planeHandler.getActivePlane().x >= 0):
            unit_x = vector_x / magnitude_velocity
            unit_y = vector_y / magnitude_velocity

            planeHandler.getActivePlane().velocity_x = unit_x * planeHandler.getActivePlane().moveSpeed * dt * 0.8
            planeHandler.getActivePlane().velocity_y = unit_y * planeHandler.getActivePlane().moveSpeed * dt * 0.8
        elif (
                magnitude_velocity >= 30 and magnitude_velocity <= 200 and planeHandler.getActivePlane().x <= user32.GetSystemMetrics(
            0) and planeHandler.getActivePlane().x >= 0):
            unit_x = vector_x / magnitude_velocity
            unit_y = vector_y / magnitude_velocity

            planeHandler.getActivePlane().velocity_x = unit_x * planeHandler.getActivePlane().moveSpeed * dt
            planeHandler.getActivePlane().velocity_y = unit_y * planeHandler.getActivePlane().moveSpeed * dt
        else:
            planeHandler.getActivePlane().velocity_x = 0
            planeHandler.getActivePlane().velocity_y = 0
        if (planeHandler.getActivePlane().laser):
            planeHandler.getActivePlane().laser.x = planeHandler.getActivePlane().x
            planeHandler.getActivePlane().laser.y = planeHandler.getActivePlane().y +100
            # planeHandler.getActivePlane().laser.velocity_x = planeHandler.getActivePlane().velocity_x
            # planeHandler.getActivePlane().laser.velocity_y = planeHandler.getActivePlane().velocity_y

    def checkCollision():
        global quitCheck
        for obj in game_objects:
            if (obj.dead == True):
                if obj.is_enemy == True:
                    # enemies.remove(obj)
                    if (obj.destroyed == True):
                        if (obj.boss == True):
                            score_obj['score'] += 100
                        else:
                            score_obj['score'] += 1

                        #label.text = 'Score: ' + str(score_obj['score'])

                        print(score_obj)
                        if score_obj['score'] >= score_obj['target_score']:  # change this to change the required score to win
                            # pyglet.clock.schedule_once(end_screen, 1)
                            # quitCheck = True
                            print("game end")

                game_objects.remove(obj)

            if (obj.is_enemy):
                if (obj.boss == True):
                    if (planeHandler.getActivePlane().name == "helicopter"):
                        if (obj.boss_collision_radius(planeHandler.getActivePlane(), planeHandler.getActivePlane().rotorRadius)):
                            obj.health = obj.health - planeHandler.getActivePlane().rotorDamage
                            obj.color = (255, 100, 100)
                            pyglet.clock.schedule_once(obj.revert_color, 0.1)
                    if (obj.boss_collision_radius(planeHandler.getActivePlane(), planeHandler.getActivePlane().collisionRadius)):
                        planeHandler.getActivePlane().handle_collision_with(obj)
                else:
                    if (planeHandler.getActivePlane().name == "helicopter"):
                        if (obj.collides_with_rotor(planeHandler.getActivePlane())):
                            obj.health = obj.health - planeHandler.getActivePlane().rotorDamage
                            obj.color = (255, 100, 100)
                            pyglet.clock.schedule_once(obj.revert_color, 0.1)

                    if (obj.collides_with(planeHandler.getActivePlane()) and planeHandler.getActivePlane().damageable == True):
                        planeHandler.getActivePlane().handle_collision_with(obj)

            if (obj.is_bullet):
                if (obj.is_enemyBullet):
                    if (planeHandler.getActivePlane().collides_with(obj) == True and planeHandler.getActivePlane().damageable == True):
                        planeHandler.getActivePlane().handle_collision_with(obj)
                        # updateHealthBar()
                else:
                    for enemyObj in enemies:
                        if (enemyObj.boss == True):
                            if (enemyObj.boss_collision(obj) == True):
                                enemyObj.handle_collision_with(obj)
                        elif (enemyObj.collides_with(obj) == True):
                            enemyObj.handle_collision_with(obj)

    def checkHeal():
        for i in planeHandler.getAllPlanes():
            if i.get_name() == "support_plane" and i.get_can_heal() == True:
                pyglet.clock.schedule_once(regeneratePlane, 1, False)
                i.heal = False
                # updateHealthBar()

    # def rotorCollide(dt, obj, damage):
    #    print('before: ' + str(obj.health))
    #    obj.health = obj.health - damage
    #    print('after: ' + str(obj.health))

    def updateHealthBar():
        count = 0
        for i in planeHandler.getAllPlanes():
            if i.maxHealth * 7 / 8 < i.health:
                healthBarIcons[count].image = healthbar_7
            elif i.maxHealth * 6 / 8 < i.health:
                healthBarIcons[count].image = healthbar_6
            elif i.maxHealth * 5 / 8 < i.health:
                healthBarIcons[count].image = healthbar_5
            elif i.maxHealth * 4 / 8 < i.health:
                healthBarIcons[count].image = healthbar_4
            elif i.maxHealth * 3 / 8 < i.health:
                healthBarIcons[count].image = healthbar_3
            elif i.maxHealth * 2 / 8 < i.health:
                healthBarIcons[count].image = healthbar_2
            elif i.maxHealth * 0 / 8 < i.health:
                healthBarIcons[count].image = healthbar_1
            else:
                healthBarIcons[count].image = healthbar_0
            count += 1
            # peytonhere

    def update(dt):
        global time
        global finalTime
        global mode
        global quitCheck
        # print(quitCheck)
        # print(enemies)
        # print(time)
        # print(finalTime)
        # print(planeHandler.autoFire)
        # print(mode)
        # print(game_objects)
        # print(enemies)
        for enemy in enemies:
            if enemy.boss == True and enemy.dead == False:
                finalTime += dt
        if (time >= finalTime):  # and len(enemies) == 0:
            # mode = 'menu'
            planeHandler.autoFire = False
            quitCheck = True
            # modeCheck()
        if paused == False:
            time += dt
            if (mode != "game"):
                planeHandler.autoFire = False
                # return
            # print(time)
            updateHealthBar()
            handle_move(dt)
            checkCollision()
            if (planeHandler.getActivePlane().health <= 0):
                planeHandler.getActivePlane().dead = True
                checkEnd()
            checkHeal()
            if (planeHandler.autoFire and mode == "game"):
                planeHandler.getActivePlane().fire(mouse_x, mouse_y)

            to_add = []
            for obj in game_objects:
                if obj.dead:
                    game_objects.remove(obj)
                obj.update(1)

                to_add.extend(obj.new_objects)
                obj.new_objects = []
            # Add new objects to the list
            game_objects.extend(to_add)

            #health.text = 'Health: ' + str(planeHandler.getActivePlane().health)

    # print(dir())
    pyglet.clock.schedule_interval(update, 1 / 120.0)

    pyglet.app.run()


if __name__ == '__main__':
    init()
