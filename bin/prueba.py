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


import os
import sys
import datetime
import random

today = datetime.date.today()

print('La fecha actual es : '+str(datetime.datetime.now()))
print('La fecha actual es : '+today.ctime())

w = list()
for i in range(100):
    w.append(random.uniform(0,1))

print(w)
