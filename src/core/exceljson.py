
#-*-encoding: utf-8 -*-
#Created by @ceapalaciosal
#Codigo bajo Creative Commons


#!/usr/bin/env python

#List Library Import

from operator import index
import xlrd
from fecha import *



def convertXLSJSON(datos_generales, equipos, telefonos, impresoras):
		

		datos_generales = xlrd.open_workbook(datos_generales)
		equipos = xlrd.open_workbook(equipos)
		telefonos = xlrd.open_workbook(telefonos)
		impresoras = xlrd.open_workbook(impresoras)

		#Numero de Sheet donde se encuentran los datos BASE
		book_general = datos_generales.sheet_by_index(0) 
		book_equipos = equipos.sheet_by_index(0)
		book_telefonos = telefonos.sheet_by_index(0)
		book_impresoras = impresoras.sheet_by_index(0)

		datos = {}
	
		index = 0

		#recorremos datos generales
		for row in range(0, book_general.ncols):

			#Recorremos las posiciones de los encabezados de los datos generales
			titulo = book_general.cell_value(0, row).encode('utf-8')
			if titulo == 'CEDULA' or titulo == 'Cedula':
				colCedulaGeneral = index
			if titulo == 'NOMBRE' or titulo == 'Nombre':
				colNombreGeneral = index
			if titulo == 'APELLIDO' or titulo == 'Apellidos':
				colApellidosGeneral = index	
			if titulo == 'CARGO' or titulo == 'Cargo':
				colCargoGeneral = index
			if titulo == 'CORREO' or titulo == 'Correo':
				colEmailGeneral = index

			index += 1
		
		#Recorremos las posiciones de los encabezados equipos de computo
		index = 0
		for row in range(0, book_equipos.ncols):
			titulo = book_equipos.cell_value(0, row).encode('utf-8')
			if titulo == 'Tipo':
				colTipoPC = index
			if titulo == 'Número de inventario':
				colInventarioPC = index
			if titulo == 'Fabricante':
				colFabricantePC = index
			if titulo == 'Número de serie':
				colNumeroSeriePC = index
			if titulo == 'Modelo':
				colModeloPC = index
			if titulo == 'Estado': 
				colEstadoPC = index
			if titulo == 'Cedula':
				colCedulaPC = index
			index += 1


		#Recorremos las posiciones de los encabezados equipos de telefono
		index = 0
		for row in range(0, book_telefonos.ncols):
			titulo = book_telefonos.cell_value(0, row).encode('utf-8')
			if titulo == 'Número de inventario':
				colInventarioTel = index
			if titulo == 'Estado':
				colEstadoTel = index
			if titulo == 'Tipo':
				colTipoTel = index
			if titulo == 'Número de serie': 
				colSerieTel = index
			if titulo == 'Fabricante': 
				colFabricanteTel = index
			if titulo == 'Cedula':
				colCedulaTel = index
			index += 1

		#Recorremos las posiciones de los encabezados equipos de Impresoras
		index = 0
		for row in range(0, book_impresoras.ncols):
			titulo = book_impresoras.cell_value(0, row).encode('utf-8')
			if titulo == 'Nombre':
				colNombreImp = index
			if titulo == 'Cedula':
				colCedulaImp = index
			if titulo == 'Número de inventario':
				colInventarioImp = index
			if titulo == 'Número de serie': 
				colSerieImp = index
			if titulo == 'Fabricante': 
				colFabricanteImp = index
			if titulo == 'Estado':
				colEstadoImp = index
			if titulo == 'Modelo':
				colModeloImp = index
			index += 1

		#Recorremos la BD y llenamos el Json con los datos basicos
		for col in range(1, book_general.nrows):		
		 	datos[int(book_general.cell_value(col,colCedulaGeneral))] = {
		 	'Nombres': str(book_general.cell_value(col,colApellidosGeneral).encode('latin1')) + ' ' + str(book_general.cell_value(col,colNombreGeneral).encode('latin1')), 
			'Nombre': str(book_general.cell_value(col,colNombreGeneral).encode('latin1')),
			'Apellidos': str(book_general.cell_value(col,colApellidosGeneral).encode('latin1')),
		 	'Cargo': str(book_general.cell_value(col,colCargoGeneral).encode('utf-8')),
		 	'Correo': str(book_general.cell_value(col,colEmailGeneral)), 
		 	'Equipos': {'PC':{}, 'CEL':{}, 'IP': {}, 'IMP': {}},
		 	}


		
		#Llenamos la BD con los Equipos de Computo
		for col in range(1, book_equipos.nrows):
				if book_equipos.cell_value(col,colCedulaPC) == '':
					pass
				else: 
					if datos[int(book_equipos.cell_value(col,colCedulaPC))]['Equipos']['PC'].get(book_equipos.cell_value(col,colInventarioPC)) is None:
						datos[int(book_equipos.cell_value(col,colCedulaPC))]['Equipos']['PC'][str(book_equipos.cell_value(col,colInventarioPC))] = {
							'Tipo': str(book_equipos.cell_value(col,colTipoPC)),
							'Fabricante': str(book_equipos.cell_value(col,colFabricantePC)),
							'Serie': str(book_equipos.cell_value(col,colNumeroSeriePC)),
							'Modelo': int(book_equipos.cell_value(col,colModeloPC)),
							'Estado': str(book_equipos.cell_value(col,colEstadoPC))
							}

		
		#Llenamos con los telefonos
		for col in range(1, book_telefonos.nrows):
			if book_telefonos.cell_value(col,colCedulaTel) == '':
					pass
			else: 
				if book_telefonos.cell_value(col,colTipoTel) == 'Celular':
						if datos[int(book_telefonos.cell_value(col,colCedulaTel))]['Equipos']['CEL'].get(str(book_telefonos.cell_value(col,colInventarioTel))) is None:
							datos[int(book_telefonos.cell_value(col,colCedulaTel))]['Equipos']['CEL'][str(book_telefonos.cell_value(col,colInventarioTel))] = {
								'Estado': str(book_telefonos.cell_value(col,colEstadoTel)),
								'Tipo': str(book_telefonos.cell_value(col,colTipoTel)),
								'Serie': str(book_telefonos.cell_value(col,colSerieTel)),
								'Fabricante': str(book_telefonos.cell_value(col,colFabricanteTel))
								}
						
				elif book_telefonos.cell_value(col,colTipoTel) == 'IP' or book_telefonos.cell_value(col,colTipoTel) == 'Inalambrico':
					if datos[int(book_telefonos.cell_value(col,colCedulaTel))]['Equipos']['IP'].get(str(book_telefonos.cell_value(col,colInventarioTel))) is None:
						datos[int(book_telefonos.cell_value(col,colCedulaTel))]['Equipos']['IP'][str(book_telefonos.cell_value(col,colInventarioTel))] = {
							'Estado': str(book_telefonos.cell_value(col,colEstadoTel)),
							'Tipo': str(book_telefonos.cell_value(col,colTipoTel)),
							'Serie': str(book_telefonos.cell_value(col,colSerieTel)),
							'Fabricante': str(book_telefonos.cell_value(col,colFabricanteTel))
							}

		#Llenamos con Impresoras
		for col in range(1, book_impresoras.nrows):
				if book_impresoras.cell_value(col,colCedulaImp) == '':
					pass
				else: 
					#print book_impresoras.cell_value(col,colInventarioImp)
					if datos[int(book_impresoras.cell_value(col,colCedulaImp))]['Equipos']['IMP'].get(book_impresoras.cell_value(col,colInventarioImp)) is None:
						datos[int(book_impresoras.cell_value(col,colCedulaImp))]['Equipos']['IMP'][str(book_impresoras.cell_value(col,colInventarioImp))] = {
							'Nombre': str(book_impresoras.cell_value(col,colNombreImp)),
							'Fabricante': str(book_impresoras.cell_value(col,colFabricanteImp)),
							'Serie': str(book_impresoras.cell_value(col,colSerieImp)),
							'Modelo': str(book_impresoras.cell_value(col,colModeloImp)),
							'Estado': str(book_impresoras.cell_value(col,colEstadoImp))
							}

		return datos

def convertXLSJSONrealizados(direccion):
		realizados = []
		workbook = xlrd.open_workbook(direccion)
		sh = workbook.sheet_by_index(0) #Numero de Sheet donde se encuentran los datos BASE
		for col in range(0, sh.nrows):
			realizados.append(int(sh.cell_value(col,0)))	
		return realizados