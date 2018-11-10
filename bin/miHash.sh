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

if [ $# -lt 2 ] || [ $# -gt 4 ] ; then 
	echo 'Faltan parametros'
	exit 1 
else
	if [ -f "$2" ] ; then
		case "$1" in
			"-enc-sha")
				echo "Codificando..."
				openssl dgst -sha -out "$2".hash "$2" ;;
			"-enc-aes")
				echo "Codificando..."
				openssl enc -aes-128-cbc -in "$2" "$2".enc ;;
			"-dec-aes")
				echo "Descodificando..."
				openssl -d -aes-128-cbc -in "$2" "$2".dec ;;
			"-dec")
				echo "Descodificando..."
				openssl enc -d -in "$2" "$2".dec ;;
			"-enc-pri")
				# Para cifrar con privada
				echo "Codificando..."
				openssl genpkey -algorithmRSA -out "$2".txt ;;
			"-enc-pub")
				# Para cifrar con pública
				echo "Codificando..."
				openssl -pkey -in "$2" -pubout -out "$2".salida ;;
			"-enc-pub2")
				# Para cifrar con pública 2
				echo "Codificando..."
				openssl pkeyutl -pubin -encrypt -in "$2" -out "$2".enc -inkey "$3" ;;
			"-dec-pub2")
				# Para cifrar con pública 2
				echo "Descodificando..."
				openssl pkeyutl -decrypt -in "$2" -mkey "$3" -out "$2".enc ;;
			"-firma")
				# Para hacer una firma
				echo "Frimando..."
				openssl pkeyutl -sign -in "$2" -out "$2".sig -inkey "$3" ;;
			"-verificar")
				# Para hacer una firma
				echo "Verificando..."
				openssl pkeyutl -pubin -verify -sigfile "$4" -in "$2" -inkey "$3" ;;
			*)
				echo 'Parametro erroneo.' ;;
		esac
	else
		echo $2' no es un fichero.'
	fi
fi


