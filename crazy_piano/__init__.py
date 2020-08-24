"""
Crazy Piano
"""

from .frequencies import compute_frequencies

import pkg_resources
__version__ = pkg_resources.require('crazy_piano')[0].version