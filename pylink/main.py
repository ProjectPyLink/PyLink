import logging
logger = logging.getLogger(__name__)

import pyglet.app
import pyglet.text
import pyglet.window

import pylink.game
import pylink.game.characters
import pylink.sandbox
import pylink.story

import pylink.state

@pylink.state.window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.Q:
        pylink.state.window.close()

hero = pylink.game.characters.Hero()

background_image = pylink.game.loader.image('pycity.png')
background = pyglet.sprite.Sprite(background_image, batch=pylink.state.world.batch, group=pylink.state.world.background)

pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_RECTANGLE, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST)
pyglet.gl.glTexParameteri(pyglet.gl.GL_TEXTURE_2D, pyglet.gl.GL_TEXTURE_MAG_FILTER, pyglet.gl.GL_NEAREST)

pylink.state.camera.scale = 5.0

pyglet.app.run()
