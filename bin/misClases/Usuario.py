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

import datetime

"""
libreria de la clase: Usuario
"""

class Usuario():
    def __init__(self,id=0,activo=False,fecha_baja=datetime.date(2000,1,1),nombre="",clave="",descripcion="",estado_coche=0):
        """
        Constructor por defecto parametrizado: padre (directorio padre del objeto), nom (nombre del objeto),  tipo (tipo de objeto), estado (como esta)
        """
        self.id = id
        self.activo = activo
        self.fecha_baja = fecha_baja
        self.nombre = nombre
        self.clave = clave
        self.descripcion = descripcion
        self.estado_coche = estado_coche
        
    def cadena(self):
        cad="\t|"
        return str(
            str(self.id)+cad+
            str(self.activo)+cad+
            str(self.fecha_baja)+cad+
            self.nombre+cad+
            self.clave+cad+
            self.descripcion+cad+
            str(self.estado_coche)
            )
