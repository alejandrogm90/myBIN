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
import psycopg2

"""
libreria de la clase: BDpostgre
"""
class BDpostgre():
    """
    Clase BDpostgre: Clase para trabajar con todo tipo de BDs
    """
    def __init__(self, db, usuario, clave, serbidor, puerto):
        """
        Constructor por defecto parametrizado: padre (directorio padre del objeto),
        nom (nombre del objeto), tipo (tipo de objeto), estado (como esta)
        """
        self.db = db
        self.usuario = usuario
        self.puerto = puerto
        self.clave = clave
        self.serbidor = serbidor
        self.conexion=""
        self.cursor=""

    def setConexion(self):
        """
        Funcion setConexion: establece una coxion con la BD
        """
        try:
            self.conexion = psycopg2.connect(
                user = self.usuario,
                database = self.db,
                port = self.puerto,
                password = self.clave,
                host = self.serbidor
            )
        except psycopg2.Error as error1:
            print(error1.pgerror)
	    # Open a cursor to perform database operations
        try:
            self.cursor = self.conexion.cursor()
        except psycopg2.Error as error1:
            print(error1.pgerror)

    def closeConexion(self):
        """
        Funcion closeConexion: cierra la conexion con la BD
        """
        self.cursor.close()
        self.conexion.close()

    def setConsulta(self,consulta):
        """
        Funcion setConsulta: consulta (cadena de consulta)
        """
        try:
            self.cursor.execute(consulta)
        except psycopg2.Error as error1:
            print(error1.pgerror)
        # Devuelvo la salida
        return self.cursor

    def getNumFilas(self):
        """
        Funcion closeConexion: cierra la conexion con la BD
        """
        return len(self.cursor)

    def makeCommit(self):
        """
        Make the changes to the database persistent
        """
        self.conexion.commit()

    def makeRollback(self):
        """
        Make the changes to the database persistent
        """
        self.conexion.rollback()

if __name__ == "__main__" :
    print("Libreria BDpostgre.")
