import pyglet.graphics

class World(object):
	def __init__(self):
		self.entities = []
		self.batch = pyglet.graphics.Batch()
		self.background = pyglet.graphics.OrderedGroup(0)
		self.foreground = pyglet.graphics.OrderedGroup(1)

	def draw(self):
		self.batch.draw()

	def spawn(self, entity):
		self.entities.append(entity)
