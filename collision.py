import numpy as np
import math
from scipy.spatial import distance


def collisionMath(pin, ball):
    pTotal = pin.getMass() * distance.euclidean([0,0,0], pin.getVelocity()) + ball.getMass() * distance.euclidean([0,0,0], ball.getVelocity())
    pPin = pin.getMass() / (pin.getMass() + ball.getMass())
    pBall  = ball.getMass() / (ball.getMass() + pin.getMass())
    vMagBall = pBall / ball.getMass()
    vMagPin = pPin / pin.getMass()
    dirPin = np.normalize(np.subtract(ball.getPosition(), pin.getPosition()))
    pin.setVelocity(dirPin * vMapPin)
    ball.setVelocity([0,vMagBall])

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
