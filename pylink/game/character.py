import logging
logger = logging.getLogger(__name__)

from pylink.game.entity import Entity

import pylink.state

class Character(Entity):
	res = 'character'
	images = ['idle', 'run', 'jump']
	static = False
	rotation = False
	mass = 40
	friction = 0.5
	speed = 1

	def animation(function):
		pass

	def control(control):
		def dcontrol(function):
			pass

		return dcontrol
