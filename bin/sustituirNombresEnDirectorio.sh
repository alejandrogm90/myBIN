#!/bin/bash

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

# Variables
ficheroTemporal="/tmp/`echo "$0" | cut -d'/' -f5`.tmp"
lineasFicheroTemporal=0

# Funciones
function error1 () { echo '\n [DIRECTORIO] [CADENA-ORIGINAL] [CADENA-SUSTITUTA]' ; exit $1 }		# Fución de salida de error

if [ $1 == '-h' ] || [ $1 == '--help' ] ; then error1 1 ; fi						# Para la ayuda
if [ $# -ne 3 ] ; then echo 'El número de parámetros introducidos es erroneo.' ; error1 2 ; fi		# Posible error en el número de parámetros introducidos
if [ ! -d $1 ] ; then echo 'El directorio "'$1'" no existe.' ; error1 3 ; fi				# Por si el directorio no existe

ls $1 >> $ficheroTemporal
lineasFicheroTemporal=`wc -l $ficheroTemporal | cut -d' ' -f1`

for linea in `seq 1 $lineasFicheroTemporal` ; do
	cadena1="`awk 'NR=='$linea $ficheroTemporal`"
	cadena2="`echo "$cadena1" | sed -e "s/$2/$3/g" `"
	mv "$1/$cadena1" "$1/$cadena2" &> /dev/null
	echo "$cadena1"' -> '`echo "$cadena1" | sed -e "s/$2/$3/g" `
done

if [ -f $ficheroTemporal ] ; then rm $ficheroTemporal ; fi						# Elimino los ficheros temporales



