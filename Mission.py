from Balise import *

class Mission(object):
  def __init__(self, id_mission, planification = 0, mode_photo = 0, jour, heure):
    self.id_mission = id_mission
    self.planification = planification
    self.mode_photo = mode_photo
    self.jour = jour
    self.heure = heure

  def ajouterBalise(self, balise):
    pass

  def getBalise(self, id_balise):
    pass

  def supprimerBalise(self, id_balise):
    pass

  def afficheDuree(self):
    pass

  def afficheNombreBalises(self):
    pass

  def afficheModePhoto(self):
    pass

  def affichePlanification(self):
    pass

  def setJour(self, jour):
    self.jour = jour

  def setHeure(self, heure):
    self.heure = heure

  def setPlanification(self, planification = 0):
    self.planification = planification

  def setModePhoto(self, mode_photo = 0):
    self.mode_photo = mode_photo

  def execution(self):
    pass



