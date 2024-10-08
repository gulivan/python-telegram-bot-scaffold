import os
import sys


def log_custom_format(record):
    path = os.path.relpath(record["file"].path)

    record["extra"]["abspath"] = path
    logger_format = (
        "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{function}</cyan> → "
        "<blue>{extra[abspath]}:{line}</blue> : "
        "<level>{message}</level>\n"
    )
    return logger_format


def get_logger():
    from loguru import logger

    logger.remove()
    logger.add(sys.stderr, colorize=True, format=log_custom_format)
    return logger


logger = get_logger()
