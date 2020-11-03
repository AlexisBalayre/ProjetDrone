# coding=System
from Mission import *
from AvanceeMission import *

class Utilisateur(object):

  """
   

  :version:
  :author:
  """

  """ ATTRIBUTES

   

  id_utilisateur  (private)

   

  nom  (private)

   

  prenom  (private)

   

  email  (private)

   

  vitesse  (private)

   

  latitude_base  (private)

   

  longitude_base  (private)

   

  mode_camera  (private)

   

  suivie_mail  (private)

   

  mail_coord  (private)

   

  mail_alt  (private)

   

  mail_vitesse  (private)

   

  mail_batterie  (private)

   

  mail_photo  (private)

   

  missions  (private)

  """

  def __init__(self, id_utilisateur, prenom, nom, email, vitesse = 0, latitude_base, longitude_base, mode_camera = 0, suivie_mail = 0, mail_coord = 0, mail_alt = 0, mail_vitesse = 0, mail_batterie = 0, mail_photo = 0):
    """
     

    @param int id_utilisateur : 
    @param string prenom : 
    @param string nom : 
    @param string email : 
    @param float vitesse : 
    @param float latitude_base : 
    @param float longitude_base : 
    @param bool mode_camera : 
    @param bool suivie_mail : 
    @param bool mail_coord : 
    @param bool mail_alt : 
    @param bool mail_vitesse : 
    @param bool mail_batterie : 
    @param bool mail_photo : 
    @return  :
    @author
    """
    pass

  def ajouterMission(self, mission):
    """
     

    @param Mission mission : 
    @return  :
    @author
    """
    pass

  def getMission(self, id_mission):
    """
     

    @param int id_mission : 
    @return Mission :
    @author
    """
    pass

  def supprimerMission(self, id_mission):
    """
     

    @param int id_mission : 
    @return  :
    @author
    """
    pass

  def executionMission(self, id_mission):
    """
     

    @param int id_mission : 
    @return bool :
    @author
    """
    pass

  def afficherInformationsMission(self, avanceeMission):
    """
     

    @param AvanceeMission avanceeMission : 
    @return  :
    @author
    """
    pass

  def setNom(self, nom):
    """
     

    @param string nom : 
    @return  :
    @author
    """
    pass

  def setPrenom(self, prenom):
    """
     

    @param string prenom : 
    @return  :
    @author
    """
    pass

  def setEmail(self, email):
    """
     

    @param string email : 
    @return  :
    @author
    """
    pass

  def setVitesse(self, vitesse = 0):
    """
     

    @param float vitesse : 
    @return  :
    @author
    """
    pass

  def setLatitudeBase(self, latitude_base):
    """
     

    @param float latitude_base : 
    @return  :
    @author
    """
    pass

  def setLongitudeBase(self, longitude_base):
    """
     

    @param float longitude_base : 
    @return  :
    @author
    """
    pass

  def setModeCamera(self, mode_camera = 0):
    """
     

    @param bool mode_camera : 
    @return  :
    @author
    """
    pass

  def setSuivieMail(self, suivie_mail = 0):
    """
     

    @param bool suivie_mail : 
    @return  :
    @author
    """
    pass

  def setMailCoord(self, mail_coord = 0):
    """
     

    @param bool mail_coord : 
    @return  :
    @author
    """
    pass

  def setMailAlt(self, mail_alt = 0):
    """
     

    @param bool mail_alt : 
    @return  :
    @author
    """
    pass

  def setMailVitesse(self, mail_vitesse = 0):
    """
     

    @param bool mail_vitesse : 
    @return  :
    @author
    """
    pass

  def setMailBatterie(self, mail_batterie = 0):
    """
     

    @param bool mail_batterie : 
    @return  :
    @author
    """
    pass

  def setMailPhoto(self, mail_photo = 0):
    """
     

    @param bool mail_photo : 
    @return  :
    @author
    """
    pass



