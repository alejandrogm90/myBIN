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
MiDirBin="/home/COMPARTIDA/PROYECTOS/myBIN/bin"

#Muestra versión de linux
lsb_release -a

# POR MI PARTE ....
#if [ -f "$MiDirBin/archey.py" ] ; then $MiDirBin/archey.py ; fi
if [ -f "$MiDirBin/miCPU.sh" ] ; then $MiDirBin/miCPU.sh ; fi
if [ -f "$MiDirBin/modificaciones.sh" ] ; then $MiDirBin/modificaciones.sh ; fi
if [ -f "/home/COMPARTIDA/datos/frases" ] ; then cat /home/COMPARTIDA/datos/frases ; fi

