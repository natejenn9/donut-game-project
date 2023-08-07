import pygame
pygame.init()

#constants
WIDTH = 700
HIGHT = 600

#screen name icon caption ect
screen = pygame.display.set_mode([WIDTH, HIGHT])
pygame.display.set_caption("my game")

#donut player
donut_img = pygame.image.load('donut.png')
donut_x = 320
donut_y = 480
change_x = 0


#player method
def donut(x,y):
    screen.blit(donut_img, (x, y))

#game loop
running = True
while running:
    
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                change_x = -2.1
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                change_x = 2.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a  or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                change_x = 0

    donut_x += change_x
    donut(donut_x, donut_y)

    pygame.display.update()
