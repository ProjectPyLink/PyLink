#!/usr/bin/env python3
from setuptools import setup, find_packages

from pylink import name, version

setup(
	name=name,
	version=version,
	description='a small game for teaching the basics of object oriented programming using Python',
	license='MIT',
	url='https://github.com/ProjectPyLink/PyLink',
	author='ProjectPyLink Developers',
	author_email='fkmclane@gmail.com',
	install_requires=['pyglet>=1.2.2'],
	packages=find_packages(),
	package_data={'': ['res/*.*']},
	entry_points = {'console_scripts': ['pylink = pylink.main']},
)
