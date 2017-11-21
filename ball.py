class ball:
    def __init__(self, point, mass, height, radius, velocity):
        self.x = point[0]
        self.y = point[1]
        self.z = point[2]
        self.m = mass
        self.h = height
        self.r = radius
        self.vx = velocity[0]
        self.vz = velocity[1]

    def getHeight(self):
        return self.h

    def getRadius(self):
        return self.r

    def getPosition(self):
        return [self.x, self.y, self.z]

    def getMass(self):
        return self.m

    def getVelocity(self):
        return [self.vx, self.vz]

    def setPosition(self, point):
        self.x, self.y, self.z = point

    def updatePositiion(self):
        x = self.x + self.vx
        z = self.z + self.vz
        setPosition([x, self.y, z])

bowlingBall = ball([0,0,0], 8, 7, 5, [0, 3])
#bowlingBall.collision([0,5,0])
bowlingBall.setPosition([0, 0, 0])
