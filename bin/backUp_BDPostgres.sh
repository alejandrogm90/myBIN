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

# SELECT DISTINCT cod FROM proveedor INNER JOIN pieza ON (proveedor.ciudad=pieza.ciudad) WHERE pieza.cod LIKE '%1';

function copiar() {
	pg_dump --inserts -U postgres /tmp/"$1" > /tmp/"$1.sql"
}

function restaurar() {
	psql -U postgres < /tmp/"$1.sql" > /tmp/"$1.log" 2>&1
}

function error() {
	echo "ERROR: Titenes que ejecutarlo como usuario 'postgres'."
	exit $1
}

if [ $# -eq 2 ] ; then
	if [ `whoami` != 'postgres' ] ; then error -2 ; fi
	case "$1" in
		"-co") copiar $2 ;;
		"-re") restaurar $2 ;;
		*) error -3 ;;
	esac
else
	error -1
fi


