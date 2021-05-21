import tkinter as tk 
from PIL import Image, ImageTk

from pages import *
import app as a

class Enigme3(Page):

	def __init__(self, parent, controller):
		
		Page.__init__(self, parent, controller)

		## Canva et Scrollbar
		scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
		scrollbar.grid(row=0, column=1, sticky='ns')
		
		canva = tk.Canvas(self, yscrollcommand=scrollbar.set, width = controller.W-20, height = controller.H)
		canva.grid(row=0, column=0, sticky='nswe')
		
		scrollbar.config(command=canva.yview)

		## Le Frame, dans le Canvas, mais sans pack ou grid
		frame = tk.Frame(canva, width = controller.W-20, height = 400)
		frame.pack_propagate(False)

		Label1 = tk.Label(frame, text = "\nC'est parti ! \n Classez ces espèces par nombre de morts humaines par an\n", font= ("Courier",20), fg = '#00d0cb')
		Label1.pack()

		cadre0=tk.Frame(frame)
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

		Label4 = tk.Label(frame, text= " ")
		Label4.pack()
		cadre1=tk.Frame(frame)
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
		
		Label2 = tk.Label(frame,font= ("Courier",10), text = "- meurtrière <------                 ------> + meurtrière\n")
		Label2.pack()
		Label3 = tk.Label(frame, font= ("Courier",10), text = "NB : il faut entrer le nom des animaux dans les différentes cases\n")
		Label3.pack()
		Bouton0  = tk.Button(frame, text = 'Valider',font= ("Courier",10), command = lambda : self.test(controller), bg = '#00d0cb', activebackground = '#00d0cb')
		Bouton0.pack()

		## MAJ de la frame
		frame.update() 

		## Ajout du frame au canva
		canva.create_window(0, 0, anchor=tk.NW, window=frame)

		## La scrollregion est la boite englobante pour tout ce qu'il y a dans le Canvas
		canva.configure(scrollregion=canva.bbox(tk.ALL))

	def test(self, controller):

		if self.Saisie1.get() == 'requin':
			self.Saisie1.configure(state = 'disabled')	
		else :
			self.wrong()
			self.Saisie1.delete(0,40)
		
		if self.Saisie2.get() == 'éléphant':
			self.Saisie2.configure(state = 'disabled')	
		else :
			self.wrong()
			self.Saisie2.delete(0,40)

		if self.Saisie3.get() == 'hippopotame':
			self.Saisie3.configure(state = 'disabled')	
		else :
			self.wrong()
			self.Saisie3.delete(0,40)

		if self.Saisie4.get() == 'chien' :
			self.Saisie4.configure(state = 'disabled')	
		else :
			self.wrong()
			self.Saisie4.delete(0,40)

		if self.Saisie5.get() == 'serpent':
			self.Saisie5.configure(state = 'disabled')	
		else :
			self.wrong()
			self.Saisie5.delete(0,40)	

		if (self.Saisie1.get() == 'requin' and self.Saisie2.get() == 'éléphant' and self.Saisie3.get() == 'hippopotame' and self.Saisie4.get() == 'chien' and self.Saisie5.get() == 'serpent'):
			self.destroy_all()
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

		Label1 = tk.Label(self.popup, text = "\nVeuillez réessayer\n", font= ("Courier",12), fg = 'white',bg = '#717171')
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

		Label3 = tk.Label(self.popup,font= ("Courier",12),fg = 'white',bg = '#717171', wraplength = 1000, text = "Dans notre classement, la première place est occupée par le serpent avec 40.000 morts par an.")
		Label3.pack()
		Label4 = tk.Label(self.popup, font= ("Courier",12),fg = 'white',bg = '#717171', wraplength = 1000, text = "La seconde place revient au meilleur ami de l'homme, avec 25.000 maîtres tués.")
		Label4.pack()
		Label5 = tk.Label(self.popup,font= ("Courier",12),fg = 'white',bg = '#717171', wraplength = 1000, text = "Vient ensuite l'hippopotame, avec 500 morts par an.")
		Label5.pack()
		Label6 = tk.Label(self.popup,font= ("Courier",12),fg = 'white',bg = '#717171', wraplength = 1000, text = "En quatrième place, nous avons l'éléphant avec 100 morts par an.")
		Label6.pack()
		Label7 = tk.Label(self.popup,font= ("Courier",12),fg = 'white',bg = '#717171', wraplength = 1000, text = "Et la dernière place revient à notre espèce favorite : les requins, avec seulement une dizaine de morts par an.\nCela vous surprend ? Les requins sont énormément diabolisés dans les films et médias, alors que statistiquement ils sont moins meurtriers que votre animal de compagnie.\n")
		Label7.pack()

		Bouton1 = tk.Button(self.popup,font= ("Courier",10),bg = '#00d0cb', wraplength = 700, text = 'Suivant', command = lambda : self.popup.destroy(), activebackground = '#00d0cb')
		Bouton1.pack()
