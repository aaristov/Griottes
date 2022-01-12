#!/usr/bin/env python

from setuptools import setup

with open("requirements.txt", "r") as f:
    REQUIREMENTS = f.read().splitlines()

setup(
    name="griottes",
    version="0.0.1",
    description="Python program to generate NetworkX graphs from segmented images.",
    author="Gustave Ronteix",
    author_email="gustave.ronteix@pasteur.fr",
    url="https://github.com/BaroudLab/Griottes",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": ""},
    python_requires=">=3.6",
    install_requires=REQUIREMENTS,
    packages=[
        "griottes",
        "griottes.analyse",
        "griottes.graphmaker",
        "griottes.graphplotter",
    ],
)
