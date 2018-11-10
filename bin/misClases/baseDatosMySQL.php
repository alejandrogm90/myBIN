<?php

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

class BaseDatos {
    private $conexion;
    private $resultado;

    // constructor asi no es necesario llamar al metodo setConection para establecer la conexion
    function __construct ($servidor=null, $usuario=null, $pass=null){
        if ($servidor != null && $usuario != null && $pass !=null)
            $this->setConexion($servidor, $usuario, $pass);
    }
    
    //metodos: para conectar se le pasa el server, el user, el password
    function setConexion($servidor, $usuario, $pass) {
        //para acceder a la variable con $this
        $this->conexion = mysql_connect($servidor, $usuario, $pass);

        if ($this->conexion)
            return true;
        else
            return false;
    }

    //para cerrar la conexion
    function closeConexion() {
        mysql_close($this->conexion);
    }

    //para seleccionar la base de datos, le pasa el nombre de la base de dato
    function setBaseDatos($bd) {
        if (mysql_select_db($bd, $this->conexion))
            return true;
        else
            return false;
    }

    // para  ejecutar una consulta 
    function setConsulta ($sql){
        // se asigna dentro el if el valor de $resultado
        if($this->resultado = mysql_query($sql, $this->conexion)){
            echo mysql_error();
            return true;
        }
        else{
            echo mysql_error();
            return false;
        }
    }
    
    //para obtener una fila
    function getFila (){
        //devuelve un array la siguiente fila de la consulta que se lanzo 
        return mysql_fetch_array($this->resultado);
    }
    
    //para obtener el numero de fila de una consulta
    function getNumFilas(){
        echo mysql_error();
        return mysql_num_rows($this->resultado);
    }
    
    
    
}


?>
