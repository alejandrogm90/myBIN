#!/usr/bin/env python3

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

import pymongo
import sys

class Jugador:
    def __init__(self, nombre1="", id1="", votos1=""):
        self.nombre = nombre1
        self.id = id1
        self.votos = votos1

    def setJugador(self, vector1):
        self.nombre = vector1[0]
        self.id = vector1[2]
        self.votos = vector1[1]

    def setJugador2(self, vector1):
        self.nombre = vector1['nombre']
        self.id = vector1['id']
        self.votos = vector1['votos']

    def getJSON(self):
        return { "nombre":self.nombre, "id":self.id, "votos":self.votos }

    def toString(self):
        return 'nombre: '+self.nombre+' | id: '+self.id+' | votos: '+str(self.votos)

if __name__ == '__main__' :
	# Empieza el main

    con = pymongo.MongoClient("localhost", 27017)
    #print(con.database_names())

    db = con.arkuna
    coleccion = db.arkuna

    cursor = coleccion.find()
    #cursor = collection.find({'nombre':'Falcon90'})
    for lin in coleccion.find():
        jug1 = Jugador()
        jug1.setJugador2(lin)
        print(jug1.toString())

    if (sys.argv[1] == '-c' and len(sys.argv) == 3):
        jug1 = Jugador()
        jug1.setJugador(sys.argv[2].split('|'))
        print(jug1.toString())
        coleccion.insert(jug1.getJSON())
