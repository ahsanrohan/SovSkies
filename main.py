from playerPlaneHandler import *
from pyglet.gl import *
from resources import *
from physicalObject import *
from enemy import *
import math
import pyglet
from longTermData import *
import time

# createGame()


window = pyglet.window.Window(fullscreen=True)
windowWidth = window.width
windowHeight = window.height
maps_layer = pyglet.graphics.OrderedGroup(-2)
buttons_layer = pyglet.graphics.OrderedGroup(-1)

playerName = "Peyton"


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
    # createPlayer("Peyton")
    # createPlayerPlanes("Peyton", "oldy")
    #createPlaneUpgradeTable()

    getPlayerPlanes(playerName)
    menu()


def shop_upgrade(plane_choice_shopping, batch):
    upgrade_box_array = []
    if plane_choice_shopping == 1:
        # Tier 1
        upgrade_box_array += create_square(batch, x=windowWidth / 3 - 50,
                                           y=windowHeight / 3 - 50,
                                           x2=windowWidth / 3 + 50, y2=windowHeight / 3 + 50)
        upgrade_box_array += create_square(batch, x=windowWidth / 3 - 50,
                                           y=2 * windowHeight / 3 - 50,
                                           x2=windowWidth / 3 + 50,
                                           y2=2 * windowHeight / 3 + 50)
        # Tier 2
        upgrade_box_array += create_square(batch, x=windowWidth / 2 - 50,
                                           y=windowHeight / 3 - 50,
                                           x2=windowWidth / 2 + 50, y2=windowHeight / 3 + 50)
        upgrade_box_array += create_square(batch, x=windowWidth / 2 - 50,
                                           y=2 * windowHeight / 3 - 50,
                                           x2=windowWidth / 2 + 50,
                                           y2=2 * windowHeight / 3 + 50)
        # Tier 3
        upgrade_box_array += create_square(batch, x=2 * windowWidth / 3 - 50,
                                           y=windowHeight / 2 - 50,
                                           x2=2 * windowWidth / 3 + 50,
                                           y2=windowHeight / 2 + 50)

        # Connections
        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 3 + 50, x2=windowWidth / 2 - 50,
                                           y=windowHeight / 3, y2=windowHeight / 3)
        upgrade_box_array += create_square(batch, x=windowWidth / 3 + 50,
                                           x2=windowWidth / 2 - 50,
                                           y=2 * windowHeight / 3, y2=2 * windowHeight / 3)
        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 2 + 50, x2=2 * windowWidth / 3,
                                           y=2 * windowHeight / 3, y2=2 * windowHeight / 3)
        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 2 + 50, x2=2 * windowWidth / 3,
                                           y=windowHeight / 3, y2=windowHeight / 3)
        upgrade_box_array += create_square(batch,
                                           x=2 * windowWidth / 3, x2=2 * windowWidth / 3,
                                           y=windowHeight / 2 - 50, y2=windowHeight / 3)
        upgrade_box_array += create_square(batch,
                                           x=2 * windowWidth / 3, x2=2 * windowWidth / 3,
                                           y=windowHeight / 2 + 50, y2=2 * windowHeight / 3)
    if plane_choice_shopping == 2:
        # Tier 1
        upgrade_box_array = create_square(batch, x=windowWidth / 3 - 50,
                                          y=windowHeight / 3 - 50,
                                          x2=windowWidth / 3 + 50, y2=windowHeight / 3 + 50)
        upgrade_box_array += create_square(batch, x=windowWidth / 3 - 50,
                                           y=2 * windowHeight / 3 - 50,
                                           x2=windowWidth / 3 + 50,
                                           y2=2 * windowHeight / 3 + 50)
        # Tier 2
        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 2 - 50, x2=windowWidth / 2 + 50,
                                           y=windowHeight / 2 + 50, y2=windowHeight / 2 - 50)

        # Tier 3
        upgrade_box_array += create_square(batch,
                                           x=2 * windowWidth / 3 - 50,
                                           x2=2 * windowWidth / 3 + 50,
                                           y=windowHeight / 3 - 50, y2=windowHeight / 3 + 50)
        upgrade_box_array += create_square(batch,
                                           x=2 * windowWidth / 3 - 50,
                                           x2=2 * windowWidth / 3 + 50,
                                           y=2 * windowHeight / 3 - 50,
                                           y2=2 * windowHeight / 3 + 50)

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
    if plane_choice_shopping == 3:
        # Tier 1
        upgrade_box_array = create_square(batch,
                                          x=windowWidth / 3 - 50, x2=windowWidth / 3 + 50,
                                          y=windowHeight / 2 - 50, y2=windowHeight / 2 + 50)
        # Tier 2
        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 2 - 50, x2=windowWidth / 2 + 50,
                                           y=2 * windowHeight / 3 + 50,
                                           y2=2 * windowHeight / 3 - 50)
        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 2 - 50, x2=windowWidth / 2 + 50,
                                           y=windowHeight / 3 + 50, y2=windowHeight / 3 - 50)

        # Tier 3
        upgrade_box_array += create_square(batch,
                                           x=2 * windowWidth / 3 - 50,
                                           x2=2 * windowWidth / 3 + 50,
                                           y=windowHeight / 3 - 50, y2=windowHeight / 3 + 50)
        upgrade_box_array += create_square(batch,
                                           x=2 * windowWidth / 3 - 50,
                                           x2=2 * windowWidth / 3 + 50,
                                           y=2 * windowHeight / 3 - 50,
                                           y2=2 * windowHeight / 3 + 50)

        # Connections 1
        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 3 + 50, x2=windowWidth / 2,
                                           y=windowHeight / 2, y2=windowHeight / 2)

        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 2, x2=windowWidth / 2,
                                           y=2 * windowHeight / 3 - 50, y2=windowHeight / 2)
        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 2, x2=windowWidth / 2,
                                           y=windowHeight / 3 + 50, y2=windowHeight / 2)
        # Connections 2
        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 2 + 50, x2=2 * windowWidth / 3 - 50,
                                           y=windowHeight / 3, y2=windowHeight / 3)
        upgrade_box_array += create_square(batch,
                                           x=windowWidth / 2 + 50, x2=2 * windowWidth / 3 - 50,
                                           y=2 * windowHeight / 3, y2=2 * windowHeight / 3)

    return upgrade_box_array


# menu funtion
def menu():
    start_screen_batch = pyglet.graphics.Batch()

    start_map_sprite = pyglet.sprite.Sprite(start_map, x=windowWidth / 2, y=windowHeight / 2,
                                            batch=start_screen_batch,
                                            group=maps_layer)
    start_map_sprite.scale_x = windowWidth / start_map_sprite.width
    start_map_sprite.scale_y = windowHeight / start_map_sprite.height
    start_button_sprite = pyglet.sprite.Sprite(start_button, x=windowWidth / 4, y=windowHeight / 4,
                                               batch=start_screen_batch,
                                               group=buttons_layer)
    store_button_sprite = pyglet.sprite.Sprite(store_button, x=3 * windowWidth / 4,
                                               y=windowHeight / 4,
                                               batch=start_screen_batch,
                                               group=buttons_layer)

    level_select_square = create_square(start_screen_batch, x=windowWidth / 2 - 200,
                                        y=windowHeight / 4 - 40,
                                        x2=windowWidth / 2 + 200, y2=windowHeight / 4 + 40, width=2)

    plane_1_label = pyglet.text.Label('Level Select', color=(0, 0, 0, 255),
                                      font_name='Times New Roman',
                                      font_size=50, group=buttons_layer,
                                      x=window.width / 2, y=windowHeight / 4 - 20,
                                      batch=start_screen_batch)
    plane_1_label.x = plane_1_label.x - plane_1_label.content_width / 2

    sov_logo_sprite = pyglet.sprite.Sprite(sov_logo_image, x=windowWidth / 2,
                                           y=windowHeight * 3 / 4,
                                           batch=start_screen_batch,
                                           group=buttons_layer)

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        if windowWidth / 4 - 150 < x < (
                windowWidth / 4) + 150 and windowHeight / 4 - 50 < y < windowHeight / 4 + 50:  # start game
            inGame = True
            # live_batch = level_batch
            window.clear()
            # print(level_batch)
            start()
        elif ((3 * windowWidth / 4 - 150) < x < (3 * windowWidth / 4) + 150) and (
                windowHeight / 4 - 50 < y < windowHeight / 4 + 50):  # goto store
            window.clear()
            store_menu()
        elif ((windowWidth / 2 - 200) < x < (windowWidth / 2 + 200)) and (
                windowHeight / 4 - 40 < y < windowHeight / 4 + 40):  # goto store
            window.clear()
            level_menu()

    @window.event
    def on_draw():
        window.clear()
        start_screen_batch.draw()

    pyglet.app.run()


def level_menu():
    level_menu_batch = pyglet.graphics.Batch()
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
    exit_button_sprite = pyglet.sprite.Sprite(exit_button, x=windowWidth - exit_button.anchor_x,
                                              y=windowHeight - exit_button.anchor_y,
                                              batch=level_menu_batch,
                                              group=buttons_layer)

    level_1 = create_square(level_menu_batch,
                            x=windowWidth / 3 - 50, x2=windowWidth / 3 + 50,
                            y=windowHeight / 2 - 50, y2=windowHeight / 2 + 50)
    level_2 = create_square(level_menu_batch,
                            x=windowWidth / 2 - 50, x2=windowWidth / 2 + 50,
                            y=windowHeight / 2 - 50, y2=windowHeight / 2 + 50)
    level_3 = create_square(level_menu_batch,
                            x=2 * windowWidth / 3 - 50, x2=2 * windowWidth / 3 + 50,
                            y=windowHeight / 2 - 50, y2=windowHeight / 2 + 50)

    connection_1 = create_square(level_menu_batch,
                                 x=windowWidth / 3 + 50, x2=windowWidth / 2 - 50,
                                 y=windowHeight / 2, y2=windowHeight / 2)
    connection_2 = create_square(level_menu_batch,
                                 x2=windowWidth / 2 + 50, x=2 * windowWidth / 3 - 50,
                                 y=windowHeight / 2, y2=windowHeight / 2)

    @window.event
    def on_draw():
        window.clear()
        level_menu_batch.draw()

    @window.event
    def on_mouse_press(x, y, button, modifiers):
        if (windowWidth - exit_button.width) < x < windowWidth and y > (
                windowHeight - exit_button.height):  # clicking X button
            menu()

    def update(dt):
        level_menu_batch.draw()

    pyglet.clock.schedule_interval(update, 1 / 120.0)
    pyglet.app.run()


def store_menu():
    def item_buy(item):
        if item[0] == 1:
            print(item[1])
            if item[1] == 1:
                createPlayerPlaneUpgrades("Peyton", "improved_movespeed", "lightning")
            elif item [1] == 3:
                createPlayerPlaneUpgrades("Peyton", "improved_bullet_damage", "lightning")
            elif item [1] == 4:
                createPlayerPlaneUpgrades("Peyton", "shorter_special_charge_time", "lightning")
            elif item [1] == 6:
                createPlayerPlaneUpgrades("Peyton", "improved_fire_rate", "lightning")
            elif item [1] == 8:
                createPlayerPlaneUpgrades("Peyton", "increased_special_damage", "lightning") 
            elif item [1] == 0:
                createPlayerPlaneUpgrades("Peyton", "increase_dodge_bullets", "lightning")
        elif item[0] == 2:
            if item[1] == 0:
                createPlayerPlaneUpgrades("Peyton", "improved_bullet_damage", "oldy")
            elif item [1] == 3:
                createPlayerPlaneUpgrades("Peyton", "bomb", "oldy")
            elif item [1] == 5:
                createPlayerPlaneUpgrades("Peyton", "improved_bomb_damage", "oldy")
            elif item [1] == 7:
                createPlayerPlaneUpgrades("Peyton", "improved_bomb_fire_rate", "oldy")
            elif item [1] == 9:
                createPlayerPlaneUpgrades("Peyton", "triples_fire_rate", "oldy")
        elif item[0] == 3:
            if item[1] == 0:
                createPlayerPlaneUpgrades("Peyton", "improved_collision_damage", "oldy")
            elif item [1] == 3:
                createPlayerPlaneUpgrades("Peyton", "improved_health", "oldy")
            elif item [1] == 5:
                createPlayerPlaneUpgrades("Peyton", "improved_movement_speed", "oldy")
            elif item [1] == 7:
                createPlayerPlaneUpgrades("Peyton", "increase_special_time", "oldy")
            elif item [1] == 9:
                createPlayerPlaneUpgrades("Peyton", "increased_special_damage", "oldy")
            elif item [1] == 0:
                createPlayerPlaneUpgrades("Peyton", "increased_damage_to_closer_enemies", "oldy")
        elif item[0] == 4:
            if item[1] == 0:
                createPlayerPlaneUpgrades("Peyton", "improved_regen_rate", "oldy")
            elif item [1] == 3:
                createPlayerPlaneUpgrades("Peyton", "regenerate_self", "oldy")
            elif item [1] == 5:
                createPlayerPlaneUpgrades("Peyton", "revive_planes_full_health", "oldy")
            elif item [1] == 7:
                createPlayerPlaneUpgrades("Peyton", "shorter_special_charge_time", "oldy")
            elif item [1] == 9:
                createPlayerPlaneUpgrades("Peyton", "revives_all_planes", "oldy")

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

    plane_square_1 = create_square(store_menu_batch, x=windowWidth / 4 - 100, y=windowHeight * 0.80,
                                   x2=windowWidth / 4 + 100, y2=windowHeight * 0.85, width=2)
    plane_1_label = pyglet.text.Label('P L A N E 1', color=(0, 0, 255, 255),
                                      font_name='Times New Roman',
                                      font_size=20, group=buttons_layer,
                                      x=window.width / 4, y=window.height * 0.82,
                                      batch=store_menu_batch)
    plane_1_label.x = plane_1_label.x - plane_1_label.content_width / 2

    plane_square_2 = create_square(store_menu_batch, x=windowWidth / 2 - 100, y=windowHeight * 0.80,
                                   x2=windowWidth / 2 + 100, y2=windowHeight * 0.85, width=2)
    plane_2_label = pyglet.text.Label('P L A N E 2', color=(0, 255, 0, 255),
                                      font_name='Times New Roman',
                                      font_size=20, group=buttons_layer,
                                      x=window.width / 2, y=window.height * 0.82,
                                      batch=store_menu_batch)
    plane_2_label.x = plane_2_label.x - plane_2_label.content_width / 2

    plane_square_3 = create_square(store_menu_batch, x=3 * windowWidth / 4 - 100,
                                   y=windowHeight * 0.80,
                                   x2=3 * windowWidth / 4 + 100, y2=windowHeight * 0.85, width=2)
    plane_3_label = pyglet.text.Label('P L A N E 3', color=(255, 0, 0, 255),
                                      font_name='Times New Roman',
                                      font_size=20, group=buttons_layer,
                                      x=3 * window.width / 4, y=window.height * 0.82,
                                      batch=store_menu_batch)
    plane_3_label.x = plane_3_label.x - plane_3_label.content_width / 2
    exit_button_sprite = pyglet.sprite.Sprite(exit_button, x=windowWidth - exit_button.anchor_x,
                                              y=windowHeight - exit_button.anchor_y,
                                              batch=store_menu_batch,
                                              group=buttons_layer)
    plane_choice_shopping = 2

    temp_upgrades = shop_upgrade(plane_choice_shopping, store_menu_batch)
    store_menu_batch.draw()

    @window.event
    def on_mouse_press(x, y, button, modifiers):
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
        elif 2*windowWidth / 3 - 50 < x < 2*windowWidth / 3 + 50 and 2 * windowHeight / 3 - 50 < y < 2 * windowHeight / 3 + 50:  # top right
            item_buy([plane_choice_shopping, 7])
        elif 2*windowWidth / 3 - 50 < x < 2*windowWidth / 3 + 50 and windowHeight / 2 - 50 < y < windowHeight / 2 + 50:  # middle right
            item_buy([plane_choice_shopping, 8])
        elif 2*windowWidth / 3 - 50 < x < 2*windowWidth / 3 + 50 and windowHeight / 3 - 50 < y < windowHeight / 3 + 50:  # bottom right
            item_buy([plane_choice_shopping, 9])

        elif windowWidth / 4 - 100 < x < windowWidth / 4 + 100 and windowHeight * 0.80 < y < windowHeight * 0.85:  # swap plane 1
            plane_choice_shopping = 1
            temp_upgrades = shop_upgrade(1, store_menu_batch)
            print("plane choice change to 1")
        elif windowWidth / 2 - 100 < x < windowWidth / 2 + 100 and windowHeight * 0.80 < y < windowHeight * 0.85:  # swap plane 2
            plane_choice_shopping = 2
            temp_upgrades = shop_upgrade(2, store_menu_batch)

        elif 3 * windowWidth / 4 - 100 < x < 3 * windowWidth / 4 + 100 and windowHeight * 0.80 < y < windowHeight * 0.85:  # swap plane 3
            plane_choice_shopping = 3
            temp_upgrades = shop_upgrade(3, store_menu_batch)

        elif (windowWidth - exit_button.width) < x < windowWidth and y > (
                windowHeight - exit_button.height):  # clicking X button
            menu()
            window.clear()

    @window.event
    def on_draw():
        store_menu_batch.draw()

    def update(dt):
        store_menu_batch.draw()

    pyglet.clock.schedule_interval(update, 1 / 120.0)

    pyglet.app.run()


def end_screen(dt):
    end_screen_batch = pyglet.graphics.Batch()

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
        if windowWidth / 2 - 150 < x < (windowWidth / 2) + 150 and y < 100:
            window.clear()
            # print(level_batch)
            start()

        if windowWidth / 2 - 150 < x < (windowWidth / 2) + 150 and 150 < y < 250:
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
    score_obj = {'score': 0, 'target_score': 3}
    label = pyglet.text.Label('Score: ' + str(score_obj['score']),
                              font_name='Times New Roman',
                              font_size=24, group=buttons_layer,
                              x=window.width - 200, y=window.height // 2, batch=level_batch)

    # initializing plane handler which holds all the planes
    planeHandler = PlayerPlaneHandler(getPlayerPlanes(playerName), batch=level_batch,
                                      group=plane_layer)
    #createPlayerPlaneUpgrades("Peyton", "oldy", "improved_movespeed")
    for i in planeHandler.getAllPlanes():
        i.add_upgrades(getPlayerPlanesUpgrades("Peyton", i.get_name()))
    game_objects += planeHandler.getAllPlanes()

    # add enemy
    test_enemy = Enemy(resources.plane_1, 50, batch=level_batch, group=plane_layer)
    # test_enemy.color = (255, 0, 0)
    game_objects.append(test_enemy)
    enemies.append(test_enemy)
    # initializing the background
    level_map_object = PhysicalObject(level_map, x=windowWidth / 2, batch=level_batch,
                                      group=maps_layer)
    level_map_object.scale_x = windowWidth / level_map_object.width

    game_objects.append(level_map_object)
    level_map_object.velocity_y = -1

    # initialize the exit button
    exit_button_sprite = pyglet.sprite.Sprite(exit_button, x=windowWidth - exit_button.anchor_x,
                                              y=windowHeight - exit_button.anchor_y,
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

        if (windowWidth - exit_button.width) < x < windowWidth and y > (
                windowHeight - exit_button.height):  # clicking X button
            end_screen(0)
            window.clear()
        if (button == 1):
            planeHandler.getActivePlane().fire(mouse_x, mouse_y)
        if (button == 4):
            planeHandler.getActivePlane().specialAbilityFire(mouse_x, mouse_y)

        # print(game_objects)

    @window.event
    def on_draw():
        window.clear()
        level_batch.draw()

    def handle_move(dt):
        test_enemy.velocity_x = 5
        test_enemy.y = 700

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
        if (planeHandler.getActivePlane().laser):
            planeHandler.getActivePlane().laser.velocity_x = planeHandler.getActivePlane().velocity_x
            planeHandler.getActivePlane().laser.velocity_y = planeHandler.getActivePlane().velocity_y

    def checkCollision():
        for obj in game_objects:
            if (obj.dead == True):
                if obj.is_enemy == True:
                    score_obj['score'] += 1
                    label.text = 'Score: ' + str(score_obj['score'])
                    print(score_obj)
                    if score_obj['score'] >= score_obj[
                        'target_score']:  # change this to change the required score to win
                        pyglet.clock.schedule_once(end_screen, 1)
                        print("game end")
                    else:
                        # create new enemy when enemy dies (for demo only, should initialize it elsewhere)
                        new_test_enemy = Enemy(resources.plane_1, 50, batch=level_batch,
                                               group=plane_layer)
                        # new_test_enemy.color = (255, 0, 0)
                        new_test_enemy.velocity_x = 5
                        new_test_enemy.y = 700
                        game_objects.append(new_test_enemy)
                        enemies.append(new_test_enemy)

                game_objects.remove(obj)
                # print(game_objects)

            if (obj.is_bullet):
                for enemyObj in enemies:
                    if (enemyObj.collides_with(obj) == True):
                        enemyObj.handle_collision_with(obj)

    def update(dt):
        # enemy
        handle_move(dt)
        checkCollision()

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
