''' Modules required: wxPython ,pandas, numpy '''

import wx
import wx.grid
import os
import pandas as pd
import numpy as np

EVEN_ROW_COLOUR = '#CCE6FF'
GRID_LINE_COLOUR = '#ccc'
BACKGROUND_COLOUR = '#deedee'

#Frame: MainFrame --Start-- 
class MDIFrame(wx.MDIParentFrame):
    def __init__(self,*args, **kwargs):
        wx.MDIParentFrame.__init__(self, None, -1, "Winnington RFID ", style= wx.DEFAULT_DIALOG_STYLE|wx.MAXIMIZE_BOX ^ wx.RESIZE_BORDER)#, size = (600,400))
        self.InitUI()
    # Set Menubar on parent frame
    def InitUI(self):  
        menubar = wx.MenuBar() 
        optionmenu = wx.Menu()
        '''
        tableMenuitem = optionmenu.Append(wx.NewId(),"Table")
        #self.Bind(wx.EVT_MENU, self.Tabler, tableMenuitem)
        '''
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
        '''
        win = wx.MDIChildFrame(self, -1,  "Decoder Window",size = (1024,600) )
        '''
        win = DECODEFrame(self)
        win.Show(True)
        win.SetIcon(wx.Icon(os.getcwd() + "\icons\decode.ico"))

    def Encoder(self, event): 
        win = wx.MDIChildFrame(self, -1, "Encoder Window",size = (800,600) )
        win.Show(True)
        win.SetIcon(wx.Icon(os.getcwd() + "\icons\encode.ico"))
#Frame: MainFrame --Finish-- 


'''
#Object: Another way to make table (not use)  --Start--
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
#Object: Another way to make table (not use)  --Finish--
'''

#Object: Button inside Decode Frame

#Object: Table in Decode Frame --Start-- 
class MyGrid(wx.grid.Grid):
    
    def __init__(self,parent):
        wx.grid.Grid.__init__(self, parent)
        self.CreateGrid(12,8)
                        
        self.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.OnCellLeftClick)
        self.Bind(wx.grid.EVT_GRID_CELL_RIGHT_CLICK, self.OnCellRightClick)
        self.Bind(wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.OnCellLeftDClick)
        self.Bind(wx.grid.EVT_GRID_CELL_RIGHT_DCLICK, self.OnCellRightDClick)
        
        self.Bind(wx.grid.EVT_GRID_LABEL_LEFT_CLICK, self.OnLabelLeftClick)
        self.Bind(wx.grid.EVT_GRID_LABEL_RIGHT_CLICK, self.OnLabelRightClick)
        self.Bind(wx.grid.EVT_GRID_LABEL_LEFT_DCLICK, self.OnLabelLeftDClick)
        self.Bind(wx.grid.EVT_GRID_LABEL_RIGHT_DCLICK, self.OnLabelRightDClick)
        
        self.Bind(wx.grid.EVT_GRID_ROW_SIZE, self.OnRowSize)
        self.Bind(wx.grid.EVT_GRID_COL_SIZE, self.OnColSize)
 
        self.Bind(wx.grid.EVT_GRID_RANGE_SELECT, self.OnRangeSelect)
        self.Bind(wx.grid.EVT_GRID_CELL_CHANGED, self.OnCellChange)
        self.Bind(wx.grid.EVT_GRID_SELECT_CELL, self.OnSelectCell)
 
        '''
        self.Bind(wx.grid.EVT_GRID_EDITOR_SHOWN, self.OnEditorShown)
        self.Bind(wx.grid.EVT_GRID_EDITOR_HIDDEN, self.OnEditorHidden)
        '''
        self.Bind(wx.grid.EVT_GRID_EDITOR_CREATED, self.OnEditorCreated)
        self.Bind(wx.grid.EVT_GRID_EDITOR_CREATED, self.onCellEdit)
    
    def OnCellLeftClick(self,evt):
        print ('OnCellLeftClick: (%d,%d) %s\n' %(evt.GetRow(),evt.GetCol(),evt.GetPosition()))
        evt.Skip()
    
    def OnCellRightClick(self, evt):
        print ('OnCellRightClick: (%d,%d) %s\n' % (evt.GetRow(),evt.GetCol(),evt.GetPosition()))
        evt.Skip()

    def OnCellLeftDClick(self, evt):
        print ("OnCellLeftDClick: (%d,%d) %s\n" % (evt.GetRow(),
                                                  evt.GetCol(),
                                                  evt.GetPosition()))
        evt.Skip()
 
    def OnCellRightDClick(self, evt):
        print ("OnCellRightDClick: (%d,%d) %s\n" % (evt.GetRow(),
                                                   evt.GetCol(),
                                                   evt.GetPosition()))
        evt.Skip()
 
    def OnLabelLeftClick(self, evt):
        print ("OnLabelLeftClick: (%d,%d) %s\n" % (evt.GetRow(),
                                                  evt.GetCol(),
                                                  evt.GetPosition()))
        evt.Skip()
 
    def OnLabelRightClick(self, evt):
        print ("OnLabelRightClick: (%d,%d) %s\n" % (evt.GetRow(),
                                                   evt.GetCol(),
                                                   evt.GetPosition()))
        evt.Skip()
 
    def OnLabelLeftDClick(self, evt):
        print ("OnLabelLeftDClick: (%d,%d) %s\n" % (evt.GetRow(),
                                                   evt.GetCol(),
                                                   evt.GetPosition()))
        evt.Skip()
 
    def OnLabelRightDClick(self, evt):
        print ("OnLabelRightDClick: (%d,%d) %s\n" % (evt.GetRow(),
                                                    evt.GetCol(),
                                                    evt.GetPosition()))
        evt.Skip()
 
    def OnRowSize(self, evt):
        print ("OnRowSize: row %d, %s\n" % (evt.GetRowOrCol(),
                                           evt.GetPosition()))
        evt.Skip()
 
    def OnColSize(self, evt):
        print ("OnColSize: col %d, %s\n" % (evt.GetRowOrCol(),
                                           evt.GetPosition()))
        evt.Skip()
 
    def OnRangeSelect(self, evt):
        if evt.Selecting():
            msg = 'Selected'
        else:
            msg = 'Deselected'
        print ("OnRangeSelect: %s  top-left %s, bottom-right %s\n" % (msg, evt.GetTopLeftCoords(),
                                                                     evt.GetBottomRightCoords()))
        evt.Skip()
 
 
    def OnCellChange(self, evt):
        print ("OnCellChange: (%d,%d) %s\n" % (evt.GetRow(), evt.GetCol(), evt.GetPosition()))
 
        # Show how to stay in a cell that has bad data.  We can't just
        # call SetGridCursor here since we are nested inside one so it
        # won't have any effect.  Instead, set coordinates to move to in
        # idle time.
        value = self.GetCellValue(evt.GetRow(), evt.GetCol())
 
        if value == 'no good':
            self.moveTo = evt.GetRow(), evt.GetCol()
 
    def OnSelectCell(self, evt):
        if evt.Selecting():
            msg = 'Selected'
        else:
            msg = 'Deselected'
        print ("OnSelectCell: %s (%d,%d) %s\n" % (msg, evt.GetRow(),
                                                 evt.GetCol(), evt.GetPosition()))
 
        # Another way to stay in a cell that has a bad value...
        row = self.GetGridCursorRow()
        col = self.GetGridCursorCol()
 
        if self.IsCellEditControlEnabled():
            self.HideCellEditControl()
            self.DisableCellEditControl()
 
        value = self.GetCellValue(row, col)
 
        if value == 'no good 2':
            return  # cancels the cell selection
 
        evt.Skip()
 
    #Function to ask yes/no for cell edit
    '''
    def OnEditorShown(self, evt):
        if evt.GetRow() == evt.GetRow() and evt.GetCol() == evt.GetRow() and \
           wx.MessageBox("Are you sure you wish to edit this cell?",
                        "Checking", wx.YES_NO) == wx.NO:
            evt.Veto()
            return
 
        print ("OnEditorShown: (%d,%d) %s\n" % (evt.GetRow(), evt.GetCol(),
                                               evt.GetPosition()))
        evt.Skip()
 
 
    def OnEditorHidden(self, evt):
        if evt.GetRow() == 6 and evt.GetCol() == 3 and \
           wx.MessageBox("Are you sure you wish to  finish editing this cell?",
                        "Checking", wx.YES_NO) == wx.NO:
            evt.Veto()
            return
 
        print ("OnEditorHidden: (%d,%d) %s\n" % (evt.GetRow(),
                                                evt.GetCol(),
                                                evt.GetPosition()))
        evt.Skip()
    '''
 
    def OnEditorCreated(self, evt):
        print ("OnEditorCreated: (%d, %d) %s\n" % (evt.GetRow(),
                                                  evt.GetCol(),
                                                  evt.GetControl()))

    def onCellEdit(self, event):
        '''
        When cell is edited, get a handle on the editor widget
        and bind it to EVT_KEY_DOWN
        '''        
        editor = event.GetControl()        
        editor.Bind(wx.EVT_KEY_DOWN, self.onEditorKey)
        event.Skip()
    
    def onEditorKey(self, event):
        '''
        Handler for the wx.grid's cell editor widget's keystrokes. Checks for specific
        keystrokes, such as arrow up or arrow down, and responds accordingly. Allows
        all other key strokes to pass through the handler.
        '''
        keycode = event.GetKeyCode() 
        if keycode == wx.WXK_UP:
            print ('you pressed the UP key!')
            self.grid.MoveCursorUp(False)
        elif keycode == wx.WXK_DOWN:
            print ('you pressed the down key!')
            self.grid.MoveCursorDown(False)
        elif keycode == wx.WXK_LEFT:
            print ('you pressed the left key!')
            self.grid.MoveCursorLeft(False)
        elif keycode == wx.WXK_RIGHT:
            print ('you pressed the right key')
            self.grid.MoveCursorRight(False)
        else:
            pass
        event.Skip()        

#Object: Table in Decode Frame --Finish-- 

'''#Object: Button in Decode Frame --Start--
class buildButtons(wx.grid.Grid):
    def __init__(self,parent):
        wx.grid.Grid.__init__(self, parent)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        buttonOne = wx.Button(panel, id=wx.ID_ANY, label="One", name="one")
        buttonTwo = wx.Button(panel, id=wx.ID_ANY, label="Two", name="two")
        buttonThree = wx.Button(panel, id=wx.ID_ANY, label="Three", name="three")
        buttons = [buttonOne, buttonTwo, buttonThree]
 
        for button in buttons:
            self.buildButtons(button, sizer)
 
        panel.SetSizer(sizer)

    def buildButtons(self, btn, sizer):
        """"""
        btn.Bind(wx.EVT_BUTTON, self.onButton)
        sizer.Add(btn, 0, wx.ALL, 5)
    
    def onButton(self, event):
        """
        This method is fired when its corresponding button is pressed
        """
        button = event.GetEventObject()
        print ("The button you pressed was labeled: " + button.GetLabel())
        print ("The button's name is " + button.GetName())
 
        button_id = event.GetId()
        button_by_id = self.FindWindowById(button_id)
        print ("The button you pressed was labeled: " + button_by_id.GetLabel())
        print ("The button's name is " + button_by_id.GetName())

#Object: Button in Decode Frame --Finish-- '''

#Frame: Decoder Frame --Start--         
class DECODEFrame(wx.MDIChildFrame):
    def __init__(self,parent):
        wx.MDIChildFrame.__init__(self, parent, wx.ID_ANY, pos= ((mw*0.2),0), title= "Decoder Window", size = ((mw*0.79),(mh*0.9)))
        panel = wx.Panel(self, wx.ID_ANY)
        myGrid = MyGrid(panel)
        csvButton = wx.Button(panel,-1,'Choose data file to decode')
        csvButton.Bind(wx.EVT_BUTTON, self.opencsvButton)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(csvButton,0,wx.LEFT| wx.ALL,5)
        sizer.Add(myGrid, 10, wx.EXPAND)
        sizer.SetSizeHints(panel)
        panel.SetSizer(sizer)

    def opencsvButton(self,event):
        # Create and show the Open FileDialog
        wildcard = "CSV Source (*.csv)|*.csv"
        dlg = wx.FileDialog(self,message='Choose a csv file', defaultFile="",wildcard= wildcard, style= wx.FD_OPEN |wx.FD_MULTIPLE |wx.FD_CHANGE_DIR )
        
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            print(" You chose the following files: ")
            for path in paths:
                print (path)
        dlg.Destroy()
    
    
    '''
    #def onButton(self, event):
    #    print ("Button pressed.")
    
    def __init__(self,parent):
        wx.MDIChildFrame.__init__(self, parent,pos= ((mw*0.2),0), title= "Decoder Window", size = ((mw*0.79),(mh*0.9)))
        #panel = wx.Panel(self, wx.ID_ANY)
        #button = wx.Button(panel, wx.ID_ANY, 'Test', (10, 10))
        #button.Bind(wx.EVT_BUTTON, onButton)
        
        df = pd.DataFrame(np.random.random((10,5)))
        table = DataTable(df)

        grid = wx.grid.Grid(self,-1)
        grid.SetTable(table,takeOwnership=True)
        grid.AutoSizeColumns()

        ##topsizer = wx.BoxSizer(wx.VERTICAL)
        ##panelsizer = wx.BoxSizer(wx.HORIZONTAL)
        ##tablesizer = wx.BoxSizer(wx.VERTICAL)
        
        ##panelsizer.Add(panel,100)
        ##tablesizer.Add(table,200, wx.EXPAND)
       
        ##topsizer.Add(panelsizer,100)
        ##topsizer.Add(tablesizer,200)

        ##self.panel.SetSizer(topsizer)
        ##topsizer.Fit(self)

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

    ''' 
''' 
#Old set table method (not use)  
class DataGrid(gridlib.Grid):
    def __init__(self, parent, size=wx.Size(1000, 500)):
        self.parent = parent
        gridlib.Grid.__init__(self, self.parent, -1)
        self.SetGridLineColour(GRID_LINE_COLOUR)
        self.SetRowLabelSize(0)
        self.SetColLabelSize(30)
        self.table = DataTable()
'''
#Frame:Decoder Frame --Finish--

app = wx.App()
frame = MDIFrame() 
frame.SetIcon(wx.Icon(os.getcwd() + "\icons\wtonlogo.ico"))
frame.Show()
frame.Maximize(True)
mw, mh = frame.GetSize()

app.MainLoop()