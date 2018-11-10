#!/bin/bash

function instalar_PYTHON() {
	sudo apt install python libapache2-mod-python python-mysqldb -y
	sudo apt install python3 libapache2-mod-python3 python3-mysqldb -y
	sudo apt install python-matplotlib python-numpy -y
}

function instalar_APACHE2_Y_PHP() {
	sudo apt install apache2 libapache2-mod-php php php-mcrypt -y
	sudo service apache2 restart
}

function instalar_POSTGRESQL() {
	sudo apt install postgresql php-pgsql libapache2-mod-auth-pgsql -y
	sudo service apache2 restart
}

function instalar_NETBEANS() {
	sudo apt install openjdk-8-jre openjdk-8-jdk -y
	echo '\n\n'
	echo 'IMPORTANTE!!!! - Guardar netbeans en la carpeta "/opt"'
	~/bin/netbeans-8.1-linux.sh
}

function instalar_JDONWLOADER() {
	~/bin/JD2Setup_x64.sh
}

function instalar_ECLIPSE() {
	sudo add-apt-repository ppa:ubuntu-desktop/ubuntu-make
	sudo apt update
	sudo apt install ubuntu-make
	#umake ide eclipse-jee
	#umake ide idea --eap
	#umake kotlin kotlin-lang
	#umake ide eclipse-jee --remove
}

function instalar_MYSQL() {
	sudo apt install mysql-server libapache2-mod-auth-mysql php-mysql -y
	sudo service mysql restart
}

function instalar_Otros() {
	sudo apt install linux-tools-common
	sudo apt install mame mame-tools -y
	sudo apt install mupen64plus -y
	sudo apt install python-epydoc -y
}

function intalar_COMPARTIDA() {
	dirCompratida="/home/COMPARTIDA"
	if [ -d $dirCompratida ] ; then
		ln -sf $dirCompratida/bin ~/bin
		ln -sf $dirCompratida/DOCUMENTOS ~/Documentos
		ln -sf $dirCompratida/IMAGENES ~/Imágenes
		ln -sf $dirCompratida/MUSICA ~/Música
		ln -sf $dirCompratida/VIDEO ~/Vídeos
	else
		echo 'El directorio "'$dirCompratida'" no existe.'
		#mkdir -p "$dirCompratida"
	fi
}

#instalar_NETBEANS
#instalar_JDONWLOADER
#instalar_ECLIPSE
#instalar_MYSQL
#instalar_Otros
intalar_COMPARTIDA
