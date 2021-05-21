import tkinter as tk 
from PIL import Image, ImageTk

class Page(tk.Frame):
	#variable contenant les pop-ups
	list_of_tops = []

	#intialisation d'une Frame
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

	#détruit les pop-ups
	def destroy_all(self):
		for window in Page.list_of_tops :
			window.destroy()