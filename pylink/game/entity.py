import logging
logger = logging.getLogger(__name__)

import pyglet.image
import pyglet.sprite

import pymunk

import pylink.game
import pylink.game.util

import pylink.state

class Entity(object):
	res = 'entity'
	images = ['idle']
	physics = 'rectangle'
	width = 20
	height = 40
	static = True
	range = 10

	def __init__(self, x=0, y=0, world=pylink.state.world):
		self.image_res = {}
		for image in self.images:
			try:
				self.image_res[image] = pylink.game.loader.animation(self.res + '.' + image + '.gif')
			except pyglet.resource.ResourceNotFoundException:
				logger.exception('entity image not found')

		self.sprite = pyglet.sprite.Sprite(self.image_res['idle'], batch=pylink.state.world.batch, group=pylink.state.world.foreground)

		self.world = world

		if self.physics == 'rectangle':
			self.body = pymunk.Body(self.mass, pymunk.inf)
			#self.body = pymunk.Body(self.mass, pymunk.moment_for_box(self.mass, self.width, self.height))
			self.shape = pymunk.Poly.create_box(self.body, (self.width, self.height))
		elif self.physics == 'circle':
			self.body = pymunk.Body(self.mass, pymunk.moment_for_circle(self.mass, 0, self.radius))
			self.shape = pymunk.Circle(self.body, self.radius)
		elif self.physics == 'segment':
			self.body = pymunk.Body(self.mass, pymunk.moment_for_segment(self.mass, self.start, self.end))
			self.shape = pymunk.Segment(self.body, self.start, self.end, self.radius)
		elif self.physics == 'polygon':
			self.body = pymunk.Body(self.mass, pymunk.moment_for_poly(self.mass, self.poly))
			self.shape = pymunk.Poly(self.body, self.vertices)
		else:
			#TODO: specialize this exception
			raise Exception()

		self.shape.friction = self.friction

		self.move_to(x, y)

		self.world.spawn(self)

	def set_image(self, image):
		self.sprite.image = self.image_res[image]

	def move(self, dx, dy):
		self.body.position = (self.body.position[0] + dx, self.body.position[1] + dy)
		self.x += dx
		self.y += dy

	def move_to(self, x, y):
		self.body.position = (x, y)
		self.x = x
		self.y = y

	def find(self, type):
		min_dist = self.range
		min_ent = None

		for other in self.world.entities:
			if isinstance(other, type):
				dist = pylink.game.util.distance(self.x, self.y, other.x, other.y)
				if dist < min_dist:
					min_dist = dist
					min_ent = other

		return min_ent
