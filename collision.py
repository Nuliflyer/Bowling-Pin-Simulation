import numpy as np
import math
from scipy.spatial import distance

hit = False

def setCollision(boolVal):
    hit = boolVal

def getCollision():
    return hit

def collisionMath(pin, ball):
    pTotal = pin.getMass() * distance.euclidean(0, pin.getVelocity()) + ball.getMass() * distance.euclidean(0, ball.getVelocity())
    pPin = (pin.getMass() + ball.getMass() * 0.8) / (pin.getMass() + ball.getMass())
    pBall  = (pin.getMass() + ball.getMass() * 0.2) / (ball.getMass() + pin.getMass())
    vMagBall = pBall / ball.getMass()
    vMagPin = pPin / pin.getMass()
    dirPin = np.subtract(ball.getPosition(), pin.getPosition())
    normVal = (dirPin[0]**2 + dirPin[1]**2 + dirPin[2]**2)**0.5
    dirPinNorm = [dirPin[0]/normVal, dirPin[1]/normVal, dirPin[2]/normVal]
    print (dirPin)
    print (dirPinNorm)
    print (vMagPin)
    for x in range(3):
        dirPinNorm[x] = dirPinNorm[x] * vMagPin
    pin.setVelocity(dirPinNorm)
    ball.setVelocity([0,vMagBall])
    setCollision(True)

def collision(pin, ball):
    length = distance.euclidean(pin.getPosition(), ball.getPosition()) - ball.getRadius()

    xPin = length * math.sin(pin.getAngles()[0]) * math.cos(pin.getAngles()[1])
    yPin = length * math.sin(pin.getAngles()[0]) * math.sin(pin.getAngles()[1])
    zPin = length * math.cos(pin.getAngles()[0])

    if(pin.getDefinition()[0] * xPin**2 + pin.getDefinition()[1] * yPin**2 + pin.getDefinition()[2] * zPin**2 > 3):
        print("Pin:", pin.getPosition(), " Ball:", ball.getPosition(), " l: ", length)
        return False
    else:
        print("Collision")
        collisionMath(pin, ball)
        return True
