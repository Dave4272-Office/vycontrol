from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import vyos

from config.models import Instance


def vycenter_login(request):
    
    template = loader.get_template('vycenter/vycenter_login.html')
    context = {
    }
    return HttpResponse(template.render(context, request))



