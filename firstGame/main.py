import pygame
pygame.init()
from game import Game

pygame.display.set_caption("Shooter")
screen = pygame.display.set_mode((1080, 720))

background = pygame.image.load('PygameAssets-main/bg.jpg')

game = Game()
run = True

while run:

    screen.blit(background, (0, -250))

    screen.blit(game.player.image, game.player.rect)
    pygame.display.flip()

    if game.pressed.get(pygame.K_d):
        game.player.move_right()
    elif game.pressed.get(pygame.K_q):
        game.player.move_left()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

