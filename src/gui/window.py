import pygame
import random

from bridge import init_flight_data, update_flight
from theme import DARK
from draw import draw_card, draw_dial

pygame.init()

WIDTH, HEIGHT = 1600, 900
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AirDashboard")
clock = pygame.time.Clock()

theme = DARK

aircraft = init_flight_data()
throttle_arr = [random.random() for _ in range(60)]

# 卡片布局（5 个）
CARD_Y   = 100
CARD_H   = 400
CARD_W   = 290
CARD_GAP = 20
CARD_X0  = 20

cards = [
    (CARD_X0 + 0 * (CARD_W + CARD_GAP), CARD_Y, CARD_W, CARD_H, "空速"),
    (CARD_X0 + 1 * (CARD_W + CARD_GAP), CARD_Y, CARD_W, CARD_H, "高度"),
    (CARD_X0 + 2 * (CARD_W + CARD_GAP), CARD_Y, CARD_W, CARD_H, "姿态角"),
    (CARD_X0 + 3 * (CARD_W + CARD_GAP), CARD_Y, CARD_W, CARD_H, "油量"),
    (CARD_X0 + 4 * (CARD_W + CARD_GAP), CARD_Y, CARD_W, CARD_H, "转速"),
]

running = True
frame_count = 0

while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    throttle = throttle_arr[(frame_count // 60) % 60]
    update_flight(aircraft, dt, throttle)

    # 绘制
    screen.fill(theme.bg)

    # 顶部标题
    font_title = pygame.font.SysFont("consolas", 32, bold=True)
    title = font_title.render("✈ FLIGHT DASHBOARD", True, theme.text)
    screen.blit(title, (40, 30))

    # 5个卡片
    for (x, y, w, h, label) in cards:
        draw_card(screen, (x, y, w, h), theme)

    # 第一个卡片->空速表
    cx = cards[0][0] + CARD_W // 2
    cy = cards[0][1] + CARD_H // 2 + 20
    draw_dial(screen, cx, cy, 120, theme, value=aircraft.speed, min_val=0, max_val=1000, unit="km/h", label="")

    pygame.display.flip()

    if frame_count % 60 == 0:
        print(f"t={frame_count * dt:.1f}s | speed={aircraft.speed:.2f} | rpm={aircraft.rpm:.1f} | fuel={aircraft.fuel:.1f}")

    frame_count += 1

pygame.quit()
