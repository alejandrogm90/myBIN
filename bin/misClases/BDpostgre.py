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
import postgresql

"""
libreria de la clase: BDpostgre
"""
class BDpostgre():
    """     
    Clase miArchivo: Clase para trabajar con todo tipo de archivos
    """
    def __init__(self,config):
        """
        Constructor por defecto parametrizado: padre (directorio padre del objeto),
        nom (nombre del objeto), tipo (tipo de objeto), estado (como esta)
        """        
        self.configuracion=config
        self.conexion=""
        self.resultado=""

    def setConexion(self):
        """
        Funcion setConexion: establece una coxion con la BD
        """
        self.conexion = postgresql.open(
            user = self.configuracion.user,
            database = self.configuracion.database,
            port = self.configuracion.port,
            password = self.configuracion.password,
            host = self.configuracion.host
        )

    def closeConexion(self):
        """
        Funcion closeConexion: cierra la conexion con la BD
        """
        self.conexion.close()

    def setConsulta(self,consulta):
        """
        Funcion setConsulta: consulta (cadena de consulta)
        """
        try:
            #self.resultado = self.conexion.prepare(consulta).first()
            #self.resultado = self.conexion.execute(consulta)
            self.resultado = self.conexion.prepare(consulta)            
        except :
            print("Unexpected error: ", sys.exc_info()[0])
            for lin in sys.exc_info():
                print(str(lin))
        # Devuelvo la salida
        return self.resultado

    def getNumFilas(self):
        """
        Funcion closeConexion: cierra la conexion con la BD
        """
        return len(self.resultado())

if __name__ == "__main__" :
    print("Libreria BDpostgre.")
