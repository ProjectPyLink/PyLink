from pyglet.window import Window

from pylink.game.camera import Camera
from pylink.game.world import World

window = Window()
world = World(window)
camera = Camera(world)
