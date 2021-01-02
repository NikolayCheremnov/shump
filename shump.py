import pygame 
from os import path

from settings import WIDTH
from settings import HEIGHT
from settings import FPS
from settings import MOB_COUNT
from settings import IMGDIR

from Player import Player
from Mob import Mob

# точка входа игры
if __name__ == '__main__':
    # инициализация движка
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Shmup!")
    clock = pygame.time.Clock()

    # набор всех спрайтов
    all_sprites = pygame.sprite.Group()

    # настройка экрана
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # загрузка игровой графики
    background = pygame.image.load(path.join(IMGDIR, 'purple.png')).convert()
    background_rect = background.get_rect()
    player_img = pygame.image.load(path.join(IMGDIR, "spaceship.png")).convert()
    mob_img = pygame.image.load(path.join(IMGDIR, "mob.png")).convert()
    bullet_img = pygame.image.load(path.join(IMGDIR, "bullet.png")).convert()

    # добавление игрока
    player = Player(player_img, bullet_img)
    all_sprites.add(player)

    # добавление мобов
    mobs = pygame.sprite.Group()
    for i in range(MOB_COUNT):
        m = Mob(mob_img)
        all_sprites.add(m)
        mobs.add(m)
    
    # пули
    bullets = pygame.sprite.Group()

    # игровой цикл
    isRunning = True
    while isRunning:
        clock.tick(FPS) # держим игровую скорость
        
        # обработка события
        for event in pygame.event.get():
            # проверка на закрытие игры
            if event.type == pygame.QUIT:
                isRunning = False
            
            # проверка нажатия клавиш
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: # если нажали пробел
                    player.shoot(all_sprites, bullets)              # то стреляем

        all_sprites.update() # обновление

        # проверка на столкновение пуль и мобов с установкой dokill
        hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
        for hit in hits:
            m = Mob(mob_img)
            all_sprites.add(m)
            mobs.add(m)

        # проверка моба на столкновение
        hits = pygame.sprite.spritecollide(player, mobs, False)
        if hits:
            isRunning = False

       
        screen.fill((0, 0, 0))      # отрисовка фона
        screen.blit(background, background_rect) # установить фоновую картинку
        all_sprites.draw(screen)    # отрисовка спрайтов
        pygame.display.flip()       # флип экрана

    pygame.quit()

