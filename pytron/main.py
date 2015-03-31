import pyglet.app
import pyglet.text
import pyglet.window

import pytron.game.entity

import pytron.state

@pytron.state.window.event
def on_key_press(symbol, modifiers):
	global hero

	if symbol == pyglet.window.key.Q:
		pytron.state.window.close()

	if symbol == pyglet.window.key.W:
		hero.move(0, 10)

	if symbol == pyglet.window.key.A:
		hero.move(-10, 0)

	if symbol == pyglet.window.key.S:
		hero.move(0, -10)

	if symbol == pyglet.window.key.D:
		hero.move(10, 0)

class Hero(pytron.game.entity.Entity):
	res = 'hero'

background = pyglet.sprite.Sprite(pytron.game.loader.image('pycity.png'))

@pytron.state.window.event
def on_draw():
	pytron.state.window.clear()
	background.draw()
	pytron.state.world.draw()

hero = Hero()

pyglet.app.run()
