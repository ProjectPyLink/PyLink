import logging
logger = logging.getLogger(__name__)

import collections

import pylink.state

from . import entity

class Character(entity.Entity):
    res = 'character'
    images = ['idle', 'run', 'jump']

    def __init__(self, *args):
        pylink.state.control.subscribe(self)

        super().__init__(*args)

    def animation(function):
        def animation_wrapper(self, *args):
            try:
                self.set_image(function.__name__)
            except NameError:
                logger.exception('animation not in character: ' + function.__name__)

            return function(self, *args)

        return animation_wrapper

    def control_key_press(self, symbol, modifiers):
        if symbol not in self.controls:
            return

        getattr(self, self.controls[symbol])()
