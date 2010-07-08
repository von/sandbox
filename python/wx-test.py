#!/usr/bin/env python
import wx

class Frame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Frame, self).__init__(None, title="Hello World")

        # Sizer code here causes panel to fill frame
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(Panel(self), proportion=1, flag=wx.EXPAND)
        self.SetSizer(sizer)

        self.SetAutoLayout(1)

class Panel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        super(Panel, self).__init__(parent, *args, **kwargs)
        self.SetBackgroundColour("BLUE")
        #sizer = wx.BoxSizer(wx.VERTICAL)
        sizer = wx.FlexGridSizer(cols=2, vgap=3, hgap=3)
        sizer.SetFlexibleDirection(wx.BOTH)
        # Make all columns grow to fit our parent
        sizer.AddGrowableCol(0)
        sizer.AddGrowableCol(1)
        # Only have first row grow to fit our parent
        sizer.AddGrowableRow(0)
        # Add two TextCtrl boxes, which fills first row
        sizer.Add(wx.TextCtrl(self, style=wx.TE_MULTILINE),
                  proportion=1, flag=wx.ALIGN_CENTER|wx.EXPAND)
        sizer.Add(wx.TextCtrl(self, style=wx.TE_MULTILINE),
                  proportion=1, flag=wx.ALIGN_CENTER|wx.EXPAND)
        # Now add button to second row
        sizer.Add(wx.Button(self, label="Hello"),
                  flag=wx.ALIGN_CENTER|wx.EXPAND)
        self.SetSizerAndFit(sizer)
        self.SetAutoLayout(1)

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = Frame()
    frame.Show()
    app.MainLoop()
