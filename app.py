import tkinter as tk 
from PIL import Image, ImageTk

from menu import *
from enigme import *

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(2, weight=1)
        container.grid_columnconfigure(2, weight=1)
        
        self.frames = {}
        pages = (Menu1, Menu2, Menu3, Menu4, Enigme1, Enigme2, Enigme3, MenuFinal)
        for F in pages:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
            #frame.configure(background = '#00d0cb')
            
        self.show_frame("Menu1")
            
    def show_frame(self, page_name):
        # show a frame for the given page name 
        frame = self.frames[page_name]
        frame.tkraise()