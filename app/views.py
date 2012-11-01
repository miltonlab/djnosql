# Create your views here.

from django.http import HttpResponse
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

from isummit2012.app import forms
from isummit2012.app import models

def index(request):
    if request.method == 'GET':
        form = forms.FormAsistente()
        data= dict(form=form)
        data.update(csrf(request))
        return render_to_response("registro.html", data)
    elif request.method == 'POST':
        ###asistente = models.Asistente.objects.create()
        asistente = models.Asistente()
        form = forms.FormAsistente(request.POST, instance=asistente)
        if form.is_valid():
            form.save()
            return render_to_response("ok.html", {'asistente':asistente})
        else:
            data = dict(form=form)
            data.update(csrf(request))
            return render_to_response("registro.html", data)
