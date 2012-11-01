# -*- coding: utf-8 -*-

from django.forms import ModelForm, RadioSelect, ValidationError
from isummit2012.app import models 

class FormAsistente(ModelForm):

    """
    def __init__(self, *args, **kwargs):
        super(FormAsistente, self).__init__(*args, **kwargs)
        self.fields['sexo'].widget = RadioSelect(choices= (('M', 'Masculino'), ('F', 'Femenino')))
    """
    
    class Meta:
        model = models.Asistente

    def clean_dni(self):
        data = self.cleaned_data['dni']
        if len(data) < 10:
            raise ValidationError(u"Error tamaño dni")
        if len(data) == 10 and not data.isdigit():
            raise ValidationError(u"Error formato dni")
        try:
            existente = models.Asistente.objects.get(dni=data)
            if existente:
                raise ValidationError(u"Error dni ya está registrado")
        except models.Asistente.DoesNotExist:
            return data

    def clean_email(self):
        data = self.cleaned_data['email']
        try:
            existente = models.Asistente.objects.get(email=data)
            if existente:
                raise ValidationError(u"Error  email ya está registrado")
        except models.Asistente.DoesNotExist:
            return data 
    """
    def clean(self):
        data = self.cleaned_data
        email = data['email']
        try:
            existente = models.Asistente.objects.get(email=email)
            if existente:
                raise ValidationError(u"Error dni ya está registrado")
        except models.Asistente.DoesNotExist:
            return data
    """
