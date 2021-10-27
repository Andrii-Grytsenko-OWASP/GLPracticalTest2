import logging
import os

from pytest import *


@fixture(scope="class")
def logger():
    # For running tests from IDE
    #log_file = logging.FileHandler(os.path.join(os.pardir, 'logs', 'api_testing.log'), 'a')

    # For running tests from command line
    log_file = logging.FileHandler(os.path.join(os.curdir, 'gorest', 'logs', 'api_testing.log'), 'a')

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log_file.setFormatter(formatter)
    _logger = logging.getLogger(None)
    _logger.setLevel(logging.DEBUG)
    for hdlr in _logger.handlers[:]:
        _logger.removeHandler(hdlr)
    _logger.addHandler(log_file)
    yield _logger
    del _logger
