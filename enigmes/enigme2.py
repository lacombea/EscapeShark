import tkinter as tk 
from PIL import Image, ImageTk

from pages import *
import app as a

class Enigme2(Page):

	def __init__(self, parent, controller):
		
		Page.__init__(self, parent, controller)

		Label1 = tk.Label(self, text= " ")
		Label1.pack()
		Label2 = tk.Label(self, text = "C'est parti !", font= ("Courier",20), fg = '#00d0cb')
		Label2.pack()
		Label3 = tk.Label(self, text = "Trouvez le code", font= ("Courier",20), fg = '#00d0cb')
		Label3.pack()
		Label4 = tk.Label(self, text= " ")
		Label4.pack()

		self.Saisie = tk.Entry(self, textvariable="bl",font= ("Courier",10))
		self.Saisie.pack()
		Label5 = tk.Label(self, text= " ")
		Label5.pack()
		Bouton0  = tk.Button(self, text = 'Valider',font= ("Courier",10), command = lambda : self.test(controller), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton0.pack()
		Label6 = tk.Label(self, text= " ")
		Label6.pack()

		cadre0=tk.Frame(self)
		cadre0.pack()
		Bouton1 = tk.Button(cadre0,font= ("Courier",10), text = 'Indice 1', command = lambda : self.indice(0), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack(side = 'left')
		Label1 = tk.Label(cadre0, text= " ")
		Label1.pack()
		Bouton2 = tk.Button(cadre0,font= ("Courier",10), text = 'Indice 2', command = lambda : self.indice(1), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton2.pack(side = 'left')
		Label2 = tk.Label(cadre0, text= " ")
		Label2.pack()
		Bouton3 = tk.Button(cadre0,font= ("Courier",10), text = 'Indice 3', command = lambda : self.indice(2), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton3.pack(side = 'left')
		Label3 = tk.Label(cadre0, text= " ")
		Label3.pack()

		cadre1=tk.Frame(self)
		cadre1.pack()
		Bouton4 = tk.Button(cadre1,font= ("Courier",10), text = 'Indice 4', command = lambda : self.indice(3), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton4.pack(side = 'left')
		Label1 = tk.Label(cadre1, text= " ")
		Label1.pack()
		Bouton5 = tk.Button(cadre1,font= ("Courier",10), text = 'Indice 5', command = lambda : self.indice(4), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton5.pack(side = 'left')


	def test(self, controller):

		if self.Saisie.get() == 'squale':
			self.destroy_all()
			self.squale()
			controller.show_frame("Enigme3")
		else :
			self.wrong()
			self.Saisie.delete(0,40)

	def indice(self, n):
		self.destroy_all()

		self.popup = tk.Toplevel(self)
		Page.list_of_tops.append(self.popup)
		self.popup.configure(bg = '#717171')

		indice = ['images/affiche1.png', 'images/affiche2.png', 'images/affiche3.png', 'images/affiche4.png', 'images/affiche5.png']

		indicen = tk.PhotoImage(file=indice[n])
		Label1 = tk.Label(self.popup, image = indicen)
		Label1.image = indicen
		Label1.pack()

		Bouton1 = tk.Button(self.popup, text = 'Fermer',font= ("Courier",10), command = lambda : self.popup.destroy(), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()

	def wrong(self):
		self.destroy_all()
		
		self.popup = tk.Toplevel(self)
		Page.list_of_tops.append(self.popup)
		self.popup.configure(bg = '#717171')

		Label1 = tk.Label(self.popup, text= " ",bg = '#717171')
		Label1.pack()
		Label2 = tk.Label(self.popup, text = "Réessayer", font= ("Courier",12), fg = 'white',bg = '#717171')
		Label2.pack()
		Label3 = tk.Label(self.popup, text= " ",bg = '#717171')
		Label3.pack()

		Bouton1 = tk.Button(self.popup, text = 'Retour à la saisie',font= ("Courier",10), command = lambda : self.popup.destroy(), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()

	def squale(self):
		self.popup = tk.Toplevel(self)
		Page.list_of_tops.append(self.popup)
		self.popup.configure(bg = '#717171')

		alpha = tk.PhotoImage(file='images/squale.png')
		Label1 = tk.Label(self.popup, image = alpha)
		Label1.image = alpha
		Label1.pack()

		Label2 = tk.Label(self.popup,font= ("Courier",15),fg = 'white',bg = '#717171', text = "Bien joué, vous avez trouvé la réponse ! \n\n Le saviez-vous ? \n")
		Label2.pack()

		Label3 = tk.Label(self.popup,font= ("Courier",12),fg = 'white',bg = '#717171', wraplength = 700, text = "Le mot squale est un terme qui englobe l'ensemble des espèces de requins avec des caractéristiques communes, comme la dentition, la texture de la peau ou la silhouette fuselée. ")
		Label3.pack()
		Label4 = tk.Label(self.popup, text= " ",bg = '#717171')
		Label4.pack()

		Bouton1 = tk.Button(self.popup, text = 'Suivant',font= ("Courier",10), command = lambda : self.popup.destroy(), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()