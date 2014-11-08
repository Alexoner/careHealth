# -*- coding: utf8 -*-
import datetime
import calendar

from django.utils import timezone
from django.utils.timezone import utc


def now():
    return datetime.datetime.now() \
        .replace(tzinfo=utc)


def today():
    return now().date()


def utcnow():
    return datetime.datetime.utcnow() \
        .replace(tzinfo=utc)


def expired(expires_timestamp):
    return bool(
        expires_timestamp < now_timestamp(),
    )


def expires_in(expires):
    return now() + datetime.timedelta(
        seconds=expires
    )


def now_timestamp():
    return calendar.timegm(timezone.now().utctimetuple())


def datetime_to_timestamp(timestamp):
    return calendar.timegm(timestamp.utctimetuple())


def timestamp_to_datetime(timestamp):
    return datetime.datetime.utcfromtimestamp(timestamp) \
        .replace(tzinfo=utc)


def str_to_date(date_str):
    return datetime.datetime.strptime(
        date_str, '%Y-%m-%d',
    ).replace(tzinfo=utc).date()


def str_to_datetime(datetime_str):
    return datetime.datetime.strptime(
        datetime_str, '%Y-%m-%d %H:%M:%S',
    ).replace(tzinfo=utc)


def date_to_str(date):
    return date.strftime('%Y-%m-%d')


def datetime_to_str(datetime):
    return datetime.strftime('%Y-%m-%d %H-%M-%S')
