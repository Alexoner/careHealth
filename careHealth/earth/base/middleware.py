# -*- coding: utf-8 -*-
import sys
import logging
import traceback


error_file_logger = logging.getLogger('error_log')


class LogExceptionMiddleware(object):

    def process_exception(self, request, exception):
        error_file_logger.error(request)
        trace_info = '\n'.join(traceback.format_exception(*sys.exc_info()))
        error_file_logger.error(trace_info)
