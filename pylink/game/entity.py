import pyglet.image
import pyglet.sprite

import pylink.game

import pylink.state

class Entity(object):
	res = 'entity'

	def __init__(self):
		self.image = pylink.game.loader.animation(self.res + '.idle.gif')
		self.sprite = pyglet.sprite.Sprite(self.image, batch=pylink.state.world.batch, group=pylink.state.world.foreground)

	def move(self, dx, dy):
		self.sprite.set_position(self.sprite.x+dx, self.sprite.y+dy)

	def move_to(self, x, y):
		self.sprite.set_position(x, y)
