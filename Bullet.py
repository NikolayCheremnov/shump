import pygame

import random

from settings import WIDTH

class Bullet(pygame.sprite.Sprite):
    """Bullet for shooting"""

    def __init__(self, x, y, bullet_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 20))
        #self.image.fill((255, 0, 0))
        self.image = bullet_img
        self.image = pygame.transform.scale(bullet_img, (10, 30))   # ставим нужный размер корабля
        self.image.set_colorkey((0,0,0))                              # ставим прозрачный фон
        self.rect = self.image.get_rect()
        
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # убить, если он заходит за верхнюю часть экрана
        if self.rect.bottom < 0:
            self.kill()
