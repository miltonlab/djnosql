# -*- coding: utf-8 -*-

from django.db import models
from djangotoolbox.fields import EmbeddedModelField

# Create your models here.

class Asistente(models.Model):
    dni = models.CharField(max_length='15')
    nombres = models.CharField(max_length='30')
    apellidos = models.CharField(max_length='30')
    sexo = models.CharField(max_length='1',
                            choices=(('M','Masculino'), ('F', 'Femenino')))
    email = models.EmailField(max_length=255, verbose_name=u'Correo electrónico')
    institucion = models.CharField(max_length='255',
                                   verbose_name=u'Institución/Empresa')
    # TODO
    # categoria = EmbeddedModelField('Categoria')
    categoria = models.CharField(max_length='2',
                                 choices=(('E', 'Estudiante'),('D','Docente'),
                                         ('P','Profesional'),('I', 'Independiente')
                                          )
                                 )
    registro = models.DateTimeField(auto_now_add=True,
                                    verbose_name=u'Fecha Registro')
                                   
    def __unicode__(self):
        return "{0} {1}".format(self.nombres, self.apellidos)
            
    
class Categoria(models.Model):
    nombre = models.CharField(max_length='255')

    def __unicode__(self):
        return self.nombre
