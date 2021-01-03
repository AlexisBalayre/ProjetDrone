class AvanceeMission(object):
    def __init__(self, longitude, latitude, altitude=0, vitesse=0, batterie=0):
        self.longitude = longitude
        self.latitude = latitude
        self.altitude = altitude
        self.vitesse = vitesse
        self.batterie = batterie

    def setLongitude(self, longitude):
        self.longitude = longitude

    def setLatitude(self, latitude):
        self.latitude = latitude

    def setAltitude(self, altitude):
        self.altitude = altitude

    def setVitesse(self, vitesse):
        self.vitesse = vitesse

    def setBatterie(self, batterie):
        self.batterie = batterie

    def getLongitude(self):
        return "Longitude : %s" % self.longitude

    def getLatitude(self):
        return "Latitude : %s" % self.latitude

    def getAltitude(self):
        return "Altitude : %s" % self.altitude

    def getVitesse(self):
        return "Vitesse : %s" % self.vitesse

    def getBatterie(self):
        return "Batterie : %s" % self.batterie
