import pygame
import random
import sys

# --- Настройки ---
WIDTH, HEIGHT = 800, 600
FPS = 60
SPIDER_COUNT = 5

# --- Инициализация pygame ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Игра с пауками")
clock = pygame.time.Clock()

# --- Загрузка спрайта паука ---
try:
    spider_img = pygame.image.load("паук.png").convert_alpha()
except:
    spider_img = pygame.Surface((40, 40), pygame.SRCALPHA)
    pygame.draw.circle(spider_img, (0, 0, 0), (20, 20), 20)

# --- Класс Паука ---
class Spider(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = spider_img
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = random.randint(2, 4)

        # Двигается только по горизонтали (в ряд)
        self.dx = random.choice([-1, 1])
        self.dy = 0

    def update(self):
        self.rect.x += self.dx * self.speed

        # Отскок от стен по X
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.dx *= -1

# --- Создаём группу пауков ---
spiders = pygame.sprite.Group()
# Расположим пауков в ряд по Y
for i in range(SPIDER_COUNT):
    x = random.randint(50, WIDTH - 50)
    y = 100 + i * 80   # каждый паук ниже предыдущего
    spiders.add(Spider(x, y))

# --- Главный цикл игры ---
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    spiders.update()

    screen.fill((50, 150, 50))
    spiders.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()
