'''
Abstract class patching functionality
'''

# standart
from functools import wraps

__all__ = [
    'patch_class'
    ]

class patch_class(object):
    """
    Container for class-monkey-patching decorators
    """
    @staticmethod
    def replace(target):
        """
        Totally replaces method
        
        Example:
            >>> class A(object):
            ...     def do(self):
            ...         print 1
            ...
            >>> @patch_class.replace(A)
            ... def do(self):
            ...     print 2
            ...
            >>> a = A()
            >>> a.do()
            2
        """
        def _(function):
            @wraps(function)
            def dummy(self, *args, **kwargs):
                return function(self, *args, **kwargs)
            setattr(target, function.__name__, dummy)
            return dummy
        return _

    @staticmethod
    def wrap(target):
        """
        Wraps method result

        Example:
            >>> class A(object):
            ...     def do(self):
            ...         return 2
            ...
            >>> @patch_class.wrap(A)
            ... def do(self, result):
            ...     return result * 2
            ...
            >>> a = A()
            >>> a.do()
            4
        """
        def _(function):
            oldfunc = getattr(target, function.__name__)
            @wraps(function)
            def dummy(self, *args, **kwargs):
                return function(self, oldfunc(self, *args, **kwargs))
            setattr(target, function.__name__, dummy)
            return dummy
        return _
    @staticmethod
    def raw(target):
        """
        Wraps method and arguments

        Example:
            >>> class A(object):
            ...     def do(self, argument):
            ...         return argument**2
            ...
            >>> @patch_class.raw(A)
            ... def do(self, method, argument):
            ...     return method(self, argument + 1) + 1
            ...
            >>> a = A()
            >>> a.do(2)
            10
        """
        def _(function):
            oldfunc = getattr(target, function.__name__)
            @wraps(function)
            def dummy(self, *args, **kwargs):
                return function(self, oldfunc, *args, **kwargs)
            setattr(target, function.__name__, dummy)
            return dummy
        return _

try:
    from ..modapp import ModuleApplication
    class Application(ModuleApplication):
        'Command line enabling'
except ImportError:
    pass
