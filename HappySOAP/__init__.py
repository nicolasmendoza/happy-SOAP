try:
    import colorama  # if colorama already installed...
    from .loggers import getLogger
except ImportError:
    from logging import getLogger