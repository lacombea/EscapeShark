import tkinter as tk 
from PIL import Image, ImageTk

from pages import * 
from timer import *
import app as a
import joueur as joueur

class Menu1(Page):
	def __init__(self, parent, controller):
		Page.__init__(self, parent, controller)

		Label1 = tk.Label(self, text = '\nBienvenue dans Escape Shark !',font=("Courier",20), fg = '#00d0cb')
		Label1.pack()
		logo = tk.PhotoImage(file='images/logo.png')
		Label2 = tk.Label(self, image = logo)
		Label2.image = logo
		Label2.pack()

		Label3 = tk.Label(self, text = 'Projet Ingénieur Honnête Homme',font=("Courier",15))
		Label3.pack()
		Label4 = tk.Label(self, text = 'LACOMBE Alexia et MARY Baptiste\n',font=("Courier",15))
		Label4.pack()

		Bouton1 = tk.Button(self, text = 'En avant',font=("Courier",10), command = lambda: controller.show_frame("Menu2"), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()

class Menu2(Page):

	def __init__(self, parent, controller):
		
		Page.__init__(self, parent, controller)

		Label1 = tk.Label(self, text = '\nQui sommes nous ?\n', font= ("Courier",20), fg = '#00d0cb')
		Label1.pack()

		alexia = tk.PhotoImage(file='images/alexia.png')
		Label2 = tk.Label(self, image = alexia)
		Label2.image = alexia
		Label2.pack()

		Label3 = tk.Label(self, font=("Courier",12), wraplength = 700, text = 'Je m’appelle Alexia LACOMBE. Ayant beaucoup voyagé, j’ai découvert  une passion  pour  le  Snorkeling ainsi  que  pour  la  plongée sous-marine que j’ai pratiquée en club et ainsi passé mon niveau 1.\n')
		Label3.pack()

		baptiste = tk.PhotoImage(file='images/baptiste.png')
		Label4 = tk.Label(self, image = baptiste)
		Label4.image = baptiste
		Label4.pack()

		Label5 = tk.Label(self, font=("Courier",12), wraplength = 700,  text = 'Je me nomme Baptiste MARY. Passionné par la voile et le surf depuis toujours, j’ai également voyagé à plusieurs reprises et ai effectué du Snorkeling. J’ai appris à aimer la faune et la flore marine lors de ces activités.\n')
		Label5.pack()

		Bouton1 = tk.Button(self, text = 'Suivant',font=("Courier",10), command = lambda: controller.show_frame("Menu3"), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()

class Menu3(Page):

	def __init__(self, parent, controller):
		
		Page.__init__(self, parent, controller)

		Label1 = tk.Label(self, text = "\nQu'est ce qu'un projet IHH ?\n", font= ("Courier",20), fg = '#00d0cb')
		Label1.pack()

		Label2 = tk.Label(self, font=("Courier",12), wraplength = 700, text = "Etant en troisième année à l’Ecole Nationale d’Ingénieur de Brest, nous devons, dans le cadre de notre cours de Sciences Humaines pour l’Ingénieur, réaliser un projet Ingénieur Honnête Homme.\n\n")
		Label2.pack() 

		Label3 = tk.Label(self, text = "Pourquoi ce projet ?\n", font= ("Courier",20), fg = '#00d0cb')
		Label3.pack()

		Label4 = tk.Label(self, font=("Courier",12), wraplength = 700, text = "Lors de la bourse aux projets IHH du 8 Octobre 2020, nous avons rencontré Emma DARBOIS, élève ingénieure en quatrième année. Suite au confinement de Mars 2020, les projets IHH de l’année passée n’avaient pas pu être réalisés, d’où la mise en place de cette bourse, afin que les projets inachevés puissent voir le jour. Le projet d’Emma était de mettre en place un Escape Game sur le thème des requins afin de démystifier leur mauvaise image auprès de la population. Après avoir échangé avec elle, nous avons décidé de reprendre son projet car ce dernier nous plaisait beaucoup et que nous avons été particulièrement touchés par la passion d’Emma pour les requins.\n")
		Label4.pack()

		Bouton1 = tk.Button(self, text = 'Suivant', font= ("Courier",10), command = lambda: controller.show_frame("Menu4"), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()

class Menu4(Page):

	def __init__(self, parent, controller):
		
		Page.__init__(self, parent, controller)

		Label1 = tk.Label(self, text = "\nMise en contexte\n", font= ("Courier",20), fg = '#00d0cb')
		Label1.pack()

		Label2 = tk.Label(self, font=("Courier",12), wraplength = 700, text = "Lors de ce jeu intercatif, vous allez devoir résoudre différentes énigmes sur le thème des requins afin de pouvoir progresser. Vous allez devoir utiliser votre matière grise ... si vous en avez, mais attention, votre temps est compté !\n")
		Label2.pack()
		Label3 = tk.Label(self, font=("Courier",12), text = "Alors, êtes-vous prêt à relever le défi ?\n")
		Label3.pack()
		
		Label4 = tk.Label(self, text = "Présentez vous!\n", font= ("Courier",20), fg = '#00d0cb')
		Label4.pack()

		cadre0=tk.Frame(self)
		cadre0.pack()
		Label5 = tk.Label(cadre0, text = "Prénom:",font= ("Courier",10))
		Label5.pack(side = 'left')
		self.Saisie5 = tk.Entry(cadre0, textvariable="Prénom",font= ("Courier",10))
		self.Saisie5.pack(side = 'left')
		Label6 = tk.Label(cadre0, text = "Nom:",font= ("Courier",10))
		Label6.pack(side = 'left')
		self.Saisie6 = tk.Entry(cadre0, textvariable="Nom",font= ("Courier",10))
		self.Saisie6.pack(side = 'left')

		Label7 = tk.Label(self, text= " ")
		Label7.pack()
		Bouton1 = tk.Button(self, text = 'Jouer',font= ("Courier",10), command = lambda: self.debut_jeu(controller), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()
		Label8 = tk.Label(self, text= "\n! En cas de problème n'hésitez pas à appeler Alexia ou Baptiste !", font= ("Courier",15), fg = 'red')
		Label8.pack()

	def debut_jeu(self, controller):
		if (self.Saisie5.get() == '' or self.Saisie6.get() == ''):
			self.destroy_all()
		
			self.popup = tk.Toplevel(self)
			Page.list_of_tops.append(self.popup)
			self.popup.configure(bg = '#717171')

			Label1 = tk.Label(self.popup, text = "\nVeuillez rentrer votre nom et prénom\n", font= ("Courier",12), fg = 'white',bg = '#717171')
			Label1.pack()

			Bouton1 = tk.Button(self.popup, text = 'Retour à la saisie',font= ("Courier",10), command = lambda : self.popup.destroy(), bg = '#00d0cb', activebackground = '#00d0cb')
			Bouton1.pack()
		else : 
			joueur.prénom = self.Saisie5.get()
			joueur.nom = self.Saisie6.get()
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

		self.Bouton1 = tk.Button(self, text = 'Suspence.....',font= ("Courier",10), command = lambda : self.afficher_score(), bg = '#00d0cb', activebackground = '#00d0cb')
		self.Bouton1.pack()

		self.Label5 = tk.Label(self, text = " ")
		self.Label5.pack()

	def afficher_score(self):
		self.destroy_all()
		Timer.time = Timer.get_time(a.App)
		self.Bouton1.destroy()
		self.Label1.configure(text="\nFélicitations "+ joueur.prénom + " " + joueur.nom + "!!!", font= ("Courier",20), fg = '#00d0cb') 
		self.Label2.configure(text = "\nVous avez terminé le jeu dans le temps imparti", font= ("Courier",15))
		self.Label3.configure(text = "Votre temps :", font= ("Courier",15))
		self.Label4 = tk.Label(self, text=Timer.time, fg = '#00d0cb', font= ("Courier",20)) 
		self.Label4.pack()
		self.Label5 = tk.Label(self, text = "\nNous espérons que vous avez apprécier jouer à notre jeu, et que vous en avez appris plus sur les requins.", font= ("Courier",15))
		self.Label5.pack()
		self.Label6 = tk.Label(self, text = "\n! Veuillez appeler Alexia ou Baptiste pour valider votre score !",fg = 'red', font= ("Courier",15))
		self.Label6.pack()