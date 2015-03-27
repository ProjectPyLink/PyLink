import pyglet.app
import pyglet.text
import pyglet.window

import pytron.game.entity

import pytron.state

label = pyglet.text.Label('')

@pytron.state.window.event
def on_key_press(symbol, modifiers):
	global label, hero

	label = pyglet.text.Label(pyglet.window.key.symbol_string(symbol))
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
	graphic = 'hero.png'

@pytron.state.window.event
def on_draw():
	pytron.state.window.clear()
	pytron.state.world.draw()
	label.draw()

hero = Hero()

pyglet.app.run()
