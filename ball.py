import pygame

class ball:
    def __init__(self, point, mass, radius, velocity):
        self.x = point[0]
        self.y = point[1]
        self.z = point[2]
        self.m = mass
        self.r = radius
        self.vx = velocity[0]
        self.vz = velocity[1]

    def add(self, imgfile, radius, mass):
        bBall = Ball2D(imgfile, radius, mass)
        self.bowlBall = bBall
        return bBall

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

    def setVelocity(self, velocity):
        self.vx, self.vz = velocity

    def updatePositiion(self):
        x = self.x + self.vx
        if x >= 20:
            x = 20
            setVelocity([0, self.vz])
        elif x <= -20:
            x = -20
            setVelocity([0, self.vz])

        z = self.z + self.vz
        setPosition([x, self.y, z])

class Ball2D(pygame.sprite.Sprite):
    def __init__(self, imgfile, radius, mass):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(imgfile)
        self.image = pygame.transform.scale(self.image, (radius*2, radius*2))
