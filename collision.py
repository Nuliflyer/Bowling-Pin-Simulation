import numpy as np

def collision(pin, ball):
    diff = np.subtract(pin.getPosition(), ball.getPosition())
    definition = pin.getDefinition()
    if (diff[0]**2 / definition[0]**2) + (diff[1]**2 / definition[1]**2) + (diff[2]**2 / definition[2]**2) > 1:
    else:
        return true
