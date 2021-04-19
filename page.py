
import tkinter as tk 
from PIL import Image, ImageTk

class Page(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		self.list_of_tops = []

	def destroy_all(self):
		for window in self.list_of_tops :
			window.destroy()