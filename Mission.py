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
        return self.balises[id_balise]

    def supprimerBalise(self, id_balise):
        self.balises.remove[id_balise]

    def afficheDuree(self):
        print("Durée : ")

    def afficheNombreBalises(self):
        print("Nombre balises : %s" % len(self.balises))

    def afficheModePhoto(self):
        print("Mode Photo : ")

    def affichePlanification(self):
        pass

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
