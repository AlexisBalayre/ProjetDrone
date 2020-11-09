from Utilisateurs import *

balise1 = Balise(0, 48.78074845187753, 1.7698891842542932, 5, 10, 0, 0)
balise2 = Balise(1, 49.78074845187753, 1.8698891842542932, 8, 15, 3, 1)


mission1 = Mission(0, '11/10/2020', '15h 31min 00sec', 1, 1)
mission2 = Mission(1, '13/10/2020', '16h 31min 00sec', 1, 1)
mission1.ajouterBalise(balise1)
mission2.ajouterBalise(balise1)
mission2.ajouterBalise(balise2)


utilisateur1 = Utilisateur(0, 'Alexis', 'Balayre', 'Alexis.balayre@gmail.com', 8.78074845187753, 1.7698891842542932, 10, 0, 0, 0, 0, 0, 0, 0)
utilisateur2 = Utilisateur(1, 'Tom', 'Dupont', 'Tom.dupont@gmail.com', 9.78074845187753, 0.7698891842542932, 16, 0, 1, 1, 1, 1, 1, 1)
utilisateur1.ajouterMission(mission1)
utilisateur2.ajouterMission(mission1)
utilisateur2.ajouterMission(mission2)


utilisateurs = Utilisateurs()
utilisateurs.ajouterUtilisateur(utilisateur1)