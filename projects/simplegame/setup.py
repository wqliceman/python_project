try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config={
    "descrption": "simplegame",
    "author": "wqliceman",
    "url": "www.github.com/wqliceman",
    "version": "0.1",
    "name": "game"
    }

setup(**config)
