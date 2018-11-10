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

"""
libreria de la clase: miArchivo
"""

class miArchivo:
    """
    Clase miArchivo: Clase para trabajar con todo tipo de archivos
    """
    
    def __init__(self, padre, nom, tipo,  esta):
        """
        Constructor por defecto parametrizado: padre (directorio padre del objeto), nom (nombre del objeto),  tipo (tipo de objeto), estado (como esta)
        """
        self.nombre = nom
        self.padre = padre
        self.tipo = tipo
        self.estado = esta

    def getNombre(self):
        """
        Devuelve el nombre del objeto
        """
        return self.nombre

    def getPadre(self):
        """
        Devuelve el directorio padre del objeto
        """
        return self.padre

    def getTipo(self):
        """
        Devuelve el tipo del objeto
        """
        return self.tipo

    def getEstado(self):
        """
        Devuelve el estado del objeto
        """
        return self.estado
    def setEstado(self, esta):
        """
        Devuelve el estado del objeto
        """
        self.estado = esta


