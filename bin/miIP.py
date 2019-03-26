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

import sys
import socket
import urllib.request

def IP_local():
    respuesta = ""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    respuesta = s.getsockname()[0]
    s.close()
    return respuesta

def IP_externa():
    response = urllib.request.urlopen('http://www.vermiip.es/')
    html = response.read()
    cad1 = str(html)
    cad1 = cad1.split('id="cuerpo"')[1]
    cad1 = cad1.split('h2')[1]
    cad1 = cad1.split(' ')[4].split('<')[0]
    return cad1

if __name__ == '__main__':
    if sys.argv[1] == "-l" or sys.argv[1] == "--local" :
        print(IP_local())
    else:
        print(IP_externa())

    