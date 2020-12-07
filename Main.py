import json
from Classes.Utilisateurs import *


# Chargement des données 
f = open("Data/Utilisateurs.json", "r")
Json_Utilisateur = f.read()
if Json_Utilisateur != None : 
    Dict_Utilisateurs = json.loads(Json_Utilisateur)
    Donnees = 1
else:
    Donnees = 0 # Fichier vide
f.close()


# Objet Utilisateurs
utilisateurs = Utilisateurs()


# Création des objets Utilisateur 
if Donnees == 1:
    for x in Dict_Utilisateurs["utilisateurs"]:
        utilisateurs.ajouterUtilisateur(Dict_Utilisateurs["utilisateurs"][x])
        id = x # Id du dernier objet présent dans le dictionnaire


# Sauvegarde des modifications 
def Sauvegarde():
    utilisateurs_json = json.dumps(utilisateurs.__dict__, indent=4) # Conversion en JSON
    # Sauvegarde dans le fichier Data/Utilisateurs.json
    f = open("Data/Utilisateurs.json", "w") 
    f.write(utilisateurs_json)
    f.close()


# Création d'un utilisateur 
def CreationUtilisateur(prenom, nom, email, latitude_base, longitude_base, vitesse, mode_camera, suivie_mail, mail_coord, mail_alt, mail_vitesse, mail_batterie, mail_photo):
    if Donnees == 1:
        id_utilisateur = int(id) + 1 # Création d'id unique
    else:
        id_utilisateur = 0 # Création d'id unique
    utilisateur = Utilisateur(id_utilisateur, prenom, nom, email, latitude_base, longitude_base, vitesse, mode_camera, suivie_mail, mail_coord, mail_alt, mail_vitesse, mail_batterie, mail_photo)
    utilisateurs.ajouterUtilisateur(utilisateur.__dict__)
    Sauvegarde()
    

# Création d'une mission 
def CreationMission(jour, heure, planification, mode_photo):
    pass


# Création d'une balise 
def CreationBalise(latitude, longitude, altitude, vitesse, pause, photo):
    pass 

'''
# Ajout des balises aux missions 
mission1.ajouterBalise(balise1.__dict__)
mission2.ajouterBalise(balise1.__dict__)
mission2.ajouterBalise(balise2.__dict__)

# Ajout des missions aux utilisateurs 
utilisateur1.ajouterMission(mission1.__dict__)
utilisateur1.ajouterMission(mission2.__dict__)
utilisateur2.ajouterMission(mission2.__dict__)
'''

#CreationUtilisateur('NATDU93', 'Dupont', 'Tom.dupont@gmail.com', 9.78074845187753, 0.7698891842542932, 16, 0, 1, 1, 1, 1, 1, 1)
#CreationMission('11/10/2020', '15h 31min 00sec', 1, 1)
#CreationBalise(49.78074845187753, 1.8698891842542932, 8, 15, 3, 1)

