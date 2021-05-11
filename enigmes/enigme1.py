import tkinter as tk 
from PIL import Image, ImageTk

from pages import *
import app as a

class Enigme1(Page):

	def __init__(self, parent, controller):
		
		Page.__init__(self, parent, controller)

		Label1 = tk.Label(self, text = "\nC'est parti ! \n Décodez ceci pour continuer\n",  font= ("Courier",20), fg = '#00d0cb')
		Label1.pack()

		code = tk.PhotoImage(file='images/codemorse.png')
		Label2 = tk.Label(self, image = code)
		Label2.image = code
		Label2.pack()
		Label3 = tk.Label(self, text= " ")
		Label3.pack()

		Bouton1  = tk.Button(self, text = 'Alphabet',font= ("Courier",10), command = lambda : self.alphabet(), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()
		Label4 = tk.Label(self, text= " ")
		Label4.pack()

		self.Saisie = tk.Entry(self, textvariable="code",font= ("Courier",10))
		self.Saisie.pack()
		Label5 = tk.Label(self, text= " ")
		Label5.pack()
		Bouton2  = tk.Button(self, text = 'Valider',font= ("Courier",10), command = lambda : self.test(controller), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton2.pack()


	def test(self, controller):
		if self.Saisie.get() == 'requin blanc':
			self.destroy_all()
			self.requin_blanc()
			controller.show_frame("Enigme3")
		elif self.Saisie.get() == 'secret':
			self.destroy_all()
			self.requin_blanc()
			controller.show_frame("Enigme4")
		else :
			self.wrong()
			self.Saisie.delete(0,40)

	def alphabet(self):
		self.popup = tk.Toplevel(self)
		Page.list_of_tops.append(self.popup)
		self.popup.configure(bg = '#717171')

		alpha = tk.PhotoImage(file='images/alphamorse.png')
		Label1 = tk.Label(self.popup, image = alpha)
		Label1.image = alpha
		Label1.pack()

		Bouton1 = tk.Button(self.popup, text = 'Fermer',font= ("Courier",10), command = lambda : self.popup.destroy(), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()

	def wrong(self):
		self.destroy_all()
		
		self.popup = tk.Toplevel(self)
		Page.list_of_tops.append(self.popup)
		self.popup.configure(bg = '#717171')

		Label1 = tk.Label(self.popup, text = "\nVeuillez réessayer\n", font= ("Courier",12), fg = 'white',bg = '#717171')
		Label1.pack()

		Bouton1 = tk.Button(self.popup, text = 'Retour à la saisie',font= ("Courier",10), command = lambda : self.popup.destroy(), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()

	def requin_blanc(self):
		self.popup = tk.Toplevel(self)
		Page.list_of_tops.append(self.popup)
		self.popup.configure(bg = '#717171')

		alpha = tk.PhotoImage(file='images/requinblanc.png')
		Label1 = tk.Label(self.popup, image = alpha)
		Label1.image = alpha
		Label1.pack()

		Label2 = tk.Label(self.popup, text = "Bien joué, vous avez trouvé la réponse ! \n\n Le saviez-vous ? \n",font= ("Courier",15),fg = 'white',bg = '#717171')
		Label2.pack()

		Label3 = tk.Label(self.popup,wraplength = 600, font= ("Courier",12), fg = 'white', bg = '#717171', text = " Rendu célèbre grâce aux Dents de la Mer de Spielberg, le requin blanc est l'une des espèces les plus imposantes de requins. Le dos gris et le ventre blanc, il peut atteindre jusqu'à 5m de longueur à l'âge adulte, et peut vivre pendant 40 ans !\n")
		Label3.pack()
		Bouton1 = tk.Button(self.popup, text = 'Suivant',font= ("Courier",10),command = lambda : self.popup.destroy(), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()