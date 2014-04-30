#! /usr/bin/env python
# Yes. Python 2. Because wx won't work with Python 3.

import wx, time, random

width = 400
height = 300

class Frame(wx.Frame):
	def __init__(self, parent, title):
		super(Frame, self).__init__(parent, wx.ID_ANY, title=title, size=(width, height))
		self.SetMinSize((width, height))
		self.SetMaxSize((width, height))
		panel = wx.Panel(self)
		self.button = wx.Button(panel, label="Begin 10 Button Race!", size=(width, 40))
		self.button.SetPosition(wx.Point(0,(height-40)/2))
		self.button.Bind(wx.EVT_BUTTON, self.on_click)
		self.Centre()
		self.Show()
		self.count = 1

	def on_click(self, e):
		self.button.SetPosition(wx.Point(random.randint(0,width-40), random.randint(0,height-40)))
		if self.count == 1:
			self.time = time.time()
			self.button.SetSize(wx.Size(40, 40))
			self.button.SetLabel(str(self.count))
			self.count += 1
		elif self.count == 11:
			self.time = time.time() - self.time
			self.button.SetSize(wx.Size(width, 40))
			self.button.SetPosition(wx.Point(0,(width-40)/2))
			if self.time < 5:
				self.button.SetLabel("YOU CHEATED! YOU COULDN'T HAVE DONE THIS IN " + str(self.time) + " SECONDS!!!")
			elif self.time < 10:
				self.button.SetLabel(str(self.time) + " seconds... are you cheating?")
			elif self.time < 20:
				self.button.SetLabel("You are okay. " + str(self.time) + " seconds. Meh.")
			elif self.time < 40:
				self.button.SetLabel("At " + str(self.time) + " seconds, you suck. Just saying.")
			elif self.time < 100:
				self.button.SetLabel("You are SO F**KING SLOW! At " + str(self.time) + " seconds, YOU DESERVE TO BE CURSED AT.")
			elif self.time > 99999999999999999999:
				self.button.SetLabel("HOLY CRAP. HOW LONG HAVE YOU LEFT THIS RUNNING!?!?!? " + str(self.time) + " SECONDS!!!!!")
			else:
				self.button.SetLabel("You are a failure in life. " + str(self.time) + " seconds.")
			self.count += 1
		elif self.count < 11:
			self.button.SetLabel(str(self.count))
			self.count += 1
		else:
			exit()

if __name__ == '__main__':
	app = wx.App(False)
	Frame(None, "10 Button Race")
	app.MainLoop()
