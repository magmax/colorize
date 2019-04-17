# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

from colorize import APP


def read_description():
    with open("README.rst") as fd:
        return fd.read()


setup(
    name="colorize",
    version=APP.version,
    description=APP.description,
    long_description=read_description(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: User Interfaces",
    ],
    keywords="interface,command line",
    author="Miguel Ángel García",
    author_email="miguelangel.garcia@gmail.com",
    url="https://github.com/magmax/colorize",
    license="MIT",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    entry_points={"setuptools.installation": ["eggsecutable = colorize.bar:foo"]},
    scripts=["bin/colorize"],
)
