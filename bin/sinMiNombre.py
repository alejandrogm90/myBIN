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

import os
import sys

if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        print("Número de parámetros erroneo.")
        exit(1)
    else:
        trozos = sys.argv[1].split("/")
        if len(trozos) <= 1:
            print("La cadena enviada es erronea erroneo.")
            exit(2)
        else:
            cadena_nueva = ""
            for parte in range(len(trozos)-1):
                cadena_nueva = cadena_nueva + trozos[parte] + "/"
            print(cadena_nueva)

