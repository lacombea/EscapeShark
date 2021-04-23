import tkinter as tk 
from PIL import Image, ImageTk

from page import * 
from timer import *
import app as a
import joueur as joueur

class Menu1(Page):
    def __init__(self, parent, controller):
        Page.__init__(self, parent, controller)

        Label1 = tk.Label(self, text = 'Bienvenue dans Escape Shark !',font=("Courier",20), fg = '#00d0cb')
        Label1.pack()
        logo = tk.PhotoImage(file='image/logo.png')
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

		alexia = tk.PhotoImage(file='image/alexia.png')
		Label2 = tk.Label(self, image = alexia)
		Label2.image = alexia
		Label2.pack()

		Label3 = tk.Label(self, font=("Courier",12), wraplength = 700, text = 'Je m’appelle Alexia LACOMBE. Ayant beaucoup voyagé, j’ai découvert  une passion  pour  le  Snorkeling ainsi  que  pour  la  plongée sous-marine que j’ai pratiquée en club et ainsi passé mon niveau 1.')
		Label3.pack()

		baptiste = tk.PhotoImage(file='image/baptiste.png')
		Label4 = tk.Label(self, image = baptiste)
		Label4.image = baptiste
		Label4.pack()

		Label5 = tk.Label(self, font=("Courier",12), wraplength = 700,  text = 'Je me nomme Baptiste MARY. Passionné par la voile et le surf depuis toujours, j’ai également voyagé à plusieurs reprises et ai effectué du Snorkeling. J’ai appris à aimer la faune et la flore marine lors de ces activités.')
		Label5.pack()

		Bouton1 = tk.Button(self, text = 'Suivant',font=("Courier",10), command = lambda: controller.show_frame("Menu3"), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()

class Menu3(Page):

	def __init__(self, parent, controller):
		
		Page.__init__(self, parent, controller)

		Label1 = tk.Label(self, text = "Qu'est ce qu'un projet IHH ?", font= ("Courier",20), fg = '#00d0cb')
		Label1.pack()

		Label2 = tk.Label(self, font=("Courier",12), wraplength = 700, text = "Etant en troisième année à l’Ecole Nationale d’Ingénieur de Brest, nous devons, dans le cadre de notre cours de Sciences Humaines pour l’Ingénieur, réaliser un projet Ingénieur Honnête Homme")
		Label2.pack() 

		Label3 = tk.Label(self, text = "Pourquoi ce projet ?", font= ("Courier",20), fg = '#00d0cb')
		Label3.pack()

		Label4 = tk.Label(self, font=("Courier",12), wraplength = 700, text = "Lors de la bourse aux projets IHH du 8 Octobre 2020, nous avons rencontré Emma DARBOIS, élève ingénieure en quatrième année. Suite auconfinement de Mars 2020, les projets IHH de l’année passée n’avaient pas pu être réalisés, d’où la mise en place de cette bourse, afin que les projets inachevés puissent voir le jour. Le projet d’Emma était de mettre en place un Escape Game sur le thème des requins afin de démystifier leur mauvaise image auprès de la population. Après avoir échangé avec elle, nous avons décidé de reprendre son projet car ce dernier nous plaisait beaucoup et que nous avons été particulièrement touchés par la passion d’Emma pour les requins")
		Label4.pack()

		Bouton1 = tk.Button(self, text = 'Suivant', font= ("Courier",10), command = lambda: controller.show_frame("Menu4"), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()

class Menu4(Page):

	def __init__(self, parent, controller):
		
		Page.__init__(self, parent, controller)

		Label1 = tk.Label(self, text = "Mise en contexte", font= ("Courier",20), fg = '#00d0cb')
		Label1.pack()

		Label2 = tk.Label(self, font=("Courier",12), wraplength = 700, text = "Les joueurs incarnent une équipe de recherche scientifique sur la faune marine. Lors d’une excursion à bord du bateau d’un vieux pêcheur, ils découvrent une brèche dans la coque du navire qui leur fait supposer une attaque de requins, le capitaine a disparu et les voilà enfermés dans la cale ! Ils ont une heure pour remonter jusqu’à la cabine du capitaine en passant par la salle des machines et envoyer un message de secours via la radio.")
		Label2.pack()

		Label3 = tk.Label(self, text = "Présentez vous!", font= ("Courier",20), fg = '#00d0cb')
		Label3.pack()

		cadre0=tk.Frame(self)
		cadre0.pack()
		Label4 = tk.Label(cadre0, text = "Prénom:",font= ("Courier",10))
		Label4.pack(side = 'left')
		self.Saisie4 = tk.Entry(cadre0, textvariable="Prénom",font= ("Courier",10))
		self.Saisie4.pack(side = 'left')
		Label5 = tk.Label(cadre0, text = "Nom:",font= ("Courier",10))
		Label5.pack(side = 'left')
		self.Saisie5 = tk.Entry(cadre0, textvariable="Nom",font= ("Courier",10))
		self.Saisie5.pack(side = 'left')

		Bouton1 = tk.Button(self, text = 'Jouer',font= ("Courier",10), command = lambda: self.debut_jeu(controller), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()

	def debut_jeu(self, controller):
		if (self.Saisie4.get() == '' or self.Saisie5.get() == ''):
			self.destroy_all()
		
			self.popup = tk.Toplevel(self)
			Page.list_of_tops.append(self.popup)
			self.popup.configure(bg = '#717171')

			Label1 = tk.Label(self.popup, text = "Veuillez rentrer votre nom et prénom", font= ("Courier",12), fg = 'white',bg = '#717171')
			Label1.pack()

			Bouton1 = tk.Button(self.popup, text = 'Retour à la saisie',font= ("Courier",10), command = lambda : self.popup.destroy(), bg = '#00d0cb', activebackground = '#00d0cb')
			Bouton1.pack()
		else : 
			joueur.prénom = self.Saisie4.get()
			joueur.nom = self.Saisie5.get()
			Timer.__init__(a.App)
			controller.show_frame("Enigme1")


class MenuFinal(Page):

	def __init__(self, parent, controller):

		Page.__init__(self, parent, controller)

		self.Label1 = tk.Label(self, text = " ")
		self.Label1.pack()

		self.Label2 = tk.Label(self, text = " ")
		self.Label2.pack()

		self.Label3 = tk.Label(self, text = " ")
		self.Label3.pack()

		self.Label4 = tk.Label(self, text = " ")
		self.Label4.pack()

		self.Bouton1 = tk.Button(self, text = 'suspence.....',font= ("Courier",10), command = lambda : self.afficher_score(), bg = '#00d0cb', activebackground = '#00d0cb')
		self.Bouton1.pack()

		self.Label5 = tk.Label(self, text = " ")
		self.Label5.pack()

	def afficher_score(self):
		self.destroy_all()
		self.Bouton1.destroy()
		self.Label1.configure(text="Félicitations "+ joueur.prénom + " " + joueur.nom + "!!!", font= ("Courier",20), fg = '#00d0cb') 
		self.Label2.configure(text = "Vous avez terminé le jeu dans le temps imparti", font= ("Courier",15))
		self.Label3.configure(text = "Votre temps :", font= ("Courier",15))
		self.Label4.configure(text=Timer.time, fg = '#00d0cb', font= ("Courier",20)) 
		self.Label5.configure(text = "Veuillez appeller Alexia ou Baptiste pour valider votre score!", font= ("Courier",15))