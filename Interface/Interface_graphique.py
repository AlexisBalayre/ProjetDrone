from tkinter import *
import tkinter as tk

class Interface(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)  # constructeur de la classe parente
        self.Menu() #appel de la methode "BarredeMenu"
        self.geometry("1922x1080")  # Redimensionne la fenetre
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


    def bouttonvol(self): #Methode présente pour supprimer les widgets de Etape2_parametre  et afficher ceux de Etape1_Vols
        self.param_label_frame.destroy()

        self.mission_listeutilisateur.destroy()
        self.mission_frame1.destroy()
        self.mission_utilisateurselectionné.destroy()
        self.mission_labelframe.destroy()

        self.Etape1_Vols()

    def bouttonmission(self):
        self.param_label_frame.destroy()

        self.vols_text_label.destroy()
        self.vols_label_frame2.destroy()

        self.Etape3_Mission()

    def Etape1_Vols(self): #Methode comprenant les widgets de la première fenetre
        self.vols_text_label = Label(self, text="Pas de mission en cours", fg="black", font=("Arial_black", 16), bg="#dbdadb", relief=SUNKEN, width = 55, height = 2) #Label "pas de mission en cours"
        self.vols_text_label.place(relx= 0.3, rely=0.02)

        self.vols_label_frame2 = LabelFrame(self, text="Missions programmées", width=1070, height=800, borderwidth=3) #Label_frame contenant les missions programmées
        self.vols_label_frame2.place(relx= 0.2, rely= 0.1)


    def bouttonparam(self): #Methode présente pour supprimer les widgets de Etape1_Vols et afficher ceux de Etape2_parametre
        self.vols_text_label.destroy()
        self.vols_label_frame2.destroy()

        self.Etape2_parametre()


    def Etape2_parametre(self): #Methode comprenant les widgets de l'étape 2 du doc spe fonctionelles
        self.param_label_frame = LabelFrame(self, text = "Réglages", font=("Arial_black", 12), width = 1070, height=800, borderwidth=3)
        self.param_label_frame.place(relx= 0.2, rely= 0.1)

        self.param_label_frame2 = LabelFrame(self.param_label_frame, text = "Liste des utilisateurs", font=("Arial_black", 12), bg = "#a4a1a3", width= 600, height= 300, borderwidth=3 )
        self.param_label_frame2.place(relx= 0.05, rely= 0.1)

        self.param_boutton_utilisateur = Button(self.param_label_frame, text="Ajouter un utilisateur", font=("Arial_black", 16), bg= "#ffffff", width= 20, height= 2, command=self.BouttonAjouterUtilisateur)
        self.param_boutton_utilisateur.place(relx= 0.7, rely= 0.25)

        self.param_label_frame3 = LabelFrame(self.param_label_frame, text="Utilisateur selectionné:", font=("Arial_black", 12), width= 500, height= 300, borderwidth=3)
        self.param_label_frame3.place(relx= 0.3, rely= 0.55)

    def BouttonAjouterUtilisateur(self): #Methode présente pour supprimer les widgets de Etape2_parametre et afficher ceux de ParamAjouterUtilisateur
        self.param_label_frame.destroy()
        self.param_label_frame2.destroy()
        self.param_boutton_utilisateur.destroy()
        self.param_label_frame3.destroy()

        self.ParamAjouterUtilisateur()

    def BouttonEnregistrerInfo(self):
        self.pau_label_frame.destroy()

        self.Etape2_parametre()

    def ParamAjouterUtilisateur(self): # Mehtode comprenant les widgets de l'etape 2 du doc spe fonctionnelles si la personne clique sur "Ajouter un utilisateur"
        self.pau_label_frame = LabelFrame(self, text = "Utilisateur n°", font=("Arial_black", 12), width = 1070, height=800, borderwidth=3)
        self.pau_label_frame.place(relx=0.2, rely=0.1)

        self.pau_text_frame2 = Label(self.pau_label_frame, text="Informations personnelles", font=("Arial_black", 12))
        self.pau_text_frame2.place(relx=0.05, rely=0.055)
        self.pau_label_frame2 = LabelFrame(self.pau_label_frame, width=500, height=300, bg="#a4a1a3",relief=SUNKEN)
        self.pau_label_frame2.place(relx=0.05, rely=0.1)

        self.pau_text_prénom = Label(self.pau_label_frame2, text="Prénom", font=("Arail", 14, "bold"), bg="#a4a1a3")
        self.pau_text_prénom.place(relx=0.1, rely=0.1)
        self.pau_text_nom = Label(self.pau_label_frame2, text = "Nom", font=("Arail", 14, "bold"), bg="#a4a1a3")
        self.pau_text_nom.place(relx=0.1, rely=0.4)
        self.pau_text_mail = Label(self.pau_label_frame2, text="Email", font=("Arail", 14, "bold"), bg="#a4a1a3")
        self.pau_text_mail.place(relx=0.1, rely=0.75)

        self.pau_entry_prénom = Entry(self.pau_label_frame2, width=40)
        self.pau_entry_prénom.place(relx=0.35, rely=0.12)
        self.pau_entry_nom =Entry(self.pau_label_frame2, width=40)
        self.pau_entry_nom.place(relx=0.35, rely=0.42)
        self.pau_entry_mail = Entry(self.pau_label_frame2, width=40)
        self.pau_entry_mail.place(relx=0.35, rely=0.77)

        self.pau_text_frame3 = Label(self.pau_label_frame, text="Options de vols", font=("Arial_black", 12))
        self.pau_text_frame3.place(relx=0.6, rely=0.055)
        self.pau_label_frame3 = LabelFrame (self.pau_label_frame, width=400, height=300, bg="#a4a1a3", relief=SUNKEN)
        self.pau_label_frame3.place(relx=0.6, rely=0.1)

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
        self.pau_text_frame4.place(relx=0.17, rely=0.535)
        self.pau_label_frame4 = LabelFrame(self.pau_label_frame, width=800, height=250, bg="#a4a1a3", relief=SUNKEN)
        self.pau_label_frame4.place(relx=0.17, rely=0.57)

        self.pau_text_vitesse = Label(self.pau_label_frame4, text="Vitesse", font=("Arail", 14, "bold"), bg="#a4a1a3")
        self.pau_text_vitesse.place(relx=0.05, rely=0.1)
        self.pau_text_latitudebase = Label(self.pau_label_frame4, text="Latitude \n base", font=("Arail", 14, "bold"), bg="#a4a1a3")
        self.pau_text_latitudebase.place(relx=0.05, rely=0.35)
        self.pau_text_longitudebase = Label(self.pau_label_frame4, text="Longitude \n base", font=("Arail", 14, "bold"),bg="#a4a1a3")
        self.pau_text_longitudebase.place(relx=0.04, rely=0.65)
        self.pau_text_modecam = Label(self.pau_label_frame4, text="Mode caméra", font=("Arail", 14, "bold"), bg="#a4a1a3")
        self.pau_text_modecam.place(relx=0.6, rely=0.35)


        self.pau_entry_vitesse = Entry(self.pau_label_frame4, width=30)
        self.pau_entry_vitesse.place(relx=0.17, rely=0.12)
        self.pau_entry_latitudebase = Entry(self.pau_label_frame4, width=30)
        self.pau_entry_latitudebase.place(relx=0.17, rely=0.42)
        self.pau_entry_longitude = Entry(self.pau_label_frame4, width=30)
        self.pau_entry_longitude.place(relx=0.17, rely=0.72)
        self.pau_modecam_photo_check = Checkbutton(self.pau_label_frame4, text="Photo", font=("Arail", 14), bg="#a4a1a3")
        self.pau_modecam_photo_check.place(relx=0.8, rely=0.35)
        self.pau_modecam_video_check = Checkbutton(self.pau_label_frame4, text="Vidéo", font=("Arail", 14), bg="#a4a1a3")
        self.pau_modecam_video_check.place(relx=0.8, rely=0.55)

        self.pau_boutton = Button(self.pau_label_frame, text = "Enregistrer les informations", font=("Arial_black", 12), width=22, height=2, bg="#ffffff", command=self.BouttonEnregistrerInfo)
        self.pau_boutton.place(relx=0.45, rely=0.92)

    def Etape3_Mission(self):

        self.mission_listeutilisateur = Label(self, text="Liste Utilisateurs", font=("Arial", 14, "bold"))
        self.mission_listeutilisateur.place(relx=0.3, rely=0.15)
        self.mission_frame1 = Frame(self, width=800, height=300, bg="#a4a1a3")
        self.mission_frame1.place(relx=0.3, rely=0.18)
        self.mission_utilisateurselectionné = Label(self, text="Utilisateur sélectionné:", font=("Arial", 14, "bold"))
        self.mission_utilisateurselectionné.place(relx=0.38, rely=0.6)
        self.mission_labelframe = LabelFrame(self, width=500, height=200, borderwidth=3)
        self.mission_labelframe.place(relx=0.38, rely=0.63)
        self.mission_boutton1 = Button(self.mission_labelframe, text="Visualiser les missions", font=("Arial", 12, "bold"), width=42, height=2)
        self.mission_boutton1.place(relx=0.07, rely=0.1)
        self.mission_boutton2 = Button(self.mission_labelframe, text="Créer une mission", font=("Arial", 12, "bold"), width=42, height=2, command=self.BouttonCreerUneMission)
        self.mission_boutton2.place(relx=0.07, rely=0.6)

    def BouttonCreerUneMission(self):

        self.mission_frame1.destroy()
        self.mission_labelframe.destroy()

        self.CreerUneMission()

    def CreerUneMission(self):

        self.cumission_labelframe = LabelFrame(self, text = "Mission n°", font=("Arial_black", 12), width = 1070, height=800, borderwidth=3)
        self.cumission_labelframe.place(relx=0.2, rely=0.1)
        self.cumission_label = Label(self.cumission_labelframe, text="Déroulée de la mission", font=("Arial", 12, "bold"))
        self.cumission_label.place(relx=0.1, rely=0.05)
        self.cumission_frame1 = Frame(self.cumission_labelframe, width=300, height=600, bg="#a4a1a3", relief=SUNKEN)
        self.cumission_frame1.place(relx=0.1, rely=0.08)


#Il faut faire un boutton quitter pour chaque interface pour eviter que tout soit melanger et que ça bug

instance = Interface()
instance.mainloop()