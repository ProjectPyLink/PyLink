import logging
logger = logging.getLogger(__name__)

import collections

import pyglet.window

import pylink.state

from . import entity

class Character(entity.Entity):
    res = 'character'
    images = ['idle', 'run', 'jump']
    controls = {}

    def animation(function):
        def animation_wrapper(self, *args):
            try:
                self.set_image(function.__name__)
            except NameError:
                logger.exception('animation not in character: ' + function.__name__)

            return function(self, *args)

        return animation_wrapper

    def __init__(self, *args):
        self.keys = pyglet.window.key.KeyStateHandler()

        pylink.state.window.push_handlers(self.keys)
        pylink.state.window.push_handlers(on_key_press=self.send_key)

        super().__init__(*args)

    def __del__(self):
        pylink.state.window.remove_handlers(on_key_press=self.send_key)

    def send_key(self, symbol, modifiers):
        if symbol not in self.controls:
            return

        getattr(self, self.controls[symbol])()
