import tkinter as tk 
from PIL import Image, ImageTk

from pages import *
import app as a

class Enigme7(Page):

	def __init__(self, parent, controller):
		
		Page.__init__(self, parent, controller)

		## Canva et Scrollbar
		scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
		scrollbar.grid(row=0, column=1, sticky='ns')
		
		canva = tk.Canvas(self, yscrollcommand=scrollbar.set, width = controller.W-20, height = controller.H)
		canva.grid(row=0, column=0, sticky='nswe')
		
		scrollbar.config(command=canva.yview)

		## Le Frame, dans le Canvas, mais sans pack ou grid
		frame = tk.Frame(canva, width = controller.W-20, height = controller.H)
		frame.pack_propagate(False)

		Label1 = tk.Label(frame, text = "\nComme dit précédemment le requin a une énorme machoire ! \n Mais combien de dents peut-il perdre au cours de sa vie ?\n",  font= ("Courier",20), fg = '#00d0cb')
		Label1.pack()

		code = tk.PhotoImage(file='images/codecrypte.png')
		Label2 = tk.Label(frame, image = code)
		Label2.image = code
		Label2.pack()
		Label3 = tk.Label(frame, text= " ")
		Label3.pack()

		Bouton1  = tk.Button(frame, text = 'Alphabet',font= ("Courier",10), command = lambda : self.alphabet(), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()
		Label4 = tk.Label(frame, text= " ")
		Label4.pack()

		self.Saisie = tk.Entry(frame, textvariable="crypte",font= ("Courier",10))
		self.Saisie.pack()
		Label5 = tk.Label(frame, text= " ")
		Label5.pack()
		Bouton2  = tk.Button(frame, text = 'Valider',font= ("Courier",10), command = lambda : self.test(controller), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton2.pack()

		Label6 = tk.Label(frame, font= ("Courier",10), text = "\nNB : si nécessaire vous pouvez ajouter un espace\n")
		Label6.pack()

		## MAJ de la frame
		frame.update() 

		## Ajout du frame au canva
		canva.create_window(0, 0, anchor=tk.NW, window=frame)

		## La scrollregion est la boite englobante pour tout ce qu'il y a dans le Canvas
		canva.configure(scrollregion=canva.bbox(tk.ALL))

	def test(self, controller):
		if self.Saisie.get() == 'trente mille':
			self.destroy_all()
			self.dents()
			controller.show_frame("MenuFinal")
		else :
			self.wrong()
			self.Saisie.delete(0,40)      

	def alphabet(self):
		self.popup = tk.Toplevel(self)
		Page.list_of_tops.append(self.popup)
		self.popup.configure(bg = '#717171')

		alpha = tk.PhotoImage(file='images/alphacrypte.png')
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

	def dents(self):
		self.popup = tk.Toplevel(self)
		Page.list_of_tops.append(self.popup)
		self.popup.configure(bg = '#717171')

		alpha = tk.PhotoImage(file='images/dents.png')
		Label1 = tk.Label(self.popup, image = alpha)
		Label1.image = alpha
		Label1.pack()

		Label2 = tk.Label(self.popup, text = "Bien joué, vous avez trouvé la réponse ! \n\n Le saviez-vous ? \n",font= ("Courier",15),fg = 'white',bg = '#717171')
		Label2.pack()

		Label3 = tk.Label(self.popup,wraplength = 600, font= ("Courier",12), fg = 'white', bg = '#717171', text = "Les requins ont plusieurs rangées de dents qui se renouvellent régulièrement au cours leur vie. Ainsi certains individus en perdent plus de 30.000 dans leur vie.\n")
		Label3.pack()
		Bouton1 = tk.Button(self.popup, text = 'Suivant',font= ("Courier",10),command = lambda : self.popup.destroy(), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()