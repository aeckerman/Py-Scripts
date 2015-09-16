from tkinter import *

root = Tk()
root.title("Input and Print")

def out():
	txtVar = txt.get()
	print (txtVar)

txt = StringVar()

stringIN = Entry(root, textvariable=txt)
stringIN.insert(0, "String")
stringIN.pack()
Button(root, text="OK", command=out).pack()

root.mainloop()