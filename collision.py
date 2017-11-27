<<<<<<< HEAD
import numpy as np

def collision(pin, ball):
    diff = np.subtract(pin.getPosition(), ball.getPosition())
    definition = pin.getDefinition()
    if (diff[0]**2 / definition[0]**2) + (diff[1]**2 / definition[1]**2) + (diff[2]**2 / definition[2]**2) > 1:
        return false
    else:
        return true
=======
def collision(pin, ball):
    if (pin.getRadius() + pin.getHeight() >= (((pin.getPosition()[0]-ball.getPosition()[0])**2 +
       (pin.getPosition()[1]-ball.getPosition()[1])**2 +
       (pin.getPosition()[2]-ball.getPosition()[2])**2)**0.5)) :
        print ("collision potentially happening.")
>>>>>>> master
