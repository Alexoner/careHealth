from .base import BaseAction
from .hooks import (
    jsonp_post_render_hook,
    json_pre_process_hook,
    query_pre_process_hook,
    form_pre_process_hook,
)


class RestJsonAction(BaseAction):

    def __init__(self, *args, **kwargs):
        super(RestJsonAction, self).__init__(*args, **kwargs)

    def pre_process_hook(self, request, *args, **kwargs):
        if request.method.lower() == 'get':
            return query_pre_process_hook(
                self,
                request,
                *args,
                **kwargs
            )
        elif request.method.lower() == 'post' or \
                request.method.lower() == 'put':
            return json_pre_process_hook(
                self,
                request,
                *args,
                **kwargs
            )
        elif request.method.lower() == 'delete':
            if request.GET:
                return query_pre_process_hook(
                    self,
                    request,
                    *args,
                    **kwargs
                )
            else:
                return json_pre_process_hook(
                    self,
                    request,
                    *args,
                    **kwargs
                )

        return True


class RestJsonActionWithJsonp(RestJsonAction):

    def __init__(self, *args, **kwargs):
        super(RestJsonActionWithJsonp, self).__init__(
            *args,
            **kwargs
        )

    def post_render_hook(self):
        return jsonp_post_render_hook(
            self,
        )


class RestFormAction(BaseAction):

    def __init__(self, *args, **kwargs):
        super(RestFormAction, self).__init__(*args, **kwargs)

    def pre_process_hook(self, request, *args, **kwargs):
        if request.method.lower() == 'get':
            return query_pre_process_hook(
                self,
                request,
                *args,
                **kwargs
            )
        elif request.method.lower() == 'post' or \
                request.method.lower() == 'put':
            return form_pre_process_hook(
                self,
                request,
                *args,
                **kwargs
            )
        elif request.method.lower() == 'delete':
            if request.GET:
                return query_pre_process_hook(
                    self,
                    request,
                    *args,
                    **kwargs
                )
            else:
                return form_pre_process_hook(
                    self,
                    request,
                    *args,
                    **kwargs
                )

        return True


class RestFormActionWithJsonp(RestFormAction):

    def __init__(self, *args, **kwargs):
        super(RestFormActionWithJsonp, self).__init__(
            *args,
            **kwargs
        )

    def post_render_hook(self):
        return jsonp_post_render_hook(
            self,
        )
