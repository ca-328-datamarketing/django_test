from http.client import HTTPResponse
from os import lseek


from django.http import HttpResponse
from datetime import datetime
import datetime
import pytz
from django.views.generic import TemplateView


def helloworldfunction(request):
    now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    return HttpResponse(f"<h1>{now}</h1>")

class helloworldclass(TemplateView):
    template_name = "hello.html"