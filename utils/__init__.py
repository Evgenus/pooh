'''
Scope of common utilities.
'''

# internal
from .path import Path
from .underlying import import_underlying

__all__ = [
    'patchException',
    ]

import_underlying()

def patch_exception():
    'Adds exception helpers to builtins'
    import __builtin__
    def exc_name(error):
        'Returns name of given exception'
        return '{0}.{1}'.format(
            error.__class__.__module__,
            error.__class__.__name__,
            )
    __builtin__.exc_name = exc_name
