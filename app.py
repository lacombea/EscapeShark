import tkinter as tk 
from PIL import Image, ImageTk

from menus import *
from enigmes.enigme1 import *
from enigmes.enigme2 import *
from enigmes.enigme3 import *
from enigmes.enigme4 import *
from enigmes.enigme5 import *
from enigmes.enigme6 import *
from enigmes.enigme7 import *

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # le conteneur est l'endroit où nous empilerons un tas de cadres
        # les uns sur les autres, puis celui que nous voulons voir
        # sera élevé au-dessus des autres
        container = tk.Frame(self)
        
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(2, weight=1)
        container.grid_columnconfigure(2, weight=1)
        
        self.frames = {}
        pages = (Menu1, Menu2, Menu3, Menu4, Enigme1, Enigme2, Enigme3, Enigme4, Enigme5, Enigme6, Enigme7, MenuFinal)
        for F in pages:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            # mettre toutes les pages au même endroit;
            # celui en haut de l'ordre de superposition
            # sera celui qui est visible.
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame("Menu1")
            
    def show_frame(self, page_name):
        # afficher un cadre pour le nom de page donné
        frame = self.frames[page_name]
        frame.tkraise()