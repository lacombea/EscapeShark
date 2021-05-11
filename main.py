#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

import tkinter as tk 
from PIL import Image, ImageTk

from app import *

if __name__ == "__main__":
	application = App()
	application.geometry('%dx%d+0+0'%(application.W, application.H))
	application.title("Escape Shark")
	application.mainloop()
