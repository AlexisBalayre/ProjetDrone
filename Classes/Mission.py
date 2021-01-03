from Classes.Balise import *
from Simulateur.ExecutionDrone import *
import geopy.distance


class Mission(object):
    def __init__(self, id_mission, jour, heure, planification=0, mode_photo=0):
        self.id_mission = id_mission
        self.planification = planification
        self.mode_photo = mode_photo
        self.jour = jour
        self.heure = heure
        self.balises = {}

    def ajouterBalise(self, balise):
        self.balises[balise.__dict__["id_balise"]] = balise

    def getBalise(self, id_balise):
        return self.balises[id_balise]

    def supprimerBalise(self, id_balise):
        del self.balises[id_balise]

    def afficheDuree(self, home):
        nombre_balises = len(self.balises) # Nombre Balises de la mission
        latitude_base = home[0] # Latitude de la base
        longitude_base = home[1] # Longitude de la base 
        vitesse_initiale = home[2] # Vitesse initiale au départ de la base

        # Liste vitesses contenant toutes les vitesses de la mission
        vitesses = [vitesse_initiale] # Ajout vitesse de décollage 
        for x in self.balises:
            balise = self.balises[x].__dict__
            vitesses.append(balise['vitesse'])
        vitesses.append(vitesses[nombre_balises]) # Ajout vitesse d'atterissage

        # Calcul de la vitesse moyenne (m.s)
        vitesse_moyenne = sum(vitesses)/len(vitesses)

        # Liste distances_verticales contenant toutes les distances verticales de la mission 
        distances_verticales = []
        for x in self.balises:
            balise = self.balises[x].__dict__
            distances_verticales.append(balise['altitude'])

        # Calcul de la distance verticale totale (m)
        distance = 0
        nombre_distances_vert = len(distances_verticales)
        for x in range(1, nombre_distances_vert-2):
            distance = distance + abs(distances_verticales[x+1] - distances_verticales[x])
        distance = distance + distances_verticales[0] + distances_verticales[nombre_distances_vert-1] # Ajout distances décollage et atterissage
        
        # Liste distances_horizontales contenant toutes les distances horizontales de la mission 
        distances_horizontales = []
        # Calcul des distances horizontales (m)
        coords_1 = (latitude_base, longitude_base)
        coords_2 = (48.82555, 2.278478)
        print(geopy.distance.distance(coords_1, coords_2).km*1000)
        for x in self.balises:
            balise = self.balises[x].__dict__
            distances_horizontales.append(balise['altitude'])
      
        return "Durée : "

    def afficheNombreBalises(self):
        return "Nombre balises : %s" % len(self.balises)

    def afficheModePhoto(self):
        if self.mode_photo == 0:
            return "Mode Photo : Désactivé"
        else:
            return "Mode Photo : Activé"

    def affichePlanification(self):
        if self.planification == 0:
            return "Mission Planifiée : NON"
        else:
            return "Mission Planifiée : OUI"

    def setJour(self, jour):
        self.jour = jour

    def setHeure(self, heure):
        self.heure = heure

    def setPlanification(self, planification):
        self.planification = planification

    def setModePhoto(self, mode_photo):
        self.mode_photo = mode_photo

    def execution(self):
        ExecutionDrone(self.balises)
