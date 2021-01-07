#!/usr/bin/python
# -*- coding: utf-8 -*-

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
        latitude_base = float(home[0])  # Latitude de la base
        longitude_base = float(home[1])  # Longitude de la base
        vitesse_initiale = float(home[2])  # Vitesse initiale au départ de la base

        # Liste vitesses contenant toutes les vitesses de la mission
        vitesses = [vitesse_initiale]

        for x in self.balises:
            balise = self.balises[x].__dict__
            vitesses.append(float(balise["vitesse"]))

        # Calcul de la vitesse moyenne (m.s)
        vitesse_moyenne = sum(vitesses) / len(vitesses)

        # Liste distances_verticales contenant toutes les distances verticales de la mission
        distances_verticales = []
        for x in self.balises:
            balise = self.balises[x].__dict__
            distances_verticales.append(float(balise["altitude"]))

        # Calcul de la distance verticale totale distance_vert (m)
        distance_vert = 0
        nombre_distances_vert = len(distances_verticales)
        for x in range(1, nombre_distances_vert - 2):
            distance_vert = distance_vert + abs(
                distances_verticales[x + 1] - distances_verticales[x]
            )
        distance_vert = (
            distance_vert
            + distances_verticales[0]
            + distances_verticales[nombre_distances_vert - 1]
        )  # Ajout distances décollage et atterissage

        # Liste distances_horizontales contenant toutes les distances horizontales de la mission
        distances_horizontales = []
        # Liste coord_balises contenant les coordonnées de chaque balise
        coord_balises = []
        for x in self.balises:
            coord = (
                float(self.balises[x].__dict__["latitude"]),
                float(self.balises[x].__dict__["longitude"]),
            )
            coord_balises.append(coord)
        # Calcul des distances horizontales (m)
        coords_base = (latitude_base, longitude_base)
        distance_ini_horiz = (
            geopy.distance.distance(coords_base, coord_balises[0]).km * 1000
        )  # Distance horizontale initiale
        distance_fin_horiz = (
            geopy.distance.distance(
                coord_balises[len(coord_balises) - 1], coords_base
            ).km
            * 1000
        )  # Distance horizontale finale
        # Distances entre les balises
        for x in range(0, len(self.balises) - 1):
            coord1 = coord_balises[x]
            coord2 = coord_balises[x + 1]
            distances_horizontales.append(
                geopy.distance.distance(coord1, coord2).km * 1000
            )

        # Calcul de la distance horizontale totale distance_horiz (m)
        distance_horiz = (
            sum(distances_horizontales) + distance_ini_horiz + distance_fin_horiz
        )

        # Calcul de la durée de mission (s)
        duree = (
            distance_horiz / vitesse_moyenne
            + distances_verticales[0]
            + distances_verticales[nombre_distances_vert - 1]
        )

        return duree

    def afficheNombreBalises(self):
        return len(self.balises)

    def afficheModePhoto(self):
        if self.mode_photo == 0:
            return "Désactivé"
        else:
            return "Activé"

    def affichePlanification(self):
        if self.planification == 0:
            return "NON"
        else:
            return "OUI"

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
