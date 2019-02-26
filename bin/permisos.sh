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

#===========================
#VARIABLES
#===========================
compartida='/home/COMPARTIDA'

#===========================
#CODIGO
#===========================

echo 'Modificando... '"$compartida/${directorios[$lin1]}"
#sudo chown -R `whoami`:grupo1 "$compartida/${directorios[$lin1]}" 
sudo chmod -R 777 "$compartida/${directorios[$lin1]}"
echo 'Finalizado... '

# Para Django
if [ -d "$compartida/PROYECTOS/Django-project" ] ; then
	echo 'Modificando... Django'
	sudo chmod -R 775 $compartida/PROYECTOS/Django-project
	sudo chmod 755 $compartida/PROYECTOS/Django-project/*/manage.py
	proyectos=`ls $compartida/PROYECTOS/Django-project`
	#for lin1 in $proyectos ; do
	#	sudo chmod -R 644 "$compartida/PROYECTOS/Django-project/"$lin1'/'$lin1/*
	#done
	sudo chmod -R 644 "$compartida/PROYECTOS/Django-project/*/*/*
	echo 'Finalizado... '
fi

# Para WEB
if [ -f "/var/www/html" ] && [ -f "/var/www/html/permisos.sh" ] ; then
	echo 'Modificando... WEB'
	cd /var/www/html
	./permisos.sh
	echo 'Finalizado... '
else
	echo "El directorio: \"/var/www/html\" no existe."
fi
