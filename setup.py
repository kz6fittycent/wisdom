#!/usr/bin/env python3

from setuptools import setup

setup(
    name="wisdom",
    version="1.2.0",
    description="A collection of wise quotes for the terminal",
    long_description=open("README.md").read(),
    license="MIT",
    packages=["libwisdom"],
    scripts=["wisdom"],
    package_data={"libwisdom": ["data/*"]},
)
