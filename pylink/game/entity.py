import logging
logger = logging.getLogger(__name__)

import pyglet.image
import pyglet.sprite

import pylink.util

import pylink.state

from . import resource

class Entity(object):
    res = 'entity'
    images = ['idle']
    range = 10

    def __init__(self, x=0, y=0, world=pylink.state.world):
        self.image_res = {}
        for image in self.images:
            filename = self.res + '.' + image + '.gif'
            try:
                self.image_res[image] = resource.loader.animation(filename)
            except pyglet.resource.ResourceNotFoundException:
                logger.exception('entity image not found: ' + filename)

        self.sprite = pyglet.sprite.Sprite(self.image_res['idle'])

        self.move_to(x, y)

        if world:
            world.spawn(self)

    def set_image(self, image):
        self.sprite.image = self.image_res[image]

    def move(self, dx, dy):
        self.sprite.set_position(self.sprite.x+dx, self.sprite.y+dy)

        self.x += dx
        self.y += dy

    def move_to(self, x, y):
        self.sprite.set_position(x, y)

        self.x = x
        self.y = y

    def find(self, type):
        min_dist = self.range
        min_ent = None

        for other in self.world.entities:
            if isinstance(other, type):
                dist = pylink.util.distance(self.x, self.y, other.x, other.y)
                if dist < min_dist:
                    min_dist = dist
                    min_ent = other

        return min_ent

    def update(self, delta):
        pass
