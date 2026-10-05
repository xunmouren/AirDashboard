import pygame
import math


def draw_rect(screen, color, rect, width=0, radius=0):
    pygame.draw.rect(screen, color, rect, width=width, border_radius=radius)


def draw_card(screen, rect, theme):
    """画一个卡片背景"""
    x, y, w, h = rect
    pygame.draw.rect(screen, theme.card_border, (x, y, w, h), border_radius=12)
    pygame.draw.rect(screen, theme.card_bg, (x + 2, y + 2, w - 4, h - 4), border_radius=11)


def draw_dial(screen, cx, cy, radius, theme, value=0.0, min_val=0, max_val=1000,
              start_angle=135, sweep_angle=270, unit="km/h", label=""):
    """完整表盘：外圈 + 彩色弧 + 刻度 + 数字 + 指针 + 中央读数"""
    font_tick = pygame.font.SysFont("consolas", 16, bold=True)
    font_big  = pygame.font.SysFont("consolas", 30, bold=True)
    font_unit = pygame.font.SysFont("consolas", 18)
    font_label= pygame.font.SysFont("consolas", 20, bold=True)

    # 卡片标题
    if label:
        text = font_label.render(label, True, theme.text)
        screen.blit(text, text.get_rect(center=(cx, cy - radius - 20)))

    # 弧形彩色区间
    arc_rect = (cx - radius, cy - radius, radius * 2, radius * 2)
    segments = 60
    for i in range(segments):
        t0 = i / segments
        t1 = (i + 1) / segments
        # 绿→黄→红插值
        if t0 < 0.6:
            r = int(0 + (255 - 0) * (t0 / 0.6))
            g = 255
            b = 0
        else:
            r = 255
            g = int(255 - 255 * ((t0 - 0.6) / 0.4))
            b = 0
        color = (r, g, b)

        a0 = math.radians(start_angle + t0 * sweep_angle)
        a1 = math.radians(start_angle + t1 * sweep_angle)
        pygame.draw.arc(screen, color, arc_rect, -a1, -a0, 6)

    # 外圈
    pygame.draw.circle(screen, theme.dial_ring, (int(cx), int(cy)), int(radius), 2)

    # 刻度数字
    for i in range(0, 101, 2):
        ratio = i / 100.0
        angle_deg = start_angle + ratio * sweep_angle
        angle_rad = math.radians(angle_deg)

        is_main = (i % 10 == 0)
        length  = 20 if is_main else 8
        width   = 3  if is_main else 1
        color   = theme.tick_main if is_main else theme.tick_sub

        x_out = cx + radius * math.cos(angle_rad)
        y_out = cy + radius * math.sin(angle_rad)
        x_in  = cx + (radius - length) * math.cos(angle_rad)
        y_in  = cy + (radius - length) * math.sin(angle_rad)

        pygame.draw.line(screen, color, (int(x_in), int(y_in)), (int(x_out), int(y_out)), width)

        if is_main:
            v = min_val + (max_val - min_val) * ratio
            x_text = cx + (radius - 50) * math.cos(angle_rad)
            y_text = cy + (radius - 50) * math.sin(angle_rad)
            text = font_tick.render(str(int(v)), True, theme.text)
            screen.blit(text, text.get_rect(center=(int(x_text), int(y_text))))

    # 指针
    angle = start_angle + (value - min_val) / (max_val - min_val) * sweep_angle
    angle_rad = math.radians(angle)

    tip_x = cx + radius * 0.75 * math.cos(angle_rad)
    tip_y = cy + radius * 0.75 * math.sin(angle_rad)

    # 指针主体
    pygame.draw.line(screen, theme.needle, (cx, cy), (tip_x, tip_y), 4)

    # 中心轴
    pygame.draw.circle(screen, theme.needle_tip, (int(cx), int(cy)), 10)
    pygame.draw.circle(screen, theme.card_bg, (int(cx), int(cy)), 5)

    # 中央读数
    text_big = font_big.render(f"{value:.0f}", True, theme.text)
    screen.blit(text_big, text_big.get_rect(center=(cx, cy + radius * 0.6)))

    text_unit = font_unit.render(unit, True, theme.text_dim)
    screen.blit(text_unit, text_unit.get_rect(center=(cx, cy + radius * 0.45 + 40)))