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

windowWidth = 500
windowHeight = 500

screen = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Bowling Pin Simulation')

ballHeight = 8
pinHeight = 10
bowlingBall = ball([0,ballHeight/2,0], 10, ballHeight, 5, [0,5])
bowlingPin = pin([0,pinHeight/2,100], [0,0,0], 5, pinHeight, 1, [0,0])

dt = 0.1

while True:
    clock.tick(10)

    event = pygme.event.poll()
    if event.type == pygame.Quit:
        pygame.quit()
        sys.exit
    elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
        pygame.quit()
        sys.exit(0)
    else:
        pass

    screen.fill(GREY)

    pygame.display.update()
