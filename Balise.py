class Balise(object):
  def __init__(self, id_balise, latitude, longitude, altitude = 0, vitesse = 0, pause = 0, photo = 0):
    self.id_balise = id_balise
    self.latitude = latitude
    self.longitude = longitude
    self.altitude = altitude
    self.vitesse = vitesse 
    self.pause = pause
    self.photo = photo 

  def setLatitude(self, latitude):
    self.latitude = latitude

  def setLongitude(self, longitude):
    self.longitude = longitude

  def setAltitude(self, altitude = 0):
    self.altitude = altitude

  def setVitesse(self, vitesse = 0):
    self.vitesse = vitesse

  def setPause(self, pause = 0):
    self.pause = pause

  def setPhoto(self, photo = 0):
    self.photo = photo



