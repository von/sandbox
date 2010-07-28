#!/usr/bin/env python
import wx

class App(wx.PySimpleApp):
    def OnInit(self):
        self.frame = Frame()
        self.frame.Show()

        # Find a button in the GUI and bind it to an event
        helloButton = wx.FindWindowByName("HelloButton")
        if not helloButton:
            print "Could not find 'Hello World' button"
        else:
            self.Bind(wx.EVT_BUTTON, self.HelloWorld, helloButton)

        return True

    def HelloWorld(self, event):
        leftText = wx.FindWindowByName("LeftText")
        if leftText:
            leftText.SetValue("Hello")
        rightText = wx.FindWindowByName("RightText")
        if rightText:
            rightText.SetValue("World")

class Frame(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(Frame, self).__init__(None, title="Hello World")

        # Sizer code here causes panel to fill frame
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(Panel(self, name="MyPanel"), proportion=1, flag=wx.EXPAND)
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
        sizer.Add(wx.TextCtrl(self, style=wx.TE_MULTILINE, name="LeftText"),
                  proportion=1, flag=wx.ALIGN_CENTER|wx.EXPAND)
        sizer.Add(wx.TextCtrl(self, style=wx.TE_MULTILINE, name="RightText"),
                  proportion=1, flag=wx.ALIGN_CENTER|wx.EXPAND)
        # Now add button to second row
        sizer.Add(wx.Button(self, label="Hello", name="HelloButton"),
                  flag=wx.ALIGN_CENTER|wx.EXPAND)
        self.SetSizerAndFit(sizer)
        self.SetAutoLayout(1)

if __name__ == '__main__':
    app = App()
    app.MainLoop()
