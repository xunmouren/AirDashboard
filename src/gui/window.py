import pygame
import random

from bridge import init_flight_data, update_flight
from theme import DARK
from draw import draw_rect

pygame.init()

screen = pygame.display.set_mode((1600, 900))
pygame.display.set_caption("AirDashboard")
clock = pygame.time.Clock()

theme = DARK

aircraft = init_flight_data()
throttle_arr = [random.random() for _ in range(60)]

running = True
frame_count = 0

while running:
    dt = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    throttle = throttle_arr[(frame_count // 60) % 60]
    update_flight(aircraft, dt, throttle)

    screen.fill(theme.bg)
    draw_rect(screen, theme.dial_ring, (100, 100, 320, 400), radius=20)
    pygame.display.flip()

    if frame_count % 60 == 0:
        print(f"t={frame_count * dt:.1f}s | throttle={throttle*100:.1f}% | "
              f"speed={aircraft.speed:.2f} | rpm={aircraft.rpm:.1f} | fuel={aircraft.fuel:.1f}")

    frame_count += 1

pygame.quit()
