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

#import sqlite3
#from tkinter import *
#from tkinter import ttk
import tkinter

def calculate(*args):
	try:
		value = float(feet.get())
		meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
	except ValueError:
		pass

if __name__ == '__main__' :
	# Empieza el main	
    
	root = Tk()
	root.title("Pies a Metros")

	mainframe = ttk.Frame(root, padding="3 3 12 12")
	mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
	mainframe.columnconfigure(0, weight=1)
	mainframe.rowconfigure(0, weight=1)

	feet = StringVar()
	meters = StringVar()

	feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
	feet_entry.grid(column=2, row=1, sticky=(W, E))

	ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
	ttk.Button(mainframe, text="Calcular", command=calculate).grid(column=3, row=3, sticky=W)

	ttk.Label(mainframe, text="Pies").grid(column=3, row=1, sticky=W)
	ttk.Label(mainframe, text=" es igual a ").grid(column=1, row=2, sticky=E)
	ttk.Label(mainframe, text="Metros").grid(column=3, row=2, sticky=W)

	for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

	feet_entry.focus()
	root.bind('<Return>', calculate)

	root.mainloop()
	
	
	print('fin')
	
	
	
	

