'''
Patching loggers output
'''

# standart
import sys
import logging

__all__ = [
    'wrap_logger',
    'make_colored_logging',
    'LoggingFile',
    'send_stderr_to',
    ]

def wrap_logger(logger):
    """
    Wraps logger instance to allow it consume new style formatting

    Example:

        >>> from io import BytesIO
        >>> stream = BytesIO()
        >>> logging.basicConfig(stream=stream)
        >>> logger = wrap_logger(logging.getLogger('mylogger'))
        >>> logger.addHandler(logging.StreamHandler(stream))
        >>> logger.propagate = False
        >>> logger.error('{0} {1}', 'my', 'message')
        >>> stream.getvalue()
        'my message\\n'
    """
    _log = logger._log
    def wrapped(level, msg, args, exc_info=None, extra=None, **kwargs):
        try:
            msg = msg.format(*args, **kwargs)
        except Exception:
            pass
        _log(level, msg, (), exc_info, extra)
    logger._log = wrapped
    return logger

def make_colored_logging():
    """
    Patches default logging formatter to write colored level-names
    """
    import colorama
    logging_formatter = logging.Formatter

    class Formatter(logging_formatter):
        '''
        Formats logging string to make level type colored
        '''
        _styles = {
            'DEBUG'     : colorama.Back.BLUE + colorama.Fore.WHITE,
            'INFO'      : colorama.Style.RESET_ALL,
            'WARNING'   : colorama.Fore.RED,
            'ERROR'     : colorama.Back.RED + colorama.Fore.WHITE,
            'CRITICAL'  : colorama.Back.RED + colorama.Fore.YELLOW,
            }
        def format(self, record):
            record.levelname = (
                self._styles.get(record.levelname, colorama.Style.RESET_ALL)
                + '{0:8s}'.format(record.levelname)
                + colorama.Style.RESET_ALL)
            return logging_formatter.format(self, record)

    logging.Formatter = Formatter
    logging._defaultFormatter = Formatter()

class LoggingFile(object):
    """
    File like object which writes everything to given logger.
    
    Example:

        >>> from io import BytesIO
        >>> stream = BytesIO()
        >>> logging.basicConfig(stream=stream)
        >>> logger = wrap_logger(logging.getLogger('mylogger'))
        >>> logger.addHandler(logging.StreamHandler(stream))
        >>> logger.propagate = False
        >>> file = LoggingFile(logger, level=logging.ERROR)
        >>> file.write('bang\\n')
        >>> stream.getvalue()
        'bang\\n'
    """
    def __init__(self, logger, level=logging.INFO):
        self.logger = logger
        self.level = level
        self.buffer = ''
    def write(self, message):
        self.buffer += message
        lines = self.buffer.splitlines(False)
        if len(lines) > 1:
            for line in lines[:-1]:
                self.logger.log(self.level, line)
        self.buffer = lines[-1]
        if message.endswith('\n'):
            self.flush()
    def flush(self):
        if self.buffer != '':
            self.logger.log(self.level, self.buffer)
            self.buffer = ''

def send_stderr_to(logger):
    'Redirecting stderr output for logger'
    sys.stderr = LoggingFile(logger, logging.ERROR)

try:
    from ..modapp import ModuleApplication
    class Application(ModuleApplication):
        'Command line enabling'
except ImportError:
    pass
