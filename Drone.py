from Utilisateurs import *

# Créations objets Balise 1 et Balise 2
balise1 = Balise(0, 48.78074845187753, 1.7698891842542932, 5, 10, 0, 0)
balise2 = Balise(1, 49.78074845187753, 1.8698891842542932, 8, 15, 3, 1)

# Créations objets Mission 1 et Mission 2
mission1 = Mission(0, '11/10/2020', '15h 31min 00sec', 1, 1)
mission2 = Mission(1, '13/10/2020', '16h 31min 00sec', 1, 1)

# Créations objets Utilisateur 1 et Utilisateur 2
utilisateur1 = Utilisateur(1, 'Alexis', 'Balayre', 'Alexis.balayre@gmail.com', 8.78074845187753, 1.7698891842542932, 10, 0, 0, 0, 0, 0, 0, 0)
utilisateur2 = Utilisateur(0, 'Tom', 'Dupont', 'Tom.dupont@gmail.com', 9.78074845187753, 0.7698891842542932, 16, 0, 1, 1, 1, 1, 1, 1)

# Création objet Utilisateurs
utilisateurs = Utilisateurs()

# Ajout des utilisateurs 1 et 2 aux utilisateurs
utilisateurs.ajouterUtilisateur(utilisateur1)
utilisateurs.ajouterUtilisateur(utilisateur2)

# Ajout des balises aux missions 
mission1.ajouterBalise(balise1)
mission2.ajouterBalise(balise1)
mission2.ajouterBalise(balise2)

# Ajout des missions aux utilisateurs 
utilisateur1.ajouterMission(mission1)
utilisateur1.ajouterMission(mission2)
utilisateur2.ajouterMission(mission2)

# Avancée 1 
avancee1 = AvanceeMission(8.78074845187753, 1.7698891842542932, 10, 15, 100)

# Test 1 utilisateur Id 0
utilisateur = utilisateurs.getUtilisateur(0)
print(utilisateur.nom)
utilisateur.setNom('Douchet')
print(utilisateur.nom)
utilisateur.executionMission(1) # Exécution Mission Id 1
avance1 = utilisateur.afficherInformationsMission(avancee1)
print(avance1.getLatitude())
mission = utilisateur.getMission(1) # Id 1
print(mission.jour)
mission.setJour('15/12/2020')
print(mission.jour)
balise = mission.getBalise(0) # Id 0 
print(balise.vitesse)
balise.setVitesse(13)
print(balise.vitesse)

# Test 2
print(utilisateurs.__dict__)
utilisateur = utilisateurs.supprimerUtilisateur(0) # Supprimer Utilisateur Id 0
print(utilisateurs.__dict__)