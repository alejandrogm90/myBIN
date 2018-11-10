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
 
# AHORA - Obtenemos la IP nuestra IP real de la WEB - (http://www.mi-ip.net/)
import urllib2

if __name__ == '__main__':
    try:
        respuesta = pagina = trozo = ""
        indice = 0

        respuesta = urllib2.urlopen('http://www.cualesmiip.com/')
        pagina = respuesta.read()
        # Hay que buscar el id por que no siempre la posición es la misma en la página
        indice = pagina.find("titulo-ip")
        indice = indice + 52
        for ind2 in range(indice, (indice + 15)):
            trozo += pagina[ind2]
        trozo = trozo.split("<")
        # Escribe tu IP
        print(trozo[0])
    except:
        print("ERROR")
        exit(1)
