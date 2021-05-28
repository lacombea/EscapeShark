import tkinter as tk 
from PIL import Image, ImageTk

class Page(tk.Frame):

	list_of_tops = []

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

	def destroy_all(self):
		for window in Page.list_of_tops :
			window.destroy()