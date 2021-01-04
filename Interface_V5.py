from tkinter import *
import tkinter as tk

class Interface(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)  # constructeur de la classe parente
        self.Menu() #appel de la methode "BarredeMenu"
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry("%dx%d" % (w, h))  # Redimensionne la fenetre
        self.Etape1_Vols() #appel la première fenetre à s'afficher

    def Menu(self): #Methode de la barre de menu
        self.label_frame1 = LabelFrame(self, text="menu", width=200, height=110)  # label_frame pour encadrer les bouton menu en haut à gauche
        self.label_frame1.place(relx=0.01, rely=0.02)

        self.frame1 = Frame(self.label_frame1)
        self.frame1.place(relx=0, rely=0)

        self.frame2 = Frame(self.label_frame1)
        self.frame2.place(relx=0, rely=0.77, width=175)

        self.photo = PhotoImage(file='icon_reglage.gif')  # boutton reglage avec icone contenu dans le label_frame menu
        self.boutton_reglage = Button(self.frame1, image=self.photo, command= self.bouttonparam)
        self.boutton_reglage.photo = self.photo
        self.boutton_reglage.pack(side=LEFT)

        self.text_reglage = Label(self.frame2, text="Réglages")  # texte en dessous du bouton reglage avec écrit réglage
        self.text_reglage.pack(side=LEFT)

        self.photo3 = PhotoImage(file='icon_vols.gif')  # boutton vols avec icone contenu dans le label_frame menu
        self.boutton_vols = Button(self.frame1, image=self.photo3, command= self.bouttonvol)
        self.boutton_vols.photo = self.photo3
        self.boutton_vols.pack(side=RIGHT)

        self.text_vols = Label(self.frame2, text="Vols")  # texte en dessous du bouton vols avec écrit vols
        self.text_vols.pack(side=RIGHT)

        self.photo2 = PhotoImage(file='icon_mission.gif')  # boutton mission avec icone contenu dans le label_frame menu
        self.boutton_mission = Button(self.frame1, image=self.photo2, command= self.bouttonmission)
        self.boutton_mission.photo = self.photo2
        self.boutton_mission.pack()

        self.text_mission = Label(self.frame2, text="Missions")  # texte en dessous du bouton missions avec écrit missions
        self.text_mission.pack()

    def bouttonparam(self): #Methode présente pour supprimer les widgets de Etape1_Vols et afficher ceux de Etape2_parametre
        for i in self.winfo_children():
            i.destroy()

        self.Menu()
        self.Etape2_parametre()

    def bouttonvol(self): #Methode présente pour supprimer les widgets de Etape2_parametre  et afficher ceux de Etape1_Vols
        for i in self.winfo_children():
            i.destroy()

        self.Menu()
        self.Etape1_Vols()

    def bouttonmission(self):
        for i in self.winfo_children():
            i.destroy()

        self.Menu()
        self.Etape3_Mission()

    def Etape1_Vols(self): #Methode comprenant les widgets de la première fenetre
        self.vols_text_label = Label(self, text="Pas de mission en cours", fg="black", font=("Arial_black", 16), bg="#dbdadb", relief=SUNKEN, width = 55, height = 2) #Label "pas de mission en cours"
        self.vols_text_label.place(relx= 0.305, rely=0.15)

        self.vols_label_frame2 = LabelFrame(self, text="Missions programmées", width=870, height=500, borderwidth=3) #Label_frame contenant les missions programmées
        self.vols_label_frame2.place(relx= 0.25, rely= 0.25)

    def Etape2_parametre(self): #Methode comprenant les widgets de l'étape 2 du doc spe fonctionelles
        self.param_label_frame = LabelFrame(self, text = "Réglages", font=("Arial_black", 12), width = 870, height=500, borderwidth=3)
        self.param_label_frame.place(relx= 0.25, rely= 0.25)

        self.param_label_frame2 = LabelFrame(self.param_label_frame, text = "Liste des utilisateurs", font=("Arial_black", 12), bg = "#a4a1a3", width= 350, height= 200, borderwidth=3 )
        self.param_label_frame2.place(relx= 0.05, rely= 0.08)

        self.param_boutton_utilisateur = Button(self.param_label_frame, text="Ajouter un utilisateur", font=("Arial_black", 16), bg= "#ffffff", width= 20, height= 2, command=self.BouttonAjouterUtilisateur)
        self.param_boutton_utilisateur.place(relx= 0.6, rely= 0.25)

        self.param_label_frame3 = LabelFrame(self.param_label_frame, text="Utilisateur selectionné:", font=("Arial_black", 12), width= 500, height= 200, borderwidth=3)
        self.param_label_frame3.place(relx= 0.23, rely= 0.53)

    def BouttonAjouterUtilisateur(self): #Methode présente pour supprimer les widgets de Etape2_parametre et afficher ceux de ParamAjouterUtilisateur
        for i in self.winfo_children():
            i.destroy()

        self.Menu()
        self.ParamAjouterUtilisateur()

    def ParamAjouterUtilisateur(self): # Mehtode comprenant les widgets de l'etape 2 du doc spe fonctionnelles si la personne clique sur "Ajouter un utilisateur"
        self.pau_label_frame = LabelFrame(self, text = "Utilisateur n°", font=("Arial_black", 12), width = 870, height=600, borderwidth=3)
        self.pau_label_frame.place(relx=0.25, rely=0.2)

        self.pau_text_frame2 = Label(self.pau_label_frame, text="Informations personnelles", font=("Arial_black", 12))
        self.pau_text_frame2.place(relx=0.05, rely=0.025)
        self.pau_label_frame2 = LabelFrame(self.pau_label_frame, width=350, height=200, bg="#a4a1a3",relief=SUNKEN)
        self.pau_label_frame2.place(relx=0.05, rely=0.08)

        self.pau_text_prenom = Label(self.pau_label_frame2, text="Prénom", font=("Arail", 14, "bold"), bg="#a4a1a3")
        self.pau_text_prenom.place(relx=0.1, rely=0.1)
        self.pau_text_nom = Label(self.pau_label_frame2, text = "Nom", font=("Arail", 14, "bold"), bg="#a4a1a3")
        self.pau_text_nom.place(relx=0.1, rely=0.4)
        self.pau_text_mail = Label(self.pau_label_frame2, text="Email", font=("Arail", 14, "bold"), bg="#a4a1a3")
        self.pau_text_mail.place(relx=0.1, rely=0.75)

        self.pau_entry_prenom = Entry(self.pau_label_frame2, width=30)
        self.pau_entry_prenom.place(relx=0.35, rely=0.12)
        self.pau_entry_nom =Entry(self.pau_label_frame2, width=30)
        self.pau_entry_nom.place(relx=0.35, rely=0.42)
        self.pau_entry_mail = Entry(self.pau_label_frame2, width=30)
        self.pau_entry_mail.place(relx=0.35, rely=0.77)

        self.pau_text_frame3 = Label(self.pau_label_frame, text="Options de vols", font=("Arial_black", 12))
        self.pau_text_frame3.place(relx=0.6, rely=0.025)
        self.pau_label_frame3 = LabelFrame (self.pau_label_frame, width=300, height=200, bg="#a4a1a3", relief=SUNKEN)
        self.pau_label_frame3.place(relx=0.6, rely=0.08)

        self.pau_check_suiviedevol = Checkbutton(self.pau_label_frame3, text="Suivie de vol par mail", font=("Arail", 14, "bold"), bg="#a4a1a3")
        self.pau_check_suiviedevol.place(relx=0.1, rely=0.1)
        self.pau_check_coordonnées = Checkbutton(self.pau_label_frame3, text="Coordonnées", font=("Arail", 14), bg="#a4a1a3")
        self.pau_check_coordonnées.place(relx=0.2, rely=0.25)
        self.pau_check_altitude = Checkbutton(self.pau_label_frame3, text="Altitude", font=("Arail", 14), bg="#a4a1a3")
        self.pau_check_altitude.place(relx=0.2, rely=0.4)
        self.pau_check_vitesse = Checkbutton(self.pau_label_frame3, text="Vitesse", font=("Arail", 14), bg="#a4a1a3")
        self.pau_check_vitesse.place(relx=0.2, rely=0.55)
        self.pau_check_batterie = Checkbutton(self.pau_label_frame3, text="Charge batterie", font=("Arail", 14), bg="#a4a1a3")
        self.pau_check_batterie.place(relx=0.2, rely=0.7)
        self.pau_check_photo = Checkbutton(self.pau_label_frame3, text="Photos", font=("Arail", 14), bg="#a4a1a3")
        self.pau_check_photo.place(relx=0.2, rely=0.85)

        self.pau_text_frame4 = Label(self.pau_label_frame, text="Paramètres de vol favoris", font=("Arial_black", 12))
        self.pau_text_frame4.place(relx=0.1, rely=0.48)
        self.pau_label_frame4 = LabelFrame(self.pau_label_frame, width=700, height=200, bg="#a4a1a3", relief=SUNKEN)
        self.pau_label_frame4.place(relx=0.1, rely=0.53)

        self.pau_text_vitesse = Label(self.pau_label_frame4, text="Vitesse", font=("Arail", 14, "bold"), bg="#a4a1a3")
        self.pau_text_vitesse.place(relx=0.05, rely=0.1)
        self.pau_text_latitudebase = Label(self.pau_label_frame4, text="Latitude \n base", font=("Arail", 14, "bold"), bg="#a4a1a3")
        self.pau_text_latitudebase.place(relx=0.05, rely=0.35)
        self.pau_text_longitudebase = Label(self.pau_label_frame4, text="Longitude \n base", font=("Arail", 14, "bold"),bg="#a4a1a3")
        self.pau_text_longitudebase.place(relx=0.04, rely=0.65)
        self.pau_text_modecam = Label(self.pau_label_frame4, text="Mode caméra", font=("Arail", 14, "bold"), bg="#a4a1a3")
        self.pau_text_modecam.place(relx=0.6, rely=0.35)

        self.pau_entry_vitesse = Entry(self.pau_label_frame4, width=30)
        self.pau_entry_vitesse.place(relx=0.2, rely=0.12)
        self.pau_entry_latitudebase = Entry(self.pau_label_frame4, width=30)
        self.pau_entry_latitudebase.place(relx=0.2, rely=0.42)
        self.pau_entry_longitude = Entry(self.pau_label_frame4, width=30)
        self.pau_entry_longitude.place(relx=0.2, rely=0.72)
        self.pau_modecam_photo_check = Checkbutton(self.pau_label_frame4, text="Photo", font=("Arail", 14), bg="#a4a1a3")
        self.pau_modecam_photo_check.place(relx=0.8, rely=0.35)
        self.pau_modecam_video_check = Checkbutton(self.pau_label_frame4, text="Vidéo", font=("Arail", 14), bg="#a4a1a3")
        self.pau_modecam_video_check.place(relx=0.8, rely=0.55)

        self.pau_boutton = Button(self.pau_label_frame, text = "Enregistrer les informations", font=("Arial_black", 12), width=22, height=2, bg="#ffffff", command=lambda:[self.GetInfoUtilisateur(), self.BouttonEnregistrerInfo()])
        self.pau_boutton.place(relx=0.4, rely=0.9)

    def GetInfoUtilisateur(self):
        prenom = self.pau_entry_prenom.get()
        nom = self.pau_entry_nom.get()
        mail = self.pau_entry_mail.get()
        pauvitesse = self.pau_entry_vitesse.get()
        paulatitude = self.pau_entry_latitudebase.get()
        paulongitude = self.pau_entry_longitude.get()
        print(prenom)
        print(nom)

    def BouttonEnregistrerInfo(self):
        for i in self.winfo_children():
            i.destroy()

        self.Menu()
        self.Etape2_parametre()

    def Etape3_Mission(self):
        self.mission_frame_principale = Frame(self, width=870, height=550)
        self.mission_frame_principale.place(relx=0.25, rely=0.25)
        self.mission_listeutilisateur = Label(self.mission_frame_principale, text="Liste Utilisateurs", font=("Arial", 14, "bold"))
        self.mission_listeutilisateur.place(relx=0.15, rely=0.01)
        self.mission_frame1 = Frame(self.mission_frame_principale, width=600, height=250, bg="#a4a1a3")
        self.mission_frame1.place(relx=0.15, rely=0.06)
        self.mission_utilisateurselectionné = Label(self.mission_frame_principale, text="Utilisateur sélectionné:", font=("Arial", 14, "bold"))
        self.mission_utilisateurselectionné.place(relx=0.22, rely=0.565)
        self.mission_labelframe = LabelFrame(self.mission_frame_principale, width=500, height=200, borderwidth=3)
        self.mission_labelframe.place(relx=0.22, rely=0.62)
        self.mission_boutton1 = Button(self.mission_labelframe, text="Visualiser les missions", font=("Arial", 12, "bold"), width=42, height=2, command=self.BouttonVisualiserLesMissions)
        self.mission_boutton1.place(relx=0.07, rely=0.1)
        self.mission_boutton2 = Button(self.mission_labelframe, text="Créer une mission", font=("Arial", 12, "bold"), width=42, height=2, command=self.BouttonCreerUneMission)
        self.mission_boutton2.place(relx=0.07, rely=0.6)

    def BouttonVisualiserLesMissions(self):
        for i in self.winfo_children():
            i.destroy()

        self.Menu()
        self.VisualiserLesMissions()

    def BouttonCreerUneMission(self):
        for i in self.winfo_children():
            i.destroy()

        self.Menu()
        self.CreerUneMission()

    def BouttonEnregistrerInfo2(self):
        for i in self.winfo_children():
            i.destroy()

        self.Menu()
        self.Etape3_Mission()

    def CreerUneMission(self):
        self.cumission_labelframe = LabelFrame(self, text="Mission n°", font=("Arial_black", 12), width=870, height=500, borderwidth=3)
        self.cumission_labelframe.place(relx=0.25, rely=0.25)
        self.cumission_label1 = Label(self.cumission_labelframe, text="Déroulée de la mission", font=("Arial", 12, "bold"))
        self.cumission_label1.place(relx=0.05, rely=0.008)
        self.cumission_labelframe1 = LabelFrame(self.cumission_labelframe, width=250, height=370, bg="#a4a1a3", relief=SUNKEN)
        self.cumission_labelframe1.place(relx=0.05, rely=0.05)
        self.cumission_boutton_decollage = Button(self.cumission_labelframe1, text="Décollage", font=("Arial", 12), width=20, height=2)
        self.cumission_boutton_decollage.place(relx=0.1, rely=0.02)
        self.cumission_boutton_balise1 = Button(self.cumission_labelframe1, text="Balise 1", font=("Arial", 12), width=20, height=2)
        self.cumission_boutton_balise1.place(relx=0.1, rely=0.19)
        self.cumission_boutton_atterissage = Button(self.cumission_labelframe1, text="Atterissage", font=("Arial", 12), width=20, height=2)
        self.cumission_boutton_atterissage.place(relx=0.1, rely=0.87)
        self.cumission_label2 = Label(self.cumission_labelframe, text="Rajouter une étape", font=("Arial", 12, "bold"))
        self.cumission_label2.place(relx=0.1, rely=0.84)

        self.cumission_boutton_etape = Button(self.cumission_labelframe, text="+", font=("Arial", 16, "bold"), width=10, bg="#a4a1a3", command=self.BouttonBalise2)
        self.cumission_boutton_etape.place(relx=0.1, rely=0.89)

        self.cumission_babel3 = Label(self.cumission_labelframe, text="Balise 1", font=("Arial", 12, "bold"))
        self.cumission_babel3.place(relx=0.5, rely=0.008)
        self.cumission_labelframe2 = LabelFrame(self.cumission_labelframe, width=400, height=370, borderwidth=3)
        self.cumission_labelframe2.place(relx=0.5, rely=0.05)
        self.cumission_label_latitude = Label(self.cumission_labelframe2, text="Latitude (en °):", font=("Arial", 12))
        self.cumission_label_latitude.place(relx=0.1, rely=0.08)
        self.cumission_entry_latitude = Entry(self.cumission_labelframe2, width=30)
        self.cumission_entry_latitude.place(relx=0.45, rely=0.09)
        self.cumission_label_longitude = Label(self.cumission_labelframe2, text="Longitude (en °):", font=("Arial", 12))
        self.cumission_label_longitude.place(relx=0.1, rely=0.2)
        self.cumission_entry_longitude = Entry(self.cumission_labelframe2, width=30)
        self.cumission_entry_longitude.place(relx=0.45, rely=0.21)
        self.cumission_label_altitude = Label(self.cumission_labelframe2, text="Altitude (en m):", font=("Arial", 12))
        self.cumission_label_altitude.place(relx=0.1, rely=0.33)
        self.cumission_entry_altitude = Spinbox(self.cumission_labelframe2, from_=0, to=100, justify=CENTER, width=30)
        self.cumission_entry_altitude.place(relx=0.45, rely=0.34)
        self.cumission_label_vitesse = Label(self.cumission_labelframe2, text="vitesse(en %):", font=("Arial", 12))
        self.cumission_label_vitesse.place(relx=0.1, rely=0.48)
        self.cumission_entry_vitesse = Spinbox(self.cumission_labelframe2, from_=0, to=100, justify=CENTER, width=30)
        self.cumission_entry_vitesse.place(relx=0.45, rely=0.49)
        self.cumission_label_pause = Label(self.cumission_labelframe2, text="pause(en s):", font=("Arial", 12))
        self.cumission_label_pause.place(relx=0.1, rely=0.63)
        self.cumission_entry_pause = Spinbox(self.cumission_labelframe2, from_=0, to=120, justify=CENTER, width=30)
        self.cumission_entry_pause.place(relx=0.45, rely=0.64)
        self.cumission_label_photo = Label(self.cumission_labelframe2, text="photo:", font=("Arial", 12))
        self.cumission_label_photo.place(relx=0.1, rely=0.79)
        self.cumission_checkbutton_photo_oui = Checkbutton(self.cumission_labelframe2, text="Oui", font=("Arail", 12))
        self.cumission_checkbutton_photo_oui.place(relx=0.75, rely=0.75)
        self.cumission_checkbutton_photo_non = Checkbutton(self.cumission_labelframe2, text="Non", font=("Arail", 12))
        self.cumission_checkbutton_photo_non.place(relx=0.75, rely=0.83)

        self.cumission_boutton_enregistrer = Button(self.cumission_labelframe, text="Enregistrer les informations", font=("Arial", 12), bg="#ffffff", width=30, height=2, command=self.BouttonEnregistrerInfo2)
        self.cumission_boutton_enregistrer.place(relx=0.575, rely=0.85)

    def GetCréerUneMission(self):
        cumlatitude = self.cumission_entry_latitude.get()
        cumlongitude = self.cumission_entry_longitude.get()
        cumaltitude = self.cumission_entry_altitude.get()
        cumvitesse = self.cumission_entry_vitesse.get()
        cumpause = self.cumission_entry_pause.get()

    def BouttonBalise2(self):
        self.boutton_nouvelle_etape_2 = Button(self.cumission_labelframe1, text="Balise 2", font=("Arial", 12), width=20, height=2)
        self.boutton_nouvelle_etape_2.place(relx=0.1, rely=0.36)

        self.cumission_boutton_etape.destroy()
        self.cumission_babel3.destroy()
        self.cumission_labelframe2.destroy()

        self.cumission_boutton_etape_2 = Button(self.cumission_labelframe, text="+", font=("Arial", 16, "bold"), width=10, bg="#a4a1a3", command=self.BouttonBalise3)
        self.cumission_boutton_etape_2.place(relx=0.1, rely=0.89)

        self.balise2_babel3 = Label(self.cumission_labelframe, text="Balise 2", font=("Arial", 12, "bold"))
        self.balise2_babel3.place(relx=0.5, rely=0.008)
        self.balise2_labelframe2 = LabelFrame(self.cumission_labelframe, width=400, height=370, borderwidth=3)
        self.balise2_labelframe2.place(relx=0.5, rely=0.05)
        self.balise2_label_latitude = Label(self.balise2_labelframe2, text="Latitude (en °):", font=("Arial", 12))
        self.balise2_label_latitude.place(relx=0.1, rely=0.08)
        self.balise2_entry_latitude = Entry(self.balise2_labelframe2, width=30)
        self.balise2_entry_latitude.place(relx=0.45, rely=0.09)
        self.balise2_label_longitude = Label(self.balise2_labelframe2, text="Longitude (en °):", font=("Arial", 12))
        self.balise2_label_longitude.place(relx=0.1, rely=0.2)
        self.balise2_entry_longitude = Entry(self.balise2_labelframe2, width=30)
        self.balise2_entry_longitude.place(relx=0.45, rely=0.21)
        self.balise2_label_altitude = Label(self.balise2_labelframe2, text="Altitude (en m):", font=("Arial", 12))
        self.balise2_label_altitude.place(relx=0.1, rely=0.33)
        self.balise2_entry_altitude = Spinbox(self.balise2_labelframe2, from_=0, to=100, justify=CENTER, width=30)
        self.balise2_entry_altitude.place(relx=0.45, rely=0.34)
        self.balise2_label_vitesse = Label(self.balise2_labelframe2, text="vitesse(en %):", font=("Arial", 12))
        self.balise2_label_vitesse.place(relx=0.1, rely=0.48)
        self.balise2_entry_vitesse = Spinbox(self.balise2_labelframe2, from_=0, to=100, justify=CENTER, width=30)
        self.balise2_entry_vitesse.place(relx=0.45, rely=0.49)
        self.balise2_label_pause = Label(self.balise2_labelframe2, text="pause(en s):", font=("Arial", 12))
        self.balise2_label_pause.place(relx=0.1, rely=0.63)
        self.balise2_entry_pause = Spinbox(self.balise2_labelframe2, from_=0, to=120, justify=CENTER, width=30)
        self.balise2_entry_pause.place(relx=0.45, rely=0.64)
        self.balise2_label_photo = Label(self.balise2_labelframe2, text="photo:", font=("Arial", 12))
        self.balise2_label_photo.place(relx=0.1, rely=0.79)
        self.balise2_checkbutton_photo_oui = Checkbutton(self.balise2_labelframe2, text="Oui", font=("Arail", 12))
        self.balise2_checkbutton_photo_oui.place(relx=0.75, rely=0.75)
        self.balise2_checkbutton_photo_non = Checkbutton(self.balise2_labelframe2, text="Non", font=("Arail", 12))
        self.balise2_checkbutton_photo_non.place(relx=0.75, rely=0.83)

    def GetBalise2(self):
        cumlatitude = self.balise2_entry_latitude.get()
        cumlongitude = self.balise2_entry_longitude.get()
        cumaltitude = self.balise2_entry_altitude.get()
        cumvitesse = self.balise2_entry_vitesse.get()
        cumpause = self.balise2_entry_pause.get()

    def BouttonBalise3(self):
        self.boutton_nouvelle_etape_3 = Button(self.cumission_labelframe1, text="Balise 3", font=("Arial", 12), width=20, height=2)
        self.boutton_nouvelle_etape_3.place(relx=0.1, rely=0.53)

        self.cumission_boutton_etape_2.destroy()
        self.balise2_babel3.destroy()
        self.balise2_labelframe2.destroy()

        self.cumission_boutton_etape_3 = Button(self.cumission_labelframe, text="+", font=("Arial", 16, "bold"), width=10, bg="#a4a1a3", command=self.BouttonBalise4)
        self.cumission_boutton_etape_3.place(relx=0.1, rely=0.89)

        self.balise3_babel3 = Label(self.cumission_labelframe, text="Balise 3", font=("Arial", 12, "bold"))
        self.balise3_babel3.place(relx=0.5, rely=0.008)
        self.balise3_labelframe2 = LabelFrame(self.cumission_labelframe, width=400, height=370, borderwidth=3)
        self.balise3_labelframe2.place(relx=0.5, rely=0.05)
        self.balise3_label_latitude = Label(self.balise3_labelframe2, text="Latitude (en °):", font=("Arial", 12))
        self.balise3_label_latitude.place(relx=0.1, rely=0.08)
        self.balise3_entry_latitude = Entry(self.balise3_labelframe2, width=30)
        self.balise3_entry_latitude.place(relx=0.45, rely=0.09)
        self.balise3_label_longitude = Label(self.balise3_labelframe2, text="Longitude (en °):", font=("Arial", 12))
        self.balise3_label_longitude.place(relx=0.1, rely=0.2)
        self.balise3_entry_longitude = Entry(self.balise3_labelframe2, width=30)
        self.balise3_entry_longitude.place(relx=0.45, rely=0.21)
        self.balise3_label_altitude = Label(self.balise3_labelframe2, text="Altitude (en m):", font=("Arial", 12))
        self.balise3_label_altitude.place(relx=0.1, rely=0.33)
        self.balise3_entry_altitude = Spinbox(self.balise3_labelframe2, from_=0, to=100, justify=CENTER, width=30)
        self.balise3_entry_altitude.place(relx=0.45, rely=0.34)
        self.balise3_label_vitesse = Label(self.balise3_labelframe2, text="vitesse(en %):", font=("Arial", 12))
        self.balise3_label_vitesse.place(relx=0.1, rely=0.48)
        self.balise3_entry_vitesse = Spinbox(self.balise3_labelframe2, from_=0, to=100, justify=CENTER, width=30)
        self.balise3_entry_vitesse.place(relx=0.45, rely=0.49)
        self.balise3_label_pause = Label(self.balise3_labelframe2, text="pause(en s):", font=("Arial", 12))
        self.balise3_label_pause.place(relx=0.1, rely=0.63)
        self.balise3_entry_pause = Spinbox(self.balise3_labelframe2, from_=0, to=120, justify=CENTER, width=30)
        self.balise3_entry_pause.place(relx=0.45, rely=0.64)
        self.balise3_label_photo = Label(self.balise3_labelframe2, text="photo:", font=("Arial", 12))
        self.balise3_label_photo.place(relx=0.1, rely=0.79)
        self.balise3_checkbutton_photo_oui = Checkbutton(self.balise3_labelframe2, text="Oui", font=("Arail", 12))
        self.balise3_checkbutton_photo_oui.place(relx=0.75, rely=0.75)
        self.balise3_checkbutton_photo_non = Checkbutton(self.balise3_labelframe2, text="Non", font=("Arail", 12))
        self.balise3_checkbutton_photo_non.place(relx=0.75, rely=0.83)

    def GetBalise3(self):
        cumlatitude = self.balise3_entry_latitude.get()
        cumlongitude = self.balise3_entry_longitude.get()
        cumaltitude = self.balise3_entry_altitude.get()
        cumvitesse = self.balise3_entry_vitesse.get()
        cumpause = self.balise3_entry_pause.get()

    def BouttonBalise4(self):
        self.boutton_nouvelle_etape_4 = Button(self.cumission_labelframe1, text="Balise 4", font=("Arial", 12), width=20, height=2)
        self.boutton_nouvelle_etape_4.place(relx=0.1, rely=0.70)

        self.cumission_boutton_etape_3.destroy()
        self.balise3_babel3.destroy()
        self.balise3_labelframe2.destroy()

        self.balise4_babel3 = Label(self.cumission_labelframe, text="Balise 4", font=("Arial", 12, "bold"))
        self.balise4_babel3.place(relx=0.5, rely=0.008)
        self.balise4_labelframe2 = LabelFrame(self.cumission_labelframe, width=400, height=370, borderwidth=3)
        self.balise4_labelframe2.place(relx=0.5, rely=0.05)
        self.balise4_label_latitude = Label(self.balise4_labelframe2, text="Latitude (en °):", font=("Arial", 12))
        self.balise4_label_latitude.place(relx=0.1, rely=0.08)
        self.balise4_entry_latitude = Entry(self.balise4_labelframe2, width=30)
        self.balise4_entry_latitude.place(relx=0.45, rely=0.09)
        self.balise4_label_longitude = Label(self.balise4_labelframe2, text="Longitude (en °):", font=("Arial", 12))
        self.balise4_label_longitude.place(relx=0.1, rely=0.2)
        self.balise4_entry_longitude = Entry(self.balise4_labelframe2, width=30)
        self.balise4_entry_longitude.place(relx=0.45, rely=0.21)
        self.balise4_label_altitude = Label(self.balise4_labelframe2, text="Altitude (en m):", font=("Arial", 12))
        self.balise4_label_altitude.place(relx=0.1, rely=0.33)
        self.balise4_entry_altitude = Spinbox(self.balise4_labelframe2, from_=0, to=100, justify=CENTER, width=30)
        self.balise4_entry_altitude.place(relx=0.45, rely=0.34)
        self.balise4_label_vitesse = Label(self.balise4_labelframe2, text="vitesse(en %):", font=("Arial", 12))
        self.balise4_label_vitesse.place(relx=0.1, rely=0.48)
        self.balise4_entry_vitesse = Spinbox(self.balise4_labelframe2, from_=0, to=100, justify=CENTER, width=30)
        self.balise4_entry_vitesse.place(relx=0.45, rely=0.49)
        self.balise4_label_pause = Label(self.balise4_labelframe2, text="pause(en s):", font=("Arial", 12))
        self.balise4_label_pause.place(relx=0.1, rely=0.63)
        self.balise4_entry_pause = Spinbox(self.balise4_labelframe2, from_=0, to=120, justify=CENTER, width=30)
        self.balise4_entry_pause.place(relx=0.45, rely=0.64)
        self.balise4_label_photo = Label(self.balise4_labelframe2, text="photo:", font=("Arial", 12))
        self.balise4_label_photo.place(relx=0.1, rely=0.79)
        self.balise4_checkbutton_photo_oui = Checkbutton(self.balise4_labelframe2, text="Oui", font=("Arail", 12))
        self.balise4_checkbutton_photo_oui.place(relx=0.75, rely=0.75)
        self.balise4_checkbutton_photo_non = Checkbutton(self.balise4_labelframe2, text="Non", font=("Arail", 12))
        self.balise4_checkbutton_photo_non.place(relx=0.75, rely=0.83)

    def GetBalise4(self):
        cumlatitude = self.balise4_entry_latitude.get()
        cumlongitude = self.balise4_entry_longitude.get()
        cumaltitude = self.balise4_entry_altitude.get()
        cumvitesse = self.balise4_entry_vitesse.get()
        cumpause = self.balise4_entry_pause.get()

    def VisualiserLesMissions(self):
        self.vlm_labelframe_utilisateur = LabelFrame(self, text="", font=("Arial_black", 12), width=870, height=500, borderwidth=3)
        self.vlm_labelframe_utilisateur.place(relx=0.25, rely=0.25)
        self.vlm_label_listemission = Label(self.vlm_labelframe_utilisateur, text="Liste des missions", font=("Arial", 12, "bold"))
        self.vlm_label_listemission.place(relx=0.08, rely=0.03)
        self.vlm_frame_listemission = LabelFrame(self.vlm_labelframe_utilisateur, width=200, height=350, bg="#a4a1a3", relief=SUNKEN)
        self.vlm_frame_listemission.place(relx=0.08, rely=0.08)
        self.vlm_label_modifmission = Label(self.vlm_labelframe_utilisateur, text="Modifier la mission", font=("Arial", 12))
        self.vlm_label_modifmission.place(relx=0.025, rely=0.83)
        self.vlm_boutton_modifmission = Button(self.vlm_labelframe_utilisateur, text="+", font=("Arial", 16, "bold"), width=9, bg="#a4a1a3")
        self.vlm_boutton_modifmission.place(relx=0.03, rely=0.88)
        self.vlm_label_suppmission = Label(self.vlm_labelframe_utilisateur, text="Supprimer la mission", font=("Arial", 12))
        self.vlm_label_suppmission.place(relx=0.21, rely=0.83)
        self.vlm_boutton_suppmission = Button(self.vlm_labelframe_utilisateur, text="-", font=("Arial", 16, "bold"), width=9, bg="#a4a1a3")
        self.vlm_boutton_suppmission.place(relx=0.22, rely=0.88)
        self.vlm_label_mission = Label(self.vlm_labelframe_utilisateur, text="Mission n°", font=("Arial", 12, "bold"))
        self.vlm_label_mission.place(relx=0.55, rely=0.03)
        self.vlm_labelframe_mission1 = LabelFrame(self.vlm_labelframe_utilisateur, width=350, height=200, borderwidth=3)
        self.vlm_labelframe_mission1.place(relx=0.55, rely=0.08)
        self.vlm_label_recap = Label(self.vlm_labelframe_mission1, text="Récapitulatif", font=("Arial", 12, "bold"))
        self.vlm_label_recap.place(relx=0.35, rely=0.01)
        self.vlm_label_durée = Label(self.vlm_labelframe_mission1, text="Durée:", font=("Arial", 12))
        self.vlm_label_durée.place(relx=0.01, rely=0.15)
        self.vlm_label_nbretape = Label(self.vlm_labelframe_mission1, text="Nombre étapes:", font=("Arial", 12))
        self.vlm_label_nbretape.place(relx=0.01, rely=0.30)
        self.vlm_label_modephoto = Label(self.vlm_labelframe_mission1, text="Mode photo:", font=("Arial", 12))
        self.vlm_label_modephoto.place(relx=0.01, rely=0.45)
        self.vlm_label_missionplanifiee = Label(self.vlm_labelframe_mission1, text="Mission planifiée:", font=("Arial", 12))
        self.vlm_label_missionplanifiee.place(relx=0.01, rely=0.60)
        self.vlm_boutton_lancermission = Button(self.vlm_labelframe_mission1, text="Lancer la mission", font=("Arial", 12), bg="#a4a1a3", width=30, height=1, command=self.BouttonLancerMission)
        self.vlm_boutton_lancermission.place(relx=0.1, rely=0.75)
        self.vlm_labelframe_mission2 = LabelFrame(self.vlm_labelframe_utilisateur, width=350, height=200, borderwidth=3)
        self.vlm_labelframe_mission2.place(relx=0.55, rely=0.53)
        self.vlm_label_planif = Label(self.vlm_labelframe_mission2, text="Planificateur", font=("Arial", 12, "bold"))
        self.vlm_label_planif.place(relx=0.35, rely=0.01)
        self.vlm_label_jour = Label(self.vlm_labelframe_mission2, text="Jour:", font=("Arial", 12))
        self.vlm_label_jour.place(relx=0.01, rely=0.18)
        self.vlm_entry_jour = Entry(self.vlm_labelframe_mission2, width=30)
        self.vlm_entry_jour.place(relx=0.25, rely=0.19)
        self.vlm_label_heure = Label(self.vlm_labelframe_mission2, text="Heure:", font=("Arial", 12))
        self.vlm_label_heure.place(relx=0.01, rely=0.45)
        self.vlm_entry_heure = Entry(self.vlm_labelframe_mission2, width=30)
        self.vlm_entry_heure.place(relx=0.25, rely=0.46)
        self.vlm_boutton_planifiermission = Button(self.vlm_labelframe_mission2, text="Planifier la mission", font=("Arial", 12), bg="#a4a1a3", width=30, height=1)
        self.vlm_boutton_planifiermission.place(relx=0.1, rely=0.75)

    def GetVisualiserLesMissions(self):
        vlmjour = self.vlm_entry_jour.get()
        vlmheure = self.vlm_entry_heure.get()

    def BouttonLancerMission(self):
        for i in self.winfo_children():
            i.destroy()

        self.Menu()
        self.ExecutionMission()

    def ExecutionMission(self):

        self.execmission_frame_principale = Frame(self, width=870, height=500)
        self.execmission_frame_principale.place(relx=0.25, rely=0.25)
        self.execmission_labelframe_retourvideo = LabelFrame(self.execmission_frame_principale, text="Retour Vidéo", font=("Arial", 14, "bold"), width= 500, height=300, borderwidth=3)
        self.execmission_labelframe_retourvideo.place(relx=0.05, rely=0.05)
        self.execmission_labelframe_controle_drone = LabelFrame(self.execmission_frame_principale, text="Contrôles Drone", font=("Arial", 8, "bold"), width= 150, height=200, borderwidth=3)
        self.execmission_labelframe_controle_drone.place(relx=0.75, rely=0.2)
        self.execmission_boutton_retourbase = Button(self.execmission_labelframe_controle_drone, text="Retour base", width=15, height=2, bg="#d3c04d")
        self.execmission_boutton_retourbase.place(relx=0.1, rely=0.08)
        self.execmission_boutton_arret = Button(self.execmission_labelframe_controle_drone, text="Arret urgence", width=15, height=2, bg="#d3272d")
        self.execmission_boutton_arret.place(relx=0.1, rely=0.4)
        self.execmission_boutton_arret = Button(self.execmission_labelframe_controle_drone, text="Prendre photo", width=15, height=2, bg="#959495")
        self.execmission_boutton_arret.place(relx=0.1, rely=0.7)
        self.execmission_frame_info_vol = LabelFrame(self.execmission_frame_principale, width=400, height= 120, borderwidth=3, bg="#a4a1a3")
        self.execmission_frame_info_vol.place(relx=0.1, rely=0.725)
        self.execmission_label_info_vol = Label(self.execmission_frame_info_vol, text="Information de vol", font=("Arial", 12, "bold"), bg="#a4a1a3")
        self.execmission_label_info_vol.place(relx=0.01, rely=0.01)
        self.execmission_latitude = Label(self.execmission_frame_info_vol, text="Latitude:", font=("Arial", 12), bg="#a4a1a3")
        self.execmission_latitude.place(relx=0.01, rely=0.22)
        self.execmission_longitude = Label(self.execmission_frame_info_vol, text="Longitude:", font=("Arial", 12), bg="#a4a1a3")
        self.execmission_longitude.place(relx=0.01, rely=0.46)
        self.execmission_altitude = Label(self.execmission_frame_info_vol, text="Altitude:", font=("Arial", 12), bg="#a4a1a3")
        self.execmission_altitude.place(relx=0.01, rely=0.7)
        self.execmission_Vitesse = Label(self.execmission_frame_info_vol, text="Vitesse:", font=("Arial", 12), bg="#a4a1a3")
        self.execmission_Vitesse.place(relx=0.58, rely=0.35)
        self.execmission_batterie = Label(self.execmission_frame_info_vol, text="Batterie:", font=("Arial", 12), bg="#a4a1a3")
        self.execmission_batterie.place(relx=0.58, rely=0.65)





instance = Interface()
instance.resizable(width=False, height=False)
instance.mainloop()