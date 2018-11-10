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

import sqlite3


if __name__ == '__main__' :
	# Empieza el main	
	try:
		conn = sqlite3.connect('prueba.sql')
		#conn = sqlite3.connect('usuario1','usuario1','prueba.sql')
		c = conn.cursor()
	except:
		print('Problemas de conexión.')
	try:
		c.execute('SELECT * FROM cliente')
	except:
		print('Error en la consulta.')
	try:
		conn.commit()
		conn.close()
	except:
		print('Error al cerrar la base de datos.')
	
	print('fin')
	
	
	
	

