''' Modules required: wxPython '''

import wx
import wx.grid
import os
import pandas as pd
import numpy as np

EVEN_ROW_COLOUR = '#CCE6FF'
GRID_LINE_COLOUR = '#ccc'
BACKGROUND_COLOUR = '#ccc'

 
class MDIFrame(wx.MDIParentFrame):
    def __init__(self,*args, **kwargs):
        wx.MDIParentFrame.__init__(self, None, -1, "Winnington RFID ", style=wx.DEFAULT_DIALOG_STYLE|wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER)#, size = (600,400))
        self.InitUI()
    # Set Menubar on parent frame
    def InitUI(self):  
        menubar = wx.MenuBar() 
        optionmenu = wx.Menu()
        #tableMenuitem = optionmenu.Append(wx.NewId(),"Table")
        #self.Bind(wx.EVT_MENU, self.Tabler, tableMenuitem)
        encodeMenuitem = optionmenu.Append(wx.NewId(),"Encode")
        self.Bind(wx.EVT_MENU, self.Encoder, encodeMenuitem)
        decodeMenuitem = optionmenu.Append(wx.NewId(),"Decode")
        self.Bind(wx.EVT_MENU, self.Decoder, decodeMenuitem)
        exitMenuitem = optionmenu.Append(wx.NewId(),"Exit")
        menubar.Append(optionmenu,"&Options")
        self.Bind(wx.EVT_MENU, self.OnExit, exitMenuitem)
        self.SetMenuBar(menubar)
       
    def OnExit(self, event):
        self.Close(True)  
		
    def Decoder(self, event): 
        #win = wx.MDIChildFrame(self, -1,  "Decoder Window",size = (1024,600) )
        win = DECODEFrame(self)
        win.Show(True)
        win.SetIcon(wx.Icon(os.getcwd() + "\icons\decode.ico"))
    #def Decoder(self, event): 
    #    win = wx.MDIChildFrame(self, -1, "Decoder Window",size = (800,600) )
    #    win.Show(True)
    #    win.SetIcon(wx.Icon(os.getcwd() + "\icons\decode.ico"))
    def Encoder(self, event): 
        win = wx.MDIChildFrame(self, -1, "Encoder Window",size = (800,600) )
        win.Show(True)
        win.SetIcon(wx.Icon(os.getcwd() + "\icons\encode.ico"))


class DataTable(wx.grid.GridTableBase):

    def __init__(self, data=None):
        wx.grid.GridTableBase.__init__(self)
        self.headerRows = 1
        if data is None:
            data = pd.DataFrame()
        self.data = data

    def GetNumberRows(self):
        return len(self.data)
    
    def GetNumberCols(self):
        return len(self.data.columns) + 1
    
    def GetValue(self, row, col):
        if col == 0:
            return self.data.index[row]
        return self.data.iloc[row, col-1]
    
    def SetValue(self, row, col, value):
        self.data.iloc[row,col -1] = value
    
    def GetColLabelValue(self, col):
        if col == 0:
            if self.data.index.name is None:
                return 'Index'
            else:
                return self.data.index.name
        return str(self.data.columns[col-1])
    
    def GetTypeName(self, row, col):
        return wx.grid.GRID_VALUE_STRING

    def GetAttr(self, row, col, prop):
        attr = wx.grid.GridCellAttr()
        if row % 2 == 1:
            attr.SetBackgroundColour(EVEN_ROW_COLOUR)
        return attr

class DECODEFrame(wx.MDIChildFrame): 
    #def onButton(self, event):
    #    print ("Button pressed.")
    
    def __init__(self,parent):
        wx.MDIChildFrame.__init__(self, parent,pos= ((mw*0.2),0), title= "Decoder Window", size = ((mw*0.79),(mh*0.9)))
        
        panel = wx.Panel(self, wx.ID_ANY)
        #button = wx.Button(panel, wx.ID_ANY, 'Test', (10, 10))
        #button.Bind(wx.EVT_BUTTON, onButton)
        
        df = pd.DataFrame(np.random.random((10,5)))
        table = DataTable(df)

        grid = wx.grid.Grid(self,-1)
        grid.SetTable(table,takeOwnership=True)
        grid.AutoSizeColumns()

        topsizer = wx.BoxSizer(wx.VERTICAL)
        panelsizer = wx.BoxSizer(wx.HORIZONTAL)
        tablesizer = wx.BoxSizer(wx.VERTICAL)
        
        panelsizer.Add(panel,100)
        tablesizer.Add(table,200, wx.EXPAND)
       
        topsizer.Add(panelsizer,100)
        topsizer.Add(tablesizer,200)

        self.panel.SetSizer(topsizer)
        topsizer.Fit(self)

        #sizer = wx.BoxSizer(wx.VERTICAL)
        #sizer.Add(self,"one", 0, wx.EXPAND)
        #sizer.Add(self,"two", 0, wx.EXPAND)
        #sizer.Add(self,"three", 0, wx.EXPAND)
        #sizer.Add(self,"four", 0, wx.EXPAND)
        ##sizer = wx.FlexGridSizer(1,4,0)
        ##sizer.Add(panel,1,wx.EXPAND)
        ##sizer.Add(grid,1,wx.EXPAND)
        ##sizer.Add((-1, -1))
        ##self.SetSizer(sizer)

        self.Bind(wx.EVT_CLOSE, self.quit)
    
    def quit(self,event):
        self.Destroy()
#class DataGrid(gridlib.Grid):
#    def __init__(self, parent, size=wx.Size(1000, 500)):
#        self.parent = parent
#        gridlib.Grid.__init__(self, self.parent, -1)
#        self.SetGridLineColour(GRID_LINE_COLOUR)
#        self.SetRowLabelSize(0)
#        self.SetColLabelSize(30)
#        self.table = DataTable()

app = wx.App()
frame = MDIFrame() 
frame.SetIcon(wx.Icon(os.getcwd() + "\icons\wtonlogo.ico"))
frame.Show()
frame.Maximize(True)
mw, mh = frame.GetSize()

app.MainLoop()