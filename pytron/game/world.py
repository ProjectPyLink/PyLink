import pyglet.graphics

class World(object):
	def __init__(self):
		self.entities = []
		self.batch = pyglet.graphics.Batch()

	def draw(self):
		self.batch.draw()
