def collision(pin, ball):
    if (pin.getRadius() + pin.getHeight() >= (((pin.getPosition()[0]-ball.getPosition()[0])**2 +
    (pin.getPosition()[1]-ball.getPosition()[1])**2 +
    (pin.getPosition()[2]-ball.getPosition()[2])**2)**0.5)) :
            print "collision potentially happening."
