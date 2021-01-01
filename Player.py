import pygame

from settings import WIDTH
from settings import HEIGHT
from settings import FPS

class Player(pygame.sprite.Sprite):
    """класс игрока"""

    # конструктор
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 40))   # заменяем пока что героя прямоугольником
        self.image.fill((0, 255, 0))           # раскрашиваем макет
        self.rect = self.image.get_rect()
        # устанавливаем начальные положения
        self.rect_centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
    
    # обновление
    def update(self):
        self.speedx = 0
        # проверка нажатия кнопок управления
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx # сдвинуть 
        # оставим спрайт в пределеах экрана
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0



