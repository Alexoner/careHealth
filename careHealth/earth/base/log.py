import json
import logging
import pprint


dev_logger = logging.getLogger('dev')


def log_obj(obj):
    dev_logger.debug(pprint.pformat(obj))


def log_array(array):
    dev_logger.debug(json.dumps(array))
