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

import MySQLdb

class bd_mysql():

    def __init__(self, host='localhost', user='user', password='password', database='database'):
        self.datos = [host, user, password, database]

    def run_query(self, query=''): 
         
    
        conn = MySQLdb.connect(*self.datos)     # Conectar a la base de datos 
        cursor = conn.cursor()                  # Crear un cursor 
        cursor.execute(query)                   # Ejecutar una consulta 
    
        if query.upper().startswith('SELECT'): 
            data = cursor.fetchall()            # Traer los resultados de un select 
        else: 
            conn.commit()                       # Hacer efectiva la escritura de datos 
            data = None 
    
        cursor.close()                          # Cerrar el cursor 
        conn.close()                            # Cerrar la conexión 
    
        return data

if __name__ == '__main__':
    print("Clase bd_mysql")