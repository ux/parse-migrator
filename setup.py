#!/usr/bin/env python

from setuptools import setup

setup(name='stackmob-parse-migrator',
version='0.1.0',
description='A script to add exported Parse data to StackMob',
author='Douglas Rapp',
author_email='support@stackmob.com',
url='http://github.com/stackmob/stackmob-parse-migrator',
scripts=['stackmob-parse-migrator'],
packages=['client'],
install_requires=['oauth', 'requests'])
