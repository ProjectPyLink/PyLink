import pyglet.image
import pyglet.sprite

import pytron.game

import pytron.state

class Entity(object):
	res = 'entity'

	def __init__(self):
		self.image = pytron.game.loader.animation(self.res + '.idle.gif')
		self.sprite = pyglet.sprite.Sprite(self.image, batch=pytron.state.world.batch)

	def move(self, dx, dy):
		self.sprite.set_position(self.sprite.x+dx, self.sprite.y+dy)

	def move_to(self, x, y):
		self.sprite.set_position(x, y)
