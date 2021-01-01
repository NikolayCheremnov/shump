import pygame 

from settings import WIDTH
from settings import HEIGHT
from settings import FPS
from settings import MOB_COUNT

from Player import Player
from Mob import Mob

# точка входа игры
if __name__ == '__main__':
    # инициализация движка
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Shmup!")
    clock = pygame.time.Clock()

    # добавление игрока
    all_sprites = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)

    # добавление моба
    for i in range(MOB_COUNT):
        m = Mob()
        all_sprites.add(m)
    

    # игровой цикл
    isRunning = True
    while isRunning:
        clock.tick(FPS) # держим игровую скорость
        
        # обработка события
        for event in pygame.event.get():
            # проверка на закрытие игры
            if event.type == pygame.QUIT:
                isRunning = False
        
        all_sprites.update() # обновление

        screen.fill((0, 0, 0))      # отрисовка фона
        all_sprites.draw(screen)    # отрисовка спрайтов
        pygame.display.flip()       # флип экрана

    pygame.quit()

