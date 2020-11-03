# coding=System
from Balise import *

class Mission(object):

  """
   

  :version:
  :author:
  """

  """ ATTRIBUTES

   

  id_mission  (private)

   

  planification  (private)

   

  mode_photo  (private)

   

  jour  (private)

   

  heure  (private)

   

  balises  (private)

  """

  def __init__(self, id_mission, planification = 0, mode_photo = 0, jour, heure):
    """
     

    @param int id_mission : 
    @param bool planification : 
    @param bool mode_photo : 
    @param string jour : 
    @param string heure : 
    @return  :
    @author
    """
    pass

  def ajouterBalise(self, balise):
    """
     

    @param Balise balise : 
    @return  :
    @author
    """
    pass

  def getBalise(self, id_balise):
    """
     

    @param int id_balise : 
    @return Balise :
    @author
    """
    pass

  def supprimerBalise(self, id_balise):
    """
     

    @param int id_balise : 
    @return  :
    @author
    """
    pass

  def afficheDuree(self):
    """
     

    @return string :
    @author
    """
    pass

  def afficheNombreBalises(self):
    """
     

    @return string :
    @author
    """
    pass

  def afficheModePhoto(self):
    """
     

    @return string :
    @author
    """
    pass

  def affichePlanification(self):
    """
     

    @return string :
    @author
    """
    pass

  def setJour(self, jour):
    """
     

    @param string jour : 
    @return  :
    @author
    """
    pass

  def setHeure(self, heure):
    """
     

    @param string heure : 
    @return  :
    @author
    """
    pass

  def setPlanification(self, planification = 0):
    """
     

    @param bool planification : 
    @return  :
    @author
    """
    pass

  def setModePhoto(self, mode_photo = 0):
    """
     

    @param bool mode_photo : 
    @return  :
    @author
    """
    pass

  def execution(self):
    """
     

    @return bool :
    @author
    """
    pass



