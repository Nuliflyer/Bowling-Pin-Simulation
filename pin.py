import pygame

class pin:
    #Position is origin of pin, angles are xy and yz angles, definition is stretch factors on elipsoid. (a, b, c)
    def __init__(self, imgfile, position, velocity, mass, angles, definition):
        self.image = pygame.image.load(imgfile)
        self.image = pygame.transform.scale(self.image, (int(4*2), int(4*2)))
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

    def draw(self, surface):
        rect = self.image.get_rect()
        rect.center = (1080, 75)
        surface.blit(self.image, rect)
