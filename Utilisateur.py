from Mission import *
from AvanceeMission import *

class Utilisateur(object):
  def __init__(self, id_utilisateur, prenom, nom, email, vitesse = 0, latitude_base, longitude_base, mode_camera = 0, suivie_mail = 0, mail_coord = 0, mail_alt = 0, mail_vitesse = 0, mail_batterie = 0, mail_photo = 0):
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

  def ajouterMission(self, mission):
    pass

  def getMission(self, id_mission):
    pass

  def supprimerMission(self, id_mission):
    pass

  def executionMission(self, id_mission):
    pass

  def afficherInformationsMission(self, avanceeMission):
    pass

  def setNom(self, nom):
    pass

  def setPrenom(self, prenom):
    pass

  def setEmail(self, email):
    pass

  def setVitesse(self, vitesse = 0):
    pass

  def setLatitudeBase(self, latitude_base):
    pass

  def setLongitudeBase(self, longitude_base):
    pass

  def setModeCamera(self, mode_camera = 0):
    pass

  def setSuivieMail(self, suivie_mail = 0):
    pass

  def setMailCoord(self, mail_coord = 0):
    pass

  def setMailAlt(self, mail_alt = 0):
    pass

  def setMailVitesse(self, mail_vitesse = 0):
    pass

  def setMailBatterie(self, mail_batterie = 0):
    pass

  def setMailPhoto(self, mail_photo = 0):
    pass



