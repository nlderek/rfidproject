'''
library required: pandas, pandastable, tkinter, csv

'''

import tkinter as tk
import tkinter.filedialog as filed
import pandas as pd
import csv

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
        filename =  filed.askopenfile(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        opendata = csv.reader(filename)
        opendatalist = []
        scrollbar = tk.Scrollbar(root, orient="vertical")
        lis = tk.Listbox(root, width=300, height=300 , yscrollcommand=scrollbar.set)
        scrollbar.config(command=lis.yview)
        lis.pack(side="left",fill="both", expand=True)
        lis.insert( tk.END, "ABCDE")
        for row in opendata:
            if len (row) !=0:
                opendatalist = opendatalist + [row]
                lis.insert(tk.END,row)
        
        #for row in df:
        #    lis.insert(df.[column])
        
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

    def create_widgets(self):
        self.label = tk.Label(self.parent, text="Welcome to Winnington RFID Decoder", font=("Calbiri", 20))
        self.label.pack()
        self.button = tk.Button(self.parent, text="Merge",command=self.f_start_merge)
        self.button.pack()
        self.button = tk.Button(self.parent, text="Opencsv",command=self.f_open_csv)
        self.button.pack()
        self.button = tk.Button(self.parent, text="Exit Program",command=self.f_close_program)
        self.button.pack()
        
        


    
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


    
