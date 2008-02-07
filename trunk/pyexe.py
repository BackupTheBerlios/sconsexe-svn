#!/usr/bin/env python
'''Just print out the location of the python executable'''

__author__ = "Miki Tebeka <miki.tebeka@gmail.com>"

from sys import executable
from os import environ

if environ.get("OSTYPE", None) == "msys":
    executable = executable.replace("\\", "/")
print executable
