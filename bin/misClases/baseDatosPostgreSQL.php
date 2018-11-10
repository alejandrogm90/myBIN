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

    # constructor asi no es necesario llamar al metodo setConection para establecer la conexion
    function __construct ($servidor="", $dataBase="", $usuario="", $pass=""){
        if ($servidor != "" && $dataBase != "" && $usuario != "" && $pass != "") { $this->setConexion($servidor, $dataBase, $usuario, $pass); }
    }

    # Conector de la BD al cual se le pasa el server, la BD, el user y el password
    function setConexion ($servidor, $dataBase, $usuario, $pass) {
        $this->conexion = pg_connect("host=".$servidor." dbname=".$dataBase." user=".$usuario." password=".$pass);
        //$this->conexion = pg_connect("host=".$servidor." dbname=".$dataBase." user=".$usuario." password=".$pass) or trigger_error('No puedo conectar a la BD "'.$dataBase.'": '.pg_last_error(), E_USER_ERROR);
        if ($this->conexion) { return true; } else { return false; }
    }

    # para cerrar la conexion
    function closeConexion () { pg_close($this->conexion); }

    # para  ejecutar una consulta
    function setConsulta ($sql) { if($this->resultado = pg_query($sql)) { return true; } else { return false; } }

    # para obtener una fila
    function getFila () { return pg_fetch_array($this->resultado); }

    # para obtener el numero de fila de una consulta
    function getNumFilas () { return pg_num_rows($this->resultado); }

    function sinEspacios ($cadena) {
        $salida = "";
        //$division = split(" ",$cadena);
        //$numCadena = count($division);
        $numVacios = 0;
        $posActual = 0;
        /*
        //while ($posActual < $numCadena or $numVacios > 1 ) {
        //	if ($cadena[$posActual] != " ") { $salida += $cadena[$posActual]; }
        //	else { $numVacios++; }
        //	$posActual++;
        //}

        for $d1 as $division {
                if ($d1 != " ") { $salida += $d1; }
                else { $numVacios++; }
                $posActual++;
        }
        //$salida = count(split(" ",$cadena));
        */
        $salida = $cadena;
        return $salida;
    }

}


?>
