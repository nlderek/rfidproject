import tkinter as tk
import tkinter.filedialog as filed
import csv
import pandas as pd

class MainApplication(tk.Frame):
    
    def close_program (self): 
        root.destroy()
         
    def start_merge(self):
        var = tk.StringVar() 
        l = tk.Label(self.parent, 
            textvariable=var,
            bg='red', font=('Arial', 12), width=15, height=2)
        l.pack()
        var.set ('Hi!How Are yOU!')
    
    def open_csv(self):
        filename =  filed.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        df = pd.read_csv(open_csv.filename)

        print (self.df)

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
        self.button = tk.Button(self.parent, text="Merge",command=self.start_merge)
        self.button.pack()
        self.button = tk.Button(self.parent, text="Opencsv",command=self.open_csv)
        self.button.pack()
        self.button = tk.Button(self.parent, text="Exit Program",command=self.close_program)
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
    
