#!/bin/bash

#
#
#       Copyright 2020 Alejandro Gomez
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
fichLista="$HOME/bin/datos/lista-backup.txt"
fichLOG="$HOME/bin/log/BACKUP_log.txt"
fichErrorLOG="$HOME/bin/log/BACKUP_error_log.txt"
dirBackup="$HOME/backups"
nomFichGenerado="$dirBackup"'/copia-'`date +%F`'.tar'

# ANTES DE EMPEZAR
if [ ! -f "$fichLista" ] ; then echo "" >> "$fichLista" ; fi
if [ ! -f "$fichLOG" ] ; then echo "" >> "$fichLOG" ; fi
if [ ! -f "$fichErrorLOG" ] ; then echo "" >> "$fichErrorLOG" ; fi
if [ ! -d "$dirBackup" ] ; then mkdir "$dirBackup" ; fi

# Creo los BackUps
lineasficheroLista=`wc -l "$fichLista" | cut -d' ' -f1`
if [ $lineasficheroLista -gt 0 ] && [ "`awk 'NR=='1 $fichLista`" != '' ] ; then
	echo 'Se ha hecho una copia el "'`date +%F` `date +%T`'".' >> $fichLOG
	echo 'Empaquetando....'"$lineasficheroLista"' elementos'
	for linea in `seq 1 $lineasficheroLista` ; do
	    cadena1="`awk 'NR=='$linea $fichLista`"
	    if [ "$cadena1" != '' ] && [ `echo "$cadena1" | cut -d':' -f1` != 2 ] ; then
            directorio="`echo "$cadena1" | cut -d':' -f2`"
            tar -rvf "$nomFichGenerado" "$directorio" 2>> $fichErrorLOG
	    fi
	done
	echo 'Comprimientdo...'
	gzip -v9 "$nomFichGenerado" 2>> $fichErrorLOG
	echo 'La copia ya ha sido realizada.'
fi

