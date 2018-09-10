''' Modules required: wxPython '''

import wx
import os

 
class MDIFrame(wx.MDIParentFrame): 
    def __init__(self,*args, **kwargs):
        wx.MDIParentFrame.__init__(self, None, -1, "Winnington RFID ")#, size = (600,400))
        self.InitUI()
    # Set Menubar on parent frame
        
    def InitUI(self):
        
        menubar = wx.MenuBar() 
        menu = wx.Menu()
        qmi = wx.MenuItem(menu, ID_DECODE, '&Decoder')
        qmi.SetBitmap(wx.Bitmap(os.getcwd() + "\icons\decode.ico")) 
        qmi = wx.MenuItem(menu, ID_ENCODE, '&Decoder')
        qmi.SetBitmap(wx.Bitmap(os.getcwd() + "\icons\encode.ico"))
        qmi = wx.MenuItem(menu, ID_EXIT, '&Decoder')
        qmi.SetBitmap(wx.Bitmap(os.getcwd() + "\icons\wtonlogo.ico"))        
        #menu.Append(5000, "&Decoder") 
        #menu.Append(5001, "&Encoder")
        #menu.Append(5002, "&Exit")

        self.Bind(wx.EVT_MENU, self.Decoder, id = ID_DECODE) 
        self.Bind(wx.EVT_MENU, self.Encoder, id = ID_ENCODE)
        self.Bind(wx.EVT_MENU, self.OnExit, id = ID_EXIT)
        
        menubar.Append(qmi, "&Options") 
		self.SetMenuBar(menubar)

    # Set icon Menubar
        
    def OnExit(self, evt): 
        self.Close(True)  
		
    def Decoder(self, evt): 
        win = wx.MDIChildFrame(self, -1,  "Decoder Window",size = (800,600) )
        win.Show(True)
        win.SetIcon(wx.Icon(os.getcwd() + "\icons\decode.ico"))
        
    
    def Encoder(self, evt): 
        win = wx.MDIChildFrame(self, -1, "Encoder Window",size = (800,600) )
        win.Show(True)
        win.SetIcon(wx.Icon(os.getcwd() + "\icons\encode.ico"))
		
app = wx.App() 
frame = MDIFrame() 
frame.SetIcon(wx.Icon(os.getcwd() + "\icons\wtonlogo.ico"))
frame.Show()
frame.Maximize(True)
app.MainLoop()