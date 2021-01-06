#!/usr/bin/python
# -*- coding: utf-8 -*-

class Balise(object):
    def __init__(
        self, id_balise, latitude, longitude, altitude=0, vitesse=0, pause=0, photo=0
    ):
        self.id_balise = id_balise
        self.latitude = latitude
        self.longitude = longitude
        self.altitude = altitude
        self.vitesse = vitesse
        self.pause = pause
        self.photo = photo

    def setLatitude(self, latitude):
        self.latitude = latitude

    def setLongitude(self, longitude):
        self.longitude = longitude

    def setAltitude(self, altitude):
        self.altitude = altitude

    def setVitesse(self, vitesse):
        self.vitesse = vitesse

    def setPause(self, pause):
        self.pause = pause

    def setPhoto(self, photo):
        self.photo = photo
