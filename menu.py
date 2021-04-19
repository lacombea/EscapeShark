import tkinter as tk 
from PIL import Image, ImageTk

from page import * 
from timer import *
import app as a

import main as m

class Menu1(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)

        Label1 = tk.Label(self, text = 'Bienvenue dans Escape Shark !',font=("Courier",20), fg = '#00d0cb')
        Label1.pack()
        logo = tk.PhotoImage(file='logo.png')
        Label2 = tk.Label(self, image = logo)
        Label2.image = logo
        Label2.pack()

        Label3 = tk.Label(self, text = 'Projet Ingénieur Honnête Homme',font=("Courier",15))
        Label3.pack()
        Label4 = tk.Label(self, text = 'LACOMBE Alexia et MARY Baptiste',font=("Courier",15))
        Label4.pack()

        Bouton1 = tk.Button(self, text = 'En avant',font=("Courier",10), command = lambda: controller.show_frame("Menu2"), bg = '#00d0cb', activebackground = '#00d0cb')
        Bouton1.pack()

class Menu2(Page):

	def __init__(self, parent, controller):
		
		Page.__init__(self, parent, controller)

		Label1 = tk.Label(self, text = 'Qui sommes nous ?', font= ("Courier",20), fg = '#00d0cb')
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

		Bouton1 = tk.Button(self, text = 'Suivant',font=("Courier",10), command = lambda: controller.show_frame("Menu3"), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()

class Menu3(Page):

	def __init__(self, parent, controller):
		
		Page.__init__(self, parent, controller)

		Label1 = tk.Label(self, text = "Qu'est ce qu'un projet IHH ?", font= ("Courier",20), fg = '#00d0cb')
		Label1.pack()

		Label2 = tk.Label(self, text = "Etant en troisième année à l’Ecole Nationale d’Ingénieur de Brest, nous devons, \n dans le cadre de notre cours de Sciences Humaines pour l’Ingénieur, réaliser un projet Ingénieur Honnête Homme")
		Label2.pack()

		Label3 = tk.Label(self, text = "Pourquoi ce projet ?", font= ("Courier",20), fg = '#00d0cb')
		Label3.pack()

		Label4 = tk.Label(self, text = "Lors de la bourse aux projets IHH du 8 Octobre 2020, nous avons rencontré Emma DARBOIS, élève ingénieure en quatrième année. \n Suite auconfinement de Mars 2020, les projets IHH de l’année passée n’avaient pas pu être réalisés, d’où la mise en place de cette bourse, \n  afin que les projets inachevés puissent voir le jour. \n Le projet d’Emma était de mettre en place un Escape Game sur le thème des requins afin de démystifier leur mauvaise image auprès de la population.\n Après avoir échangé avec elle, nous avons décidé de reprendre son projet car ce dernier nous plaisait beaucoup \net que nous avons été particulièrement touchés par la passion d’Emma pour les requins")
		Label4.pack()

		Bouton1 = tk.Button(self, text = 'Suivant', font= ("Courier",10), command = lambda: controller.show_frame("Menu4"), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()

class Menu4(Page):

	def __init__(self, parent, controller):
		
		Page.__init__(self, parent, controller)

		Label1 = tk.Label(self, text = "Mise en contexte", font= ("Courier",20), fg = '#00d0cb')
		Label1.pack()

		Label2 = tk.Label(self, text = "Les joueurs incarnent une équipe de recherche scientifique sur la faune marine. \n Lors d’une excursion à bord du bateau d’un vieux pêcheur, ils découvrent une brèche dans la coque du navire \n qui leur fait supposer une attaque de requins, le capitaine a disparu et les voilà enfermés dans la cale ! \n Ils ont une heure pour remonter jusqu’à la cabine du capitaine en passant par la salle des machines \n et envoyer un message de secours via la radio.")
		Label2.pack()

		Bouton1 = tk.Button(self, text = 'Jouer',font= ("Courier",10), command = lambda: self.debut_jeu(controller), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()

	def debut_jeu(self, controller):
		Timer.__init__(a.App)
		controller.show_frame("Enigme1")

class MenuFinal(Page):

	def __init__(self, parent, controller):

		Page.__init__(self, parent, controller)

		Label1 = tk.Label(self, text = "BRAVO!", font= ("Courier",20), fg = '#00d0cb')
		Label1.pack()

		Label2 = tk.Label(self, text = "Vous avez terminé le jeu dans le temps imparti", font= ("Courier",20), fg = '#00d0cb')
		Label2.pack()

		Label3 = tk.Label(self, text = "Votre temps :", font= ("Courier",20), fg = '#00d0cb')
		Label3.pack()

		self.Label4 = tk.Label(self, text = "suspence.....", font= ("Courier",20), fg = 'black')
		self.Label4.pack()

		Bouton1 = tk.Button(self, text = 'Afficher score', command = lambda : self.afficher_score(), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()

	def afficher_score(self):
		self.Label4.configure(text=Timer.time) 