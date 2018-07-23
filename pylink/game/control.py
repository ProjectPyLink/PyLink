import logging
logger = logging.getLogger(__name__)

class Control(object):
    def __init__(self, window):
        self._subscribers = set()

        window.push_handlers({
            'on_key_press': self.dispatch_key_press,
        })

    @property
    def subscribers(self):
        return list(self._subscribers)

    def subscribe(self, subscriber):
        self._subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self._subscribers.remove(subscriber)

    def dispatch_key_press(self, symbol, modifiers):
        for subscriber in self._subscribers:
            try:
                subscriber.control_key_press(symbol, modifiers)
            except AttributeError:
                pass
