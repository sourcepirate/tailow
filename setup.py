# -*- coding: utf-8 -*-
"""setup.py"""
from setuptools import setup, find_packages

with open('README.md') as f:
    README = f.read()

with open('LICENSE') as f:
    LICENSE = f.read()

setup(
    name='tailow',
    version='0.1.1',
    description='A async wrapper for mongodb',
    long_description=README,
    author='Sourcepirate',
    author_email='sathyanarrayanan@yandex.com',
    url='https://github.com/sourcepirate/tailow.git',
    license=LICENSE,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        "motor==1.2.1",
        "pymongo>=3.6,<4"
    ],
    test_suite='tests'
)