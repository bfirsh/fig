from __future__ import unicode_literals
from .service import Service  # noqa:flake8

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
