# -*- encoding: utf-8 -*-

#! /usr/bin/env python
#created by @ceapalaciosal
#under code Creative Commons
import os
import glob

def delete(dir):
    files = glob.glob(dir)
    for f in files:
        os.remove(f)