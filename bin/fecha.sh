#! /bin/bash

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

HOY=$(date +%Y/%m/%d)
AYER=$(date --date "yesterday" +%Y/%m/%d)
MANA=$(date --date "tomorrow" +%Y/%m/%d)
echo 'TODOS los datos por separado: '`date +%Y`'-'`date +%m`'-'`date +%d`' '`date +%T`
echo 'La fecha en segundos desde 1970-01-01 00:00:00 UTC es: '`date +%s`
echo "Ayer fue : $AYER"
echo "Hoy es : $HOY"
echo "Mañana será : $MANA"

