import tkinter as tk 
from PIL import Image, ImageTk

from pages import *
import app as a

class Enigme5(Page):

	def __init__(self, parent, controller):
	
		Page.__init__(self, parent, controller)

		Label1 = tk.Label(self, text = " ")
		Label1.pack()
		Label2 = tk.Label(self, text = "C'est 6 là sont les plus connus, \n mais combien existe-t-il d'espèces au total ?", font= ("Courier",20), fg = '#00d0cb')
		Label2.pack()
		Label3 = tk.Label(self, text = " ")
		Label3.pack()

		code = tk.PhotoImage(file='images/codebinaire.png')
		Label4 = tk.Label(self, image = code)
		Label4.image = code
		Label4.pack()
		Label5 = tk.Label(self, text = " ")
		Label5.pack()

		Bouton1  = tk.Button(self, text = 'Table binaire',font= ("Courier",10), command = lambda : self.table(), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()
		Label6 = tk.Label(self, text = " ")
		Label6.pack()

		Label7 = tk.Label(self, text = "Petit indice : 00100000 correspond à un espace",  font= ("Courier",10))
		Label7.pack()
		Label8 = tk.Label(self, text = " ")
		Label8.pack()

		self.Saisie = tk.Entry(self, textvariable="binaire",font= ("Courier",10))
		self.Saisie.pack()
		Label9 = tk.Label(self, text = " ")
		Label9.pack()
		Bouton2  = tk.Button(self, text = 'Valider',font= ("Courier",10), command = lambda : self.test(controller), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton2.pack()

	def table(self):
		self.popup = tk.Toplevel(self)
		Page.list_of_tops.append(self.popup)
		self.popup.configure(bg = '#717171')

		alpha = tk.PhotoImage(file='images/tablebinaire.png')
		Label1 = tk.Label(self.popup, image = alpha)
		Label1.image = alpha
		Label1.pack()

		Bouton1 = tk.Button(self.popup, text = 'Fermer',font= ("Courier",10), command = lambda : self.popup.destroy(), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()

	def test(self, controller):
		if self.Saisie.get() == '529 especes':
			self.destroy_all()
			self.especes()
			controller.show_frame("MenuFinal")
		else :
			self.wrong()
			self.Saisie.delete(0,40)

	def wrong(self):
		self.destroy_all()
		
		self.popup = tk.Toplevel(self)
		Page.list_of_tops.append(self.popup)
		self.popup.configure(bg = '#717171')

		Label1 = tk.Label(self.popup, text = " ",bg = '#717171')
		Label1.pack()
		Label2 = tk.Label(self.popup, text = "Réessayer", font= ("Courier",12), fg = 'white',bg = '#717171')
		Label2.pack()
		Label3 = tk.Label(self.popup, text = " ",bg = '#717171')
		Label3.pack()

		Bouton1 = tk.Button(self.popup, text = 'Retour à la saisie',font= ("Courier",10), command = lambda : self.popup.destroy(), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()

	def especes(self):
		self.popup = tk.Toplevel(self)
		Page.list_of_tops.append(self.popup)
		self.popup.configure(bg = '#717171')

		alpha = tk.PhotoImage(file='images/529requins.png')
		Label1 = tk.Label(self.popup, image = alpha)
		Label1.image = alpha
		Label1.pack()

		Label2 = tk.Label(self.popup, text = "Bien joué, vous avez trouvé la réponse ! \n\n Le saviez-vous ? \n",font= ("Courier",15),fg = 'white',bg = '#717171')
		Label2.pack()

		Label3 = tk.Label(self.popup,wraplength = 600, font= ("Courier",12), fg = 'white', bg = '#717171', text = " Il y a en tout 529 espèces répertoriées en 2014.\n On en compte environ une cinquantaine d'espèces en Méditerranée, et une centaine dans l'Atlantique!")
		Label3.pack()
		Label4 = tk.Label(self.popup, text = " ",bg = '#717171')
		Label4.pack()

		Bouton1 = tk.Button(self.popup, text = 'Suivant',font= ("Courier",10),command = lambda : self.popup.destroy(), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()
