import tkinter as tk 
from PIL import Image, ImageTk

from pages import *
import app as a

class Enigme4(Page):

	def __init__(self, parent, controller):
		
		Page.__init__(self, parent, controller)

		Label1 = tk.Label(self, text= " ")
		Label1.pack()
		Label2 = tk.Label(self, text = "Connaissez-vous ces requins ?", font= ("Courier",20), fg = '#00d0cb')
		Label2.pack()
		Label3 = tk.Label(self,font= ("Courier",12), text = "Saurez-vous trouver comment s'appellent ces requins ?")
		Label3.pack()
		Label4 = tk.Label(self, text= " ")
		Label4.pack()

		cadre0=tk.Frame(self)
		cadre0.pack()
		Label1 = tk.Label(cadre0, text = "requin blanc ",font= ("Courier",10))
		Label1.pack(side = 'left')
		Label2 = tk.Label(cadre0, text = " requin roussette ",font= ("Courier",10))
		Label2.pack(side = 'left')
		Label3 = tk.Label(cadre0, text = " requin baleine ",font= ("Courier",10))
		Label3.pack(side = 'left')
		Label4 = tk.Label(cadre0, text = " requin tigre ",font= ("Courier",10))
		Label4.pack(side = 'left')
		Label5 = tk.Label(cadre0, text = " requin renard",font= ("Courier",10))
		Label5.pack(side = 'left')
		Label6 = tk.Label(cadre0, text = " requin marteau",font= ("Courier",10))
		Label6.pack(side = 'left')
		Label5 = tk.Label(self, text= " ")
		Label5.pack()

		cadre1=tk.Frame(self)
		cadre1.pack()
		requin1 = tk.PhotoImage(file='images/requinbaleine.png')
		Label1 = tk.Label(cadre1, image = requin1)
		Label1.image = requin1
		Label1.pack(side = 'left')
		self.Saisie1 = tk.Entry(cadre1, textvariable="requin1",font= ("Courier",10))
		self.Saisie1.pack(side = 'left')
		requin2 = tk.PhotoImage(file='images/roussette.png')
		Label1 = tk.Label(cadre1, image = requin2)
		Label1.image = requin2
		Label1.pack(side = 'left')
		self.Saisie2 = tk.Entry(cadre1, textvariable="requin2",font= ("Courier",10))
		self.Saisie2.pack(side = 'left')

		cadre2=tk.Frame(self)
		cadre2.pack()
		requin3 = tk.PhotoImage(file='images/requintigre.png')
		Label1 = tk.Label(cadre2, image = requin3)
		Label1.image = requin3
		Label1.pack(side = 'left')
		self.Saisie3 = tk.Entry(cadre2, textvariable="requin3",font= ("Courier",10))
		self.Saisie3.pack(side = 'left')
		requin4 = tk.PhotoImage(file='images/requinblanc2.png')
		Label1 = tk.Label(cadre2, image = requin4)
		Label1.image = requin4
		Label1.pack(side = 'left')
		self.Saisie4 = tk.Entry(cadre2, textvariable="requin4",font= ("Courier",10))
		self.Saisie4.pack(side = 'left')

		cadre3=tk.Frame(self)
		cadre3.pack()
		requin5 = tk.PhotoImage(file='images/requinmarteau.png')
		Label1 = tk.Label(cadre3, image = requin5)
		Label1.image = requin5
		Label1.pack(side = 'left')
		self.Saisie5 = tk.Entry(cadre3, textvariable="requin5",font= ("Courier",10))
		self.Saisie5.pack(side = 'left')
		requin6 = tk.PhotoImage(file='images/requinrenard.png')
		Label1 = tk.Label(cadre3, image = requin6)
		Label1.image = requin6
		Label1.pack(side = 'left')
		self.Saisie6 = tk.Entry(cadre3, textvariable="requin6",font= ("Courier",10))
		self.Saisie6.pack(side = 'left')

		Label6 = tk.Label(self, text= " ")
		Label6.pack()
		Label7 = tk.Label(self, font= ("Courier",10), text = "NB : il faut entrer le nom des animaux dans les différentes cases")
		Label7.pack()
		Label8 = tk.Label(self, text= " ")
		Label8.pack()
		Bouton0  = tk.Button(self, text = 'Valider',font= ("Courier",10), command = lambda : self.test(controller), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton0.pack()

	def test(self, controller):

		if self.Saisie1.get() == 'requin baleine':
			self.Saisie1.configure(state = 'disabled')	
		else :
			self.wrong()
			self.Saisie1.delete(0,40)
		
		if self.Saisie2.get() == 'requin roussette':
			self.Saisie2.configure(state = 'disabled')	
		else :
			self.wrong()
			self.Saisie2.delete(0,40)

		if self.Saisie3.get() == 'requin tigre':
			self.Saisie3.configure(state = 'disabled')	
		else :
			self.wrong()
			self.Saisie3.delete(0,40)

		if self.Saisie4.get() == 'requin blanc':
			self.Saisie4.configure(state = 'disabled')	
		else :
			self.wrong()
			self.Saisie4.delete(0,40)

		if self.Saisie5.get() == 'requin marteau':
			self.Saisie5.configure(state = 'disabled')	
		else :
			self.wrong()
			self.Saisie5.delete(0,40)	

		if self.Saisie6.get() == 'requin renard':
			self.Saisie6.configure(state = 'disabled')	
		else :
			self.wrong()
			self.Saisie5.delete(0,40)

		if (self.Saisie1.get() == 'requin baleine' and self.Saisie2.get() == 'requin roussette' and self.Saisie3.get() == 'requin tigre' and self.Saisie4.get() == 'requin blanc' and self.Saisie5.get() == 'requin marteau' and self.Saisie6.get() == 'requin renard'):
			self.destroy_all()
			self.especesrequin()
			controller.show_frame("Enigme5")
		else :
			self.wrong()
			self.Saisie1.delete(0,40)

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

	def especesrequin(self):
		self.popup = tk.Toplevel(self)
		Page.list_of_tops.append(self.popup)
		self.popup.configure(bg = '#717171')

		alpha = tk.PhotoImage(file='images/especesrequin.png')
		Label1 = tk.Label(self.popup, image = alpha)
		Label1.image = alpha
		Label1.pack()

		Label2 = tk.Label(self.popup,font= ("Courier",15),fg = 'white',bg = '#717171', text = "Bravo, vous avez un minimum de connaissances en zoologie ! \n\n Le saviez-vous ? \n")
		Label2.pack()

		Label3 = tk.Label(self.popup,font= ("Courier",12),fg = 'white',bg = '#717171', wraplength = 700, text = "Il existe d'autres espèces que le grand requin blanc (eh oui): elles se différencient suivant dertains critères, comme la taille pour le requin baleine, la couleur de peau pour le requin tigre, ou encore leur situation géograpghique comme la roussette, que l'on peut trouver dans la rade de Brest.")
		Label3.pack()
		Label4 = tk.Label(self.popup, text= " ",bg = '#717171')
		Label4.pack()
		Bouton1 = tk.Button(self.popup,font= ("Courier",10),bg = '#00d0cb', wraplength = 700, text = 'Suivant', command = lambda : self.popup.destroy(), activebackground = '#00d0cb')
		Bouton1.pack()