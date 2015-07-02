#!/usr/bin/env python


from setuptools import find_packages, setup


setup(
    name="pelican-plugins",
    install_requires=[
        "pelican",
    ],
    packages=find_packages()
)
