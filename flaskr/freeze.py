#!/usr/bin/env python3
from flask_frozen import Freezer
import __init__

freezer = Freezer(__init__.create_app())

if __name__ == '__main__':
    freezer.freeze()
