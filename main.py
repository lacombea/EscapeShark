##Projet MARY LACOMBE dklzjkdjz

#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys

import tkinter as tk 
from PIL import Image, ImageTk

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
		pages = (Menu1, Menu2, Menu3, Menu4, Menu5, Menu6, Menu7)
		for F in pages:
			page_name = F.__name__
			frame = F(parent=container, controller=self)
			self.frames[page_name] = frame
			# put all of the pages in the same location;
			# the one on the top of the stacking order
			# will be the one that is visible.
			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame("Menu1")

	def show_frame(self, page_name):
		# show a frame for the given page name 
		frame = self.frames[page_name]
		frame.tkraise()
		

class Menu1(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		Label1 = tk.Label(self, text = 'Bienvenue dans Escape Shark !', fg = 'blue')
		Label1.grid(row=1,column=1,columnspan=2)
		logo = tk.PhotoImage(file='logo.png')
		Label2 = tk.Label(self, image = logo)
		Label2.image = logo
		Label2.grid(row=2,column=1,columnspan=2)

		Label3 = tk.Label(self, text = 'Projet Ingénieur Honnête Homme')
		Label3.grid(row=3,column=1,columnspan=2)
		Label4 = tk.Label(self, text = 'LACOMBE Alexia et MARY Baptiste')
		Label4.grid(row=4,column=1,columnspan=2)

		Bouton1 = tk.Button(self, text = 'En avant', command = lambda: controller.show_frame("Menu2"))
		Bouton1.grid(row=5,column=1)
		Bouton2 = tk.Button(self, text = 'Quitter', command = lambda : app.quit())
		Bouton2.grid(row=5,column=2)

class Menu2(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller 

		Label1 = tk.Label(self, text = 'Qui sommes nous ?', font= (10), fg = 'red')
		Label1.pack()

		alexia = tk.PhotoImage(file='alexia.png')
		Label2 = tk.Label(self, image = alexia)
		Label2.image = alexia
		Label2.pack()

		Label3 = tk.Label(self, text = 'Je m’appelle Alexia LACOMBE. Ayant beaucoup voyagé, \n j’ai découvert  une passion  pour  le  Snorkeling ainsi  que  pour  la  plongée sous-marine \n que j’ai pratiquée en club et ainsi passé mon niveau 1.')
		Label3.pack()

		baptiste = tk.PhotoImage(file='baptiste.png')
		Label4 = tk.Label(self, image = baptiste)
		Label4.image = baptiste
		Label4.pack()

		Label5 = tk.Label(self, text = 'Je me nomme Baptiste MARY. Passionné par la voile et le surf depuis toujours, \n  j’ai également voyagé à plusieurs reprises et ai effectué du Snorkeling. \n J’ai appris à aimer la faune et la flore marine lors de ces activités.')
		Label5.pack()

		Bouton1 = tk.Button(self, text = 'Suivant', command = lambda: controller.show_frame("Menu3"))
		Bouton1.pack()

class Menu3(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		Label1 = tk.Label(self, text = "Qu'est ce qu'un projet IHH ?", font= (10), fg = 'red')
		Label1.pack()

		Label2 = tk.Label(self, text = "Etant en troisième année à l’Ecole Nationale d’Ingénieur de Brest, nous devons, \n dans le cadre de notre cours de Sciences Humaines pour l’Ingénieur, réaliser un projet Ingénieur Honnête Homme")
		Label2.pack()

		Label3 = tk.Label(self, text = "Pourquoi ce projet ?", font= (10), fg = 'red')
		Label3.pack()

		Label4 = tk.Label(self, text = "Lors de la bourse aux projets IHH du 8 Octobre 2020, nous avons rencontré Emma DARBOIS, élève ingénieure en quatrième année. \n Suite auconfinement de Mars 2020, les projets IHH de l’année passée n’avaient pas pu être réalisés, d’où la mise en place de cette bourse, \n  afin que les projets inachevés puissent voir le jour. \n Le projet d’Emma était de mettre en place un Escape Game sur le thème des requins afin de démystifier leur mauvaise image auprès de la population.\n Après avoir échangé avec elle, nous avons décidé de reprendre son projet car ce dernier nous plaisait beaucoup \net que nous avons été particulièrement touchés par la passion d’Emma pour les requins")
		Label4.pack()

		Bouton1 = tk.Button(self, text = 'Suivant', command = lambda: controller.show_frame("Menu4"))
		Bouton1.pack()

class Menu4(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		Label1 = tk.Label(self, text = "Mise en contexte", font= (10), fg = 'red')
		Label1.pack()

		Label2 = tk.Label(self, text = "Les joueurs incarnent une équipe de recherche scientifique sur la faune marine. \n Lors d’une excursion à bord du bateau d’un vieux pêcheur, ils découvrent une brèche dans la coque du navire \n qui leur fait supposer une attaque de requins, le capitaine a disparu et les voilà enfermés dans la cale ! \n Ils ont une heure pour remonter jusqu’à la cabine du capitaine en passant par la salle des machines \n et envoyer un message de secours via la radio.")
		Label2.pack()

		Bouton1 = tk.Button(self, text = 'Jouer', command = lambda: controller.show_frame("Menu5"))
		Bouton1.pack()

class Menu5(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		
		self.list_of_tops = []

		Label1 = tk.Label(self, text = "C'est parti ! \n Décodez ceci pour continuer", font= (10), fg = 'red')
		Label1.pack()

		code = tk.PhotoImage(file='codemorse.png')
		Label2 = tk.Label(self, image = code)
		Label2.image = code
		Label2.pack()

		Bouton1  = tk.Button(self, text = 'alphabet', command = lambda : self.alphabet())
		Bouton1.pack()

		self.Saisie = tk.Entry(self, textvariable="bla")
		self.Saisie.pack()
		Bouton2  = tk.Button(self, text = 'valider', command = lambda : self.test(controller))
		Bouton2.pack()


	def test(self, controller):

		if self.Saisie.get() == 'requin blanc':
			self.destroy_all()
			controller.show_frame("Menu6")
		else :
			self.wrong()

	def alphabet(self):
		self.popup = tk.Toplevel(self)
		self.list_of_tops.append(self.popup)

		alpha = tk.PhotoImage(file='alphamorse.png')
		Label1 = tk.Label(self.popup, image = alpha)
		Label1.image = alpha
		Label1.pack()

		Bouton1 = tk.Button(self.popup, text = 'Quitter', command = lambda : self.popup.destroy())
		Bouton1.pack()

	def wrong(self):
		self.destroy_all()
		
		self.popup = tk.Toplevel(self)
		self.list_of_tops.append(self.popup)

		Label1 = tk.Label(self.popup, text = "Réessayer", font= (10), fg = 'red')
		Label1.pack()

		Bouton1 = tk.Button(self.popup, text = 'Quitter', command = lambda : self.popup.destroy())
		Bouton1.pack()

	def destroy_all(self):
		for window in self.list_of_tops :
			window.destroy()


class Menu6(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		
		self.list_of_tops = []

		Label1 = tk.Label(self, text = "C'est parti ! \n Trouvez le code", font= (10), fg = 'red')
		Label1.pack()

		self.Saisie = tk.Entry(self, textvariable="bl")
		self.Saisie.pack()
		Bouton1  = tk.Button(self, text = 'valider', command = lambda : self.test(controller))
		Bouton1.pack()

		Bouton1 = tk.Button(self, text = 'Indice 1', command = lambda : self.indice(0))
		Bouton1.pack()
		Bouton2 = tk.Button(self, text = 'Indice 2', command = lambda : self.indice(1))
		Bouton2.pack()
		Bouton3 = tk.Button(self, text = 'Indice 3', command = lambda : self.indice(2))
		Bouton3.pack()
		Bouton4 = tk.Button(self, text = 'Indice 4', command = lambda : self.indice(3))
		Bouton4.pack()
		Bouton5 = tk.Button(self, text = 'Indice 5', command = lambda : self.indice(4))
		Bouton5.pack()


	def test(self, controller):

		if self.Saisie.get() == 'squale':
			self.destroy_all()
			controller.show_frame("Menu7")
		else :
			self.wrong()

	def indice(self, n):
		self.destroy_all()

		self.popup = tk.Toplevel(self)
		self.list_of_tops.append(self.popup)

		indice = ['affiche1.png', 'affiche2.png', 'affiche3.png', 'affiche4.png', 'affiche5.png']

		indicen = tk.PhotoImage(file=indice[n])
		Label1 = tk.Label(self.popup, image = indicen)
		Label1.image = indicen
		Label1.pack()

		Bouton1 = tk.Button(self.popup, text = 'Quitter', command = lambda : self.popup.destroy())
		Bouton1.pack()

	def wrong(self):
		self.destroy_all()
		
		self.popup = tk.Toplevel(self)
		self.list_of_tops.append(self.popup)

		Label1 = tk.Label(self.popup, text = "Réessayer", font= (10), fg = 'red')
		Label1.pack()

		Bouton1 = tk.Button(self.popup, text = 'Quitter', command = lambda : self.popup.destroy())
		Bouton1.pack()

	def destroy_all(self):
		for window in self.list_of_tops :
			window.destroy()



class Menu7(tk.Frame):

	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller

		Label1 = tk.Label(self, text = "BRAVO!", font= (10), fg = 'red')
		Label1.pack()

		Label2 = tk.Label(self, text = "Vous avez terminé le jeu dans le temps imparti", font= (10), fg = 'red')
		Label2.pack()


		Bouton1 = tk.Button(self, text = 'Quitter', command = lambda : app.quit())
		Bouton1.pack()


if __name__ == "__main__":
	app = App()
	app.title("Escape Shark")
	app.mainloop()
