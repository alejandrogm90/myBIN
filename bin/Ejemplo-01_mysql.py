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

from misClases.bd_mysql import bd_mysql
import hashlib
import time

def insertarEnBucle(bd, cad, inicio, fin):
    for l1 in range(inicio,fin):
        cad1 = cad + str(l1)
        token = hashlib.md5()
        token.update(cad1.encode('utf-8'))
        query = "INSERT INTO usuario (id, nombre, correo, clave) VALUES (CURRENT_TIMESTAMP, '"+cad1+"', '"+cad1+"@gmail.com', '"+token.hexdigest()+"' );"
        bd.run_query(query)
        time.sleep(1)

def mostrarDatos(db, cad):
    for linea in bd.run_query(cad):
        print(linea)

if __name__ == '__main__':
    bd = bd_mysql('localhost', 'gestion1', 'G#gestion1', 'prueba1')
    
    #insertarEnBucle(bd, 'usuario', 10,20)
    mostrarDatos(bd, "SELECT * FROM usuario WHERE nombre LIKE '%2%' ")
        
    

    
