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

class DrawRect():
    def __init__(self,screen,color,position,width,border_radius):
        self.screen = screen
        self.color = color
        self.position = position
        self.width = width
        self.border_radius = border_radius

    def draw_rect(self):
        pygame.draw.rect(self.screen, self.color, self.position, self.width, self.border_radius)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # 更新屏幕
    screen.fill(color["light"])
    a = DrawRect(screen, color["red"], (100, 100, 320, 400), width = 0, border_radius=20)
    a.draw_rect()
    pygame.draw.rect(screen, color["green"], (100, 100, 320, 400), width=1, border_radius=20)
    pygame.display.flip()
    # 设置帧率
    clock.tick(60)

pygame.quit()