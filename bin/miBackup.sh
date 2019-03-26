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

# VARIABLES GLOBALES
fichTemporal="/tmp/"$0".tmp"
fichLista="/home/COMPARTIDA/datos/BACKUP_list"
fichLOG="/home/COMPARTIDA/datos/BACKUP_log"
fichErrorLOG="/home/COMPARTIDA/datos/BACKUP_error_log"
dirBackup="/home/COMPARTIDA/BACKUP/"

# FUNCIONES
function bacupRealizado() {
    salida=0
    ficheroTemporal="$fichLOG"
    lineasFicheroTemporal=`wc -l "$ficheroTemporal" | cut -d' ' -f1`
    for linea in `seq 1 $lineasFicheroTemporal` ; do
        cadena1="`awk 'NR=='$linea $ficheroTemporal`"
        if [ "$cadena1" != " " ] ; then
            if [ "`echo "$cadena1" | cut -d' ' -f7 | cut -d'"' -f2`" == "`date +%F`" ] ; then
                salida=1
            fi
        fi
    done
    echo $salida
}

# ANTES DE EMPEZAR
if [ ! -f $fichLOG ] ; then echo "" >> $fichLOG ; fi
if [ ! -f $fichErrorLOG ] ; then echo "" >> $fichErrorLOG ; fi
if [ ! -d $dirBackup ] ; then mkdir $dirBackup ; fi

if [ `bacupRealizado` == 0 ] ; then
    # Creo los BackUps
    echo 'Se ha hecho una copia el "'`date +%F` `date +%T`'".' >> $fichLOG
    ficheroLista="$fichLista"
    lineasficheroLista=`wc -l "$ficheroLista" | cut -d' ' -f1`
    echo 'Empaquetando....'
    for linea in `seq 1 $lineasficheroLista` ; do
        cadena1="`awk 'NR=='$linea $ficheroLista`"
        if [ "$cadena1" != " " ] && [ `echo "$cadena1" | cut -d':' -f1` != 2 ] ; then
            directorio="`echo "$cadena1" | cut -d':' -f2`"
            echo $directorio
            tar -rvf "$dirBackup"todo-`date +%F`.tar "$directorio" 2>> $fichErrorLOG
        fi
    done
    echo 'Comprimientdo...'
    gzip --verbose --best "$dirBackup"todo-`date +%F`.tar 2>> $fichErrorLOG
else echo 'El BACKUP ya ha sido realizado.' ; fi
