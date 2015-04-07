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

class Hero(pylink.game.entity.Entity):
	res = 'hero'

background = pyglet.sprite.Sprite(pylink.game.loader.image('pycity.png'), batch=pylink.state.world.batch, group=pylink.state.world.background)

@pylink.state.window.event
def on_draw():
	pylink.state.window.clear()
	pylink.state.world.draw()

hero = Hero()

pyglet.app.run()
