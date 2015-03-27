import pyglet.image
import pyglet.sprite

import pytron.game.res

import pytron.state

class Entity(object):
	graphic = 'entity.png'

	def __init__(self):
		self.image = pyglet.image.load(pytron.game.res.get(self.graphic))
		self.sprite = pyglet.sprite.Sprite(self.image, batch=pytron.state.world.batch)

	def move(self, dx, dy):
		self.sprite.set_position(self.sprite.x+dx, self.sprite.y+dy)

	def move_to(self, x, y):
		self.sprite.set_position(x, y)
