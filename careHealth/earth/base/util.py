import datetime

from django.conf import settings

from .time import (
    datetime_to_timestamp,
    date_to_str
)


def get_api_id(name):
    return settings.API_IDS[name]


def dict_raw_to_basic_type(dic):
    new_dic = {}

    for key, val in dic.items():
        if isinstance(val, datetime.datetime):
            new_dic[key] = datetime_to_timestamp(
                val,
            )
            continue

        if isinstance(val, datetime.date):
            new_dic[key] = date_to_str(
                val,
            )
            continue

        if isinstance(val, str) or isinstance(val, unicode):
            if is_ascii(val):
                new_dic[key] = str(val)
            else:
                new_dic[key] = unicode(val)

            continue

        if isinstance(val, list):
            new_dic[key] = val
            continue

        if isinstance(val, dict):
            new_dic[key] = val
            continue

        new_dic[key] = val

    return new_dic


def dict_raw_to_str(dic):
    new_dic = {}

    for key, val in dic.items():
        if isinstance(val, datetime.datetime):
            new_dic[key] = str(datetime_to_timestamp(
                val,
            ))
            continue

        if isinstance(val, datetime.date):
            new_dic[key] = date_to_str(
                val,
            )
            continue

        if isinstance(val, str) or isinstance(val, unicode):
            if is_ascii(val):
                new_dic[key] = str(val)
            else:
                new_dic[key] = unicode(val)

            continue

        if isinstance(val, list):
            new_dic[key] = val
            continue

        if isinstance(val, dict):
            continue

        new_dic[key] = str(val)

    return new_dic


def dict_basic_type_to_str(dic):
    new_dic = {}

    for key, val in dic.items():
        if isinstance(val, str) or isinstance(val, unicode):
            if is_ascii(val):
                new_dic[key] = str(val)
            else:
                new_dic[key] = unicode(val)

            continue

        if isinstance(val, dict) or isinstance(val, list):
            new_dic[key] = val
            continue

        new_dic[key] = str(val)

    return new_dic


def dict_raw_to_model(dic, model_type):
    model = model_type()

    for key, val in dic.items():
        setattr(
            model,
            key,
            val,
        )

    return model


def is_ascii(s):
    return all(ord(c) < 128 for c in s)
