#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import *
import tkinter as tk
from Packages.packages import *


class Interface(tk.Tk):  # définition de la classe
    def __init__(self):
        tk.Tk.__init__(self)  # constructeur de la classe parente
        self.Menu()  # appel de la methode "BarredeMenu"
        w, h = self.winfo_screenwidth(), self.winfo_screenheight()
        self.geometry(
            "%dx%d" % (w, h)
        )  # Redimensionne la fenetre en fonction du nombre de pixel de l'écran
        self.Etape1_Vols()  # appel la première fenetre à s'afficher

    def Menu(self):  # Methode de la barre de menu
        self.label_frame1 = LabelFrame(
            self, text="menu", width=200, height=110
        )  # label_frame pour encadrer les bouton menu en haut à gauche
        self.label_frame1.place(relx=0.01, rely=0.02)

        self.frame1 = Frame(self.label_frame1)
        self.frame1.place(relx=0, rely=0)

        self.frame2 = Frame(self.label_frame1)
        self.frame2.place(relx=0, rely=0.77, width=175)

        self.photo = PhotoImage(
            file="Ressources/icon_reglage.gif"
        )  # boutton reglage avec icone contenu dans le label_frame menu
        self.boutton_reglage = Button(
            self.frame1, image=self.photo, command=self.bouttonparam
        )
        self.boutton_reglage.photo = self.photo
        self.boutton_reglage.pack(side=LEFT)

        self.text_reglage = Label(
            self.frame2, text="Réglages"
        )  # texte en dessous du bouton reglage avec écrit réglage
        self.text_reglage.pack(side=LEFT)

        self.photo3 = PhotoImage(
            file="Ressources/icon_vols.gif"
        )  # boutton vols avec icone contenu dans le label_frame menu
        self.boutton_vols = Button(
            self.frame1, image=self.photo3, command=self.bouttonvol
        )
        self.boutton_vols.photo = self.photo3
        self.boutton_vols.pack(side=RIGHT)

        self.text_vols = Label(
            self.frame2, text="Vols"
        )  # texte en dessous du bouton vols avec écrit vols
        self.text_vols.pack(side=RIGHT)

        self.photo2 = PhotoImage(
            file="Ressources/icon_mission.gif"
        )  # boutton mission avec icone contenu dans le label_frame menu
        self.boutton_mission = Button(
            self.frame1, image=self.photo2, command=self.bouttonmission
        )
        self.boutton_mission.photo = self.photo2
        self.boutton_mission.pack()

        self.text_mission = Label(
            self.frame2, text="Missions"
        )  # texte en dessous du bouton missions avec écrit missions
        self.text_mission.pack()

    def bouttonparam(
        self,
    ):  # Methode présente pour supprimer les widgets de la fenetre en cours d'exécution et afficher ceux de Etape2_parametre
        for i in self.winfo_children():
            i.destroy()

        self.Menu()
        self.Etape2_parametre()

    def bouttonvol(
        self,
    ):  # Methode présente pour supprimer les widgets de la fenetre en cours d'exécution et afficher ceux de Etape1_Vols
        for i in self.winfo_children():
            i.destroy()

        self.Menu()
        self.Etape1_Vols()

    def bouttonmission(
        self,
    ):  # Methode présente pour supprimer les widgets de la fenetre en cours d'exécution et afficher ceux de Etape3_Vols
        for i in self.winfo_children():
            i.destroy()

        self.Menu()
        self.Etape3_Mission()

    def Etape1_Vols(self):  # Methode comprenant les widgets de la première fenetre
        self.vols_text_label = Label(
            self,
            text="Pas de mission en cours",
            fg="black",
            font=("Arial_black", 16),
            bg="#dbdadb",
            relief=SUNKEN,
            width=55,
            height=2,
        )  # Label "pas de mission en cours"
        self.vols_text_label.place(relx=0.305, rely=0.15)

        self.vols_label_frame2 = LabelFrame(
            self, text="Missions programmées", width=870, height=500, borderwidth=3
        )  # Label_frame contenant les missions programmées
        self.vols_label_frame2.place(relx=0.25, rely=0.25)

    def Etape2_parametre(
        self,
    ):  # Methode comprenant les widgets de l'étape 2 du doc spe fonctionelles

        self.param_label_frame = LabelFrame(
            self,
            text="Réglages",
            font=("Arial_black", 12),
            width=870,
            height=500,
            borderwidth=3,
        )  # Label_frame "Réglages" contenant tous les widgets de l'étape 2
        self.param_label_frame.place(relx=0.25, rely=0.25)

        self.param_label_frame2 = LabelFrame(
            self.param_label_frame,
            text="Liste des utilisateurs",
            font=("Arial_black", 12),
            bg="#a4a1a3",
            width=340,
            height=200,
            borderwidth=3,
        )  # Label_frame contenant les différents utilisateurs
        self.param_label_frame2.place(relx=0.05, rely=0.08)

        # Initilisation variable
        self.id_select = None

        # Récupération des utilisateurs
        donnees = Initialisation()
        self.Donnees = donnees[2]
        self.id = donnees[1]
        self.utilisateurs = donnees[0]
        self.nombre_utilisateurs = len(self.utilisateurs.__dict__["utilisateurs"])
        self.liste_id = []
        for x in self.utilisateurs.__dict__["utilisateurs"]:
            self.liste_id.append(
                self.utilisateurs.__dict__["utilisateurs"][x].__dict__["id_utilisateur"]
            )

        # Bouton utilisateur 1
        if self.nombre_utilisateurs != 0:
            state1 = "normal"
            name_1 = self.utilisateurs.__dict__["utilisateurs"][
                self.liste_id[0]
            ].__dict__["prenom"]
        else:
            state1 = "disabled"
            name_1 = "Utilisateur 1"
        self.param_boutton_utilisateur1 = Button(
            self.param_label_frame2,
            text=name_1,
            font=("Arial_black", 16),
            bg="#ffffff",
            width=10,
            height=2,
            state=state1,
            command=lambda: self.BoutonSelectionne(name_1, self.liste_id[0], 0),
        )
        self.param_boutton_utilisateur1.place(relx=0.05, rely=0.13)

        # Bouton utilisateur 2
        if self.nombre_utilisateurs > 1:
            state2 = "normal"
            name_2 = self.utilisateurs.__dict__["utilisateurs"][
                self.liste_id[1]
            ].__dict__["prenom"]
        else:
            state2 = "disabled"
            name_2 = "Utilisateur 2"
        self.param_boutton_utilisateur2 = Button(
            self.param_label_frame2,
            text=name_2,
            font=("Arial_black", 16),
            bg="#ffffff",
            width=10,
            height=2,
            state=state2,
            command=lambda: self.BoutonSelectionne(name_2, self.liste_id[1], 1),
        )
        self.param_boutton_utilisateur2.place(relx=0.56, rely=0.13)

        # Bouton utilisateur 3
        if self.nombre_utilisateurs > 2:
            state3 = "normal"
            name_3 = self.utilisateurs.__dict__["utilisateurs"][
                self.liste_id[2]
            ].__dict__["prenom"]
        else:
            state3 = "disabled"
            name_3 = "Utilisateur 3"
        self.param_boutton_utilisateur3 = Button(
            self.param_label_frame2,
            text=name_3,
            font=("Arial_black", 16),
            bg="#ffffff",
            width=10,
            height=2,
            state=state3,
            command=lambda: self.BoutonSelectionne(name_3, self.liste_id[2], 2),
        )
        self.param_boutton_utilisateur3.place(relx=0.05, rely=0.57)

        # Bouton utilisateur 4
        if self.nombre_utilisateurs > 3:
            state4 = "normal"
            name_4 = self.utilisateurs.__dict__["utilisateurs"][
                self.liste_id[3]
            ].__dict__["prenom"]
        else:
            state4 = "disabled"
            name_4 = "Utilisateur 4"
        self.param_boutton_utilisateur4 = Button(
            self.param_label_frame2,
            text=name_4,
            font=("Arial_black", 16),
            bg="#ffffff",
            width=10,
            height=2,
            state=state4,
            command=lambda: self.BoutonSelectionne(name_4, self.liste_id[3], 3),
        )
        self.param_boutton_utilisateur4.place(relx=0.56, rely=0.57)

        # Bouton ajouter utilisateur
        self.param_boutton_utilisateur = Button(
            self.param_label_frame,
            text="Ajouter un utilisateur",
            font=("Arial_black", 16),
            bg="#ffffff",
            width=20,
            height=2,
            command=self.BouttonAjouterUtilisateur,
        )
        self.param_boutton_utilisateur.place(relx=0.6, rely=0.25)
        if self.nombre_utilisateurs >= 4:
            self.param_boutton_utilisateur.destroy()  # Retire bouton lorsqu'il y a 4 utilisateurs

        # Frame Utilisateur sélectionné contenant les boutons modifier et supprimer
        self.param_label_frame3 = LabelFrame(
            self.param_label_frame,
            text="Aucun utilisateur sélectionné",
            font=("Arial_black", 12),
            width=500,
            height=200,
            borderwidth=3,
        )
        self.param_label_frame3.place(relx=0.23, rely=0.53)

        # Bouton Modifier l'utilisateur
        self.param_boutton_modif_utilisateur = Button(
            self.param_label_frame3,
            text="Modifier l'utilisateur",
            font=("Arial_black", 16),
            bg="#ffffff",
            width=30,
            height=2,
            command=lambda: self.BouttonModifierUtilisateur(),
        )
        self.param_boutton_modif_utilisateur.place(relx=0.12, rely=0.12)

        # Bouton Supprimer l'utilisateur
        self.param_boutton_sup_utilisateur = Button(
            self.param_label_frame3,
            text="Supprimer l'utilisateur",
            font=("Arial_black", 16),
            bg="#ffffff",
            width=30,
            height=2,
            command=self.BouttonSupprimerUtilisateur,
        )
        self.param_boutton_sup_utilisateur.place(relx=0.12, rely=0.56)

    def BoutonSelectionne(
        self, name, id, id_bouton
    ):  # Retourne id de l'utilisateur sélectionné
        self.param_label_frame3.configure(text="Utilisateur sélectionné : %s" % name)
        self.id_select = id
        self.id_bouton = id_bouton

    def BouttonAjouterUtilisateur(
        self,
    ):  # Methode présente pour supprimer les widgets de la fenetre en cours d'exécution et appeler ceux pour ajouter un utilisateur
        for i in self.winfo_children():
            i.destroy()
        self.Menu()
        self.ParamAjouterUtilisateur()

    def BouttonModifierUtilisateur(
        self,
    ):  # Methode présente pour supprimer les widgets de la fenetre en cours d'exécution et appeler ceux pour modifer un utilisateur
        if self.id_select != None:
            for i in self.winfo_children():
                i.destroy()
            self.Menu()
            self.ParamModifierUtilisateur()

    def BouttonSupprimerUtilisateur(self,):
        if self.id_select != None:
            self.Menu()
            # Suppression Utilisateur 1
            if self.id_bouton == 0:
                SuppressionUtilisateur(self.utilisateurs, self.id_select)
                self.param_boutton_utilisateur1.destroy()
            # Suppression Utilisateur 2
            if self.id_bouton == 1:
                SuppressionUtilisateur(self.utilisateurs, self.id_select)
                self.param_boutton_utilisateur2.destroy()
            # Suppression Utilisateur 3
            if self.id_bouton == 2:
                SuppressionUtilisateur(self.utilisateurs, self.id_select)
                self.param_boutton_utilisateur3.destroy()
            # Suppression Utilisateur 4
            if self.id_bouton == 3:
                SuppressionUtilisateur(self.utilisateurs, self.id_select)
                self.param_boutton_utilisateur4.destroy()
            self.Etape2_parametre()

    def ParamAjouterUtilisateur(
        self,
    ):  # Mehtode comprenant les widgets de l'etape 2 du doc spe fonctionnelles si la personne clique sur "Ajouter un utilisateur"
        self.pau_label_frame = LabelFrame(
            self,
            text="Utilisateur n°",
            font=("Arial_black", 12),
            width=870,
            height=600,
            borderwidth=3,
        )  # LabelFrame qui inclu les autres frames de la fenetre avec widg
        self.pau_label_frame.place(relx=0.25, rely=0.2)

        self.pau_text_frame2 = Label(
            self.pau_label_frame,
            text="Informations personnelles",
            font=("Arial_black", 12),
        )
        self.pau_text_frame2.place(relx=0.05, rely=0.025)
        self.pau_label_frame2 = LabelFrame(
            self.pau_label_frame, width=350, height=200, bg="#a4a1a3", relief=SUNKEN
        )  # LabelFrame qui inclu les différents les widgets du prénom, nom et mail
        self.pau_label_frame2.place(relx=0.05, rely=0.08)

        self.pau_text_prenom = Label(
            self.pau_label_frame2,
            text="Prénom",
            font=("Arail", 14, "bold"),
            bg="#a4a1a3",
        )
        self.pau_text_prenom.place(relx=0.1, rely=0.1)
        self.pau_text_nom = Label(
            self.pau_label_frame2, text="Nom", font=("Arail", 14, "bold"), bg="#a4a1a3"
        )
        self.pau_text_nom.place(relx=0.1, rely=0.4)
        self.pau_text_mail = Label(
            self.pau_label_frame2,
            text="Email",
            font=("Arail", 14, "bold"),
            bg="#a4a1a3",
        )
        self.pau_text_mail.place(relx=0.1, rely=0.75)

        self.pau_entry_prenom = Entry(self.pau_label_frame2, width=30)
        self.pau_entry_prenom.place(relx=0.35, rely=0.12)
        self.pau_entry_nom = Entry(self.pau_label_frame2, width=30)
        self.pau_entry_nom.place(relx=0.35, rely=0.42)
        self.pau_entry_mail = Entry(self.pau_label_frame2, width=30)
        self.pau_entry_mail.place(relx=0.35, rely=0.77)

        self.pau_text_frame3 = Label(
            self.pau_label_frame, text="Options de vols", font=("Arial_black", 12)
        )
        self.pau_text_frame3.place(relx=0.6, rely=0.025)
        self.pau_label_frame3 = LabelFrame(
            self.pau_label_frame, width=300, height=200, bg="#a4a1a3", relief=SUNKEN
        )  # LabelFrame qui inclu tous les checkbutton de "option de vol"
        self.pau_label_frame3.place(relx=0.6, rely=0.08)

        self.pau_check_suiviedevol = Checkbutton(
            self.pau_label_frame3,
            text="Suivie de vol par mail",
            font=("Arail", 14, "bold"),
            bg="#a4a1a3",
        )
        self.pau_check_suiviedevol.place(relx=0.1, rely=0.1)
        self.pau_check_coordonnees = Checkbutton(
            self.pau_label_frame3, text="Coordonnées", font=("Arail", 14), bg="#a4a1a3"
        )
        self.pau_check_coordonnees.place(relx=0.2, rely=0.25)
        self.pau_check_altitude = Checkbutton(
            self.pau_label_frame3, text="Altitude", font=("Arail", 14), bg="#a4a1a3"
        )
        self.pau_check_altitude.place(relx=0.2, rely=0.4)
        self.pau_check_vitesse = Checkbutton(
            self.pau_label_frame3, text="Vitesse", font=("Arail", 14), bg="#a4a1a3"
        )
        self.pau_check_vitesse.place(relx=0.2, rely=0.55)
        self.pau_check_batterie = Checkbutton(
            self.pau_label_frame3,
            text="Charge batterie",
            font=("Arail", 14),
            bg="#a4a1a3",
        )
        self.pau_check_batterie.place(relx=0.2, rely=0.7)
        self.pau_check_photo = Checkbutton(
            self.pau_label_frame3, text="Photos", font=("Arail", 14), bg="#a4a1a3"
        )
        self.pau_check_photo.place(relx=0.2, rely=0.85)

        self.pau_text_frame4 = Label(
            self.pau_label_frame,
            text="Paramètres de vol favoris",
            font=("Arial_black", 12),
        )
        self.pau_text_frame4.place(relx=0.1, rely=0.48)
        self.pau_label_frame4 = LabelFrame(
            self.pau_label_frame, width=700, height=200, bg="#a4a1a3", relief=SUNKEN
        )  # LabelFrame qui inclu tous les parametres de vol favoris (Vitesse, Latitude base, Longitude base, mode camera)
        self.pau_label_frame4.place(relx=0.1, rely=0.53)

        self.pau_text_vitesse = Label(
            self.pau_label_frame4,
            text="Vitesse",
            font=("Arail", 14, "bold"),
            bg="#a4a1a3",
        )
        self.pau_text_vitesse.place(relx=0.05, rely=0.1)
        self.pau_text_latitudebase = Label(
            self.pau_label_frame4,
            text="Latitude \n base",
            font=("Arail", 14, "bold"),
            bg="#a4a1a3",
        )
        self.pau_text_latitudebase.place(relx=0.05, rely=0.35)
        self.pau_text_longitudebase = Label(
            self.pau_label_frame4,
            text="Longitude \n base",
            font=("Arail", 14, "bold"),
            bg="#a4a1a3",
        )
        self.pau_text_longitudebase.place(relx=0.04, rely=0.65)
        self.pau_text_modecam = Label(
            self.pau_label_frame4,
            text="Mode caméra",
            font=("Arail", 14, "bold"),
            bg="#a4a1a3",
        )
        self.pau_text_modecam.place(relx=0.6, rely=0.35)

        self.pau_entry_vitesse = Entry(self.pau_label_frame4, width=30)
        self.pau_entry_vitesse.place(relx=0.2, rely=0.12)
        self.pau_entry_latitudebase = Entry(self.pau_label_frame4, width=30)
        self.pau_entry_latitudebase.place(relx=0.2, rely=0.42)
        self.pau_entry_longitude = Entry(self.pau_label_frame4, width=30)
        self.pau_entry_longitude.place(relx=0.2, rely=0.72)
        self.pau_modecam_photo_check = Checkbutton(
            self.pau_label_frame4, text="Photo", font=("Arail", 14), bg="#a4a1a3"
        )
        self.pau_modecam_photo_check.place(relx=0.8, rely=0.35)
        self.pau_modecam_video_check = Checkbutton(
            self.pau_label_frame4, text="Vidéo", font=("Arail", 14), bg="#a4a1a3"
        )
        self.pau_modecam_video_check.place(relx=0.8, rely=0.55)

        self.pau_boutton = Button(
            self.pau_label_frame,
            text="Enregistrer les informations",
            font=("Arial_black", 12),
            width=22,
            height=2,
            bg="#ffffff",
            command=lambda: [self.GetInfoUtilisateur(), self.BouttonEnregistrerInfo()],
        )  # Bouton qui permet d'executer les commandes GetInfoUtilisateur et BouttonEnregistrerInfo
        self.pau_boutton.place(relx=0.4, rely=0.9)

    def ParamModifierUtilisateur(
        self,
    ):  # Mehtode permettant de modifier un utilisateur (reprend beaucoup la methode AjouterUtilisateur mais pour modifer et non ajouter)
        self.pau_label_frame = LabelFrame(
            self,
            text="Utilisateur : %s"
            % self.utilisateurs.__dict__["utilisateurs"][self.id_select].__dict__[
                "prenom"
            ],
            font=("Arial_black", 12),
            width=870,
            height=600,
            borderwidth=3,
        )
        self.pau_label_frame.place(relx=0.25, rely=0.2)

        self.pau_text_frame2 = Label(
            self.pau_label_frame,
            text="Informations personnelles",
            font=("Arial_black", 12),
        )
        self.pau_text_frame2.place(relx=0.05, rely=0.025)
        self.pau_label_frame2 = LabelFrame(
            self.pau_label_frame, width=350, height=200, bg="#a4a1a3", relief=SUNKEN
        )
        self.pau_label_frame2.place(relx=0.05, rely=0.08)

        self.pau_text_prenom = Label(
            self.pau_label_frame2,
            text="Prénom",
            font=("Arail", 14, "bold"),
            bg="#a4a1a3",
        )
        self.pau_text_prenom.place(relx=0.1, rely=0.1)
        self.pau_text_nom = Label(
            self.pau_label_frame2, text="Nom", font=("Arail", 14, "bold"), bg="#a4a1a3"
        )
        self.pau_text_nom.place(relx=0.1, rely=0.4)
        self.pau_text_mail = Label(
            self.pau_label_frame2,
            text="Email",
            font=("Arail", 14, "bold"),
            bg="#a4a1a3",
        )
        self.pau_text_mail.place(relx=0.1, rely=0.75)

        # Champs de saisi du prénom
        mon_entree1 = StringVar()
        # Récupération de la valeur par défaut
        mon_entree1.set(
            self.utilisateurs.__dict__["utilisateurs"][self.id_select].__dict__[
                "prenom"
            ]
        )
        self.pau_entry_prenom = Entry(
            self.pau_label_frame2, width=30, textvariable=mon_entree1
        )
        self.pau_entry_prenom.place(relx=0.35, rely=0.12)
        # Champs de saisi du nom
        mon_entree2 = StringVar()
        # Récupération de la valeur par défaut
        mon_entree2.set(
            self.utilisateurs.__dict__["utilisateurs"][self.id_select].__dict__["nom"]
        )
        self.pau_entry_nom = Entry(
            self.pau_label_frame2, width=30, textvariable=mon_entree2
        )
        self.pau_entry_nom.place(relx=0.35, rely=0.42)
        # Champs de saisi du mail
        mon_entree3 = StringVar()
        # Récupération de la valeur par défaut
        mon_entree3.set(
            self.utilisateurs.__dict__["utilisateurs"][self.id_select].__dict__["email"]
        )
        self.pau_entry_mail = Entry(
            self.pau_label_frame2, width=30, textvariable=mon_entree3
        )
        self.pau_entry_mail.place(relx=0.35, rely=0.77)

        self.pau_text_frame3 = Label(
            self.pau_label_frame, text="Options de vols", font=("Arial_black", 12)
        )
        self.pau_text_frame3.place(relx=0.6, rely=0.025)
        self.pau_label_frame3 = LabelFrame(
            self.pau_label_frame, width=300, height=200, bg="#a4a1a3", relief=SUNKEN
        )
        self.pau_label_frame3.place(relx=0.6, rely=0.08)

        self.pau_check_suiviedevol = Checkbutton(
            self.pau_label_frame3,
            text="Suivie de vol par mail",
            font=("Arail", 14, "bold"),
            bg="#a4a1a3",
        )
        self.pau_check_suiviedevol.place(relx=0.1, rely=0.1)
        self.pau_check_coordonnees = Checkbutton(
            self.pau_label_frame3, text="Coordonnées", font=("Arail", 14), bg="#a4a1a3"
        )
        self.pau_check_coordonnees.place(relx=0.2, rely=0.25)
        self.pau_check_altitude = Checkbutton(
            self.pau_label_frame3, text="Altitude", font=("Arail", 14), bg="#a4a1a3"
        )
        self.pau_check_altitude.place(relx=0.2, rely=0.4)
        self.pau_check_vitesse = Checkbutton(
            self.pau_label_frame3, text="Vitesse", font=("Arail", 14), bg="#a4a1a3"
        )
        self.pau_check_vitesse.place(relx=0.2, rely=0.55)
        self.pau_check_batterie = Checkbutton(
            self.pau_label_frame3,
            text="Charge batterie",
            font=("Arail", 14),
            bg="#a4a1a3",
        )
        self.pau_check_batterie.place(relx=0.2, rely=0.7)
        self.pau_check_photo = Checkbutton(
            self.pau_label_frame3, text="Photos", font=("Arail", 14), bg="#a4a1a3"
        )
        self.pau_check_photo.place(relx=0.2, rely=0.85)

        self.pau_text_frame4 = Label(
            self.pau_label_frame,
            text="Paramètres de vol favoris",
            font=("Arial_black", 12),
        )
        self.pau_text_frame4.place(relx=0.1, rely=0.48)
        self.pau_label_frame4 = LabelFrame(
            self.pau_label_frame, width=700, height=200, bg="#a4a1a3", relief=SUNKEN
        )
        self.pau_label_frame4.place(relx=0.1, rely=0.53)

        self.pau_text_vitesse = Label(
            self.pau_label_frame4,
            text="Vitesse",
            font=("Arail", 14, "bold"),
            bg="#a4a1a3",
        )
        self.pau_text_vitesse.place(relx=0.05, rely=0.1)
        self.pau_text_latitudebase = Label(
            self.pau_label_frame4,
            text="Latitude \n base",
            font=("Arail", 14, "bold"),
            bg="#a4a1a3",
        )
        self.pau_text_latitudebase.place(relx=0.05, rely=0.35)
        self.pau_text_longitudebase = Label(
            self.pau_label_frame4,
            text="Longitude \n base",
            font=("Arail", 14, "bold"),
            bg="#a4a1a3",
        )
        self.pau_text_longitudebase.place(relx=0.04, rely=0.65)
        self.pau_text_modecam = Label(
            self.pau_label_frame4,
            text="Mode caméra",
            font=("Arail", 14, "bold"),
            bg="#a4a1a3",
        )
        self.pau_text_modecam.place(relx=0.6, rely=0.35)

        # Champs de saisi de la vitesse
        mon_entree4 = StringVar()
        # Récupération de la valeur par défaut
        mon_entree4.set(
            self.utilisateurs.__dict__["utilisateurs"][self.id_select].__dict__[
                "vitesse"
            ]
        )
        self.pau_entry_vitesse = Entry(
            self.pau_label_frame4, width=30, textvariable=mon_entree4
        )
        self.pau_entry_vitesse.place(relx=0.2, rely=0.12)
        # Champs de saisi de la latitude
        mon_entree5 = StringVar()
        # Récupération de la valeur par défaut
        mon_entree5.set(
            self.utilisateurs.__dict__["utilisateurs"][self.id_select].__dict__[
                "latitude_base"
            ]
        )
        self.pau_entry_latitudebase = Entry(
            self.pau_label_frame4, width=30, textvariable=mon_entree5
        )
        self.pau_entry_latitudebase.place(relx=0.2, rely=0.42)
        # Champs de saisi de la longitude
        mon_entree6 = StringVar()
        # Récupération de la valeur par défaut
        mon_entree6.set(
            self.utilisateurs.__dict__["utilisateurs"][self.id_select].__dict__[
                "longitude_base"
            ]
        )
        self.pau_entry_longitude = Entry(
            self.pau_label_frame4, width=30, textvariable=mon_entree6
        )
        self.pau_entry_longitude.place(relx=0.2, rely=0.72)

        self.pau_modecam_photo_check = Checkbutton(
            self.pau_label_frame4, text="Photo", font=("Arail", 14), bg="#a4a1a3"
        )
        self.pau_modecam_photo_check.place(relx=0.8, rely=0.35)
        self.pau_modecam_video_check = Checkbutton(
            self.pau_label_frame4, text="Vidéo", font=("Arail", 14), bg="#a4a1a3"
        )
        self.pau_modecam_video_check.place(relx=0.8, rely=0.55)

        self.pau_boutton = Button(
            self.pau_label_frame,
            text="Enregistrer les informations",
            font=("Arial_black", 12),
            width=22,
            height=2,
            bg="#ffffff",
            command=lambda: [
                self.GetInfoModifUtilisateur(),
                self.BouttonEnregistrerInfo(),
            ],
        )  # Bouton qui permet d'executer les méthode GetInfoModifUtilisateur et BouttonEnregistrerInfo
        self.pau_boutton.place(relx=0.4, rely=0.9)

    def GetInfoUtilisateur(
        self,
    ):  # Methode qui permet de retourner les infos d'un utilisateur entrer dans les entry de la methode ParamAjouterUtilisateur
        prenom = self.pau_entry_prenom.get()
        nom = self.pau_entry_nom.get()
        mail = self.pau_entry_mail.get()
        pauvitesse = self.pau_entry_vitesse.get()
        paulatitude = self.pau_entry_latitudebase.get()
        paulongitude = self.pau_entry_longitude.get()
        # Création de l'objet utilisateur
        CreationUtilisateur(
            self.Donnees,
            self.id,
            self.utilisateurs,
            prenom,
            nom,
            mail,
            paulatitude,
            paulongitude,
            pauvitesse,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        )

    def GetInfoModifUtilisateur(
        self,
    ):  # Methode qui permet de retourner les infos d'un utilisateur modifier dans les entry de la methode ParamModifierUtilisateur
        prenom = self.pau_entry_prenom.get()
        nom = self.pau_entry_nom.get()
        mail = self.pau_entry_mail.get()
        pauvitesse = self.pau_entry_vitesse.get()
        paulatitude = self.pau_entry_latitudebase.get()
        paulongitude = self.pau_entry_longitude.get()
        # Modification de l'objet utilisateur
        ModificationUtilisateur(
            self.utilisateurs,
            self.id_select,
            prenom,
            nom,
            mail,
            paulatitude,
            paulongitude,
            pauvitesse,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        )

    def BouttonEnregistrerInfo(
        self,
    ):  # Methode présente pour supprimer les widgets de la fenetre en cours d'exécution et appeler ceux de l'Etape2_parametre (appeler grace au bouton ajouter et modif utisateur)
        for i in self.winfo_children():
            i.destroy()
        self.Menu()
        self.Etape2_parametre()

    def Etape3_Mission(self):
        # Récupération des utilisateurs
        donnees = Initialisation()
        self.Donnees = donnees[2]
        self.id = donnees[1]
        self.utilisateurs = donnees[0]
        # Compte le nombre d'instances utilisateur
        self.nombre_utilisateurs = len(self.utilisateurs.__dict__["utilisateurs"])
        # Récupération des id
        self.liste_id = []
        for x in self.utilisateurs.__dict__["utilisateurs"]:
            self.liste_id.append(
                self.utilisateurs.__dict__["utilisateurs"][x].__dict__["id_utilisateur"]
            )

        # Initilisation variable
        self.id_select = None

        # Création de la fenêtre
        self.mission_frame_principale = Frame(self, width=870, height=550)
        self.mission_frame_principale.place(relx=0.25, rely=0.25)

        # Liste des utilisateurs
        self.mission_listeutilisateur = Label(
            self.mission_frame_principale,
            text="Liste Utilisateurs",
            font=("Arial", 14, "bold"),
        )
        self.mission_listeutilisateur.place(relx=0.15, rely=0.01)
        self.mission_frame1 = Frame(
            self.mission_frame_principale, width=500, height=250, bg="#a4a1a3"
        )
        self.mission_frame1.place(relx=0.15, rely=0.06)

        # Bouton utilisateur 1
        if self.nombre_utilisateurs != 0:
            state1 = "normal"  # définit l'état du bouton en actif
            name_1 = self.utilisateurs.__dict__["utilisateurs"][
                self.liste_id[0]
            ].__dict__["prenom"]
        else:
            state1 = "disabled"  # définit l'état du bouton sur non actif
            name_1 = "Utilisateur 1"
        self.param_boutton_utilisateur1 = Button(
            self.mission_frame1,
            text=name_1,
            font=("Arial_black", 16),
            bg="#ffffff",
            width=15,
            height=2,
            state=state1,
            command=lambda: self.BoutonSelectionne2(name_1, self.liste_id[0], 0),
        )
        self.param_boutton_utilisateur1.place(relx=0.08, rely=0.2)

        # Bouton utilisateur 2
        if self.nombre_utilisateurs > 1:
            state2 = "normal"
            name_2 = self.utilisateurs.__dict__["utilisateurs"][
                self.liste_id[1]
            ].__dict__["prenom"]
        else:
            state2 = "disabled"
            name_2 = "Utilisateur 2"
        self.param_boutton_utilisateur2 = Button(
            self.mission_frame1,
            text=name_2,
            font=("Arial_black", 16),
            bg="#ffffff",
            width=15,
            height=2,
            state=state2,
            command=lambda: self.BoutonSelectionne2(name_2, self.liste_id[1], 1),
        )
        self.param_boutton_utilisateur2.place(relx=0.55, rely=0.2)

        # Bouton utilisateur 3
        if self.nombre_utilisateurs > 2:
            state3 = "normal"  # définit l'état du bouton en actif
            name_3 = self.utilisateurs.__dict__["utilisateurs"][
                self.liste_id[2]
            ].__dict__["prenom"]
        else:
            state3 = "disabled"  # définit l'état du bouton sur non actif
            name_3 = "Utilisateur 3"
        self.param_boutton_utilisateur3 = Button(
            self.mission_frame1,
            text=name_3,
            font=("Arial_black", 16),
            bg="#ffffff",
            width=15,
            height=2,
            state=state3,
            command=lambda: self.BoutonSelectionne2(name_3, self.liste_id[2], 2),
        )
        self.param_boutton_utilisateur3.place(relx=0.08, rely=0.6)

        # Bouton utilisateur 4
        if self.nombre_utilisateurs > 3:
            state4 = "normal"
            name_4 = self.utilisateurs.__dict__["utilisateurs"][
                self.liste_id[3]
            ].__dict__["prenom"]
        else:
            state4 = "disabled"
            name_4 = "Utilisateur 4"
        self.param_boutton_utilisateur4 = Button(
            self.mission_frame1,
            text=name_4,
            font=("Arial_black", 16),
            bg="#ffffff",
            width=15,
            height=2,
            state=state4,
            command=lambda: self.BoutonSelectionne2(name_4, self.liste_id[3], 3),
        )
        self.param_boutton_utilisateur4.place(relx=0.55, rely=0.6)

        # Utilisateur sélectionné
        self.mission_utilisateurselectionne = Label(
            self.mission_frame_principale,
            text="Aucun utilisateur sélectionné",
            font=("Arial", 14, "bold"),
        )
        self.mission_utilisateurselectionne.place(relx=0.22, rely=0.565)
        self.mission_labelframe = LabelFrame(
            self.mission_frame_principale, width=400, height=200, borderwidth=3
        )
        self.mission_labelframe.place(relx=0.22, rely=0.62)
        self.mission_boutton1 = Button(
            self.mission_labelframe,
            text="Visualiser les missions",
            font=("Arial", 12, "bold"),
            width=30,
            height=2,
            command=self.BouttonVisualiserLesMissions,
        )
        self.mission_boutton1.place(relx=0.12, rely=0.18)
        self.mission_boutton2 = Button(
            self.mission_labelframe,
            text="Créer une mission",
            font=("Arial", 12, "bold"),
            width=30,
            height=2,
            command=self.BouttonCreerUneMission,
        )
        self.mission_boutton2.place(relx=0.12, rely=0.58)

    # Retourne id de l'utilisateur sélectionné
    def BoutonSelectionne2(self, name, id, id_bouton):
        self.mission_utilisateurselectionne.configure(
            text="Utilisateur sélectionné : %s" % name
        )
        self.id_select = id
        self.id_bouton = id_bouton

    def BouttonVisualiserLesMissions(
        self,
    ):  # Méthode présente pour supprimer les widgets de la fenetre en cours d'exécution et appeler ceux de VisualiserLesMission
        if self.id_select != None:
            for i in self.winfo_children():
                i.destroy()
            self.Menu()
            self.VisualiserLesMissions()

    def BouttonCreerUneMission(
        self,
    ):  # Méhtode présente pour supprimer les widgets de la fenetre en cours d'exécution et appeler ceux de CreerUneMission, BouttonBalise1,2,3,4
        if self.id_select != None:
            # Création d'une instance mission
            CreationMission(self.utilisateurs, self.id_select, "", "", 0, 0)
            for i in self.winfo_children():
                i.destroy()
            self.CreerUneMission()
            self.BouttonBalise4()
            self.BouttonBalise3()
            self.BouttonBalise2()
            self.BouttonBalise1()

    def CreerUneMission(self):
        # Récupération des utilisateurs
        donnees = Initialisation()
        self.utilisateurs = donnees[0]

        # Récupération des id missions
        self.liste_id_missions = []
        for x in self.utilisateurs.__dict__["utilisateurs"][self.id_select].__dict__[
            "missions"
        ]:
            self.liste_id_missions.append(
                self.utilisateurs.__dict__["utilisateurs"][self.id_select]
                .__dict__["missions"][x]
                .__dict__["id_mission"]
            )

        # Id de la mission
        self.id_mission = self.liste_id_missions[len(self.liste_id_missions) - 1]

        # Compte le nombre d'instances balise
        self.nombre_balise = len(
            self.utilisateurs.__dict__["utilisateurs"][self.id_select]
            .__dict__["missions"][self.id_mission]
            .__dict__["balises"]
        )

        # Récupération des id balise
        self.liste_id_balises = []
        for x in (
            self.utilisateurs.__dict__["utilisateurs"][self.id_select]
            .__dict__["missions"][self.id_mission]
            .__dict__["balises"]
        ):
            self.liste_id_balises.append(
                self.utilisateurs.__dict__["utilisateurs"][self.id_select]
                .__dict__["missions"][self.id_mission]
                .__dict__["balises"][x]
                .__dict__["id_balise"]
            )

        # Id de la balise
        try:
            self.id_balise = self.liste_id_balises[self.nombre_balise - 1]
        except:
            pass

        self.cumission_labelframe = LabelFrame(
            self,
            text="Mission n°%s" % len(self.liste_id_missions),
            font=("Arial_black", 12),
            width=870,
            height=500,
            borderwidth=3,
        )  # LabelFrame comprenant tous les widgets et Frame de la fenetre
        self.cumission_labelframe.place(relx=0.25, rely=0.25)
        self.cumission_label1 = Label(
            self.cumission_labelframe,
            text="Déroulée de la mission",
            font=("Arial", 12, "bold"),
        )
        self.cumission_label1.place(relx=0.05, rely=0.008)
        self.cumission_labelframe1 = LabelFrame(
            self.cumission_labelframe,
            width=250,
            height=370,
            bg="#a4a1a3",
            relief=SUNKEN,
        )  # LabelFrame comprenant les différentes balises de la mission avec l'atterissage et le decollage
        self.cumission_labelframe1.place(relx=0.05, rely=0.05)
        self.cumission_boutton_decollage = Button(
            self.cumission_labelframe1,
            text="Décollage",
            font=("Arial", 12),
            width=20,
            height=2,
            state="disabled",
        )

        self.cumission_boutton_atterissage = Button(
            self.cumission_labelframe1,
            text="Atterissage",
            font=("Arial", 12),
            width=20,
            height=2,
            state="disabled",
        )
        self.cumission_boutton_atterissage.place(relx=0.1, rely=0.87)

        self.cumission_boutton_enregistrer = Button(
            self.cumission_labelframe,
            text="Enregistrer les informations",
            font=("Arial", 12),
            bg="#ffffff",
            width=30,
            height=2,
            command=self.BouttonEnregistrerInfo2,
        )  # Bouton permettant d'executer les méthodes GetCreerUnemission et BoutonEnregistrerInfo2
        self.cumission_boutton_enregistrer.place(relx=0.575, rely=0.85)

    def BouttonBalise1(self):
        # Bouton Balise 1: permet de rajouter une étape à la mission en entrant de nouveaux parametres(longitude, latitude, altitude, vitesse, pause)
        self.cumission_boutton_decollage.place(relx=0.1, rely=0.02)
        self.cumission_boutton_balise1 = Button(
            self.cumission_labelframe1,
            text="Balise 1",
            font=("Arial", 12),
            width=20,
            height=2,
            command=lambda: self.BoutonSelectionne3(1),
        )
        self.cumission_boutton_balise1.place(relx=0.1, rely=0.19)

        self.balise1_babel3 = Label(
            self.cumission_labelframe, text="Balise 1", font=("Arial", 12, "bold")
        )
        self.balise1_babel3.place(relx=0.5, rely=0.008)

        self.balise1_labelframe2 = LabelFrame(
            self.cumission_labelframe, width=400, height=370, borderwidth=3
        )
        self.balise1_labelframe2.place(relx=0.5, rely=0.05)

        # Champs de saisi latitude
        mon_entree1 = StringVar()
        # Récupération de la valeur par défaut
        try:
            mon_entree1.set(
                self.utilisateurs.__dict__["utilisateurs"][self.id_select]
                .__dict__["missions"][self.id_mission]
                .__dict__["balises"][self.id_balise]
                .__dict__["latitude"]
            )
        except:
            mon_entree1.set("")
        self.balise1_label_latitude = Label(
            self.balise1_labelframe2, text="Latitude (en °):", font=("Arial", 12)
        )
        self.balise1_label_latitude.place(relx=0.1, rely=0.08)
        self.balise1_entry_latitude = Entry(
            self.balise1_labelframe2, width=30, textvariable=mon_entree1
        )
        self.balise1_entry_latitude.place(relx=0.45, rely=0.09)

        # Champs de saisi longitude
        mon_entree2 = StringVar()
        # Récupération de la valeur par défaut
        try:
            mon_entree2.set(
                self.utilisateurs.__dict__["utilisateurs"][self.id_select]
                .__dict__["missions"][self.id_mission]
                .__dict__["balises"][self.id_balise]
                .__dict__["longitude"]
            )
        except:
            mon_entree2.set("")
        self.balise1_label_longitude = Label(
            self.balise1_labelframe2, text="Longitude (en °) :", font=("Arial", 12)
        )
        self.balise1_label_longitude.place(relx=0.1, rely=0.2)
        self.balise1_entry_longitude = Entry(
            self.balise1_labelframe2, width=30, textvariable=mon_entree2
        )
        self.balise1_entry_longitude.place(relx=0.45, rely=0.21)

        # Champs de saisi vitesse
        mon_entree3 = StringVar()
        # Récupération de la valeur par défaut
        try:
            mon_entree3.set(
                self.utilisateurs.__dict__["utilisateurs"][self.id_select]
                .__dict__["missions"][self.id_mission]
                .__dict__["balises"][self.id_balise]
                .__dict__["altitude"]
            )
        except:
            mon_entree3.set("")
        self.balise1_label_altitude = Label(
            self.balise1_labelframe2, text="Altitude (en m) :", font=("Arial", 12)
        )
        self.balise1_label_altitude.place(relx=0.1, rely=0.33)

        self.balise1_entry_altitude = Spinbox(
            self.balise1_labelframe2, from_=0, to=100, justify=CENTER, width=30
        )
        self.balise1_entry_altitude.place(relx=0.45, rely=0.34)

        # Champs de saisi vitesse
        mon_entree4 = StringVar()
        # Récupération de la valeur par défaut
        try:
            mon_entree4.set(
                self.utilisateurs.__dict__["utilisateurs"][self.id_select]
                .__dict__["missions"][self.id_mission]
                .__dict__["balises"][self.id_balise]
                .__dict__["vitesse"]
            )
        except:
            mon_entree4.set("")
        self.balise1_label_vitesse = Label(
            self.balise1_labelframe2, text="vitesse(en %) :", font=("Arial", 12)
        )
        self.balise1_label_vitesse.place(relx=0.1, rely=0.48)

        self.balise1_entry_vitesse = Spinbox(
            self.balise1_labelframe2, from_=0, to=100, justify=CENTER, width=30
        )
        self.balise1_entry_vitesse.place(relx=0.45, rely=0.49)
        self.balise1_label_pause = Label(
            self.balise1_labelframe2, text="pause(en s) :", font=("Arial", 12)
        )
        self.balise1_label_pause.place(relx=0.1, rely=0.63)
        self.balise1_entry_pause = Spinbox(
            self.balise1_labelframe2, from_=0, to=120, justify=CENTER, width=30
        )
        self.balise1_entry_pause.place(relx=0.45, rely=0.64)
        self.balise1_label_photo = Label(
            self.balise1_labelframe2, text="photo :", font=("Arial", 12)
        )
        self.balise1_label_photo.place(relx=0.1, rely=0.79)
        self.balise1_checkbutton_photo_oui = Checkbutton(
            self.balise1_labelframe2, text="Oui", font=("Arail", 12)
        )
        self.balise1_checkbutton_photo_oui.place(relx=0.75, rely=0.75)
        self.balise1_checkbutton_photo_non = Checkbutton(
            self.balise1_labelframe2, text="Non", font=("Arail", 12)
        )
        self.balise1_checkbutton_photo_non.place(relx=0.75, rely=0.83)

        # Rajouter une étape
        if self.nombre_balise != 3:
            self.cumission_label2 = Label(
                self.cumission_labelframe,
                text="Rajouter une étape",
                font=("Arial", 12, "bold"),
            )
            self.cumission_label2.place(relx=0.1, rely=0.84)
            self.cumission_boutton_etape = Button(
                self.cumission_labelframe,
                text="+",
                font=("Arial", 16, "bold"),
                width=10,
                bg="#a4a1a3",
                command=lambda: [self.GetBalise1(), self.BouttonBalise2()],
            )  # Bouton permettant de rendre les différents boutons des balises actifs (auparavant inactifs)
            self.cumission_boutton_etape.place(relx=0.1, rely=0.89)

    def BouttonBalise2(self):
        # Bouton Balise 2: permet de rajouter une étape à la mission en entrant de nouveaux parametres(longitude, latitude, altitude, vitesse, pause)
        if self.nombre_balise >= 1:
            state2 = "normal"  # définit l'état du bouton en actif
        else:
            state2 = "disabled"  # définit l'état du bouton en actif
        self.boutton_nouvelle_etape_2 = Button(
            self.cumission_labelframe1,
            text="Balise 2",
            font=("Arial", 12),
            width=20,
            height=2,
            state=state2,
            command=lambda: self.BoutonSelectionne3(2),
        )
        self.boutton_nouvelle_etape_2.place(relx=0.1, rely=0.36)

        self.balise2_babel3 = Label(
            self.cumission_labelframe, text="Balise 2", font=("Arial", 12, "bold")
        )
        self.balise2_babel3.place(relx=0.5, rely=0.008)
        self.balise2_labelframe2 = LabelFrame(
            self.cumission_labelframe, width=400, height=370, borderwidth=3
        )
        self.balise2_labelframe2.place(relx=0.5, rely=0.05)
        self.balise2_label_latitude = Label(
            self.balise2_labelframe2, text="Latitude (en °) :", font=("Arial", 12)
        )
        self.balise2_label_latitude.place(relx=0.1, rely=0.08)
        self.balise2_entry_latitude = Entry(self.balise2_labelframe2, width=30)
        self.balise2_entry_latitude.place(relx=0.45, rely=0.09)
        self.balise2_label_longitude = Label(
            self.balise2_labelframe2, text="Longitude (en °) :", font=("Arial", 12)
        )
        self.balise2_label_longitude.place(relx=0.1, rely=0.2)
        self.balise2_entry_longitude = Entry(self.balise2_labelframe2, width=30)
        self.balise2_entry_longitude.place(relx=0.45, rely=0.21)
        self.balise2_label_altitude = Label(
            self.balise2_labelframe2, text="Altitude (en m) :", font=("Arial", 12)
        )
        self.balise2_label_altitude.place(relx=0.1, rely=0.33)
        self.balise2_entry_altitude = Spinbox(
            self.balise2_labelframe2, from_=0, to=100, justify=CENTER, width=30
        )
        self.balise2_entry_altitude.place(relx=0.45, rely=0.34)
        self.balise2_label_vitesse = Label(
            self.balise2_labelframe2, text="vitesse(en %) :", font=("Arial", 12)
        )
        self.balise2_label_vitesse.place(relx=0.1, rely=0.48)
        self.balise2_entry_vitesse = Spinbox(
            self.balise2_labelframe2, from_=0, to=100, justify=CENTER, width=30
        )
        self.balise2_entry_vitesse.place(relx=0.45, rely=0.49)
        self.balise2_label_pause = Label(
            self.balise2_labelframe2, text="pause(en s) :", font=("Arial", 12)
        )
        self.balise2_label_pause.place(relx=0.1, rely=0.63)
        self.balise2_entry_pause = Spinbox(
            self.balise2_labelframe2, from_=0, to=120, justify=CENTER, width=30
        )
        self.balise2_entry_pause.place(relx=0.45, rely=0.64)
        self.balise2_label_photo = Label(
            self.balise2_labelframe2, text="photo :", font=("Arial", 12)
        )
        self.balise2_label_photo.place(relx=0.1, rely=0.79)
        self.balise2_checkbutton_photo_oui = Checkbutton(
            self.balise2_labelframe2, text="Oui", font=("Arail", 12)
        )
        self.balise2_checkbutton_photo_oui.place(relx=0.75, rely=0.75)
        self.balise2_checkbutton_photo_non = Checkbutton(
            self.balise2_labelframe2, text="Non", font=("Arail", 12)
        )
        self.balise2_checkbutton_photo_non.place(relx=0.75, rely=0.83)

        if self.nombre_balise != 3:
            # Rajouter une étape
            self.cumission_label2_bis = Label(
                self.cumission_labelframe,
                text="Rajouter une étape",
                font=("Arial", 12, "bold"),
            )
            self.cumission_label2_bis.place(relx=0.1, rely=0.84)
            self.cumission_boutton_etape_bis = Button(
                self.cumission_labelframe,
                text="+",
                font=("Arial", 16, "bold"),
                width=10,
                bg="#a4a1a3",
                command=lambda: [self.GetBalise2(), self.BouttonBalise3()],
            )  # Bouton permettant de rendre les différents boutons des balises actifs (auparavant inactifs)
            self.cumission_boutton_etape_bis.place(relx=0.1, rely=0.89)

    def BouttonBalise3(self):
        # Bouton Balise 3: permet de rajouter une étape à la mission en entrant de nouveaux parametres(longitude, latitude, altitude, vitesse, pause)
        if self.nombre_balise >= 2:
            state3 = "normal"
        else:
            state3 = "disabled"
        self.boutton_nouvelle_etape_3 = Button(
            self.cumission_labelframe1,
            text="Balise 3",
            font=("Arial", 12),
            width=20,
            height=2,
            state=state3,
            command=lambda: self.BoutonSelectionne3(self.liste_id_missions[2], 3),
        )
        self.boutton_nouvelle_etape_3.place(relx=0.1, rely=0.53)

        self.balise3_babel3 = Label(
            self.cumission_labelframe, text="Balise 3", font=("Arial", 12, "bold")
        )
        self.balise3_babel3.place(relx=0.5, rely=0.008)
        self.balise3_labelframe2 = LabelFrame(
            self.cumission_labelframe, width=400, height=370, borderwidth=3
        )
        self.balise3_labelframe2.place(relx=0.5, rely=0.05)
        self.balise3_label_latitude = Label(
            self.balise3_labelframe2, text="Latitude (en °) :", font=("Arial", 12)
        )
        self.balise3_label_latitude.place(relx=0.1, rely=0.08)
        self.balise3_entry_latitude = Entry(self.balise3_labelframe2, width=30)
        self.balise3_entry_latitude.place(relx=0.45, rely=0.09)
        self.balise3_label_longitude = Label(
            self.balise3_labelframe2, text="Longitude (en °) :", font=("Arial", 12)
        )
        self.balise3_label_longitude.place(relx=0.1, rely=0.2)
        self.balise3_entry_longitude = Entry(self.balise3_labelframe2, width=30)
        self.balise3_entry_longitude.place(relx=0.45, rely=0.21)
        self.balise3_label_altitude = Label(
            self.balise3_labelframe2, text="Altitude (en m) :", font=("Arial", 12)
        )
        self.balise3_label_altitude.place(relx=0.1, rely=0.33)
        self.balise3_entry_altitude = Spinbox(
            self.balise3_labelframe2, from_=0, to=100, justify=CENTER, width=30
        )
        self.balise3_entry_altitude.place(relx=0.45, rely=0.34)
        self.balise3_label_vitesse = Label(
            self.balise3_labelframe2, text="vitesse(en %) :", font=("Arial", 12)
        )
        self.balise3_label_vitesse.place(relx=0.1, rely=0.48)
        self.balise3_entry_vitesse = Spinbox(
            self.balise3_labelframe2, from_=0, to=100, justify=CENTER, width=30
        )
        self.balise3_entry_vitesse.place(relx=0.45, rely=0.49)
        self.balise3_label_pause = Label(
            self.balise3_labelframe2, text="pause(en s) :", font=("Arial", 12)
        )
        self.balise3_label_pause.place(relx=0.1, rely=0.63)
        self.balise3_entry_pause = Spinbox(
            self.balise3_labelframe2, from_=0, to=120, justify=CENTER, width=30
        )
        self.balise3_entry_pause.place(relx=0.45, rely=0.64)
        self.balise3_label_photo = Label(
            self.balise3_labelframe2, text="photo :", font=("Arial", 12)
        )
        self.balise3_label_photo.place(relx=0.1, rely=0.79)
        self.balise3_checkbutton_photo_oui = Checkbutton(
            self.balise3_labelframe2, text="Oui", font=("Arail", 12)
        )
        self.balise3_checkbutton_photo_oui.place(relx=0.75, rely=0.75)
        self.balise3_checkbutton_photo_non = Checkbutton(
            self.balise3_labelframe2, text="Non", font=("Arail", 12)
        )
        self.balise3_checkbutton_photo_non.place(relx=0.75, rely=0.83)

        if self.nombre_balise != 3:
            # Rajouter une étape
            self.cumission_label2_bis2 = Label(
                self.cumission_labelframe,
                text="Rajouter une étape",
                font=("Arial", 12, "bold"),
            )
            self.cumission_label2_bis2.place(relx=0.1, rely=0.84)
            self.cumission_boutton_etape_bis2 = Button(
                self.cumission_labelframe,
                text="+",
                font=("Arial", 16, "bold"),
                width=10,
                bg="#a4a1a3",
                command=lambda: [self.GetBalise3(), self.BouttonBalise4()],
            )  # Bouton permettant de rendre les différents boutons des balises actifs (auparavant inactifs)
            self.cumission_boutton_etape_bis2.place(relx=0.1, rely=0.89)

    def BouttonBalise4(self):
        # Bouton Balise 4: permet de rajouter une étape à la mission en entrant de nouveaux parametres(longitude, latitude, altitude, vitesse, pause)
        if self.nombre_balise == 3:
            state4 = "normal"
        else:
            state4 = "disabled"
        self.boutton_nouvelle_etape_4 = Button(
            self.cumission_labelframe1,
            text="Balise 4",
            font=("Arial", 12),
            width=20,
            height=2,
            state=state4,
            command=lambda: self.BoutonSelectionne3(self.liste_id_missions[3], 4),
        )
        self.boutton_nouvelle_etape_4.place(relx=0.1, rely=0.70)

        self.balise4_babel3 = Label(
            self.cumission_labelframe, text="Balise 4", font=("Arial", 12, "bold")
        )
        self.balise4_babel3.place(relx=0.5, rely=0.008)
        self.balise4_labelframe2 = LabelFrame(
            self.cumission_labelframe, width=400, height=370, borderwidth=3
        )
        self.balise4_labelframe2.place(relx=0.5, rely=0.05)
        self.balise4_label_latitude = Label(
            self.balise4_labelframe2, text="Latitude (en °) :", font=("Arial", 12)
        )
        self.balise4_label_latitude.place(relx=0.1, rely=0.08)
        self.balise4_entry_latitude = Entry(self.balise4_labelframe2, width=30)
        self.balise4_entry_latitude.place(relx=0.45, rely=0.09)
        self.balise4_label_longitude = Label(
            self.balise4_labelframe2, text="Longitude (en °) :", font=("Arial", 12)
        )
        self.balise4_label_longitude.place(relx=0.1, rely=0.2)
        self.balise4_entry_longitude = Entry(self.balise4_labelframe2, width=30)
        self.balise4_entry_longitude.place(relx=0.45, rely=0.21)
        self.balise4_label_altitude = Label(
            self.balise4_labelframe2, text="Altitude (en m) :", font=("Arial", 12)
        )
        self.balise4_label_altitude.place(relx=0.1, rely=0.33)
        self.balise4_entry_altitude = Spinbox(
            self.balise4_labelframe2, from_=0, to=100, justify=CENTER, width=30
        )
        self.balise4_entry_altitude.place(relx=0.45, rely=0.34)
        self.balise4_label_vitesse = Label(
            self.balise4_labelframe2, text="vitesse(en %) :", font=("Arial", 12)
        )
        self.balise4_label_vitesse.place(relx=0.1, rely=0.48)
        self.balise4_entry_vitesse = Spinbox(
            self.balise4_labelframe2, from_=0, to=100, justify=CENTER, width=30
        )
        self.balise4_entry_vitesse.place(relx=0.45, rely=0.49)
        self.balise4_label_pause = Label(
            self.balise4_labelframe2, text="pause(en s) :", font=("Arial", 12)
        )
        self.balise4_label_pause.place(relx=0.1, rely=0.63)
        self.balise4_entry_pause = Spinbox(
            self.balise4_labelframe2, from_=0, to=120, justify=CENTER, width=30
        )
        self.balise4_entry_pause.place(relx=0.45, rely=0.64)
        self.balise4_label_photo = Label(
            self.balise4_labelframe2, text="photo :", font=("Arial", 12)
        )
        self.balise4_label_photo.place(relx=0.1, rely=0.79)
        self.balise4_checkbutton_photo_oui = Checkbutton(
            self.balise4_labelframe2, text="Oui", font=("Arail", 12)
        )
        self.balise4_checkbutton_photo_oui.place(relx=0.75, rely=0.75)
        self.balise4_checkbutton_photo_non = Checkbutton(
            self.balise4_labelframe2, text="Non", font=("Arail", 12)
        )
        self.balise4_checkbutton_photo_non.place(relx=0.75, rely=0.83)

        # Enregistrer les modifications
        self.cumission_boutton_enregistrer_2 = Button(
            self.cumission_labelframe,
            text="Enregistrer les informations test",
            font=("Arial", 12),
            bg="#ffffff",
            width=30,
            height=2,
            command=lambda: [self.GetBalise4(), self.BouttonEnregistrerInfo2()],
        )  # Bouton permettant d'executer les méthodes GetCreerUnemission et BoutonEnregistrerInfo2
        self.cumission_boutton_enregistrer_2.place(relx=0.575, rely=0.85)

    def GetBalise1(
        self,
    ):  # Methode qui permet de retourner les valeurs des entry de la balise 1
        balise1latitude = self.balise1_entry_latitude.get()
        balise1longitude = self.balise1_entry_longitude.get()
        balise1altitude = self.balise1_entry_altitude.get()
        balise1vitesse = self.balise1_entry_vitesse.get()
        balise1pause = self.balise1_entry_pause.get()
        CreationBalise(
            self.utilisateurs,
            self.id_select,
            self.id_mission,
            balise1latitude,
            balise1longitude,
            balise1altitude,
            balise1vitesse,
            balise1pause,
            0,
        )
        self.CreerUneMission()
        self.BouttonBalise4()
        self.BouttonBalise3()
        self.BouttonBalise2()
        self.BouttonBalise1()

    def GetBalise2(
        self,
    ):  # Methode qui permet de retourner les valeurs des entry de la balise 2
        balise2latitude = self.balise2_entry_latitude.get()
        balise2longitude = self.balise2_entry_longitude.get()
        balise2altitude = self.balise2_entry_altitude.get()
        balise2vitesse = self.balise2_entry_vitesse.get()
        balise2pause = self.balise2_entry_pause.get()
        CreationBalise(
            self.utilisateurs,
            self.id_select,
            self.id_mission,
            balise2latitude,
            balise2longitude,
            balise2altitude,
            balise2vitesse,
            balise2pause,
            0,
        )
        self.CreerUneMission()
        self.BouttonBalise4()
        self.BouttonBalise3()
        self.BouttonBalise2()
        self.BouttonBalise1()

    def GetBalise3(
        self,
    ):  # Methode qui permet de retourner les valeurs des entry de la balise 3
        balise3latitude = self.balise3_entry_latitude.get()
        balise3longitude = self.balise3_entry_longitude.get()
        balise3altitude = self.balise3_entry_altitude.get()
        balise3vitesse = self.balise3_entry_vitesse.get()
        balise3pause = self.balise3_entry_pause.get()
        CreationBalise(
            self.utilisateurs,
            self.id_select,
            self.id_mission,
            balise3latitude,
            balise3longitude,
            balise3altitude,
            balise3vitesse,
            balise3pause,
            0,
        )
        self.CreerUneMission()
        self.BouttonBalise4()
        self.BouttonBalise3()
        self.BouttonBalise2()
        self.BouttonBalise1()

    def GetBalise4(
        self,
    ):  # Methode qui permet de retourner les valeurs des entry de la balise 4
        balise4latitude = self.balise4_entry_latitude.get()
        balise4longitude = self.balise4_entry_longitude.get()
        balise4altitude = self.balise4_entry_altitude.get()
        balise4vitesse = self.balise4_entry_vitesse.get()
        balise4pause = self.balise4_entry_pause.get()
        CreationBalise(
            self.utilisateurs,
            self.id_select,
            self.id_mission,
            balise4latitude,
            balise4longitude,
            balise4altitude,
            balise4vitesse,
            balise4pause,
            0,
        )
        self.CreerUneMission()
        self.BouttonBalise4()
        self.BouttonBalise3()
        self.BouttonBalise2()
        self.BouttonBalise1()

    def BouttonEnregistrerInfo2(
        self,
    ):  # Méhtode présente pour supprimer les widgets de la fenetre en cours d'exécution et appeler ceux de Etape3_Mission et appeler la methode GetBalise4 si id_balise_ajoute ==4
        self.Menu()
        self.Etape3_Mission()

    # Retourne id de l'utilisateur sélectionné
    def BoutonSelectionne3(self, id_bouton):
        self.cumission_labelframe.configure(text="Balise : %s" % id_bouton)
        self.id_bouton = id_bouton
        if self.id_bouton == 1:
            self.BouttonBalise1
        if self.id_bouton == 2:
            self.BouttonBalise2
        if self.id_bouton == 3:
            self.BouttonBalise3
        if self.id_bouton == 4:
            self.BouttonBalise4

    def VisualiserLesMissions(self,):
        # Récupération des utilisateurs
        donnees = Initialisation()
        self.utilisateurs = donnees[0]

        # Récupération des id missions
        self.liste_id_missions = []
        for x in self.utilisateurs.__dict__["utilisateurs"][self.id_select].__dict__[
            "missions"
        ]:
            self.liste_id_missions.append(
                self.utilisateurs.__dict__["utilisateurs"][self.id_select]
                .__dict__["missions"][x]
                .__dict__["id_mission"]
            )

        # Nombre de mission
        self.nombre_missions = len(self.liste_id_missions)

        # Méthode qui permet de visaliser les différentes missions créées par les utilisateurs
        self.vlm_labelframe_utilisateur = LabelFrame(
            self,
            text="",
            font=("Arial_black", 12),
            width=870,
            height=500,
            borderwidth=3,
        )  # LabelFrame qui contient tous les widgets et frames de la page Visualiser les mission
        self.vlm_labelframe_utilisateur.place(relx=0.25, rely=0.25)
        self.vlm_label_listemission = Label(
            self.vlm_labelframe_utilisateur,
            text="Liste des missions",
            font=("Arial", 12, "bold"),
        )
        self.vlm_label_listemission.place(relx=0.08, rely=0.03)
        self.vlm_frame_listemission = LabelFrame(
            self.vlm_labelframe_utilisateur,
            width=200,
            height=350,
            bg="#a4a1a3",
            relief=SUNKEN,
        )  # Frame qui contient tous les boutons des différentes missions (jusqu'à 5)
        self.vlm_frame_listemission.place(relx=0.08, rely=0.08)

        # Bouton mission 1
        if self.nombre_missions >= 1:
            state1 = "normal"
        else:
            state1 = "disabled"
        self.vlm_bouton_mission1 = Button(
            self.vlm_frame_listemission,
            text="Mission 1",
            font=("Arial", 12),
            width=15,
            height=2,
            state=state1,
            command=lambda: self.BoutonSelectionne3(self.liste_id_missions[0], 1),
        )
        self.vlm_bouton_mission1.place(relx=0.12, rely=0.02)

        # Bouton mission 2
        if self.nombre_missions >= 2:
            state2 = "normal"
        else:
            state2 = "disabled"
        self.vlm_bouton_mission2 = Button(
            self.vlm_frame_listemission,
            text="Mission 2",
            font=("Arial", 12),
            width=15,
            height=2,
            state=state2,
            command=lambda: self.BoutonSelectionne3(self.liste_id_missions[1], 2),
        )
        self.vlm_bouton_mission2.place(relx=0.12, rely=0.22)

        # Bouton mission 3
        if self.nombre_missions >= 3:
            state3 = "normal"
        else:
            state3 = "disabled"
        self.vlm_bouton_mission3 = Button(
            self.vlm_frame_listemission,
            text="Mission 3",
            font=("Arial", 12),
            width=15,
            height=2,
            state=state3,
            command=lambda: self.BoutonSelectionne3(self.liste_id_missions[2], 3),
        )
        self.vlm_bouton_mission3.place(relx=0.12, rely=0.42)

        # Bouton mission 4
        if self.nombre_missions >= 4:
            state4 = "normal"
        else:
            state4 = "disabled"
        self.vlm_bouton_mission4 = Button(
            self.vlm_frame_listemission,
            text="Mission 4",
            font=("Arial", 12),
            width=15,
            height=2,
            state=state4,
            command=lambda: self.BoutonSelectionne3(self.liste_id_missions[3], 4),
        )
        self.vlm_bouton_mission4.place(relx=0.12, rely=0.62)

        # Bouton mission 5
        if self.nombre_missions >= 5:
            state5 = "normal"
        else:
            state5 = "disabled"
        self.vlm_bouton_mission5 = Button(
            self.vlm_frame_listemission,
            text="Mission 5",
            font=("Arial", 12),
            width=15,
            height=2,
            state=state5,
            command=lambda: self.BoutonSelectionne3(self.liste_id_missions[4], 5),
        )
        self.vlm_bouton_mission5.place(relx=0.12, rely=0.82)

        # Bouton modifier la mission
        self.vlm_label_modifmission = Label(
            self.vlm_labelframe_utilisateur,
            text="Modifier la mission",
            font=("Arial", 12),
        )
        self.vlm_label_modifmission.place(relx=0.025, rely=0.83)
        self.vlm_boutton_modifmission = Button(
            self.vlm_labelframe_utilisateur,
            text="+",
            font=("Arial", 16, "bold"),
            width=9,
            bg="#a4a1a3",
        )

        # Bouton supprimer la mission
        self.vlm_boutton_modifmission.place(relx=0.03, rely=0.88)
        self.vlm_label_suppmission = Label(
            self.vlm_labelframe_utilisateur,
            text="Supprimer la mission",
            font=("Arial", 12),
        )
        self.vlm_label_suppmission.place(relx=0.21, rely=0.83)
        self.vlm_boutton_suppmission = Button(
            self.vlm_labelframe_utilisateur,
            text="-",
            font=("Arial", 16, "bold"),
            width=9,
            bg="#a4a1a3",
        )

        self.vlm_boutton_suppmission.place(relx=0.22, rely=0.88)
        self.vlm_label_mission = Label(
            self.vlm_labelframe_utilisateur,
            text="Pas de mission sélectionnée",
            font=("Arial", 12, "bold"),
        )
        self.vlm_label_mission.place(relx=0.55, rely=0.03)

        # LabelFrame recapitulatif incluant le bouton lancer mission
        self.vlm_labelframe_mission1 = LabelFrame(
            self.vlm_labelframe_utilisateur, width=350, height=200, borderwidth=3
        )
        self.vlm_labelframe_mission1.place(relx=0.55, rely=0.08)
        self.vlm_label_recap = Label(
            self.vlm_labelframe_mission1,
            text="Récapitulatif",
            font=("Arial", 12, "bold"),
        )
        self.vlm_label_recap.place(relx=0.35, rely=0.01)

        self.pau_check_coordonnees = Label(
            self.vlm_labelframe_mission1, text="Durée : ", font=("Arial", 12)
        )
        self.pau_check_coordonnees.place(relx=0.01, rely=0.15)

        self.vlm_label_nbretape = Label(
            self.vlm_labelframe_mission1, text="Nombre étapes :", font=("Arial", 12)
        )
        self.vlm_label_nbretape.place(relx=0.01, rely=0.30)

        self.vlm_label_modephoto = Label(
            self.vlm_labelframe_mission1, text="Mode photo :", font=("Arial", 12)
        )
        self.vlm_label_modephoto.place(relx=0.01, rely=0.45)

        self.vlm_label_missionplanifiee = Label(
            self.vlm_labelframe_mission1, text="Mission planifiée :", font=("Arial", 12)
        )
        self.vlm_label_missionplanifiee.place(relx=0.01, rely=0.60)

        self.vlm_boutton_lancermission = Button(
            self.vlm_labelframe_mission1,
            text="Lancer la mission",
            font=("Arial", 12),
            bg="#a4a1a3",
            width=30,
            height=1,
            command=self.BouttonLancerMission,
        )
        self.vlm_boutton_lancermission.place(relx=0.1, rely=0.75)

        self.vlm_labelframe_mission2 = LabelFrame(
            self.vlm_labelframe_utilisateur, width=350, height=200, borderwidth=3
        )  # LabelFrame incluant le plannificateur avec le bouton "plannifier la mission"
        self.vlm_labelframe_mission2.place(relx=0.55, rely=0.53)
        self.vlm_label_planif = Label(
            self.vlm_labelframe_mission2,
            text="Planificateur",
            font=("Arial", 12, "bold"),
        )
        self.vlm_label_planif.place(relx=0.35, rely=0.01)
        self.vlm_label_jour = Label(
            self.vlm_labelframe_mission2, text="Jour:", font=("Arial", 12)
        )
        self.vlm_label_jour.place(relx=0.01, rely=0.18)
        self.vlm_entry_jour = Entry(self.vlm_labelframe_mission2, width=30)
        self.vlm_entry_jour.place(relx=0.25, rely=0.19)
        self.vlm_label_heure = Label(
            self.vlm_labelframe_mission2, text="Heure:", font=("Arial", 12)
        )
        self.vlm_label_heure.place(relx=0.01, rely=0.45)
        self.vlm_entry_heure = Entry(self.vlm_labelframe_mission2, width=30)
        self.vlm_entry_heure.place(relx=0.25, rely=0.46)
        self.vlm_boutton_planifiermission = Button(
            self.vlm_labelframe_mission2,
            text="Planifier la mission",
            font=("Arial", 12),
            bg="#a4a1a3",
            width=30,
            height=1,
            command=self.GetVisualiserLesMissions,
        )
        self.vlm_boutton_planifiermission.place(relx=0.1, rely=0.75)

    # Retourne id de la mission sélectionnée
    def BoutonSelectionne3(self, id, id_bouton):
        # Affichage du numéro de mission
        self.vlm_label_mission.configure(text="Mission n°%s" % id_bouton)

        # Récupération des id
        self.id_select_mission = id
        self.id_bouton = id_bouton

        # Affichage de la durée
        self.duree = DureeMission(
            self.utilisateurs, self.id_select, self.id_select_mission
        )
        self.pau_check_coordonnees.configure(text="Durée : %s" % self.duree)

        # Affichage du nombre de balises
        self.nombrebalises = NombreBalises(
            self.utilisateurs, self.id_select, self.id_select_mission
        )
        self.vlm_label_nbretape.configure(
            text="Nombre étapes : %s" % self.nombrebalises
        )

        # Affichage du mode photo
        self.modephoto = ModePhoto(
            self.utilisateurs, self.id_select, self.id_select_mission
        )
        self.vlm_label_modephoto.configure(text="Mode photo : %s" % self.modephoto)

        # Affichage de la planification
        self.planification = MissionPlanifiee(
            self.utilisateurs, self.id_select, self.id_select_mission
        )
        self.vlm_label_missionplanifiee.configure(
            text="Mission planifiée : %s" % self.planification
        )

    def GetVisualiserLesMissions(
        self,
    ):  # Methode qui permet de retouner les valeurs des entry (zones de saisie)
        self.id = self.id_select_mission
        vlmjour = self.vlm_entry_jour.get()
        vlmheure = self.vlm_entry_heure.get()
        # Mise à jour de la mission
        ModificationMission(
            self.utilisateurs, self.id_select, self.id, vlmjour, vlmheure, 1, 0
        )
        self.VisualiserLesMissions()

    def BouttonLancerMission(self,):
        self.id = self.id_select_mission
        CoordonneesBase(
            self.utilisateurs, self.id_select,
        )
        ExecutionMission(self.utilisateurs, self.id_select, self.id)
        # Méthode présente pour supprimer les widgets de la fenetre en cours d'exécution et appeler ceux de ExecutionMission
        for i in self.winfo_children():
            i.destroy()
        self.Menu()
        self.ExecutionMission()

    def ExecutionMission(
        self,
    ):  # Méthode qui permet de visualiser la mission en vidéo en ayant des informations en temps réel sur le vol

        self.execmission_frame_principale = Frame(
            self, width=870, height=500
        )  # Frame contenant tous les autres widgets et frame de la page ExecutionMission
        self.execmission_frame_principale.place(relx=0.25, rely=0.25)
        self.execmission_labelframe_retourvideo = LabelFrame(
            self.execmission_frame_principale,
            text="Retour Vidéo",
            font=("Arial", 14, "bold"),
            width=500,
            height=300,
            borderwidth=3,
        )  # LabelFrame contenant le retour vidéo
        self.execmission_labelframe_retourvideo.place(relx=0.05, rely=0.05)
        self.execmission_labelframe_controle_drone = LabelFrame(
            self.execmission_frame_principale,
            text="Contrôles Drone",
            font=("Arial", 8, "bold"),
            width=150,
            height=200,
            borderwidth=3,
        )  # LabelFrame contenant les controles du drone avec les différents boutons
        self.execmission_labelframe_controle_drone.place(relx=0.75, rely=0.2)
        self.execmission_boutton_retourbase = Button(
            self.execmission_labelframe_controle_drone,
            text="Retour base",
            width=15,
            height=2,
            bg="#d3c04d",
        )
        self.execmission_boutton_retourbase.place(relx=0.1, rely=0.08)
        self.execmission_boutton_arret = Button(
            self.execmission_labelframe_controle_drone,
            text="Arret urgence",
            width=15,
            height=2,
            bg="#d3272d",
        )
        self.execmission_boutton_arret.place(relx=0.1, rely=0.4)
        self.execmission_boutton_arret = Button(
            self.execmission_labelframe_controle_drone,
            text="Prendre photo",
            width=15,
            height=2,
            bg="#959495",
        )
        self.execmission_boutton_arret.place(relx=0.1, rely=0.7)
        self.execmission_frame_info_vol = LabelFrame(
            self.execmission_frame_principale,
            width=400,
            height=120,
            borderwidth=3,
            bg="#a4a1a3",
        )  # LabelFrame contenant les informations de vol(latitude, longitude, altitude, vitesse et batterie)
        self.execmission_frame_info_vol.place(relx=0.1, rely=0.725)
        self.execmission_label_info_vol = Label(
            self.execmission_frame_info_vol,
            text="Information de vol",
            font=("Arial", 12, "bold"),
            bg="#a4a1a3",
        )
        self.execmission_label_info_vol.place(relx=0.01, rely=0.01)
        self.execmission_latitude = Label(
            self.execmission_frame_info_vol,
            text="Latitude:",
            font=("Arial", 12),
            bg="#a4a1a3",
        )
        self.execmission_latitude.place(relx=0.01, rely=0.22)
        self.execmission_longitude = Label(
            self.execmission_frame_info_vol,
            text="Longitude:",
            font=("Arial", 12),
            bg="#a4a1a3",
        )
        self.execmission_longitude.place(relx=0.01, rely=0.46)
        self.execmission_altitude = Label(
            self.execmission_frame_info_vol,
            text="Altitude:",
            font=("Arial", 12),
            bg="#a4a1a3",
        )
        self.execmission_altitude.place(relx=0.01, rely=0.7)
        self.execmission_Vitesse = Label(
            self.execmission_frame_info_vol,
            text="Vitesse:",
            font=("Arial", 12),
            bg="#a4a1a3",
        )
        self.execmission_Vitesse.place(relx=0.58, rely=0.35)
        self.execmission_batterie = Label(
            self.execmission_frame_info_vol,
            text="Batterie:",
            font=("Arial", 12),
            bg="#a4a1a3",
        )
        self.execmission_batterie.place(relx=0.58, rely=0.65)


instance = Interface()
instance.resizable(
    width=False, height=False
)  # Bloque le fait de pouvoir redimmensionner la fenetre
instance.mainloop()
