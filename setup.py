#!/usr/bin/env python3


import sys

from setuptools import find_packages
from setuptools import setup


# *** functions ***

def readToList(fileName):
    return [line.strip() for line in open(fileName).readlines()]


# *** main ***

if '__main__' == __name__:

    setup(
        packages             = find_packages(),
    )

sys.exit(0)

