import os
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()


setup(name='chatgptmagic',
      version='0.3',
      description=' ipython magic for chatgpt ',
      url='https://github.com/thingless/chatgptmagic',
      install_requires=required,
     )
