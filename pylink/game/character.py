import logging
logger = logging.getLogger(__name__)

from pylink.game.entity import Entity

class Character(Entity):
    res = 'character'
    images = ['idle', 'run', 'jump']

    def animation(function):
        def animation_wrapper(self, *args):
            try:
                self.set_image(function.__name__)
            except NameError:
                logger.exception('animation not in character: ' + function.__name__)

            return function(self, *args)

    def control(control):
        def control_decoration(function):
            def control_wrapper(self, *args):
                pass

        return control_decoration
