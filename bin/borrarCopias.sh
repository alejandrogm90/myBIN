#!/bin/bash
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
ficheroTemporal="/tmp/borrarCopias.tmp"
lineasFicheroTemporal=0

find "$1" 1 | grep -F [1] > $ficheroTemporal
lineasFicheroTemporal=`wc -l $ficheroTemporal | cut -d' ' -f1`


for linea in `seq 1 $lineasFicheroTemporal` ; do
	cadena1="`awk 'NR=='$linea $ficheroTemporal`"
	if [ -d "$cadena1" ] ; then 
		echo '----'
	else
		if [ -f "$cadena1" ] ; then 
			rm -R "$cadena1"
		else
			echo 'ERROR: '$cadena1  
		fi 
	fi
done

if [ -f $ficheroTemporal ] ; then rm $ficheroTemporal ; fi						# Elimino los ficheros temporales

