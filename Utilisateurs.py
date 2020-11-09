from Utilisateur import *


class Utilisateurs(object):
    def __init__(self):
        self.utilisateurs = []

    def ajouterUtilisateur(self, utilisateur):
        self.utilisateurs.append(utilisateur)

    def getUtilisateur(self, id_utilisateur):
        return self.utilisateurs[id_utilisateur]

    def supprimerUtilisateur(self, id_utilisateur):
        self.utilisateurs.remove(id_utilisateur)
