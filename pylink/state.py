import pyglet.window

import pylink.game.camera
import pylink.game.world

window = pyglet.window.Window()
camera = pylink.game.camera.Camera(window)
world = pylink.game.world.World()
