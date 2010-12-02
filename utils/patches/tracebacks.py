'''
Patching traceback module
'''

# standart
import sys
import traceback

__all__ = [
    'send_tracebacks_to'
    ]

PYGMENTS_SCHEME = 'dark'

def send_tracebacks_to(logger, coloring=True):
    """
    Patches tracebacks printing to redirect it output into logger.
    """
    def print_exc():
        logger.exception('This error was sent to standart output')
    traceback.print_exc = print_exc

    if coloring:
        from pygments import highlight
        from pygments.lexers.agile import PythonTracebackLexer
        from pygments.formatters.terminal import TerminalFormatter
        from io import BytesIO

        old_print_exception = traceback.print_exception
        def print_exception(etype, value, trace_back, limit=None, stream=None):
            if stream is None:
                stream = sys.stderr
            buff = BytesIO()
            old_print_exception(etype, value, trace_back, limit, buff)
            stream.write(highlight(buff.getvalue(),
                PythonTracebackLexer(),
                TerminalFormatter(bg=PYGMENTS_SCHEME)))
        traceback.print_exception = print_exception

try:
    from ..modapp import ModuleApplication
    class Application(ModuleApplication):
        'Command line enabling'
except ImportError:
    pass
