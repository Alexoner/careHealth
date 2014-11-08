# -*- coding: utf-8 -*-
import json


def json_pre_process_hook(action, request, *args, **kwargs):
    json_data = request.body

    if not json_data:
        action.ret('002').msg('json_params_required')
        return False

    try:
        param_dict = json.loads(json_data)
    except ValueError:
        action.ret('003').msg('json_params_invalid')
        return False

    for key, value in param_dict.items():
        setattr(action, key, value)

    return True


def query_pre_process_hook(action, request, *args, **kwargs):
    params_dict = request.GET

    if not params_dict:
        return True

    for key, value in params_dict.items():
        setattr(action, key, value)

    return True


def form_pre_process_hook(action, request, *args, **kwargs):
    param_dict = request.POST

    if not param_dict:
        action.ret('004').msg('form_params_required')
        return False

    for key, value in param_dict.items():
        setattr(action, key, value)

    return True


def jsonp_post_render_hook(action):
    if action.jsonp_callback:
        action.resp_data_json(
            action.jsonp_callback + '('
            + action.resp_data_json + ')',
        )
    else:
        action.ret('005').msg('jsonp_callback_required')

        if action._data:
            del action._data

        action.render()

        return False

    return True
