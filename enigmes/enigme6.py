import tkinter as tk 
from PIL import Image, ImageTk

from pages import *
import app as a

class Enigme6(Page):

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

        self.liste_réponse = ["surpeche", "machoire", "nageoire", "caudale", "predateur", "indispensable"]
        self.liste_trouvé  = []
        self.liste_disabled = []

        Label1 = tk.Label(frame, text = "\nSaurez vous trouver 6 mots en rapport \n avec les requins dans cette grille ?\n",  font= ("Courier",20), fg = '#00d0cb')
        Label1.pack()

        motsmeles = tk.PhotoImage(file='images/motsmeles.png')
        Label2 = tk.Label(frame, image = motsmeles)
        Label2.image = motsmeles
        Label2.pack()
        Label3 = tk.Label(frame, text= " ")
        Label3.pack()

        cadre0=tk.Frame(frame)
        cadre0.pack()
        self.Saisie1 = tk.Entry(cadre0, textvariable="mot1",font= ("Courier",10))
        self.Saisie1.pack(side = 'left')
        Label1 = tk.Label(cadre0, text= " ")
        Label1.pack()
        self.Saisie2 = tk.Entry(cadre0, textvariable="mot2",font= ("Courier",10))
        self.Saisie2.pack(side = 'left')
        Label2 = tk.Label(cadre0, text= " ")
        Label2.pack()
        self.Saisie3 = tk.Entry(cadre0, textvariable="mot3",font= ("Courier",10))
        self.Saisie3.pack(side = 'left')
        Label3 = tk.Label(cadre0, text= " ")
        Label3.pack()

        cadre1=tk.Frame(frame)
        cadre1.pack()
        self.Saisie4 = tk.Entry(cadre1, textvariable="mot4",font= ("Courier",10))
        self.Saisie4.pack(side = 'left')
        Label1 = tk.Label(cadre1, text= " ")
        Label1.pack()
        self.Saisie5 = tk.Entry(cadre1, textvariable="mot5",font= ("Courier",10))
        self.Saisie5.pack(side = 'left')
        Label2 = tk.Label(cadre1, text= " ")
        Label2.pack()
        self.Saisie6 = tk.Entry(cadre1, textvariable="mot6",font= ("Courier",10))
        self.Saisie6.pack(side = 'left')

        Label4 = tk.Label(frame, text= " ")
        Label4.pack()
        Bouton2  = tk.Button(frame, text = 'Valider',font= ("Courier",10), command = lambda : self.test(controller), bg = '#00d0cb', activebackground = '#00d0cb')
        Bouton2.pack()

        ## MAJ de la frame
        frame.update() 

        ## Ajout du frame au canva
        canva.create_window(0, 0, anchor=tk.NW, window=frame)

        ## La scrollregion est la boite englobante pour tout ce qu'il y a dans le Canvas
        canva.configure(scrollregion=canva.bbox(tk.ALL))

        self.liste_saisie = [self.Saisie1, self.Saisie2, self.Saisie3, self.Saisie4, self.Saisie5, self.Saisie6]

    def test(self, controller):
        for i in range(len(self.liste_saisie)) :
            for j in range(len(self.liste_réponse)):
                if self.liste_saisie[i].get() == self.liste_réponse[j] :
                    if not (self.liste_réponse[j] in self.liste_trouvé):
                        self.liste_trouvé.append(self.liste_réponse[j])
                        self.liste_disabled.append(self.liste_saisie[i])
                        self.liste_saisie[i].configure(state = 'disabled')

        for i in range(len(self.liste_saisie)) :
            if not (self.liste_saisie[i] in self.liste_disabled) :
                self.liste_saisie[i].delete(0,40)

        if len(self.liste_trouvé) == 6:
            self.destroy_all()
            self.surpeche()
            controller.show_frame("MenuFinal")
        else :
            self.wrong()

    def wrong(self):
        self.destroy_all()

        self.popup = tk.Toplevel(self)
        Page.list_of_tops.append(self.popup)
        self.popup.configure(bg = '#717171')

        Label1 = tk.Label(self.popup, text = "\nVeuillez réessayer\n", font= ("Courier",12), fg = 'white',bg = '#717171')
        Label1.pack()

        Bouton1 = tk.Button(self.popup, text = 'Retour à la saisie',font= ("Courier",10), command = lambda : self.popup.destroy(), bg = '#00d0cb', activebackground = '#00d0cb')
        Bouton1.pack()

    def surpeche(self):
        self.popup = tk.Toplevel(self)
        Page.list_of_tops.append(self.popup)
        self.popup.configure(bg = '#717171')

        surpeche = tk.PhotoImage(file='images/surpeche.png')
        Label1 = tk.Label(self.popup, image = surpeche)
        Label1.image = surpeche
        Label1.pack()

        Label2 = tk.Label(self.popup, text = "Bien joué, vous avez trouvé la réponse ! \n\n Le saviez-vous ? \n",font= ("Courier",15),fg = 'white',bg = '#717171')
        Label2.pack()

        Label3 = tk.Label(self.popup,wraplength = 1000, font= ("Courier",12), fg = 'white', bg = '#717171', text = "Les deux particularités du requin sont sa nageoire caudale qu'il utilise pour se propulser et son énorme machoire composée de plusieurs rangées de dents tranchantes. \n Le requin est un prédateur qui se nourrit de cadavres et d'animaux malades, il est donc indispensable pour les océans car il mange les animaux faibles et régule les populations. \nIl est par contre victime de surpêche par les humains notamment pour ses ailerons. On estimme qu'il y a 100 millions d'individus tués chaque année dans le monde.\n")
        Label3.pack()

        Bouton1 = tk.Button(self.popup, text = 'Suivant',font= ("Courier",10),command = lambda : self.popup.destroy(), bg = '#00d0cb', activebackground = '#00d0cb')
        Bouton1.pack()