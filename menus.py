import tkinter as tk 
from PIL import Image, ImageTk

from pages import * 
from timer import *
import app as a
import joueur as joueur

class Menu1(Page):
	def __init__(self, parent, controller):
		Page.__init__(self, parent, controller)

		Label1 = tk.Label(self, text= " ")
		Label1.pack()
		Label2 = tk.Label(self, text = 'Bienvenue dans Escape Shark !',font=("Courier",20), fg = '#00d0cb')
		Label2.pack()
		logo = tk.PhotoImage(file='images/logo.png')
		Label3 = tk.Label(self, image = logo)
		Label3.image = logo
		Label3.pack()

		Label4 = tk.Label(self, text = 'Projet Ingénieur Honnête Homme',font=("Courier",15))
		Label4.pack()
		Label5 = tk.Label(self, text = 'LACOMBE Alexia et MARY Baptiste',font=("Courier",15))
		Label5.pack()
		Label6 = tk.Label(self, text= " ")
		Label6.pack()

		Bouton1 = tk.Button(self, text = 'En avant',font=("Courier",10), command = lambda: controller.show_frame("Menu2"), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()

class Menu2(Page):

	def __init__(self, parent, controller):
		
		Page.__init__(self, parent, controller)

		Label1 = tk.Label(self, text= " ")
		Label1.pack()
		Label2 = tk.Label(self, text = 'Qui sommes nous ?', font= ("Courier",20), fg = '#00d0cb')
		Label2.pack()
		Label3 = tk.Label(self, text= " ")
		Label3.pack()

		alexia = tk.PhotoImage(file='images/alexia.png')
		Label4 = tk.Label(self, image = alexia)
		Label4.image = alexia
		Label4.pack()

		Label5 = tk.Label(self, font=("Courier",12), wraplength = 700, text = 'Je m’appelle Alexia LACOMBE. Ayant beaucoup voyagé, j’ai découvert  une passion  pour  le  Snorkeling ainsi  que  pour  la  plongée sous-marine que j’ai pratiquée en club et ainsi passé mon niveau 1.')
		Label5.pack()
		Label6 = tk.Label(self, text= " ")
		Label6.pack()

		baptiste = tk.PhotoImage(file='images/baptiste.png')
		Label7 = tk.Label(self, image = baptiste)
		Label7.image = baptiste
		Label7.pack()

		Label8 = tk.Label(self, font=("Courier",12), wraplength = 700,  text = 'Je me nomme Baptiste MARY. Passionné par la voile et le surf depuis toujours, j’ai également voyagé à plusieurs reprises et ai effectué du Snorkeling. J’ai appris à aimer la faune et la flore marine lors de ces activités.')
		Label8.pack()
		Label9 = tk.Label(self, text= " ")
		Label9.pack()

		Bouton1 = tk.Button(self, text = 'Suivant',font=("Courier",10), command = lambda: controller.show_frame("Menu3"), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()

class Menu3(Page):

	def __init__(self, parent, controller):
		
		Page.__init__(self, parent, controller)

		Label1 = tk.Label(self, text= " ")
		Label1.pack()
		Label2 = tk.Label(self, text = "Qu'est ce qu'un projet IHH ?", font= ("Courier",20), fg = '#00d0cb')
		Label2.pack()
		Label3 = tk.Label(self, text= " ")
		Label3.pack()

		Label4 = tk.Label(self, font=("Courier",12), wraplength = 700, text = "Etant en troisième année à l’Ecole Nationale d’Ingénieur de Brest, nous devons, dans le cadre de notre cours de Sciences Humaines pour l’Ingénieur, réaliser un projet Ingénieur Honnête Homme.")
		Label4.pack() 
		Label5 = tk.Label(self, text= " ")
		Label5.pack()
		Label6 = tk.Label(self, text= " ")
		Label6.pack()

		Label7 = tk.Label(self, text = "Pourquoi ce projet ?", font= ("Courier",20), fg = '#00d0cb')
		Label7.pack()
		Label8 = tk.Label(self, text= " ")
		Label8.pack()

		Label9 = tk.Label(self, font=("Courier",12), wraplength = 700, text = "Lors de la bourse aux projets IHH du 8 Octobre 2020, nous avons rencontré Emma DARBOIS, élève ingénieure en quatrième année. Suite au confinement de Mars 2020, les projets IHH de l’année passée n’avaient pas pu être réalisés, d’où la mise en place de cette bourse, afin que les projets inachevés puissent voir le jour. Le projet d’Emma était de mettre en place un Escape Game sur le thème des requins afin de démystifier leur mauvaise image auprès de la population. Après avoir échangé avec elle, nous avons décidé de reprendre son projet car ce dernier nous plaisait beaucoup et que nous avons été particulièrement touchés par la passion d’Emma pour les requins.")
		Label9.pack()
		Label10 = tk.Label(self, text= " ")
		Label10.pack()

		Bouton1 = tk.Button(self, text = 'Suivant', font= ("Courier",10), command = lambda: controller.show_frame("Menu4"), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()

class Menu4(Page):

	def __init__(self, parent, controller):
		
		Page.__init__(self, parent, controller)

		Label1 = tk.Label(self, text= " ")
		Label1.pack()
		Label2 = tk.Label(self, text = "Mise en contexte", font= ("Courier",20), fg = '#00d0cb')
		Label2.pack()
		Label3 = tk.Label(self, text= " ")
		Label3.pack()

		Label4 = tk.Label(self, font=("Courier",12), wraplength = 700, text = "Lors de ce jeu intercatif, vous allez devoir résoudre différentes énigmes sur le thème des requins afin de pouvoir progresser. Vous allez devoir utiliser votre matière grise ... si vous en avez, mais attention, votre temps est compté !")
		Label4.pack()
		Label5 = tk.Label(self, text= " ")
		Label5.pack()
		Label5 = tk.Label(self, font=("Courier",12), text = "Alors, êtes-vous prêt à relever le défi ?")
		Label5.pack()
		Label6 = tk.Label(self, text= " ")
		Label6.pack()
		
		Label7 = tk.Label(self, text = "Présentez vous!", font= ("Courier",20), fg = '#00d0cb')
		Label7.pack()
		Label8 = tk.Label(self, text= " ")
		Label8.pack()

		cadre0=tk.Frame(self)
		cadre0.pack()
		Label9 = tk.Label(cadre0, text = "Prénom:",font= ("Courier",10))
		Label9.pack(side = 'left')
		self.Saisie5 = tk.Entry(cadre0, textvariable="Prénom",font= ("Courier",10))
		self.Saisie5.pack(side = 'left')
		Label10 = tk.Label(cadre0, text = "Nom:",font= ("Courier",10))
		Label10.pack(side = 'left')
		self.Saisie6 = tk.Entry(cadre0, textvariable="Nom",font= ("Courier",10))
		self.Saisie6.pack(side = 'left')

		Label11 = tk.Label(self, text= " ")
		Label11.pack()
		Bouton1 = tk.Button(self, text = 'Jouer',font= ("Courier",10), command = lambda: self.debut_jeu(controller), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()
		Label12 = tk.Label(self, text= " ")
		Label12.pack()
		Label13 = tk.Label(self, text= "! En cas de problème n'hésitez pas à appeller Alexia ou Baptiste !", font= ("Courier",15), fg = 'red')
		Label13.pack()

	def debut_jeu(self, controller):
		if (self.Saisie5.get() == '' or self.Saisie6.get() == ''):
			self.destroy_all()
		
			self.popup = tk.Toplevel(self)
			Page.list_of_tops.append(self.popup)
			self.popup.configure(bg = '#717171')

			Label1 = tk.Label(self.popup, text= " ",bg = '#717171')
			Label1.pack()
			Label2 = tk.Label(self.popup, text = "Veuillez rentrer votre nom et prénom", font= ("Courier",12), fg = 'white',bg = '#717171')
			Label2.pack()
			Label3 = tk.Label(self.popup, text= " ",bg = '#717171')
			Label3.pack()

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

		self.Bouton1 = tk.Button(self, text = 'suspence.....',font= ("Courier",10), command = lambda : self.afficher_score(), bg = '#00d0cb', activebackground = '#00d0cb')
		self.Bouton1.pack()

		self.Label5 = tk.Label(self, text = " ")
		self.Label5.pack()

	def afficher_score(self):
		self.destroy_all()
		Timer.time = Timer.get_time(a.App)
		self.Bouton1.destroy()
		self.Label1.configure(text=" ")
		self.Label2.configure(text="Félicitations "+ joueur.prénom + " " + joueur.nom + "!!!", font= ("Courier",20), fg = '#00d0cb') 
		self.Label3.configure(text=" ")
		self.Label4.configure(text = "Vous avez terminé le jeu dans le temps imparti", font= ("Courier",15))
		self.Label5.configure(text = "Votre temps :", font= ("Courier",15))
		self.Label6 = tk.Label(text=" ")
		self.Label6.pack()
		self.Label7 = tk.Label(self, text=Timer.time, fg = '#00d0cb', font= ("Courier",20)) 
		self.Label7.pack()
		self.Label8 = tk.Label(self, text=" ")
		self.Label8.pack()
		self.Label9 = tk.Label(self, text = "Nous espérons que vous avez apprécier jouer à notre jeu, et que vous en avez appris plus sur les requins.", font= ("Courier",15))
		self.Label9.pack()
		self.Label10 = tk.Label(self, text=" ")
		self.Label10.pack()
		self.Label11 = tk.Label(self, text = "! Veuillez appeller Alexia ou Baptiste pour valider votre score !",fg = 'red', font= ("Courier",15))
		self.Label11.pack()