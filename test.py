
  71         topSizer.Add(inputTwoSizer, 0, wx.ALL|wx.EXPAND, 5)
  72         topSizer.Add(inputThreeSizer, 0, wx.ALL|wx.EXPAND, 5)
  73         topSizer.Add(inputFourSizer, 0, wx.ALL|wx.EXPAND, 5)
  74         topSizer.Add(wx.StaticLine(self.panel), 0, wx.ALL|wx.EXPAND, 5)
  75         topSizer.Add(btnSizer, 0, wx.ALL|wx.CENTER, 5)
  76 
  77         self.panel.SetSizer(topSizer)
  78         topSizer.Fit(self)
  79 
  80 
  81     def onOK(self, event):
  82         # Do something
  83         print 'onOK handler'
  84 
  85     def onCancel(self, event):
  86         self.closeProgram()
  87 
  88     def closeProgram(self):
  89         self.Close()
  90 
  91 
  92 # Run the program
  93 if __name__ == '__main__':
  94     app = wx.PySimpleApp()
  95     frame = MyForm().Show()
  96     app.MainLoop()