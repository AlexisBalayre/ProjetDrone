from Mission import *
from AvanceeMission import *


class Utilisateur(object):
    def __init__(self, id_utilisateur, prenom, nom, email, latitude_base, longitude_base, vitesse=0, mode_camera=0,
                 suivie_mail=0, mail_coord=0, mail_alt=0, mail_vitesse=0, mail_batterie=0, mail_photo=0):
        self.id_utilisateur = id_utilisateur
        self.prenom = prenom
        self.nom = nom
        self.email = email
        self.vitesse = vitesse
        self.latitude_base = latitude_base
        self.longitude_base = longitude_base
        self.mode_camera = mode_camera
        self.suivie_mail = suivie_mail
        self.mail_coord = mail_coord
        self.mail_alt = mail_alt
        self.mail_vitesse = mail_vitesse
        self.mail_batterie = mail_batterie
        self.mail_photo = mail_photo
        self.missions = []

    def ajouterMission(self, mission):
        self.missions.append(mission)

    def getMission(self, id_mission):
        return self.missions[id_mission]

    def supprimerMission(self, id_mission):
        self.missions.remove[id_mission]

    def executionMission(self, id_mission):
        pass
    
    def afficherInformationsMission(self, avanceeMission):
        pass

    def setNom(self, nom):
        self.nom = nom

    def setPrenom(self, prenom):
        self.prenom = prenom

    def setEmail(self, email):
        self.email = email

    def setVitesse(self, vitesse):
        self.vitesse = vitesse

    def setLatitudeBase(self, latitude_base):
        self.latitude_base = latitude_base

    def setLongitudeBase(self, longitude_base):
        self.longitude_base = longitude_base

    def setModeCamera(self, mode_camera):
        self.mode_camera = mode_camera

    def setSuivieMail(self, suivie_mail):
        self.suivie_mail = suivie_mail

    def setMailCoord(self, mail_coord):
        self.mail_coord = mail_coord

    def setMailAlt(self, mail_alt):
        self.mail_alt = mail_alt

    def setMailVitesse(self, mail_vitesse):
        self.mail_vitesse = mail_vitesse

    def setMailBatterie(self, mail_batterie):
        self.mail_batterie = mail_batterie

    def setMailPhoto(self, mail_photo):
        self.mail_photo = mail_photo
