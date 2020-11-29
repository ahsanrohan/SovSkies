# Sovereign Skies

## Description

Sovereign skies is a 2D top down shooter with a retro WW2 theme. The 
objective is to take down waves of enemy planes while surviving to 
progress from level to level. Unlock planes and upgrade abilities as you progress through the game.

## Controls:

| `key` | action|
|--|--|
| `1` | switch to plane 1 |
| `2` | switch to plane 2 |
|`LMB` | fire |
|`RMB` | special ability |

## Installation
pip install pyglet
pip install pyinstaller

## Build and Run
Navigate to the /SovSkies directory in a terminal. From there:

- setup.py install
    This will build the project and create the 'dist' and 'build' directories. 
- pyinstaller --onefile --add-data "resources;resources" main.py
    This will create the 'main.exe' file in the dist directory. 

From the /dist directory:
- main.exe
    This will run the game.

## Repo
https://github.com/ahsanrohan/SovSkies