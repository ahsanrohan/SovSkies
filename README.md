# Sovereign Skies

## Description

Sovereign skies is a 2D top down shooter with a retro WW2 theme. The 
objective is to take down waves of enemy planes while surviving to 
progress from level to level. Unlock planes and upgrade abilities 
using stars earned from each level. 

## Controls:

| `key` | action|
|--|--|
| `1-4` | switch between planes |
|`LMB` | fire |
|`RMB` | special ability |
|`p` | pause game |

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