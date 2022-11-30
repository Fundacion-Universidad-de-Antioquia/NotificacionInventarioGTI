# -*- encoding: utf-8 -*-

#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons


def labores(cargo):
    if 'ASEO' in cargo.upper():
        texto = '1. Limpiar y mantener en orden y aseo las diferentes zonas como baños, áreas de tránsito, oficinas que le sean asignadas por el superior inmediato. \n 2. Responder por el estado y conservación de los recursos físicos dispuestos bajo su responsabilidad y adoptar los mecanismos para su conservación, protección y uso adecuado. \n 3. Responder por el uso racional de los insumos y elementos que les sean asignados para el cumplimiento de sus funciones. \n 4. Informar al superior inmediato sobre las novedades que se presenten en las áreas y dependencias que preste sus servicios. \n 5. Cumplir con las normas de bioseguridad establecidas en los protocolos de las instituciones educativas.'.decode("utf-8")
    elif 'ADMINISTRATIVO' in cargo.upper():
        texto = '1. Responder por el diligenciamiento y distribución oportuna de toda la correspondencia asignada, dejando las respectivas anotaciones o registros de control de recibo y entrega respectiva. \n 2. Atender y orientar a las personas que se presentan a la Institución Educativa por asuntos de su competencia, de acuerdo con las directrices del superior inmediato. \n 3. Realizar labores auxiliares de apoyo a los procesos administrativos, atención al público, recepción, radicación y archivo de documentos y los demás que le sean asignados y se ejecuten en la Institución Educativa. \n 4. Responder oportunamente por la información y suministro de los documentos que le sean requeridos, y elaborar los oficios y documentos que le sean confiados. \n 5. Velar por la seguridad y custodia de la documentación generada en la Institución Educativa y por el buen uso de los elementos y equipos asignados a su cargo para el desempeño de sus funciones. \n 6. Proyectar las novedades del personal docente y administrativo de la Institución Educativa para efectos de reconocimientos y pagos. \n 7. Elaborar documentos en procesadores de texto, cuadros en hojas de cálculo, enviar y recibir correos electrónicos de acuerdo a las directrices trazadas por el jefe inmediato, para apoyar las actividades propias de la Institución Educativa. \n 8. Diligenciar los libros reglamentarios del establecimiento como registro de logros, registro de matrículas, hojas de vida de docentes, alumnos y empleados, registro de títulos y actas de grados. \n 9. Expedir oportunamente los certificados de estudio, tiempo de servicio, constancias y demás documentos que le sean solicitados. \n 10. Presentar informes mensuales de actividades, con el visto bueno del Rector (a), según correspondencia  \n 11. Asistir a las capacitaciones ofrecidas por ambas entidades, en cumplimiento del Plan de Mejoramiento en la prestación del Servicio.'.decode("utf-8")
    elif 'BIBLIOTECA' in cargo.upper():
        texto = '1. Revisar, clasificar y controlar documentos, libros, datos, y elementos relacionados con los servicios de biblioteca. \n 2. Preparar y presentar informes sobre las actividades desarrollas, con la oportunidad y la periodicidad requeridas al jefe inmediato. \n 3. Orientar a los usuarios de la biblioteca acerca del uso racional de los recursos disponibles en respuesta a las necesidades presentadas. \n 4. Solicitar la autorización correspondiente para darle de baja a los textos en mal estado de acuerdo al procedimiento establecido. \n 5. Efectuar la rotulación y ubicación adecuada de cada una de las obras respondiendo a los procedimientos y técnicas respectivas. \n 6. Apoyar cuando se requiera las actividades que se desarrollan en la biblioteca de la institución educativa brindando una adecuada atención y docentes y estudiantes, velando por la buena utilización del material consultivo a disposición de los usuarios. \n 7. Clasificar el material consultivo de la biblioteca, llevar los registros correspondientes y control del material bibliográfico y audiovisual. \n 8. Presentar los informes y responder por el mantenimiento y seguridad del material a su cargo. \n 9. Administrar la biblioteca de acuerdo a las directrices institucionales y los procedimientos correspondientes. \n 10. Asistir a las capacitaciones ofrecidas por las entidades, en cumplimiento del plan de mejoramiento en la prestación del servicio. \n 11. Realizar las demás actividades asignadas por el jefe inmediato de acuerdo con la naturaleza y área de desempeño.'.decode("utf-8")
    elif 'GENERALES' in cargo.upper():
        texto = '1. Limpiar y regar los jardines que formen parte de la planta física. \n 2. Preparar y presentar informes sobre las actividades desarrolladas. \n 3. Realizar el mantenimiento de la infraestructura físicas, previo cumplimiento de los requisitos de Ley. \n 4. Colaborar con el fotocopiado de los documentos necesarios para el normal funcionamiento de la Institución Educativa. \n 5. Responder por los elementos de su cargo. \n 6. Realizar la planeación de las actividades propias de su cargo acorde con los procedimientos establecidos. \n 7. Elaborar solicitud de insumos requeridos para atender las necesidades de la Institución Educativa. \n 8. Atender al cliente interno y externo de manera personal de acuerdo a las políticas Institucionales y los procedimientos establecidos. \n 9. Apoyar las labores logísticas necesarias para la organización de los diferentes eventos que se realicen. \n 10. Realizar las reparaciones menores a que haya lugar en la infraestructura física. \n 11. Cumplir con las normas de bioseguridad establecidos en los protocolos de las instituciones educativas.'.decode("utf-8")
    return texto

def salarioCargo(cargo, doc):
    if 'ASEO' in cargo.upper():
        texto1 = ('CARGO A DESEMPEÑAR:		' + cargo.upper())
        texto2 = ('SALARIO:				$908.526 (1 SMLMV) mensuales')
        
    elif 'ADMINISTRATIVO' in cargo.upper() or 'BIBLIOTECA' in cargo.upper():
        texto1 = ('CARGO A DESEMPEÑAR:		' + cargo.upper())
        texto2 = ('SALARIO:				$989.096 mensuales')

    elif 'GENERALES' in cargo.upper():    
        texto1 = ('CARGO A DESEMPEÑAR:		' + cargo.upper())
        texto2 = ('SALARIO:				$1.010.470 mensuales')

    return texto1, texto2

def suma(cargo):
    if 'ASEO' in cargo.upper():
        texto = 'la suma de novecientos ocho mil quinientos veintiséis pesos ($908.526), pagaderos por períodos mensuales vencidos.'.decode("utf-8")
    elif 'ADMINISTRATIVO' in cargo.upper() or 'BIBLIOTECA' in cargo.upper():
        texto = 'la suma de novecientos ochenta y nueve mil noventa y seis pesos ($989.096), pagaderos por períodos mensuales vencidos.'.decode("utf-8")
    elif 'GENERALES' in cargo.upper():    
        texto = 'la suma de un millón diez mil cuatrocientos setenta pesos ($1.010.470), pagaderos por períodos mensuales vencidos.'.decode("utf-8")

    return texto