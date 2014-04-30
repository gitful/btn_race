#! /usr/bin/env python
# Yes. Python 2. Because wx won't work with Python 3.

import wx

class Frame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, wx.ID_ANY, "10 Button Race")
		panel = wx.Panel(self)


if __name__ == '__main__':
	app = wx.App(False)
	frm = Frame(None)
	frm.Show()
	app.MainLoop()
