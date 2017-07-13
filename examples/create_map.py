import pygame
from rplidar import RPLidar
import time
import random
import math
pygame.init()



lidar = RPLidar('/dev/ttyUSB0')

display_width = 1080
display_height = 720
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('PYSLAM')



def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def obstacle(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


x = (display_width * 0.5)
y = (display_height * 0.5)
x_change = 0
y_change = 0
car_speed = 0
black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('robot.jpg')



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            lidar.stop()
            lidar.stop_motor()
            lidar.disconnect()
            quit()
        ############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            if event.key == pygame.K_RIGHT:
                x_change = 5
            if event.key == pygame.K_UP:
                y_change = -5
            if event.key == pygame.K_DOWN:
                y_change = 5
            if event.key == pygame.K_s:
                try:
                    for i, scan in enumerate(lidar.iter_scans()):
                        for s in scan:
                            pygame.draw.rect(gameDisplay, black, [540+s[2]*math.sin(math.pi*s[1]/180)/10, 360-s[2]*math.cos(math.pi*s[1]/180)/10,5,5])
                        if i > 100:
                            break
                        pygame.display.update()
                except:
                    pass
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                x_change = 0
                y_change = 0

        ############################
    gameDisplay.fill(white)
    x += x_change
    y += y_change
    car(x, y)
    pygame.display.update()
    clock.tick(200)


