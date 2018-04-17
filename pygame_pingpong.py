# -*- coding: utf-8 -*-
import pygame as pg
# 导入 pygame 常量
from pygame.locals import *
from time import sleep
import sys

# 初始化
pg.init()
# 设置屏幕大小
scr = pg.display.set_mode([600, 500])
# 设置标题
pg.display.set_caption(("打乒乓球"))
# 颜色定义
pp = (255, 140, 0)
green = (0, 255, 0)
white = (255, 255, 255)
cs = (255, 121, 21)

# 乒乓球起始位置
x = 120
y = 120
# 初速度
vx = 1
vy = 1
# 球拍 x 坐标，y 坐标固定
a = 200

# 字体
# zt1 = pg.font.SysFont("", 24)
# zt2 = pg.font.SysFont("", 20)
zt1 = pg.font.Font("/Library/Fonts/Arial Unicode.ttf", 24)
zt2 = pg.font.Font("/Library/Fonts/Arial Unicode.ttf", 20)


def print_text(font, text, x, y, color):
    img = font.render(text, True, color)
    scr.blit(img, (x, y))


# 加速器，如果接住了3次，就加速
c = 0
# 分数，接到一次球就加分
fs = 0
# 基础加分
k = 1

while True:
    scr.fill((199, 21, 133))
    for eve in pg.event.get():
        # 监听退出
        if eve.type == QUIT:
            sys.exit()
    # 获得鼠标的坐标
    mx, my = pg.mouse.get_pos()
    # 把鼠标的 x 坐标赋值给球拍的 x 坐标
    a = mx
    # 深度为0，实心圆
    pg.draw.circle(scr, pp, (x, y), 40, 0)
    # 长宽分别为100，20的球拍
    pg.draw.rect(scr, green, (a, 475, 100, 20), 0)
    # 球碰到左右屏幕边缘，vx 取反
    # 碰到上边缘或者球拍，vy 取反
    # 其余情况表示球拍没有碰到球，跳出循环，游戏结束
    x = x + vx
    y = y + vy
    if x >= 560 or x <= 40:
        vx = -vx
    if y <= 40:
        vy = -vy
    # 是否接到球判断
    elif y >= 435 and (0 <= x - a <= 100):
        # 变向
        vy = -vy
        # 每接到球一次，接到次数加一
        c = c + 1
        # 每接到球一次，添加得分数
        fs = fs + k
        # 接到球三次，加速
        if c >= 3:
            c = 0
            # 加速一次，基础分翻倍
            k = k * 2
            # 加速
            if vx > 0:
                vx = vx + 1
            else:
                vx = vx - 1
        else:
            pass
    elif y >= 435 and (x - a < 0 or x - a > 100):
        break
    else:
        pass
    # 休眠
    sleep(0.005)
    print_text(zt1, "移动鼠标控制乒乓板左右移动", 20, 30, white)
    print_text(zt2, "得分", 550, 12, cs)
    print_text(zt2, str(fs), 560, 32, cs)
    pg.display.update()

# 游戏结束，改变背景色
scr.fill((211, 21, 33))
# zt3 = pg.font.SysFont("Arial Unicode.ttf", 120)
# zt4 = pg.font.SysFont("Arial Unicode.ttf", 60)
zt3 = pg.font.Font("/Library/Fonts/Arial Unicode.ttf", 120)
zt4 = pg.font.Font("/Library/Fonts/Arial Unicode.ttf", 60)
print_text(zt3, "游戏结束", 60, 120, white)
print_text(zt4, "得分：" + str(fs), 120, 400, white)
pg.display.update()






