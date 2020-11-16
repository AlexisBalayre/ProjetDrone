from Utilisateur import *


class Utilisateurs(object):
    def __init__(self):
        self.utilisateurs = []

    def ajouterUtilisateur(self, utilisateur):
        self.utilisateurs.append(utilisateur)

    def getUtilisateur(self, id_utilisateur):
        for x in self.utilisateurs:
            if x.id_utilisateur == id_utilisateur:
                return x

    def supprimerUtilisateur(self, id_utilisateur):
        for x in self.utilisateurs:
            if x.id_utilisateur == id_utilisateur:
                self.utilisateurs.remove(x)
 