#!/usr/bin/env python

from setuptools import setup

setup(name='stackmob-parse-importer',
version='0.1.0',
description='A script to add exported Parse data to StackMob',
author='Douglas Rapp',
author_email='drapp@stackmob.com',
url='http://github.com/stackmob/stackmob-parse-importer',
scripts=['stackmob-parse-importer'],
packages=['client'],
install_requires=['oauth', 'requests'])
