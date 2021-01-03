import pygame


from settings import WIDTH
from settings import HEIGHT
from settings import FPS

from Bullet import Bullet

class Player(pygame.sprite.Sprite):
    """класс игрока"""

    # конструктор
    def __init__(self, player_img, left_player_img, right_player_img, bullet_img):

        # установка начальных значений
        self.bullet_img = bullet_img
        self.score = 0
        self.player_img = player_img
        self.left_player_img = left_player_img
        self.right_player_img = right_player_img

        pygame.sprite.Sprite.__init__(self)
        
        self.changeIcon(self.player_img)
        self.rect = self.image.get_rect()

        # устанавливаем начальные положения
        self.rect_centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
    
    # обновление
    def update(self):
        self.changeIcon(self.player_img)
        self.speedx = 0
        # проверка нажатия кнопок управления
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.changeIcon(self.left_player_img)
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.changeIcon(self.right_player_img)
            self.speedx = 8
        self.rect.x += self.speedx # сдвинуть 
        # оставим спрайт в пределеах экрана
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    # метод стрельбы
    def shoot(self, all_sprites, bullets, shoot_sound):
        bullet = Bullet(self.rect.centerx, self.rect.top, self.bullet_img)
        all_sprites.add(bullet)
        bullets.add(bullet)
        shoot_sound.play()

    # метод смены иконки игрока
    def changeIcon(self, image):
        self.image = image
        self.image = pygame.transform.scale(image, (50, 30))   # ставим нужный размер корабля
        self.image.set_colorkey((0,0,0))                              # ставим прозрачный фон



