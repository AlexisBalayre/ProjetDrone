#!/usr/bin/python
# -*- coding: utf-8 -*-

from Classes.Utilisateur import *


class Utilisateurs(object):
    def __init__(self):
        self.utilisateurs = {}

    def ajouterUtilisateur(self, utilisateur):
        self.utilisateurs[utilisateur.__dict__["id_utilisateur"]] = utilisateur

    def getUtilisateur(self, id_utilisateur):
        return self.utilisateurs[id_utilisateur]

    def supprimerUtilisateur(self, id_utilisateur):
        del self.utilisateurs[id_utilisateur]
