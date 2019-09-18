# -*- coding: utf-8 -*-

"""PACKAGE INFO

This module provides some basic information about the package.

"""

# Set the package release version
version_info = (0, 0, 1)
__version__ = '.'.join(str(c) for c in version_info)

# Set the package details
__author__ = 'Samuel Farrens'
__email__ = 'samuel.farrens@cea.fr'
__year__ = '2019'
__url__ = 'https://github.com/sfarrens/bobafett'
__description__ = 'Short description of your package'
__long_description__ = 'A longer description of your package'
__requires__ = []  # Your package dependencies

# Default package properties
__license__ = 'MIT'
__about__ = ('{} \n\n Author: {} \n Email: {} \n Year: {} \n {} \n\n'
             ''.format(__name__, __author__, __email__, __year__,
                       __long_description__))
__setup_requires__ = ['pytest-runner', ]
__tests_require__ = ['pytest', 'pytest-cov', 'pytest-pep8']
