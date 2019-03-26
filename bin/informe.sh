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

# GLOBALES
#=========
fichero_IP="/home/COMPARTIDA/datos/ip.tmp"
ficheroSalida="/home/COMPARTIDA/datos/informe.tmp"
HOY=$(date +%F)' '$(date +%T)
MiIP=`~/bin/miIP.py`

# Corrección de posibles errores
#========================================================
if [ ! -f $fichero_IP ] || [ ! -s $fichero_IP ] ; then 
    echo $MiIP > $fichero_IP
fi

# Contenido del texto del fichero de salida
#========================================================
echo 'Host: '$HOSTNAME > $ficheroSalida
echo 'Fecha: '$HOY >> $ficheroSalida
if [ "$MiIP" != "`head -1 $fichero_IP`" ] ; then
	echo 'Mi IP anterior era: http://'"`head -1 $fichero_IP`" >> $ficheroSalida
fi
echo 'Mi IP actual es: http://'$MiIP >> $ficheroSalida
echo 'Mi IP local es: http://'`~/bin/miIP.py -l` >> $ficheroSalida
mpstat -P ALL >> $ficheroSalida
echo ' ' >> $ficheroSalida
free -h >> $ficheroSalida



#========================================================
# Envío por correo o muestro por pantalla
if [ $# -eq 1 ] && [ $1 == "enviar" ] ; then
	if [ "$MiIP" != "`head -1 $fichero_IP`" ] ; then
		~/bin/enviarCorreo.py $ficheroSalida
	fi
else
	cat $ficheroSalida
fi

# Elimino el fichero temporal
#echo '' > $ficheroSalida

