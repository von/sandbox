#!/usr/bin/env python

import wx

#class MyApp(wx.App):
#    def OnInit(self):
#	print "Hello"
#	return True

#app = MyApp(redirect=True)
app = wx.PySimpleApp()
frame = wx.Frame(None, title="Hello World")
frame.Show()
app.MainLoop()
