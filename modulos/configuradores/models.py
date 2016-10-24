# -*- coding: cp1252 -*-
from __future__ import unicode_literals
import pyclbr


from django.db import models

# Create your models here.

from modulos.maestras.models import  MaestraSimple, Maestra


MESES_CORTE=(('1','ENERO'),
('2','FEBRERO'),
('3','MARZO'),
('4','ABRIL'),
('5','MAYO'),
('6','JUNIO'),
('7','JULIO'),
('8','AGOSTO'),
('9','SEPTIEMBRE'),
('10','OCTUBRE'),
('11','NOVIEMBRE'),
('12','DICIEMBRE'))

def clases():
    for clase in pyclbr.readmodule(__name__).keys():
        if clase not in ['MasterProceso','DetalleMaster']:
            yield eval(clase)
