import pygame
import sys

pygame.init()
pygame.joystick.init()
clock = pygame.time.Clock()

# joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
joysticks = []
    
# for al the connected joysticks
for i in range(0, pygame.joystick.get_count()):
    # create an Joystick object in our list
    joysticks.append(pygame.joystick.Joystick(i))
    # initialize them all (-1 means loop forever)
    joysticks[-1].init()
    

#     # print a statement telling what the name of the controller is
    print ("Detected joystick: " + format(joysticks[-1].get_name()))
    print (joysticks[-1].get_name())

# joystick = pygame.joystick.Joystick(1)
# joystick.init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif  event.type == pygame.JOYBUTTONDOWN:
            if  event.button == 0: #press A button to smile
                # pygame.display.update()
                print("A button pressed")
                clock.tick(10)
                
        elif  event.type == pygame.JOYBUTTONUP:
            if  event.button == 0:
                # pygame.display.update()
                print("A button unpressed")
                clock.tick(10)