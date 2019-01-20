import logging
logger = logging.getLogger(__name__)

import pylink.game

class Terminal(pylink.game.Entity):
    res = 'terminal'
    width = 20
    height = 40

    images = ['idle', 'activate']

    @pylink.game.animation
    def activate(self):
        pass
