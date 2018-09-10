'''
library required: pandas, pandastable, tkinter, csv, os
additional library : pandastable

cite:
Farrell, D 2016 DataExplore: An Application for General Data Analysis in Research and Education. 
Journal of Open Research Software, 4: e9, DOI: http://dx.doi.org/10.5334/jors.94


'''

import tkinter as tk
import tkinter.filedialog as filed
import tkinter.ttk as ttk
import pandas as pd
import pandastable as pt
import csv
import os

currentpath = os.getcwd()

#frame_Top
class frame_top(tk.Frame):
    def __init__(self,parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.top_widget()

    def top_widget(self):
        #self.grid(sticky = tk.N + tk.S + tk.E + tk.W) 
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=10)
        #self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        #self.top_version_label = tk.Label(self, text="Version: 0.1", font=("Calbiri", 8))
        #self.top_version_label.grid(row=0, column=0, padx=1, pady=1, sticky = tk.E)
        self.top_label = tk.Label(self, text="Welcome to Winnington RFID Decoder", font=("Raleway", 24))
        self.top_label.grid(row=0, column=1, padx=100, pady=5,sticky = tk.S + tk.N + tk.E + tk.W)
        self.top_version_label = tk.Label(self, text="Version: 0.1", font=("Calbiri", 8))
        self.top_version_label.grid(row=0, column=1, padx=1, pady=1,sticky = tk.S + tk.E)
        #self.versiontext = tk.Text(self)
        #self.versiontext.insert(tk.INSERT, "version:0.1")
        #self.versiontext.grid(row=0, column=1)
        #self.text.insert(tk.END, "This is the first frame")
        
#frame_right 
class frame_right(tk.Frame):
    def f_open_csv(self):
        filename = filed.askopenfile(initialdir = os.getcwd(),title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        readcsv = pd.read_csv(filename)
        df = pd.DataFrame(readcsv)
        t = pt.Table(self,rows=100,columns=30)
        t.grid(row=1, column=0, sticky=tk.W + tk.N + tk.E + tk.S)
        ptable = pt.Table(t,dataframe=df,showtoolbar=False, showstatusbar=True)
        #df = pt.importCSV()
        #pt.data.TableModel(dataframe= df,rows=20,columns=9)
        #ptable = pt.Table(t,dataframe=df,showtoolbar=False, showstatusbar=True)
        ptable.show()
        return
        #ddf = df.values.tolist()
        #csv_df = df(columns=['EPC','RSSI','Count','Date','Time','Serial','Location','Product code','Qty'])
        #data_csv = df[:]
        #for row in ddf:

        #print (ddf)
        #print (len(df.columns))
        #print(df.columns[0])
        #print (len(df.index))
        #for i in range(len(df.index)):
        ##    for j in range(len(df.columns)):
        ##       data_csv = (df.iloc[i,j])
        ##        self.table_right.insert('',tk.END,values = data_csv)   
                   
        #opendatalist = []
        #for row in opendata:
        #    if len (row) !=0: 
        #    self.opendatalist = self.opendatalist + [row]
        #    self.opendatalist.insert(tk.END,row) 
            #c = self.f_open_csv[i]
            #self.table_right.heading(c,title(), command=lambda c=c: self._column_sort(c, RaumfeldDesktop.SortDir))
            #self.table_right.column(c, width=self.f_open_csv[i])
            #self._load_browse_data()
        #df = pd.read_csv(filename)
    
    def right_widget(self): 
        self.csv_open_button = tk.Button(self, text="Opencsv",command=self.f_open_csv)
        self.csv_open_button.config(height = 1, width = 10)
        self.csv_open_button.grid(row=0, column=0,padx=10, pady=10, sticky= tk.W)
        self.t = pt.Table(self, rows=30,columns=30)
        self.t.grid(row=1, column=0, sticky=tk.W + tk.N + tk.E + tk.S)
        self.ptable = pt.Table(self.t,dataframe=None,showtoolbar=False, showstatusbar=True)
        self.ptable.show()
        #self.table_right = ttk.Treeview(self,height=10, columns=('EPC','RSSI','Count','Date','Time','Serial','Location','Product code','Qty'), selectmode="extended")
        #self.scrollbar_horizontal = ttk.Scrollbar(self, orient="horizontal",command=self.table_right.xview)
        #self.scrollbar_horizontal.grid(row=2, column=0, sticky="we")
        #self.scrollbar_vertical = ttk.Scrollbar(self, orient="vertical", command=self.table_right.yview)
        #self.scrollbar_vertical.grid(row=1, column=1, sticky="ns")
        #self.table_right.heading('#0', text ='Index', anchor=tk.CENTER)
        #self.table_right.heading('#1', text ='EPC', anchor=tk.CENTER)
        #self.table_right.heading('#2', text ='RSSI', anchor=tk.CENTER)
        #self.table_right.heading('#3', text ='Count', anchor=tk.CENTER)
        #self.table_right.heading('#4', text ='Date', anchor=tk.CENTER)
        #self.table_right.heading('#5', text ='Time', anchor=tk.CENTER)
        #self.table_right.heading('#6', text ='Serial', anchor=tk.CENTER)
        #self.table_right.heading('#7', text ='Location', anchor=tk.CENTER)
        #self.table_right.heading('#8', text ='Product code', anchor=tk.CENTER)
        #self.table_right.heading('#9', text ='Qty', anchor=tk.CENTER)
        #self.table_right.column('#0',stretch=tk.YES, minwidth=10, width=60)
        #self.table_right.column('#1',stretch=tk.YES, minwidth=10, width=60)
        #self.table_right.column('#2',stretch=tk.YES, minwidth=10, width=60)
        #self.table_right.column('#3',stretch=tk.YES, minwidth=10, width=60)
        #self.table_right.column('#4',stretch=tk.YES, minwidth=10, width=60)
        #self.table_right.column('#5',stretch=tk.YES, minwidth=10, width=60)
        #self.table_right.column('#6',stretch=tk.YES, minwidth=10, width=100)
        #self.table_right.column('#7',stretch=tk.YES, minwidth=10, width=60)
        #self.table_right.column('#8',stretch=tk.YES, minwidth=10, width=100)
        #self.table_right.column('#9',stretch=tk.YES, minwidth=10, width=60)
        #self.table_right.grid(row=1, column=0, sticky="nswe")
        #self.table_right.configure(xscrollcommand=self.scrollbar_horizontal.set,yscrollcommand=self.scrollbar_vertical.set)
        
        
        #filename = filed.askopenfile(initialdir = os.getcwd(),title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        #df = pd.read_csv(filename)
        # only the column containing the text is resized when the window size changes:
        
        #self.columnconfigure(0, weight=1) 
        # resize row 0 height when the window is resized
        #self.rowconfigure(0, weight=1)
        
        #self.txt = tk.Text()
        #self.txt.grid()
        #self.scroll_y =     tk.Scrollbar(self, orient="vertical", command=self.txt.yview)
        #self.scroll_y.grid()
        # bind txt to scrollbar
        #self.txt.configure(yscrollcommand=self.scroll_y.set)
        #self.very_long_list = "\n".join([str(i) for i in range(100)])
        #self.txt.insert("1.0", self.very_long_list)
        # make the text look like a label
        #self.txt.configure(state="disabled", relief="flat", bg=self.cget("bg"))
    
    
    
    def __init__(self,parent):
        tk.Frame.__init__(self, parent, bg="red")
        self.parent = parent
        self.right_widget()
#frame_left
class frame_left(tk.Frame):
    def left_widget(self):
        #self.columnconfigure(0, weight=1)
        #self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.csv_open_button = tk.Button(self, text="Opencsv",command=self.f_open_csv)
        self.csv_open_button.config(height = 5, width = 10)
        self.csv_open_button.grid(row=0, column=0, padx=10, pady=10)
        self.close_button = tk.Button(self, text="Exit Program",command=self.f_close_program)
        self.close_button.config(height = 5, width = 10)
        self.close_button.grid(row=1, column=0, padx=10, pady=10)    

    def __init__ (self,parent):
        tk.Frame.__init__(self, parent, bg="green")
        self.parent = parent
        self.left_widget()    
        
    def f_open_csv(self):
        filename = filed.askopenfile(initialdir = os.getcwd(),title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
        #opendata = csv.reader(filename)
        df = pd.read_csv(filename)
        #tkk.tree.insert(df, 'end','widgets', text = 'Widget tour')
        
        #opendatalist = []
        #self.scrollbar = tk.Scrollbar(self, orient="vertical")
        #passrightlis = frame_right.right_widget(self,rightlis)
        #self.lis = passrightlis() #, yscrollcommand=scrollbar.set()
        #scrollbar.config(command=lis.yview)
        #self.lis.grid()
        #lis.place(x=700,y=50,width=500,height=1000)
        #pack(side="left",fill="both", expand=True)
        #self.lis.insert(tk.END)
        #for row in opendata:
        #    if len (row) !=0:
        #        opendatalist = opendatalist + [row]
        #        self.passrightlis.insert(tk.END,row)

    def f_close_program (self): 
        print("Bye Bye")
        destroy = app.destroy()
        #Ctr_right
        #self.label = tk.Label(self.parent, text="Welcome to Winnington RFID Decoder", font=("Calbiri", 10))
        #self.label.grid(row = 0,columnspan = 1, sticky = tk.N +tk.E)
        #self.button = tk.Button(self.parent, text="Merge",command=self.f_start_merge)
        #self.button(x=50,y=50,width=100,height=50)
        #self.button.grid(row =1, column = 1)
        #self.button.pack()
        #self.button.grid_columnconfigure(1, weight =100)
        #self.button.pack()
         #self.button.grid_columnconfigure(1, weight =100)
        #<create the rest of your GUI here>


class MainApplication(tk.Tk):
    def mainWidgets(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=25)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=25)
        self.topframe = frame_top(self)
        self.topframe.grid(row = 0, column = 0,columnspan = 2, sticky= tk.N + tk.S + tk.E + tk.W)
        self.leftframe = frame_left(self)
        self.leftframe.grid(row = 1 , column= 0, sticky=tk.W + tk.N,padx = 5)
        self.rightframe = frame_right(self)
        self.rightframe.grid(row = 1 , column= 1, sticky =tk.N + tk.W + tk.S + tk.E, padx=5, pady=5)
    #tk.N + tk.S + tk.E + tk.W
    def configure_gui(self):
        self.title("Winnington RFID Panel")
        self.iconbitmap(currentpath + r'\wtonlogo.ico')
        self.width, self.height = 960,680
        #self.width, self.height = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry('%dx%d+0+0' % (self.width, self.height))
        self.resizable(False, False)

    def __init__(self, parent, *args, **kwargs):
        tk.Tk.__init__(self, parent, *args, **kwargs)
        #self.grid(sticky = tk.N + tk.S + tk.E + tk.W)
        self.parent = parent
        self.configure_gui()
        self.mainWidgets()
    

        #width, height = root.winfo_screenwidth(), root.winfo_screenheight()
        #top_frame = tk.Frame(self, bg='cyan', width = width, height=100, padx=3, pady=3)
        #center = tk.Frame(self, bg='gray')#, width=width, height=100, padx=3, pady=3)
        #ctr_left = tk.Frame(center, bg='blue')#, width=100, height=100, pady=3)
        #ctr_right = tk.Frame(center, bg='green')#, width=700, height=100, pady=3)
         #layout all containers
        #self.grid_rowconfigure(0, weight=1)
        #self.grid_rowconfigure(1, weight=1)
        #self.grid_columnconfigure(0, weight = 1)
        #self.grid_columnconfigure(1, weight = 1)
        #top_frame.grid(row=0, column= 0,columnspan = 1, sticky= tk.E + tk.W)
        #center.grid(row=1, column = 0, sticky= tk.N + tk.S + tk.E + tk.W)
        #ctr_left.grid(row=1, column = 0, sticky= tk.E + tk.W)
        #ctr_right.grid(row=1,column = 1, sticky=tk.E + tk.W)
        #Containers
        #self.frame_top()
        #self.configure_gui()
        #self.create_widgets()
        
        #Top_frame
         
        #self.parent.viewerPanel = tk.Frame(root,bg="red").grid(row = 0, column = 1)
        #self.parent.controlerPanel = tk.Frame(root,bg="blue").grid(row = 0,column =0)
        #self.parent.controlerPanel.grid(row = 0,column =0)
        #self.parent.viewerPanel.grid(row = 0, column = 1)
        #self.parent.controlerPanel.place (x=10,y=30, width=100,height=100)
        #self.parent.viewerPanel.place(x=10,y=30, width=100,height=100)
if __name__ == "__main__":
    #root = tk.Tk()
    app = MainApplication(None) 
    #.grid (side="top", fill="both", expand=False)
    app.mainloop()



''' Farrell, D 1016 DataExplore: An Application for General Data Analysis in Research and Education. Journal of Open
Research Software, 4: e9, DOI: http://dx.doi.org/10.5334/jors.94 '''


    
