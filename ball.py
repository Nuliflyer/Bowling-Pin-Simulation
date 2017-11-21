class ball:
    def __init__(self, point, mass, height, radius):
        self.x = point[0]
        self.y = point[1]
        self.z = point[2]
        self.m = mass
        self.h = height
        self.r = radius

    def getHeight(self):
        return self.h

    def getRadius(self):
        return self.r

    def getPosition(self):
        return [self.x, self.y, self.z]

    def getMass(self):
        return self.m

    def setPosition(self, point):
        self.x, self.y, self.z = point


bowlingBall = ball([0,0,0], 8, 7, 5)
#bowlingBall.collision([0,5,0])
bowlingBall.setPosition([0, 0, 0])
