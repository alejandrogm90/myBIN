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

import os, sys
from archivo import miArchivo

"""
libreria de la clase: miDirectorio
"""

class miDirectorio:
    """
    miDirectorio: clase para trabajar con los objetos de tipo miArchivo
    """
    
    def __init__(self, dire, exte):
        """
        Constructor por defecto parametrizado
        """
        self.extension = exte
        self.direccion = dire
        self.archivo = []
        #Sacamos el contenido del directorio
        ficheros1 = os.listdir(self.direccion)
        for e in ficheros1:
            if os.path.isdir(self.direccion+self.extension+e):
                self.archivo.append(miArchivo(self.direccion, e, "d", 0))
            elif os.path.isfile(self.direccion+self.extension+e):
                self.archivo.append(miArchivo(self.direccion, e, "f", 0))
        
    def getDireccion(self):
        """
        Devuelve la direccion actual
        """
        return self.direccion

    def getNumOjetos(self):
        """
        Devuelve el numero de objetos que tiene este directorio
        """
        return len(self.archivo)        

    def getDirectorios(self):
        """
        Devuelve TODOS los objetos de tipo miArchivo
        """
        return self.archivo  

    def getDirectorio(self, posicion):
        """
        Devuelve un objeto de tipo miArchivo, con una posicion dada como parametro
        """
        return self.archivo[posicion]        

    def sacaArbolCompleto(self, lugar):
        """
        Devuelve una lista con TODOS los objetos de tipo miArchivo que hay en el lugar pasado por parametro
        """
        listaDiresctorios = []
        listaDiresctorios.append(lugar)
        dirActual = 0
        salir = True
        while salir:
            if dirActual == len(listaDiresctorios) :
                 salir = False
            else:
                if os.path.isdir(listaDiresctorios[dirActual]):
                    md1 = miDirectorio(listaDiresctorios[dirActual],self.extension)
                    for a in md1.getDirectorios():
                        listaDiresctorios.append(a.getPadre()+self.extension+a.getNombre())
                dirActual = dirActual + 1
        return listaDiresctorios

    def actualizaArbolDeDirectorios(self, lista1, directorio):
        """
        Devuelve una lista con TODOS los objetos de tipo miArchivo(solo directorios) que hay en el lugar pasado por parametro
        """
        listaDiresctorios = []
        for l1 in lista1:
            if l1[0:len(directorio)] != directorio:
                listaDiresctorios.append(l1)
        return listaDiresctorios
