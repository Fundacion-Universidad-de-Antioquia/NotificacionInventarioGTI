# -*- encoding: utf-8 -*-

#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons

import sys
import os
import commands

def generatepdf():
    wdFormatPDF = 17
    archivos = os.path.join ('..' + '/' + 'archives' + '/' + 'Word' + '/' )
    out_file = os.path.join ('..' + '/' + 'archives' + '/' + 'PDF' + '/' )
    for archive in os.listdir(archivos):
        in_file=archivos + archive
        commands.getoutput('libreoffice --headless --convert-to pdf '+ in_file +' --outdir ' + out_file)
        commands.getoutput('chmod 755 -R ' + out_file)
