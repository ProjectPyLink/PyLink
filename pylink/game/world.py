import logging
logger = logging.getLogger(__name__)

import pyglet.graphics


class World(object):
    def __init__(self, window):
        self.entities = []
        self.batch = pyglet.graphics.Batch()
        self.background = pyglet.graphics.OrderedGroup(0)
        self.foreground = pyglet.graphics.OrderedGroup(1)

        self.window = window

        self.window.push_handlers(on_draw=self.draw)

    def __del__(self):
        self.window.remove_handlers(on_draw=self.draw)

    def draw(self):
        self.window.clear()
        self.batch.draw()

    def spawn(self, entity, foreground=True):
        self.entities.append(entity)

        entity.sprite.batch = self.batch
        entity.sprite.group = self.foreground if foreground else self.background

        entity.world = self
