from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Themes")

s = ttk.Style()

settingWin = Frame(root)
settingWin.pack()

def deTheme():
	s.theme_use('default')

defaultB = ttk.Button(settingWin, text = "default", command = deTheme)
defaultB.pack()

def clTheme():
	s.theme_use('classic')

classicB = ttk.Button(settingWin, text = "classic", command = clTheme)
classicB.pack()

def alTheme():
	s.theme_use('alt')

altB = ttk.Button(settingWin, text = "alt", command = alTheme)
altB.pack()

def claTheme():
	s.theme_use('clam')

clamB = ttk.Button(settingWin, text = "clam", command = claTheme)
clamB.pack()

def aqTheme():
	s.theme_use('aqua')

aquaB = ttk.Button(settingWin, text = "aqua", command = aqTheme)
aquaB.pack()

root.mainloop()