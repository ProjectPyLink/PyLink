#!/usr/bin/env python3
import os
import re

from setuptools import setup, find_packages


name = None
version = None


def find(haystack, *needles):
    regexes = [(index, re.compile("^{}\s*=\s*'([^']*)'$".format(needle))) for index, needle in enumerate(needles)]
    values = ['' for needle in needles]

    for line in haystack:
        if len(regexes) == 0:
            break

        for rindex, (vindex, regex) in enumerate(regexes):
            match = regex.match(line)
            if match:
                values[vindex] = match.groups()[0]
                del regexes[rindex]
                break

    return values


with open(os.path.join(os.path.dirname(__file__), 'pylink', '__init__.py'), 'r') as pylink:
    name, version = find(pylink, 'name', 'version')


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
    entry_points = {'console_scripts': ['pylink = pylink.__main__:main']},
)
