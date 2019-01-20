import logging
logger = logging.getLogger(__name__)

import pyglet.window

import pylink.game
import pylink.game.entities

class Hero(pylink.game.Character):
    res = 'hero'
    width = 20
    height = 40
    speed = 1
    weight = 40

    images = ['idle', 'run', 'jump', 'link']

    controls = {
        pyglet.window.key.SPACE: 'link',
    }

    @pylink.game.animation
    def link(self):
        terminal = self.find(pylink.game.entities.Terminal)
        if terminal:
            terminal.activate()
