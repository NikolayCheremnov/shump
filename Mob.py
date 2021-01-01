import pygame

import random

from settings import WIDTH
from settings import HEIGHT

class Mob(pygame.sprite.Sprite):
    """The Mob class"""

    # конструктор
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)     # инициализируем спрайт
        self.image = pygame.Surface((30, 40))   # сделать лицевое отображение
        self.image.fill((0, 255, 255))          # заполнить цветом
        self.rect = self.image.get_rect()       # получить свойства прямоугольника
        self.rect.x = random.randrange(WIDTH - self.rect.width) # установить позиции
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)        # поставить скорость

    # обновление
    def update(self):
        self.rect.y += self.speedy
        # перемещение моба при вылете за экран
        if self.rect.top > HEIGHT + 10:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


