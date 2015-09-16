#!/usr/bin/env python
import re

from setuptools import setup, find_packages
from $PROJECT$.constants import __PROJECT__, __DESCRIPTION__, __VERSION__


def _get_requirements(path):
    try:
        with open(path) as f:
            packages = f.read().splitlines()
    except (IOError, OSError) as ex:
        raise RuntimeError("Can't open file with requirements: %s", repr(ex))
    packages = (p.strip() for p in packages if not re.match("^\s*#", p))
    packages = list(filter(None, packages))
    return packages


def _install_requirements():
    requirements = _get_requirements('requirements.txt')
    return requirements

setup(
    name = __PROJECT__,
    version = __VERSION__,
    description = __DESCRIPTION__,
    author = "Václav Pavlín",
    author_email = 'vpavlin@redhat.com',
    url = '',
    license = "LGPL3",
    entry_points = {
        'console_scripts': ['%s=%s.cli.main:main' % (__PROJECT__, __PROJECT__)],
    },
    packages = find_packages(),
    install_requires = _install_requirements()
)
