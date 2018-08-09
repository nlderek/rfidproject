import csv
import tkinter as tk
import tkinter.filedialog as filed

filename =  filed.askopenfile(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
opendata = csv.reader(filename)
opendatalist = []
for row in opendata:
            if len (row) !=0:
                opendatalist = opendatalist + [row]
print (opendatalist)