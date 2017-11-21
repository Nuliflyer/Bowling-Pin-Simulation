class pin:
    def __init__(self, point, mass, height, radius, angles):
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

bowlingPin = pin([0,5,0], 5, 10, 1, [0, 0])
