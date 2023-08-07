import pygame
import math
pygame.init()



#constants
WIDTH = 700
HIGHT = 600
timer = pygame.time.Clock()
fps = 60

#screen name icon caption ect
screen = pygame.display.set_mode([WIDTH, HIGHT])
pygame.display.set_caption("my game")

#backgound stuff
bg = pygame.image.load('bg.png')
class Background():
	def __init__(self, win):
		self.win = win

		self.image = pygame.image.load('bg.png')
		self.image = pygame.transform.scale(self.image, (WIDTH, HIGHT))
		self.rect = self.image.get_rect()

		self.reset()
		self.move = True

	def update(self, speed):
		if self.move:
			self.y1 += speed
			self.y2 += speed

			if self.y1 >= HIGHT:
				self.y1 = -HIGHT
			if self.y2 >= HIGHT:
				self.y2 = -HIGHT

		self.win.blit(self.image, (self.x,self.y1))
		self.win.blit(self.image, (self.x,self.y2))

	def reset(self):
		self.x = 0
		self.y1 = 0
		self.y2 = -HIGHT

bg = Background(screen)


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
    timer.tick(fps)

    bg.update(3)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                change_x = -4
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                change_x = 4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a  or event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                change_x = 0
    

    donut_x += change_x
    donut(donut_x, donut_y)

    pygame.display.update()
