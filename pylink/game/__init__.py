import pyglet.resource

loader = pyglet.resource.Loader(['game/res/image', 'game/res/sprite', 'game/res/sound'])

from pylink.game.camera import Camera
from pylink.game.world import World
from pylink.game.entity import Entity
from pylink.game.character import Character
