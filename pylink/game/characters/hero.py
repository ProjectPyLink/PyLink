import logging
logger = logging.getLogger(__name__)

import pyglet.window

import pylink.game

class Hero(pylink.game.Character):
	res = 'hero'
	physics = 'rectangle'
	width = 20
	height = 40
	speed = 1
	mass = 40

	@pylink.game.Character.animation
	@pylink.game.Character.control(pyglet.window.key.SPACE)
	def link(self):
		terminal = self.find(pylink.game.Terminal)
		if terminal:
			terminal.activate()
