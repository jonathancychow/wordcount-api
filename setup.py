import os

from setuptools import setup

install_requires = []
requirmentsTxt = 'requirements.txt'
if os.path.isfile(requirmentsTxt):
    with open(requirmentsTxt) as f:
        install_requires = list(f.read().splitlines())

setup(
    name="wordcount-api",
    version="1.0.0",
    author="Jonathan Chow",
    description="Count words API",
    url="https://github.com/jonathancychow/wordcount-api",
    install_requires = install_requires,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ]
)
