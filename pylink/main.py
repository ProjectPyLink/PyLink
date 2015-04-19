import pyglet.app
import pyglet.text
import pyglet.window

import pylink.game.entity

import pylink.state

@pylink.state.window.event
def on_key_press(symbol, modifiers):
	global hero

	if symbol == pyglet.window.key.Q:
		pylink.state.window.close()

	if symbol == pyglet.window.key.W:
		hero.move(0, 10)

	if symbol == pyglet.window.key.A:
		hero.move(-10, 0)

	if symbol == pyglet.window.key.S:
		hero.move(0, -10)

	if symbol == pyglet.window.key.D:
		hero.move(10, 0)

	if symbol == pyglet.window.key.UP:
		pylink.state.camera.move(0, 10)

	if symbol == pyglet.window.key.LEFT:
		pylink.state.camera.move(-10, 0)

	if symbol == pyglet.window.key.DOWN:
		pylink.state.camera.move(0, -10)

	if symbol == pyglet.window.key.RIGHT:
		pylink.state.camera.move(10, 0)

class Hero(pylink.game.entity.Entity):
	res = 'hero'

hero = Hero()

background_image = pylink.game.loader.image('pycity.png')
background = pyglet.sprite.Sprite(background_image, batch=pylink.state.world.batch, group=pylink.state.world.background)

@pylink.state.window.event
def on_draw():
	pylink.state.window.clear()
	pylink.state.world.draw()

pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_RECTANGLE, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST)
pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST)

pylink.state.camera.scale = 5.0

pyglet.app.run()
