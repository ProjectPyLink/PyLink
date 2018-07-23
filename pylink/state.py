import pyglet.window

from pylink.game.camera import Camera
from pylink.game.control import Control
from pylink.game.world import World

window = pyglet.window.Window()
control = Control(window)
camera = Camera()
world = World()
