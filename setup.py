#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='Traktor',
    version='0.1',
    author='Nickolay Sadovskiy',
    author_email='sns1081@gmail.com',
    url='http://www.sadovskiy.net',
    packages=find_packages(),
    install_requires=['pyYAML>=3']
)
