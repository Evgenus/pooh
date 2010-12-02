# -*- coding: UTF-8 -*-
"""
This module provides functionality to allow utility modules behave like
applications and provide commands.

Usually command are:
    - obtain manual documentation
    - run unit-tests
    - obtain brief information about namespace
    - obtain dependency graph
but you can extend them with you own functions

This module imports others only at execution time and if necessary.
"""

# standart
import sys
import types

__all__ = [
    'ModuleApplication',
    ]
    
class ApplicationMeta(type):
    """
    Metaclass for prepare and run command line functionality
    """
    def __init__(mcs, name, bases, internals):
        type.__init__(mcs, name, bases, internals)
        if bases == (object,):
            return
        provide = set()
        for name in dir(mcs):
            member = getattr(mcs, name)
            if isinstance(member, types.MethodType):
                provide.add(name)

        level = 1
        while True:
            frame = sys._getframe(level)
            namespace = frame.f_locals
            if '__file__' in namespace:
                mname = namespace.get('__name__')
                if mname == '__main__':
                    parser = mcs.make_parser(provide)
                    arguments = parser.parse_args()
                    if arguments.actions:
                        for action in arguments.actions:
                            getattr(mcs, action)(namespace)
                    else:
                        parser.print_help()
                break
            level += 1

    @staticmethod
    def make_parser(provided):
        """
        Creates command line arguments parser
        """
        import argparse
        parser = argparse.ArgumentParser()
        parser.add_argument('--action',
            dest='actions',
            action='append',
            choices=provided,
            default=[])
        for name in provided:
            parser.add_argument('--'+name,
                dest='actions',
                const=name,
                action='append_const')
        return parser

class ModuleApplication(object):
    """
    Basic command line fuctionality available for all modules
    """
    @classmethod
    def doctests(cls, namespace):
        """
        Runs doctesting for module
        """
        import doctest
        result = doctest.testmod(sys.modules['__main__'])
        print 'Tests passed {0}/{1}'.format(
            result.attempted-result.failed,
            result.attempted)

    @classmethod
    def manual(cls, namespace):
        """
        Prints manual documentation
        """
        help(sys.modules['__main__'])

    @classmethod
    def summary(cls, namespace):
        """
        Prints summary. Summary consists of function and classes.
        For function summary is one line with
            function name,
            arguments description,
            and docstring in rest of the 80-characters line
        For classes summary is line with
            class name,
            bases declaration,
            and docstring in rest of the 80-characters line
        classmembers are intended and print just before class by same rules
        """
        import inspect

        def doc_line(obj):
            'Makes a single line of docstring'
            doc = inspect.getdoc(obj)
            if doc is None:
                return ''
            text = ' '.join(line.strip for line in doc.splitlines(False))
            return text

        def repr_method(name, func, prefix='def'):
            'Yields function or method summary'
            yield '{0} {1}{2}'.format(prefix, name,
                inspect.formatargspec(*inspect.getargspec(func))
                ), doc_line(func)

        def repr_class(name, cls):
            'Yields classs summary'
            yield 'class {0}({1})'.format(name,
                ', '.join(base.__name__ for base in cls.__bases__),
                ), doc_line(cls)
            for name in sorted(cls.__dict__):
                if name.startswith('_' + cls.__name__):
                    continue
                value = cls.__dict__[name]
                if isinstance(value, types.TypeType):
                    for line, doc in repr_class(name, value):
                        yield '    ' + line, doc
                elif isinstance(value, types.FunctionType):
                    for line, doc in repr_method(name, value):
                        yield '    ' + line, doc
                elif isinstance(value, classmethod):
                    value = value.__get__(cls)
                    for line, doc in repr_method(name, value, 'classmethod'):
                        yield '    ' + line, doc
                elif isinstance(value, staticmethod):
                    value = value.__get__(cls)
                    for line, doc in repr_method(name, value, 'staticmethod'):
                        yield '    ' + line, doc

        result = []
        names = namespace.get('__all__', namespace)
        for name in sorted(names):
            value = namespace[name]
            if isinstance(value, types.TypeType):
                result.extend(repr_class(name, value))
            elif isinstance(value, types.FunctionType):
                result.extend(repr_method(name, value))
        for line, doc in result:
            if doc:
                if len(doc) <= 76 - len(line):
                    print '{0}: {1}'.format(line, doc)
                else:
                    print '{0}: {1}...'.format(line, doc[:75 - len(line)])
            else:
                print line

    @classmethod
    def classtree(cls, namespace):
        '''
        Prints classtree from inspect.getclasstree in intuitive manner
        '''
        import inspect
        classes = []
        names = namespace.get('__all__', namespace)
        for name in sorted(names):
            value = namespace[name]
            if isinstance(value, types.TypeType):
                classes.append(value)
        def tree(deps, start=''):
            'Prints tree of classes inheritance'
            walk = (u'│   ', u'    ')
            turn = (u'├───', u'└───')
            for i in range(len(deps)):
                dep = deps[i]
                tail = tuple not in set(type(e) for e in deps[i+1:])
                if isinstance(dep, list):
                    tree(dep, start + walk[tail])
                elif isinstance(dep, tuple):
                    print start + turn[tail] + dep[0].__name__

        tree(inspect.getclasstree(classes))

class Application(ModuleApplication):
    'Command line enabling'
