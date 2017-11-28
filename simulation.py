ballImage = "ball.png"
pinImage = "pin.png"

from ball import *
from pin import *
from collision import *

import pygame
import sys

#Colour
GREY = (128, 128, 128)

pygame.init()

clock = pygame.time.Clock()

windowWidth = 1125
windowHeight = 150

screen = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Bowling Pin Simulation')

ballHeight = 12.75
bowlingBall = ball(ballImage, [0,ballHeight/2,0], 10, ballHeight/2, [0,3])
bowlingPin = pin(pinImage, [0,5,1080], 5, 10, [0, 0], [1/2, 1/2, 1/2])

dt = 0.1

while True:
    clock.tick(30)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
        pygame.quit()
        sys.exit(0)
    else:
        pass

    screen.fill(GREY)

    bowlingBall.draw(screen)
    bowlingBall.updatePositiion()

    bowlingPin.draw(screen)
    #update needed

    collision(bowlingPin, bowlingBall)

    pygame.display.update()
