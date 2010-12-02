'''
Provides functionality for automatic loading underlying modules to package
'''

# standart
import sys
import pkgutil
# internal
from .templatable import DocTemplatable

class AllAttributeError(DocTemplatable, AttributeError):
    "Can't find {1} declared in __all__ in module {0}"

def import_underlying():
    '''
    Imports underlying modules and all names listed in their `__all__` variables
    to make them accesible from package directly.
    '''
    level = 1
    while True:
        frame = sys._getframe(level)
        namespace = frame.f_locals
        if '__file__' in namespace:
            mpath = namespace.get('__path__')
            if mpath is not None:
                mname = namespace.get('__name__')
                alls = namespace.get('__all__')
                if alls is None:
                    alls = []
                    namespace['__all__'] = alls
                for _, name, _ in pkgutil.iter_modules(mpath):
                    module = __import__('', namespace, namespace, [name])
                    module = getattr(module, name)
                    if hasattr(sys, 'modules_reloader'):
                        sys.modules_reloader.link_modules(
                            module.__name__, mname)
                    sub_alls = getattr(module, '__all__', [])
                    alls.extend(sub_alls)
                    for name in sub_alls:
                        try:
                            namespace[name] = getattr(module, name)
                        except AttributeError:
                            raise AllAttributeError(module, name)
            break
        level += 1

try:
    from .modapp import ModuleApplication
    class Application(ModuleApplication):
        'Command line enabling'
except ImportError:
    pass
