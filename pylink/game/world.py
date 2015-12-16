import logging
logger = logging.getLogger(__name__)

import pyglet.graphics

class World(object):
	def __init__(self):
		self.entities = []
		self.batch = pyglet.graphics.Batch()
		self.background = pyglet.graphics.OrderedGroup(0)
		self.foreground = pyglet.graphics.OrderedGroup(1)

	def draw(self):
		self.batch.draw()

	def spawn(self, entity, foreground=True):
		self.entities.append(entity)

		entity.sprite.batch = self.batch
		entity.sprite.group = self.foreground if foreground else self.background

		entity.world = self
