import pygame, sys
from pygame.locals import *
import time

# where did i get this code?

windowSize = (800, 600)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode(windowSize)
screen.fill((255, 255, 255))
pygame.display.flip()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("./robot.png")
        self.surf = pygame.Surface((40, 75))
        self.rect = self.surf.get_rect(center = (160, 520))

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
                self.redraw()
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
                self.redraw()

    def redraw(self):
        screen.fill((255, 255, 255))
        screen.blit(self.image, self.rect)
        pygame.display.flip()


if __name__ == "__main__":

    P1 = Player()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(P1)

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Moves and Re-draws all Sprites
        for entity in all_sprites:
            entity.move()
            # yield
            time.sleep(.01)