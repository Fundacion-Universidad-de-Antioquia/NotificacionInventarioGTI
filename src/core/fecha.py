# -*- encoding: utf-8 -*-

#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons

"""
	Formatear fecha actual de modo que su formato quede como:
	"Miércoles, 19 de Diciembre del 2018"
	@author parzibyte
"""
from datetime import datetime

def fecha(anio, mes, dia):
    #Diccionarios de días y meses
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre",
    }

    dias = {
        0: "Domingo",
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
    }

    #ahora = datetime.now()
    numero_mes = int(mes)
    # A entero para quitar los ceros a la izquierda en caso de que existan
    numero_dia = int(dia)
    # Leer diccionario
    #dia = dias.get(numero_dia)
    mes = meses.get(numero_mes)
    # Formatear
    fecha = "{} de {} del {}".format(dia, mes, anio)
    #Imprimir
    return fecha
    # Miércoles, 19 de Diciembre del 2018