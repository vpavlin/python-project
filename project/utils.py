from __future__ import print_function
import os

import logging

from constants import HOST_DIR

__all__ = ('Utils')

logger = logging.getLogger(__name__)

class Utils(object):

    @staticmethod
    def getRoot():
        if os.path.isdir(HOST_DIR):
            return HOST_DIR
        else:
            return "/"
