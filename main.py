import pygame

#pygame setup 
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #filling the screen with a color to wipe away anything from last frame
    screen.fill('purple')
    pygame.display.flip()

    clock.tick(60)
pygame.quit()