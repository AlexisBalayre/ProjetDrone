class AvanceeMission(object):
  def __init__(self, longitude, latitude, altitude = 0, vitesse = 0, batterie = 0):
    self.longitude = longitude 
    self.latitude = latitude
    self.altitude = altitude
    self.vitesse = vitesse 
    self.batterie = batterie  

  def getLongitude(self):
    print("Longitude : %s" % self.longitude)

  def getLatitude(self):
    print("Latitude : %s" % self.latitude)

  def getAltitude(self):
    print("Altitude : %s" % self.altitude)

  def getVitesse(self):
    print("Vitesse : %s" % self.vitesse)

  def getBatterie(self):
    print("Batterie : %s" % self.batterie)



