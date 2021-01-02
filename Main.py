import json
from Classes.Utilisateurs import *



# Sauvegarde des modifications
def Sauvegarde():
    utilisateurs_json = json.dumps(
        utilisateurs, default=lambda o: o.__dict__, indent=4
    )  # Conversion en JSON
    # Sauvegarde dans le fichier Data/Utilisateurs.json
    f = open("Data/Utilisateurs.json", "w")
    f.write(utilisateurs_json)
    f.close()


# Chargement des données
f = open("Data/Utilisateurs.json", "r")
Json_Utilisateur = f.read()
Dict_Utilisateurs = json.loads(Json_Utilisateur)
if Dict_Utilisateurs == {}:
    Donnees = 0  # Fichier vide
else:
    Donnees = 1
f.close()


# Objet Utilisateurs
utilisateurs = Utilisateurs()


# Création des objets Utilisateur
if Donnees == 1:
    for x in Dict_Utilisateurs["utilisateurs"]:
        u = Dict_Utilisateurs["utilisateurs"][x]
        utilisateur = Utilisateur(
            u["id_utilisateur"],
            u["prenom"],
            u["nom"],
            u["email"],
            u["latitude_base"],
            u["longitude_base"],
            u["vitesse"],
            u["mode_camera"],
            u["suivie_mail"],
            u["mail_coord"],
            u["mail_alt"],
            u["mail_vitesse"],
            u["mail_batterie"],
            u["mail_photo"],
        )
        # Création des objets Mission
        for y in u["missions"]:
            v = u["missions"][y]
            mission = Mission(
                v["id_mission"],
                v["jour"],
                v["heure"],
                v["planification"],
                v["mode_photo"],
            )
            # Création des objets Balise
            for z in v["balises"]:
                w = v["balises"][z]
                balise = Balise(
                    w["id_balise"],
                    w["latitude"],
                    w["longitude"],
                    w["altitude"],
                    w["vitesse"],
                    w["pause"],
                    w["photo"],
                )
                mission.ajouterBalise(balise)
            utilisateur.ajouterMission(mission)
        utilisateurs.ajouterUtilisateur(utilisateur)
        id = x  # Id du dernier objet présent dans le dictionnaire


# Création d'un utilisateur
def CreationUtilisateur(
    prenom,
    nom,
    email,
    latitude_base,
    longitude_base,
    vitesse,
    mode_camera,
    suivie_mail,
    mail_coord,
    mail_alt,
    mail_vitesse,
    mail_batterie,
    mail_photo,
):
    if Donnees == 1:
        id_utilisateur = int(id) + 1  # Création d'id unique
    else:
        id_utilisateur = 0  # Création d'id unique
    utilisateur = Utilisateur(
        id_utilisateur,
        prenom,
        nom,
        email,
        latitude_base,
        longitude_base,
        vitesse,
        mode_camera,
        suivie_mail,
        mail_coord,
        mail_alt,
        mail_vitesse,
        mail_batterie,
        mail_photo,
    )
    utilisateurs.ajouterUtilisateur(utilisateur)
    Sauvegarde()


# Création d'une mission
def CreationMission(id_utilisateur, jour, heure, planification, mode_photo):
    utilisateur = utilisateurs.getUtilisateur(id_utilisateur)
    if utilisateur.__dict__["missions"] == {}:
        id_mission = 0
    else:
        for x in utilisateur.missions:
            id = x
        id_mission = int(id) + 1
    mission = Mission(id_mission, jour, heure, planification, mode_photo)
    utilisateur.ajouterMission(mission)
    Sauvegarde()


# Création d'une balise
def CreationBalise(
    id_utilisateur, id_mission, latitude, longitude, altitude, vitesse, pause, photo
):
    utilisateur = utilisateurs.getUtilisateur(id_utilisateur)
    mission = utilisateur.getMission(id_mission)
    if mission.__dict__["balises"] == {}:
        id_balise = 0
    else:
        for x in mission.balises:
            id = x
        id_balise = int(id) + 1
    balise = Balise(id_balise, latitude, longitude, altitude, vitesse, pause, photo)
    mission.ajouterBalise(balise)
    Sauvegarde()


# Modification d'un utilisateur
def ModificationUtilisateur(
    id_utilisateur,
    prenom,
    nom,
    email,
    latitude_base,
    longitude_base,
    vitesse,
    mode_camera,
    suivie_mail,
    mail_coord,
    mail_alt,
    mail_vitesse,
    mail_batterie,
    mail_photo,
):
    utilisateur = utilisateurs.getUtilisateur(id_utilisateur)
    utilisateur.setPrenom(prenom)
    utilisateur.setEmail(email)
    utilisateur.setVitesse(vitesse)
    utilisateur.setLatitudeBase(latitude_base)
    utilisateur.setLongitudeBase(longitude_base)
    utilisateur.setModeCamera(mode_camera)
    utilisateur.setSuivieMail(suivie_mail)
    utilisateur.setMailCoord(mail_coord)
    utilisateur.setMailAlt(mail_alt)
    utilisateur.setMailVitesse(mail_vitesse)
    utilisateur.setMailBatterie(mail_batterie)
    utilisateur.setMailPhoto(mail_photo)
    Sauvegarde()


# Modification d'une mission
def ModificationMission(
    id_utilisateur, id_mission, jour, heure, planification, mode_photo
):
    utilisateur = utilisateurs.getUtilisateur(id_utilisateur)
    mission = utilisateur.getMission(id_mission)
    mission.setJour(jour)
    mission.setHeure(heure)
    mission.setPlanification(planification)
    mission.setModePhoto(mode_photo)
    Sauvegarde()


# Modification d'une balise
def ModificationBalise(
    id_utilisateur,
    id_mission,
    id_balise,
    latitude,
    longitude,
    altitude,
    vitesse,
    pause,
    photo,
):
    utilisateur = utilisateurs.getUtilisateur(id_utilisateur)
    mission = utilisateur.getMission(id_mission)
    balise = mission.getBalise(id_balise)
    balise.setLatitude(latitude)
    balise.setLongitude(longitude)
    balise.setAltitude(altitude)
    balise.setVitesse(vitesse)
    balise.setPause(pause)
    balise.setPhoto(photo)
    Sauvegarde()


# Suppression d'un utilisateur
def SuppressionUtilisateur(id_utilisateur):
    utilisateurs.supprimerUtilisateur(id_utilisateur)
    Sauvegarde()


# Suppression d'une mission
def SuppressionMission(id_utilisateur, id_mission):
    utilisateur = utilisateurs.getUtilisateur(id_utilisateur)
    utilisateur.supprimerMission(id_mission)
    Sauvegarde()


# Suppression d'une balise
def SuppressionBalise(id_utilisateur, id_mission, id_balise):
    utilisateur = utilisateurs.getUtilisateur(id_utilisateur)
    mission = utilisateur.getMission(id_mission)
    mission.supprimerBalise(id_balise)
    Sauvegarde()


# Exécution d'une mission 
def ExecutionMission(id_utilisateur, id_mission):
    utilisateur = utilisateurs.getUtilisateur(id_utilisateur)
    mission = utilisateur.getMission(id_mission)
    mission.execution()


# CreationUtilisateur('tom', 'Dupont', 'Tom.dupont@gmail.com', 9.78074845187753, 0.7698891842542932, 16, 0, 1, 1, 1, 1, 1, 1)
# CreationMission(0, '13/10/2020', '15h 31min 00sec', 1, 1)
# CreationBalise(0, 1, 53.78074845187753, 1.8698891842542932, 8, 15, 3, 1)

# ModificationUtilisateur(1, 'Alexis', 'Dupont', 'Tom.dupont@gmail.com', 9.78074845187753, 0.7698891842542932, 16, 0, 1, 1, 1, 0, 0, 0)
# ModificationMission(0, 1, '15/04/2021', '16h 31min 00sec', 0, 0)
# ModificationBalise(0, 1, 2, 58.78074845187753, 2.8698891842542932, 20, 30, 4, 0)

# SuppressionUtilisateur(2)
# SuppressionMission(0, 0)
# SuppressionBalise(0, 1, 1)

ExecutionMission(0, 1)
