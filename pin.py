from collision import *
from ball import *

class pin:
    #Position is origin of pin, angles are xy and yz angles, definition is stretch factors on elipsoid. (a, b, c)
    def __init__(self, position, velocity, mass, angles, definition):
        self.definition = definition
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]
        self.m = mass
        self.a = angles[0]
        self.b = angles[1]
        self.definition = definition

    def getDefinition(self):
        return self.definition

    def getPosition(self):
        return [self.x, self.y, self.z]

    def getMass(self):
        return self.m

    def getVelocity(self):
        return [self.vx, self.vy, self.vz]

    def setPosition(self, point):
        self.x, self.y, self.z = point

    def setVelocity(self, velocity):
        self.vx, self.vy, self.vz = velocity

    def getAngles(self):
        return [self.a, self.b]

    def setAngle(self, angles):
        self.a, self.b = angles

    def getDefinition(self):
        return self.definition
