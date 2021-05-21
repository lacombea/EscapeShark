#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

import tkinter as tk 
from PIL import Image, ImageTk

from app import *

#lancement de l'application
if __name__ == "__main__":
	application = App()
	#définition de la taille de la fenêtre en fonction de la taille de l'écran de l'utilisateur
	application.geometry('%dx%d+0+0'%(application.W, application.H))
	application.title("Escape Shark")
	application.mainloop()
