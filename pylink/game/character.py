import logging
logger = logging.getLogger(__name__)

from pylink.game.entity import Entity

class Character(Entity):
	res = 'character'
	images = ['idle', 'run', 'jump']

	def animation(function):
		pass

	def control(control):
		def dcontrol(function):
			pass

		return dcontrol
