# -*- encoding: utf-8 -*-

#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email import encoders
import os
 
# Iniciamos los parámetros del script

def enviarCorreo(datos, realizados):
    key = datos.keys()
    remitente = 'noreply@fundacionudea.co'
    password = 'gvqpofcmfcqtawun'
    asunto = 'Notificación de elementos a cargo según inventario'
    # Creamos la conexión con el servidor
    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    # Ciframos la conexión
    sesion_smtp.starttls() 

    # Iniciamos sesión en el servidor
    sesion_smtp.login(remitente, password)

    files = []

    for i in key:
        Nombre = ((datos[i]['Nombres']).decode('iso-8859-1').encode('utf8')).upper()
       
        if int(i) in realizados: 
            pass
        elif int(i) not in realizados:
            
            destinatario = datos[i]['Correo']
            ruta_adjunto = '../archives/PDF/' + str(i) +'.pdf'
            files.append(ruta_adjunto)
            cuerpo = "Cordial saludo ,\n \n" + Nombre + " \n \nEsperamos que se encuentre muy bien.\n \nEn el presente correo adjuntamos la información relacionada con el inventario de la Fundación Universidad de Antioquia, agradecemos leer el contenido del documento adjunto \n \nSi tiene alguna observación u objeción con la información del inventario y/o elementos asignados, la puede dar a conocer al proceso de Gestión Tecnologica e Innovación en un plazo maximo de 3 días habiles siguientes a esta notificación, en caso de no tener respuesta se considera que se acepta el inventario y/o elementos asignados. \n \nMuchas gracias. \n \nSaludos , \n \n"

            # Creamos el objeto mensaje
            mensaje = MIMEMultipart()
    
            # Establecemos los atributos del mensaje
            mensaje['From'] = remitente
            mensaje['To'] = destinatario
            mensaje['Subject'] = asunto
    
            # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
            mensaje.attach(MIMEText(cuerpo, 'plain'))
            msgText = MIMEText('<img src="https://fundacionudea.info/info_fundacion/unnamed.jpg">', 'html')
            mensaje.attach(msgText)
            # Abrimos el archivo que vamos a adjuntar
            archivo_adjunto = open(ruta_adjunto, 'rb')
            for f in files:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(open(f, "rb").read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= {0}".format(os.path.basename(f)))
                mensaje.attach(part)
                
            # Convertimos el objeto mensaje a texto
            texto = mensaje.as_string()
            
            # Enviamos el mensaje
            sesion_smtp.sendmail(remitente, destinatario, texto)
            print i
            files = []
    # Cerramos la conexión
    sesion_smtp.quit()