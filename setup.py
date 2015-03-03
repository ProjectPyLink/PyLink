#!/usr/bin/env python3
from cx_Freeze import setup, Executable

from pytron import name, version

setup(
	name=name,
	version=version,
	description='a small game for teaching the basics of object oriented programming using Python',
	license='MIT',
	url='https://github.com/ProjectPytron/FreeThePytrons',
	author='ProjectPytron Developers',
	author_email='fkmclane@gmail.com',
	packages=['pytron', 'pytron.game', 'pytron.story', 'pytron.sandbox'],
	package_data={'pytron.game': ['res/*.*'], 'pytron.story': ['res/*.*']},
	scripts=['bin/pytron'],
	executables=[Executable('bin/pytron')],
)
