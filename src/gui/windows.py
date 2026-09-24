import pygame

pygame.init()

screen = pygame.display.set_mode((1600,900))
pygame.display.set_caption("AirDashboard")

clock = pygame.time.Clock()

color = {
    "black": (0,0,0),
    "white": (255, 255, 255),
    "red": (255, 0, 0),
    "green": (0, 255, 0),
    "blue": (0, 0, 255),
    "grey": (211, 211, 211),
    "dark": (4, 12, 32),
    "light": (251, 243, 223),
}

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 更新屏幕
    screen.fill(color["light"])
    pygame.draw.rect(screen, color["red"], (100, 100, 220, 400), border_radius=90)
    pygame.draw.rect(screen, color["green"], (100, 100, 220, 400), width=3, border_radius=90)
    pygame.display.flip()
    # 设置帧率
    clock.tick(60)

pygame.quit()