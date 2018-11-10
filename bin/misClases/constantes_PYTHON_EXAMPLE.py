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
libreria de la clase: Configuracion
"""

class Constantes():
    def __init__(self):
        self.basedatos = [ "localhost","5432", "BD-name", "postgres", "postgres" ]
        self.correo = ['info@gmail.com','passMail', 'smtp.gmail.com', '587']
        self.mi_correo = 'yourmail'
        self.dir_web = "http://www.name.com"
        self.fich_error = "log_error"
        self.fich_notificacion = "log_notificacion"

    def getMiCorreo(self):
        return self.mi_correo

    def getCorreo(self):
        return self.correo