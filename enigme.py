import tkinter as tk 
from PIL import Image, ImageTk

from page import *
from timer import *
import app as a

class Enigme1(Page):

	def __init__(self, parent, controller):
		
		Page.__init__(self, parent, controller)

		Label1 = tk.Label(self, text = "C'est parti ! \n Décodez ceci pour continuer",  font= ("Courier",20), fg = '#00d0cb')
		Label1.pack()

		code = tk.PhotoImage(file='images/codemorse.png')
		Label2 = tk.Label(self, image = code)
		Label2.image = code
		Label2.pack()

		Bouton1  = tk.Button(self, text = 'Alphabet',font= ("Courier",10), command = lambda : self.alphabet(), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()

		self.Saisie = tk.Entry(self, textvariable="bla",font= ("Courier",10))
		self.Saisie.pack()
		Bouton2  = tk.Button(self, text = 'Valider',font= ("Courier",10), command = lambda : self.test(controller), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton2.pack()


	def test(self, controller):
		if self.Saisie.get() == 'requin blanc':
			self.destroy_all()
			self.requin_blanc()
			controller.show_frame("Enigme2")
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

		Bouton1 = tk.Button(self.popup, text = 'Quitter',font= ("Courier",10), command = lambda : self.popup.destroy(), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()

	def wrong(self):
		self.destroy_all()
		
		self.popup = tk.Toplevel(self)
		Page.list_of_tops.append(self.popup)
		self.popup.configure(bg = '#717171')

		Label1 = tk.Label(self.popup, text = "Réessayer", font= ("Courier",12), fg = 'white',bg = '#717171')
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

		Label3 = tk.Label(self.popup,wraplength = 600, font= ("Courier",12), fg = 'white', bg = '#717171', text = " Rendu célèbre grâce aux Dents de la Mer de Spielberg, le requin blanc est l'une des espèces les plus imposantes de requins. Le dos gris et le ventre blanc, il peut atteindre jusqu'à 5m de longueur à l'âge adulte, et peut vivre pendant 40 ans ! ")
		Label3.pack()

		Bouton1 = tk.Button(self.popup, text = 'Suivant',font= ("Courier",10),command = lambda : self.popup.destroy(), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()


class Enigme2(Page):

	def __init__(self, parent, controller):
		
		Page.__init__(self, parent, controller)

		Label1 = tk.Label(self, text = "C'est parti !", font= ("Courier",20), fg = '#00d0cb')
		Label1.pack()
		Label2 = tk.Label(self, text = "Trouvez le code", font= ("Courier",20), fg = '#00d0cb')
		Label2.pack()

		self.Saisie = tk.Entry(self, textvariable="bl",font= ("Courier",10))
		self.Saisie.pack()
		Bouton0  = tk.Button(self, text = 'Valider',font= ("Courier",10), command = lambda : self.test(controller), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton0.pack()

		cadre0=tk.Frame(self)
		cadre0.pack()
		Bouton1 = tk.Button(cadre0,font= ("Courier",10), text = 'Indice 1', command = lambda : self.indice(0), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack(side = 'left')
		Bouton2 = tk.Button(cadre0,font= ("Courier",10), text = 'Indice 2', command = lambda : self.indice(1), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton2.pack(side = 'left')
		Bouton3 = tk.Button(cadre0,font= ("Courier",10), text = 'Indice 3', command = lambda : self.indice(2), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton3.pack(side = 'left')

		cadre1=tk.Frame(self)
		cadre1.pack()
		Bouton4 = tk.Button(cadre1,font= ("Courier",10), text = 'Indice 4', command = lambda : self.indice(3), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton4.pack(side = 'left')
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

		Bouton1 = tk.Button(self.popup, text = 'Quitter',font= ("Courier",10), command = lambda : self.popup.destroy(), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()

	def wrong(self):
		self.destroy_all()
		
		self.popup = tk.Toplevel(self)
		Page.list_of_tops.append(self.popup)
		self.popup.configure(bg = '#717171')

		Label1 = tk.Label(self.popup, text = "Réessayer", font= ("Courier",12), fg = 'white',bg = '#717171')
		Label1.pack()

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

		Label3 = tk.Label(self.popup,font= ("Courier",12),fg = 'white',bg = '#717171', wraplength = 700, text = "Le mot Squale est un terme qui englobe l'ensemble des espèces de requins avec des caractéristiques communes, comme la dentition, la texture de la peau ou la silhouette fuselée. ")
		Label3.pack()

		Bouton1 = tk.Button(self.popup, text = 'Suivant',font= ("Courier",10), command = lambda : self.popup.destroy(), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()

class Enigme3(Page):

	def __init__(self, parent, controller):
		
		Page.__init__(self, parent, controller)

		Label1 = tk.Label(self, text = "C'est parti ! \n Classez ces espèces par niveau de dangerosité", font= ("Courier",20), fg = '#00d0cb')
		Label1.pack()

		cadre0=tk.Frame(self)
		cadre0.pack()
		Label1 = tk.Label(cadre0, text = "éléphant ",font= ("Courier",10))
		Label1.pack(side = 'left')
		Label2 = tk.Label(cadre0, text = " chien ",font= ("Courier",10))
		Label2.pack(side = 'left')
		Label3 = tk.Label(cadre0, text = " requin ",font= ("Courier",10))
		Label3.pack(side = 'left')
		Label4 = tk.Label(cadre0, text = " hippopotame ",font= ("Courier",10))
		Label4.pack(side = 'left')
		Label5 = tk.Label(cadre0, text = " serpent",font= ("Courier",10))
		Label5.pack(side = 'left')

		cadre1=tk.Frame(self)
		cadre1.pack()
		self.Saisie1 = tk.Entry(cadre1, textvariable="1",font= ("Courier",10))
		self.Saisie1.pack(side = 'left')
		self.Saisie2 = tk.Entry(cadre1, textvariable="2",font= ("Courier",10))
		self.Saisie2.pack(side = 'left')
		self.Saisie3 = tk.Entry(cadre1, textvariable="3",font= ("Courier",10))
		self.Saisie3.pack(side = 'left')
		self.Saisie4 = tk.Entry(cadre1, textvariable="4",font= ("Courier",10))
		self.Saisie4.pack(side = 'left')
		self.Saisie5 = tk.Entry(cadre1, textvariable="5",font= ("Courier",10))
		self.Saisie5.pack(side = 'left')
		
		Label1 = tk.Label(self,font= ("Courier",10), text = "+ dangereux <------                 ------> - dangereux")
		Label1.pack()
		Label2 = tk.Label(self, font= ("Courier",10), text = "NB : il faut entrer le nom des animaux dans les différentes cases")
		Label2.pack()

		Bouton0  = tk.Button(self, text = 'Valider',font= ("Courier",10), command = lambda : self.test(controller), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton0.pack()

	def test(self, controller):

		if self.Saisie1.get() == 'serpent':
			self.Saisie1.configure(state = 'disabled')	
		else :
			self.wrong()
			self.Saisie1.delete(0,40)
		
		if self.Saisie2.get() == 'chien':
			self.Saisie2.configure(state = 'disabled')	
		else :
			self.wrong()
			self.Saisie2.delete(0,40)

		if self.Saisie3.get() == 'hippopotame':
			self.Saisie3.configure(state = 'disabled')	
		else :
			self.wrong()
			self.Saisie3.delete(0,40)

		if self.Saisie4.get() == 'éléphant':
			self.Saisie4.configure(state = 'disabled')	
		else :
			self.wrong()
			self.Saisie4.delete(0,40)

		if self.Saisie5.get() == 'requin':
			self.Saisie5.configure(state = 'disabled')	
		else :
			self.wrong()
			self.Saisie5.delete(0,40)	

		if (self.Saisie1.get() == 'serpent' and self.Saisie2.get() == 'chien' and self.Saisie3.get() == 'hippopotame' and self.Saisie4.get() == 'éléphant' and self.Saisie5.get() == 'requin'):
			self.destroy_all()
			Timer.time = Timer.get_time(a.App)
			self.danger()
			controller.show_frame("Enigme4")
		else :
			self.wrong()
			self.Saisie1.delete(0,40)

	def wrong(self):
		self.destroy_all()
		
		self.popup = tk.Toplevel(self)
		Page.list_of_tops.append(self.popup)
		self.popup.configure(bg = '#717171')

		Label1 = tk.Label(self.popup, text = "Réessayer", font= ("Courier",12), fg = 'white',bg = '#717171')
		Label1.pack()

		Bouton1 = tk.Button(self.popup, text = 'Retour à la saisie',font= ("Courier",10), command = lambda : self.popup.destroy(), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton1.pack()

	def danger(self):
		self.popup = tk.Toplevel(self)
		Page.list_of_tops.append(self.popup)
		self.popup.configure(bg = '#717171')

		alpha = tk.PhotoImage(file='images/danger.png')
		Label1 = tk.Label(self.popup, image = alpha)
		Label1.image = alpha
		Label1.pack()

		Label2 = tk.Label(self.popup,font= ("Courier",15),fg = 'white',bg = '#717171', text = "Bien joué, vous avez trouvé le bon ordre ! \n\n Le saviez-vous ? \n")
		Label2.pack()

		Label3 = tk.Label(self.popup,font= ("Courier",12),fg = 'white',bg = '#717171', wraplength = 700, text = "Dans notre classement, la première place est occupée par le serpent avec 40.000 morts par an.")
		Label3.pack()
		Label4 = tk.Label(self.popup, font= ("Courier",12),fg = 'white',bg = '#717171', wraplength = 700, text = "La seconde place revient au meilleur ami de l'homme, avec 25.000 maîtres tués.")
		Label4.pack()
		Label5 = tk.Label(self.popup,font= ("Courier",12),fg = 'white',bg = '#717171', wraplength = 700, text = "Vient ensuite l'hippopotame, avec 500 morts par an.")
		Label5.pack()
		Label6 = tk.Label(self.popup,font= ("Courier",12),fg = 'white',bg = '#717171', wraplength = 700, text = "en quatrième place, nous avons l'éléphant avec 100 morts par an.")
		Label6.pack()
		Label7 = tk.Label(self.popup,font= ("Courier",12),fg = 'white',bg = '#717171', wraplength = 700, text = "Et la dernière place revient à notre espèce favorite : les requins, avec seulement une dizaine de morts par an.\nCela vous surprend? Les requins sont énormément diabolisés dans les films et médias, alors que statistiquement il sont moins dangereux que votre animal de compagnie.")
		Label7.pack()

		Bouton1 = tk.Button(self.popup,font= ("Courier",10),bg = '#00d0cb', wraplength = 700, text = 'Suivant', command = lambda : self.popup.destroy(), activebackground = '#00d0cb')
		Bouton1.pack()

class Enigme4(Page):

	def __init__(self, parent, controller):
		
		Page.__init__(self, parent, controller)

		Label1 = tk.Label(self, text = "Connaissez-vous ces requins ?", font= ("Courier",20), fg = '#00d0cb')
		Label1.pack()
		Label2 = tk.Label(self,font= ("Courier",12), text = "Saurez-vous trouver comment s'appellent ces requins ?")
		Label2.pack()

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
		Label5 = tk.Label(cadre0, text = " requin marteau",font= ("Courier",10))
		Label5.pack(side = 'left')
		Label6 = tk.Label(cadre0, text = " requin marteau",font= ("Courier",10))
		Label6.pack(side = 'left')

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
		self.Saisie1 = tk.Entry(cadre1, textvariable="requin2",font= ("Courier",10))
		self.Saisie1.pack(side = 'left')

		cadre2=tk.Frame(self)
		cadre2.pack()
		requin3 = tk.PhotoImage(file='images/requintigre.png')
		Label1 = tk.Label(cadre2, image = requin3)
		Label1.image = requin3
		Label1.pack(side = 'left')
		self.Saisie1 = tk.Entry(cadre2, textvariable="requin3",font= ("Courier",10))
		self.Saisie1.pack(side = 'left')
		requin4 = tk.PhotoImage(file='images/requinblanc2.png')
		Label1 = tk.Label(cadre2, image = requin4)
		Label1.image = requin4
		Label1.pack(side = 'left')
		self.Saisie1 = tk.Entry(cadre2, textvariable="requin4",font= ("Courier",10))
		self.Saisie1.pack(side = 'left')

		cadre3=tk.Frame(self)
		cadre3.pack()
		requin5 = tk.PhotoImage(file='images/requinmarteau.png')
		Label1 = tk.Label(cadre3, image = requin5)
		Label1.image = requin5
		Label1.pack(side = 'left')
		self.Saisie1 = tk.Entry(cadre3, textvariable="requin5",font= ("Courier",10))
		self.Saisie1.pack(side = 'left')
		requin6 = tk.PhotoImage(file='images/requinrenard.png')
		Label1 = tk.Label(cadre3, image = requin6)
		Label1.image = requin6
		Label1.pack(side = 'left')
		self.Saisie1 = tk.Entry(cadre3, textvariable="requin6",font= ("Courier",10))
		self.Saisie1.pack(side = 'left')

		Label3 = tk.Label(self, font= ("Courier",10), text = "NB : il faut entrer le nom des animaux dans les différentes cases")
		Label3.pack()

		Bouton0  = tk.Button(self, text = 'Valider',font= ("Courier",10), command = lambda : self.test(controller), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton0.pack()