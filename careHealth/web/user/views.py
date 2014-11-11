from django.shortcuts import render_to_response
from django.template import RequestContext

def profile(request):
    return

def login(request):
    return

def register(request):
    return render_to_response("user/templates/register.html", {}, context_instance=RequestContext(request))
