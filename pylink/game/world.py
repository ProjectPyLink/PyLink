import logging
logger = logging.getLogger(__name__)

import math

import pyglet.graphics

import pymunk

import pylink.game.util

class World(object):
	def __init__(self):
		self.entities = []

		self.batch = pyglet.graphics.Batch()
		self.background = pyglet.graphics.OrderedGroup(0)
		self.foreground = pyglet.graphics.OrderedGroup(1)

		self.space = pymunk.Space()
		self.space.gravity = (0, -900)

		#TODO: change to entity (super-entity?)
		self.ground_body = pymunk.Body()
		self.ground_shape = pymunk.Segment(self.ground_body, (-100, 0), (100, 0), 0)
		self.ground_shape.friction = 0.5
		self.space.add(self.ground_shape)

		pyglet.clock.schedule_interval(self.update, 1/60)

	def draw(self):
		self.batch.draw()

	def update(self, dt):
		self.space.step(dt)

		for entity in self.entities:
			#TODO: add properties to entity and change to entity.rotation
			#pymunk rotation is different from pyglet
			#entity.sprite.rotation = math.degrees(-entity.body.angle) + 180
			entity.sprite.rotation = math.degrees(entity.body.angle)
			entity.sprite.set_position(entity.body.position.x, entity.body.position.y)

	def spawn(self, entity):
		self.entities.append(entity)
		if entity.static:
			self.space.add(entity.shape)
		else:
			self.space.add(entity.body, entity.shape)
