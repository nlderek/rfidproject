'''
library required: pandas, pandastable, tkinter, csv, os

'''

import tkinter as tk
import tkinter.filedialog as filed
import pandas as pd
import csv
import os

class MainApplication(tk.Frame):
    
    def f_close_program (self): 
        root.destroy()
         
    def f_start_merge(self):
        var = tk.StringVar() 
        l = tk.Label(self.parent, 
            textvariable=var,
            bg='red', font=('Arial', 12), width=15, height=2)
        l.pack()
        var.set ('Hi!How Are yOU!')
    
    def f_open_csv(self):
        filename =  filed.askopenfile(initialdir = os.getcwd(),title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        opendata = csv.reader(filename)
        opendatalist = []
        scrollbar = tk.Scrollbar(root, orient="vertical")
        lis = tk.Listbox(root, width=150, height=150 , yscrollcommand=scrollbar.set)
        scrollbar.config(command=lis.yview)
        lis.place(x=700,y=50,width=500,height=2000)
        #pack(side="left",fill="both", expand=True)
        lis.insert( tk.END)
        for row in opendata:
            if len (row) !=0:
                opendatalist = opendatalist + [row]
                lis.insert(tk.END,row)
        

        
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.configure_gui()
        self.create_widgets()
 
    def configure_gui(self):
        self.parent.title("Winnington RFID")
        width, height = root.winfo_screenwidth(), root.winfo_screenheight()
        self.parent.geometry('%dx%d+0+0' % (width,height))
        self.parent.resizable(False, False)
        self.parent.viewerPanel = tk.Frame(root,bg="red")
        self.parent.controlerPanel = tk.Frame(root,bg="blue")
        self.parent.controlerPanel.place (x=20,y=30, width=200,height=200)
        self.parent.viewerPanel.place(x=220,y=30, width=200,height=200)
        

    def create_widgets(self):
        self.label = tk.Label(self.parent, text="Welcome to Winnington RFID Decoder", font=("Calbiri", 20))
        self.label.pack()
        self.button = tk.Button(self.parent, text="Merge",command=self.f_start_merge)
        self.button.place(x=50,y=50,width=100,height=50)
        #self.button.pack()
        self.button = tk.Button(self.parent, text="Opencsv",command=self.f_open_csv)
        self.button.place(x=50,y=100,width=100,height=50)
        #self.button.pack()
        self.button = tk.Button(self.parent, text="Exit Program",command=self.f_close_program)
        self.button.place(x=50,y=150,width=100,height=50)
        #self.button.pack()
        
        


    
        #<create the rest of your GUI here>

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=False)
    root.mainloop()
    print ("Hello")
    print ("Hello")
    print ("Hello")
    print ("Hello")


''' Farrell, D 2016 DataExplore: An Application for General Data Analysis in Research and Education. Journal of Open
Research Software, 4: e9, DOI: http://dx.doi.org/10.5334/jors.94 '''


    
