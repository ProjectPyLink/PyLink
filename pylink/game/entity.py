import logging
logger = logging.getLogger(__name__)

import pyglet.image
import pyglet.sprite

import pylink.game
import pylink.game.util

import pylink.state

class Entity(object):
	res = 'entity'
	images = ['idle']
	range = 10

	def __init__(self, x=0, y=0, world=pylink.state.world):
		self.image_res = {}
		for image in self.images:
			try:
				self.image_res[image] = pylink.game.loader.animation(self.res + '.' + image + '.gif')
			except pyglet.resource.ResourceNotFoundException:
				logger.exception('entity image not found')

		self.sprite = pyglet.sprite.Sprite(self.image_res['idle'], batch=pylink.state.world.batch, group=pylink.state.world.foreground)

		self.move_to(x, y)

		self.world = world
		self.world.spawn(self)

	def set_image(self, image):
		self.sprite.image = self.image_res[image]

	def move(self, dx, dy):
		self.sprite.set_position(self.sprite.x+dx, self.sprite.y+dy)
		self.x += dx
		self.y += dy

	def move_to(self, x, y):
		self.sprite.set_position(x, y)
		self.x = x
		self.y = y

	def find(self, type):
		min_dist = range
		min_ent = None

		for other in self.world.entities:
			if isinstance(other, type):
				dist = pylink.game.util.distance(self.x, self.y, other.x, other.y)
				if dist < min_dist:
					min_dist = dist
					min_ent = other

		return min_ent
