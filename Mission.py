from Balise import *


class Mission(object):
    def __init__(self, id_mission, jour, heure, planification=0, mode_photo=0):
        self.id_mission = id_mission
        self.planification = planification
        self.mode_photo = mode_photo
        self.jour = jour
        self.heure = heure
        self.balises = []

    def ajouterBalise(self, balise):
        self.balises.append(balise)

    def getBalise(self, id_balise):
        for x in self.balises:
            if x.id_balise == id_balise:
                return x

    def supprimerBalise(self, id_balise):
         for x in self.balises:
            if x.id_balise == id_balise:
                self.balises.remove(x)

    def afficheDuree(self):
        return("Durée : ")

    def afficheNombreBalises(self):
        return("Nombre balises : %s" % len(self.balises))

    def afficheModePhoto(self):
        if self.mode_photo == 0:
           return("Mode Photo : Désactivé")
        else:
            return("Mode Photo : Activé")

    def affichePlanification(self):
        if self.planification == 0:
            return("Mission Planifiée : NON")
        else:
            return("Mission Planifiée : OUI")

    def setJour(self, jour):
        self.jour = jour

    def setHeure(self, heure):
        self.heure = heure

    def setPlanification(self, planification=0):
        self.planification = planification

    def setModePhoto(self, mode_photo=0):
        self.mode_photo = mode_photo

    def execution(self):
        pass
