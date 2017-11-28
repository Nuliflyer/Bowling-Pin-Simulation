import pygame

class ball():
    def __init__(self, imgfile, point, mass, radius, velocity):
        self.image = pygame.image.load(imgfile)
        self.image = pygame.transform.scale(self.image, (int(radius*2), int(radius*2)))
        self.x = point[0]
        self.y = point[1]
        self.z = point[2]
        self.m = mass
        self.r = radius
        self.vx = velocity[0]
        self.vz = velocity[1]

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
        if x >= 43:
            x = 43
            self.setVelocity([0, self.vz])
        elif x <= -43:
            x = -43
            self.setVelocity([0, self.vz])

        z = self.z + self.vz
        self.setPosition([x, self.y, z])

    def draw(self, surface):
        rect = self.image.get_rect()
        rect.center = (self.z, 75+self.x)
        surface.blit(self.image, rect)
