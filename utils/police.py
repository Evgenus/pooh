'''
This module provides command line functionality to check you source files for
coding policies correspondency.
'''

# internal
from .path import Path
from .templatable import DocTemplatable


__all__ = []

class BadOrder(DocTemplatable, Exception):
    'Order of import groups are intended to be {0} but {1} defined'

class NoGroup(DocTemplatable, Exception):
    'No group defined for import at line {0}: {1}'

class InvalidLineEnding(DocTemplatable, Exception):
    'Invalid line ending {0!r} at line {1}'

class RulesMeta(type):
    """
    Metaclass for gathering checking rules
    """
    def __init__(mcs, name, bases, internals):
        type.__init__(mcs, name, bases, internals)
        checks = set()
        for base in bases:
            checks.update(getattr(base, 'checks', set()))
        for name in internals:
            if name.startswith('check_'):
                checks.add(name)
        mcs.checks = checks

class Rules(object):
    '''
    Container for rules
    '''
    __metaclass__ = RulesMeta
    checks = set()

    valid_groups = ('standart', 'external', 'internal')
    groups_order = (None, 'standart', 'external', 'internal')
    def check_imports(self, source):
        'Checks imports sequence at the beginning of module.'
        group = []
        groups = [(None, group)]
        for num, line in enumerate(source.splitlines(False), start=1):
            line = line.strip()
            if line.startswith('#'):
                name = line[1:].split()[0]
                if name in self.valid_groups:
                    group = []
                    groups.append((name, group))
            elif line.startswith('import '):
                group.append((num, line))
            elif line.startswith('from '):
                group.append((num, line))
            elif line == '':
                pass
            else:
                break
        order = []
        groups_names = []
        for name, group in groups:
            order.append(self.groups_order.index(name))
            if name is not None:
                groups_names.append(name)
            else:
                if group:
                    for num, line in group:
                        yield NoGroup(num, line)
        if order != sorted(order):
            yield BadOrder(self.valid_groups, groups_names)
    def check_lines(self, source):
        'Checks line ending to be a UNIX style'
        for num, line in enumerate(source.splitlines(True), start=1):
            if line.endswith('\r\n'):
                yield InvalidLineEnding('\r\n', num)
                break
            if line.endswith('\r'):
                yield InvalidLineEnding('\r', num)
                break

def filename_filter(paths):
    'Python sources filter'
    for path in paths:
        if path.ext() == '.py':
            yield path

try:
    from .modapp import ModuleApplication
    class Application(ModuleApplication):
        'Command line enabling'
        @classmethod
        def check(cls, namespace):
            'Performs internal checks'
            counter = 0
            all_messages = []
            for path in filename_filter(Path.cwd().iterfiles()):
                counter += 1
                with path.open('rb') as source_file:
                    source = source_file.read()
                    messages = []
                    rules = Rules()
                    for check in rules.checks:
                        messages.extend(getattr(rules, check)(source))
                if messages:
                    print path
                    for message in messages:
                        print '    {0}'.format(message)
                    all_messages.append(messages)
            print '{0} files checked {1} issues found'.format(
                counter, len(all_messages))
        @classmethod
        def lint(cls, namespace):
            'Performs pylint checks'
            from pylint import lint
            linter = lint.PyLinter()
            from pylint import checkers
            checkers.initialize(linter)
            linter.check([str(path) for path in Path.cwd().iterfiles()])
except ImportError:
    pass
