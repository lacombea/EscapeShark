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

        #définition de la taille de la fenêtre en fonction de la taille de l'écran de l'utilisateur
        self.H = self.winfo_screenheight()
        self.W = self.winfo_screenwidth()
        # container est l'endroit où nous empilerons un tas de Frame
        # les uns sur les autres, puis celui que nous voulons voir
        # sera élevé au-dessus des autres
        container = tk.Frame(self)
        
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(2, weight=1)
        container.grid_columnconfigure(2, weight=1)
        
        self.frames = {}
        pages = (Menu1, Menu2, Menu3, Menu4, Enigme1, Enigme2, Enigme3, Enigme4, Enigme5, Enigme6, Enigme7, MenuFinal)
        #on crée toutes les pages
        for F in pages:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame("Menu1")
            
    #mise en avant de la page appelée en paramètre
    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()