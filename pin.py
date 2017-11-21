class pin:
    def __init__(self, position, velocity, mass, height, radius, angles):
        #x y z refer to the center of mass.
        #According to bowling.com the pin is made of a solid material coated by
        #another material, so we assume the mass is uniformly distributed
        self.x = point[0]
        self.y = point[1]
        self.z = point[2]
        self.m = mass
        self.h = height
        self.r = radius
        self.a = angles[0]
        self.b = angles[1]


    def getHeight(self):
        return self.h

    def getRadius(self):
        return self.r

    def getAngles(self):
        return [self.a, self.b]

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

    def setAngle(self, angles):
        self.a, self.b = angles
    #currently, this is a cylinder.


bowlingPin = pin([0,5,0], 5, 10, 1, [0, 0])
bowlingPin.collision([0,5,0])
bowlingPin.setPosition([0, 10, 0])
