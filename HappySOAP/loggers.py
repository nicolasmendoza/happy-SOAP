# -*- coding: utf-8 -*-
from collections import defaultdict
from logging import StreamHandler, DEBUG, getLogger as realGetLogger, Formatter

try:
    from colorama import Fore, Back, init, Style

    class ColourStreamHandler(StreamHandler):
        """ A colorized output SteamHandler """

        ansi_colours = {
            'CYAN': Fore.LIGHTCYAN_EX,
            'RED': Fore.LIGHTRED_EX,
            'YELLOW': Fore.LIGHTYELLOW_EX,
            'MAGENTA': Fore.LIGHTMAGENTA_EX,
            'GREEN': Fore.GREEN,
            'WHITE': Fore.LIGHTWHITE_EX
        }

        # Some basic colour scheme defaults
        colours = {
            'DEBUG': Fore.LIGHTRED_EX,
            'INFO': Fore.LIGHTGREEN_EX,
            'WARN': Fore.LIGHTYELLOW_EX,
            'WARNING': Fore.LIGHTYELLOW_EX,
            'ERROR': Fore.LIGHTRED_EX,
            'CRIT': Back.RED + Fore.WHITE,
            'CRITICAL': Back.RED + Fore.WHITE,
            'MESSAGE': Back.MAGENTA
        }
        colours_letter = defaultdict(lambda: 'YELLOW')
        colours_letter['='] = 'RED'
        colours_letter['{'] = 'WHITE'
        colours_letter['}'] = 'WHITE'
        colours_letter['\''] = 'CYAN'
        colours_letter[':'] = 'RED'

        colours_letter['-'] = 'RED'
        colours_letter['>'] = 'RED'
        colours_letter['<'] = 'RED'
        colours_letter['.'] = 'RED'
        colours_letter[','] = 'RED'

        @property
        def is_tty(self):
            """ Check if we are using a "real" TTY. If we are not using a TTY it means that
            the colour output should be disabled.

            :return: Using a TTY status
            :rtype: bool
            """
            try: return getattr(self.stream, 'isatty', None)()
            except: return False

        def emit(self, record):
            try:
                message = self.format(record)
                if not self.is_tty:
                    self.stream.write(message)
                else:
                    level_name = "[{0}] ".format(record.levelname)
                    self.stream.write(self.colours[record.levelname] + level_name + Style.RESET_ALL)

                    for letter in record.getMessage():
                        self.stream.write(self.ansi_colours[self.colours_letter[letter]] + letter + Style.RESET_ALL)

                self.stream.write(getattr(self, 'terminator', '\n'))
                self.flush()
            except (KeyboardInterrupt, SystemExit):
                raise
            except:
                self.handleError(record)

    has_colour = True
except:
    has_colour = False

def getLogger(name=None, fmt='%(message)s'):
    """ Get and initialize a colourised logging instance if the system supports
    it as defined by the log.has_colour

    :param name: Name of the logger
    :type name: str
    :param fmt: Message format to use
    :type fmt: str
    :return: Logger instance
    :rtype: Logger
    """
    log = realGetLogger(name)
    # Only enable colour if support was loaded properly
    handler = ColourStreamHandler() if has_colour else StreamHandler()
    handler.setLevel(DEBUG)
    handler.setFormatter(Formatter(fmt))
    log.addHandler(handler)
    log.setLevel(DEBUG)
    log.propagate = 0  # Don't bubble up to the root logger

    return log