from logging.config import dictConfig
from errors import errors as err
import logging
from logging.handlers import RotatingFileHandler

from enum import Enum
import os

global g_loggers
global g_logging_config
STACKLEVEL = 2


class LoggerType(Enum):
    DEFAULT = "DEFAULT"
    DEFAULT_AND_FILE = "DEFAULT_AND_FILE"
    # add new loggers in dictConfig, programm will fail if not added


g_loggers: dict[LoggerType, logging.Logger] = {}

g_logging_config = {
    "version": 1.0,
    "formatters": {
        "default": {
            "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
        }
    },
    "handlers": {
        "console1": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "default",
        },
        "size_rotating_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "default",
            "filename": "flask.log",
            "maxBytes": 1000000,
            "backupCount": 5,
        },
    },
    "root": {"level": "DEBUG", "handlers": ["console1"]},
    "loggers": {
        LoggerType.DEFAULT.name: {
            "level": "DEBUG",
            "handlers": ["console1"],
            "propagate": False,
        },
        LoggerType.DEFAULT_AND_FILE.name: {
            "level": "DEBUG",
            "handlers": ["console1", "size_rotating_file_handler"],
            "propagate": False,
        },
        # add new logger here
    },
}

logger_function_bindings = {
    logging.ERROR: logging.error,
    logging.INFO: logging.info,
    logging.DEBUG: logging.debug,
    logging.WARNING: logging.warning,
}


class CustomFormatter(logging.Formatter):
    """Custom formatter for color in logging

    Args:
        logging (logging.Formatter): logging formatter

    Returns:
        logging.Formatter: logging formatter with color
    """

    grey = "\x1b[38;20m"
    blue = "\x1b[34;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    def __init__(self, fmt: str):
        super().__init__(fmt)
        self.FORMATS = {
            logging.DEBUG: self.blue + fmt + self.reset,
            logging.INFO: self.grey + fmt + self.reset,
            logging.WARNING: self.yellow + fmt + self.reset,
            logging.ERROR: self.red + fmt + self.reset,
            logging.CRITICAL: self.bold_red + fmt + self.reset,
        }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def init_logger(logger_type=LoggerType.DEFAULT, log_level=logging.DEBUG):
    """Return the logger and decorate it with the custom formatter for color"""
    ch = logging.StreamHandler()
    ch.setLevel(log_level)
    ch.setFormatter(
        CustomFormatter(g_logging_config["formatters"]["default"]["format"])
    )
    g_loggers[logger_type] = logging.getLogger(logger_type.name)
    g_loggers[logger_type].addHandler(ch)

    # log level based on env var
    if os.environ.get("FLASK_DEBUG") == "1":
        for logger in g_loggers.values():
            logger.setLevel(logging.DEBUG)
    else:
        for logger in g_loggers.values():
            logger.setLevel(logging.INFO)

    return g_loggers


def get_logger_type():
    """Return the logger type based on env var"""
    if os.environ.get("LOG_FILE") == "1":
        return LoggerType.DEFAULT_AND_FILE
    else:
        return LoggerType.DEFAULT


def get_logger():
    """Return the logger and decorate it with the custom formatter"""
    # check if logger_type is in enum
    logger_type = get_logger_type()
    if logger_type not in LoggerType:
        raise err.TypeException(
            message="Logger type must be of type LoggerType",
            status_code=500,
        )
    if logger_type not in g_loggers:
        init_logger(logger_type)
    return g_loggers[logger_type]


def configure_dict():
    """Called by app.py to configure the logging dict. First ting to do."""
    dictConfig(g_logging_config)
    # assert that all loggerTypes are in loggers
    assert all(
        [logger_type.name in g_logging_config["loggers"] for logger_type in LoggerType]
    )


def info(msg: str | set[str]):
    return log(msg, logging.INFO)


def debug(msg: str | set[str]):
    return log(msg, logging.DEBUG)


def warn(msg: str | set[str]):
    return log(msg, logging.WARNING)


def error(msg: str | set[str]):
    return log(msg, logging.ERROR)


def log(msg, level):
    """Log a message with the logger

    Args:
        msg (str): message to log
        level (int): logging level
    """
    logger = get_logger()
    match (level):
        case logging.WARNING:
            logger.warning(msg, stacklevel=STACKLEVEL)
        case logging.INFO:
            logger.info(msg, stacklevel=STACKLEVEL)
        case logging.DEBUG:
            logger.debug(msg, stacklevel=STACKLEVEL)
        case logging.ERROR:
            logger.error(msg, stacklevel=STACKLEVEL)

    # format return based on formatter in logging_config
    return logging.Formatter(
        g_logging_config["formatters"]["default"]["format"]
    ).format(
        logging.LogRecord(
            name=logger.name,
            level=level,
            pathname="",
            lineno=0,
            msg=msg,
            args=(),
            exc_info=None,
        )
    )
