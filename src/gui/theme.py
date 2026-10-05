from dataclasses import dataclass


@dataclass
class Theme:
    # 背景与容器
    bg:          tuple = (4, 12, 32)
    card_bg:     tuple = (12, 22, 45)
    card_border: tuple = (30, 50, 80)

    # 文字
    text:        tuple = (0, 212, 255)
    text_dim:    tuple = (100, 130, 160)

    # 表盘元素
    dial_ring:   tuple = (0, 255, 156)
    tick_main:   tuple = (0, 255, 156)
    tick_sub:    tuple = (0, 120, 80)
    needle:      tuple = (255, 255, 255)
    needle_tip:  tuple = (255, 59, 59)

    # 状态色
    normal:      tuple = (0, 255, 156)
    warn:        tuple = (255, 184, 0)
    danger:      tuple = (255, 59, 59)

    # 报警等级 → 颜色
    def alarm_color(self, level: int) -> tuple:
        return [self.normal, self.warn, self.danger][level]


# 深色主题（当前用）
DARK = Theme()

# 浅色主题（后期加，只改需要覆盖的字段）
LIGHT = Theme(
    bg          = (245, 245, 240),
    card_bg     = (255, 255, 255),
    card_border = (200, 200, 200),
    text        = (30, 30, 30),
    text_dim    = (120, 120, 120),
    dial_ring   = (0, 150, 100),
    tick_main   = (0, 150, 100),
    tick_sub    = (150, 200, 180),
    needle      = (30, 30, 30),
)