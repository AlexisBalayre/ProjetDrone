from Utilisateurs import *
import json


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
utilisateurs.ajouterUtilisateur(utilisateur1.__dict__)
utilisateurs.ajouterUtilisateur(utilisateur2.__dict__)

# Ajout des balises aux missions 
mission1.ajouterBalise(balise1.__dict__)
mission2.ajouterBalise(balise1.__dict__)
mission2.ajouterBalise(balise2.__dict__)

# Ajout des missions aux utilisateurs 
utilisateur1.ajouterMission(mission1.__dict__)
utilisateur1.ajouterMission(mission2.__dict__)
utilisateur2.ajouterMission(mission2.__dict__)

# Sauvegarde 
utilisateurs_json = json.dumps(utilisateurs.__dict__, indent=4) # convert into JSON
f = open("../Data/Utilisateurs.json", "w")
f.write(utilisateurs_json)
f.close()


