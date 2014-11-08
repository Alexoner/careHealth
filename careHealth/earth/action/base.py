import json

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.views.generic.base import View


ACTION_RET_PREFIX = '0'


class BaseAction(View):

    _http_methods_names = [
        'post',
        'get',
        'put',
        'delete',
    ]

    _ret_prefix = ACTION_RET_PREFIX

    def __init__(self, *args, **kwargs):
        super(BaseAction, self).__init__()
        self._ret = '000'
        self._msg = 'ok'
        self._content_type = 'application/json'
        self._http_status = 200

    def __getattr__(self, name):
        if name not in self.__dict__:
            return None

        return self.__dict__[name]

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):

        request_method = request.method.lower()

        if request_method in self._http_methods_names:
            processor = getattr(
                self,
                request_method,
            )
        else:
            return self.http_method_invalid(
                request,
                *args,
                **kwargs
            )

        if not processor:
            return self.http_method_invalid(
                request,
                *args,
                **kwargs
            )

        pre_process_hook = getattr(
            self,
            'pre_process_hook',
            None,
        )

        post_process_hook = getattr(
            self,
            'post_process_hook',
            None,
        )

        if pre_process_hook:
            if not pre_process_hook(request, *args, **kwargs):
                return self.response()

        if not processor(request, *args, **kwargs):
            return self.response()

        if post_process_hook:
            if not post_process_hook(request, *args, **kwargs):
                self.response()

        return self.response()

    def response(self):

        pre_render_hook = getattr(
            self,
            'pre_render_hook',
            None,
        )

        post_render_hook = getattr(
            self,
            'post_render_hook',
            None,
        )

        if pre_render_hook:
            if not pre_render_hook(self):
                return self._build_resp()

        self.render()

        if post_render_hook:
            if not post_render_hook(self):
                return self._build_resp()

        return self._build_resp()

    def _build_resp(self):
        return HttpResponse(
            self._resp_data_json,
            content_type=self._content_type,
            status=self._http_status,
        )

    def render(self):
        self._resp_data_dict = {
            'ret': self._ret_prefix + self._ret,
            'msg': self._msg,
        }

        if self._data:
            self._resp_data_dict['data'] = self._data
        elif isinstance(self._data, list):
            self._resp_data_dict['data'] = []

        self._resp_data_json = json.dumps(
            self._resp_data_dict,
        )

    def ret(self, ret):
        self._ret = ret
        return self

    def ret_prefix(self, ret_prefix):
        self._ret_prefix = ret_prefix
        return self

    def msg(self, msg):
        self._msg = msg
        return self

    def data(self, data):
        self._data = data
        return self

    def http_status(self, http_status):
        self._http_status = http_status
        return self

    def content_type(self, content_type):
        self._content_type = content_type
        return self

    def http_method_invalid(self, request, *args, **kwargs):
        self.ret('001').msg('http_method_invalid')
        return self.response()
