import logging
logger = logging.getLogger(__name__)

import pyglet.gl

class Camera(object):
    def __init__(self, x=0, y=0, rotation=0.0, scale=1.0):
        self._x = x
        self._y = y
        self._rotation = rotation
        self._scale = scale

        self._subscribers = set()

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        pyglet.gl.glTranslatef(x - self._x, 0, 0)

        self._x = x

        for subscriber in self._subscribers:
            subscriber.camera_update(self)

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        pyglet.gl.glTranslatef(0, y - self._y, 0)

        self._y = y

        for subscriber in self._subscribers:
            subscriber.camera_update(self)

    @property
    def position(self):
        return self._x, self._y

    @position.setter
    def position(self, position):
        x, y = position

        pyglet.gl.glTranslatef(x - self._x, y - self._y, 0)

        self._x, self._y = position

        for subscriber in self._subscribers:
            subscriber.camera_update(self)

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, rotation):
        pyglet.gl.glRotatef(rotation, 0, 0, 1)

        self._rotation = rotation

        for subscriber in self._subscribers:
            subscriber.camera_update(self)

    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self, scale):
        pyglet.gl.glScalef(scale, scale, 1)

        self._scale = scale

        for subscriber in self._subscribers:
            subscriber.camera_update(self)

    @property
    def subscribers(self):
        return list(self._subscribers)

    def move(self, dx, dy):
        pyglet.gl.glTranslatef(dx, dy, 0)

        self._x += dx
        self._y += dy

        for subscriber in self._subscribers:
            subscriber.camera_update(self)

    def move_to(self, x, y):
        self.position = x, y

    def subscribe(self, subscriber):
        self._subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self._subscribers.remove(subscriber)
