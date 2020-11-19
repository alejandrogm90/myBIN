#!/bin/bash
#
#
#       Copyright 2017 Alejandro Gómez Martín
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

salida=0

function cadena() {
	frase=""
	for lin1 in `seq 1 $2` ; do
		cad1=`echo $1 | cut -d':' -f$lin1`
		case $lin1 in
			4) if [ $cad1 == '\N' ] ; then cad1="'Descripcion1'" ; else cad1="'$cad1'" ; fi ;;
			5) if [ $cad1 == '\N' ] ; then cad1="'vacio'" ; else cad1="'$cad1'" ; fi ;;	
		esac
		if [ $cad1 == '\N' ] ; then cad1=50 ; fi
		if [ $lin1 -eq $2 ] ; then 
			echo "$cad1"
		else
			echo "$cad1"', '
		fi
	done
}

if [ $# -eq 2 ] ; then
	# Create de new file
	echo "" > $2
	# Create a temporal file
	cat $1 > $1.temp
	sed -i 's/\t/:/g' $1.temp
	sed -i 's/ /_/g' $1.temp
	# Start the progam
	frase=""
	cont1=5
	for columna in `cat $1.temp` ; do
		frase="INSERT INTO adjuntos (idadjunto, idpartner, tipoadjunto, descripcion, fichero) VALUES ("`cadena $columna $cont1`");"
		echo $frase
		echo $frase >> $2
	done
else
	echo ""
	echo "$0 [file_in] [file_out] "
	echo "Change db data 1"
	echo ""
	salida=1
fi
exit $salida

