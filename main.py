import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from circleshape import CircleShape 
from player import Player



def main():
    pygame.init()
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    new_player = Player(x, y)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    while True:
        log_state()

        # add x-window functionallity
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #screen clear
        screen.fill("black")
        # re-render player
        new_player.draw(screen)
        # show screen
        pygame.display.flip()
        clock.tick(60)

        # Limits framerate to 60 FPS
        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    main()
    