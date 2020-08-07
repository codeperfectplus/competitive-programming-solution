class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        return round(self.seconds / 31557600, 2)
    
    def on_mercury(self):
        earth = self.on_earth()
        return round(earth / 0.2408467, 2)

    def on_venus(self):
        return round(self.seconds/ 31557600 / 0.61519726, 2)

    def on_mars(self):
        earth = self.on_earth()
        return round(earth / 1.8808158, 2)

    def on_jupiter(self):
        earth = self.on_earth()
        return round(earth / 11.862615, 2)

    def on_saturn(self):
        earth = self.on_earth()
        return round(earth / 29.447498, 2)

    def on_uranus(self):
        earth = self.on_earth()
        return round(earth / 84.016846, 2)

    def on_neptune(self):
        earth = self.on_earth()
        return round(earth / 164.79132, 2)
