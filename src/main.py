# -*- encoding: utf-8 -*-

#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons

import sys
import os

sys.path.append('core')
from exceljson import*
from createpdf import*
from envioSMTP import*
from generate_word import *
from eliminar import *


equipos = os.path.join ('files_in/Equipos.xlsx')
telefonos = os.path.join ('files_in/Telefonos.xlsx')
impresoras = os.path.join ('files_in/Impresoras.xlsx')
datos = os.path.join ('files_in/Cedulas_Correos_Cargos.xlsx')

realizados = os.path.join('files_in/Realizados.xlsx')


delete('../archives/PDF/*')
delete('../archives/Word/*')


datos = convertXLSJSON(datos, equipos, telefonos, impresoras)
realizados = convertXLSJSONrealizados(realizados)
word(datos)
generatepdf() 

enviarCorreo(datos, realizados)