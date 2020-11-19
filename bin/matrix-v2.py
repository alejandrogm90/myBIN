#!/usr/bin/env python3

#
#
#       Copyright 2017 Alejandro Gomez
#
#       This program is free software: you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation, either version 3 of the License, or
#       (at your option) any later version.
#
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#
#       You should have received a copy of the GNU General Public License
#       along with this program.  If not, see <http://www.gnu.org/licenses/>.


import sys
import os
import re

def cambiarLinea(linea):
    nueva = ""
    for pos in range(0,len(linea)-1):
        """
        l2 = re.findall('[a-zA-Z0-9]*', linea[pos])
        if (l2[0] != ''):
            nueva = nueva + str(chr(ord(linea[pos])+1))
        else:
            nueva = nueva + linea[pos]
        """
        nueva = nueva + str(chr(ord(linea[pos])+1))
    return nueva


def procesarFichero(nombre):
    f1 = open(nombre,'r')
    linea = f1.readline()
    while (len(linea) > 0):
        print(cambiarLinea(linea))
        linea = f1.readline()

if __name__ == "__main__":
    procesarFichero('/opt/COMPARTIDA/PROYECTOS/myBin/bin/calculadora.py')
    
    

