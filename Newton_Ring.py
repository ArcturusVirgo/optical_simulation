import pygame as pg
import sys
import numpy as np
import math
from PIL import Image
import pygame.freetype
import matplotlib.pyplot as plt

# 元素位置
words_x, words_y = 875, 220  # 数据位置
pedestal_x, pedestal_y = 50, 425  # 基座位置
picture_x, picture_y = 425, 180  # 图像位置
title_x, title_y = 350, 30  # 标题位置

# 图片相关量的定义
rho = 400  # 一厘米有多少个像素
px = 100  # 图片的宽度（像素）
size = px / rho  # 图片的尺寸（厘米）
 
# 相关物理量的定义
n = 1  # 折射率
lambda_ = 450e-9  # 波长
R = 1.0  # 透镜的曲率半径
h = 0  # 平面玻璃与平凸透镜球面间的距离
I_source = 1.0  # 入射光强

# 颜色定义
BACKGROUND = 255, 255, 255
BLUE = 0, 132, 255
RED = 255, 0, 0

# 元件相关量定义
R_c = 1250  # 曲率半径
d_c = 0  # 镜座间隙
arrow_v = 160 - 19  # 箭头纵坐标

# pygame初始化
pg.init()  # 初始化窗体
icon = pg.image.load(r"image\logo.ico")
pg.display.set_icon(icon)
screen = pg.display.set_mode((1180, 700))  # 设置主窗体的尺寸
pg.display.set_caption("NewtonsRings")  # 设置窗体的标题
screen.fill(BACKGROUND)  # 将背景填充为白色

# 定义绘图窗口
plt.figure(figsize=(4, 1.5))


def draw_shade():  # 绘制遮罩
    pg.draw.rect(screen, BACKGROUND, (0, 0, pedestal_rect.left, 700), 0)  # 左
    pg.draw.rect(screen, BACKGROUND, (pedestal_rect.right, 0, 1180, 700), 0)  # 右
    pg.draw.rect(screen, BACKGROUND, (0, 0, 1180, pedestal_y - 50 - d_c), 0)  # 上


def draw_circle():  # 绘制圆
    x, y = get_circle_center()
    pg.draw.circle(screen, BLUE, (x, y), R_c, 0)


def get_circle_center():  # 获取圆心坐标
    return pedestal_rect.centerx, pedestal_rect.top - R_c - d_c if d_c >= 0 else 0


def refresh_circle(delta_R=0, delta_d=0):  # 刷新圆
    global R_c, d_c
    R_c = (R_c + delta_R) if (R_c + delta_R >= 300) and (R_c + delta_R <= 2000) else R_c
    d_c = (d_c + delta_d) if (d_c + delta_d >= 0) and (d_c + delta_d <= 50) else d_c
    draw_circle()


def matrix_creat(size):
    matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            matrix[i, j] = np.sqrt((int(matrix.shape[0] / 2) - i) ** 2 + (int(matrix.shape[1] / 2) - j) ** 2)
    return matrix


def caculator_L(R, h):
    a = matrix_creat(px) / rho / 100
    I_origin = 4 * I_source * np.sin((n * math.pi * (a ** 2)) / (R * lambda_) + (2 * n * h * math.pi) / lambda_) ** 2
    I_format = I_origin * (255 / 4)
    im = Image.fromarray(I_format)
    im = im.convert('L')
    im = im.resize((320, 320))
    im.save(r"image\Newtons_rings.png")
    y = I_origin[int(arrow_v * px / 320 - 1), :][::1]
    x = np.linspace(1, y.size, y.size)

    plt.xlabel("location", fontsize=10)
    plt.ylabel("strength", fontsize=10)
    plt.xticks([])
    plt.yticks(fontsize=10)
    plt.plot(x, y)
    plt.savefig(r"image\Newtons_rings_strength.png")
    plt.cla()

    img = Image.open(r"image\Newtons_rings_strength.png")
    img = img.resize((425, 125))
    img.save(r"image\Newtons_rings_strength.png")

    pic1 = pg.image.load(r"image\Newtons_rings.png")
    pic2 = pg.image.load(r"image\Newtons_rings_strength.png")

    return pic1, pic2


def number_check():  # 数据检查
    global R, h, n, lambda_, I_source, arrow_v

    R = R if R <= 1.5 else 1.5
    R = R if R >= 0.5 else 0.5

    h = h if h <= 10e-6 else 5e-7
    h = h if h >= 0 else 0

    n = n if n <= 2 else 2
    n = n if n >= 1 else 1

    lambda_ = lambda_ if lambda_ <= 760e-9 else 760e-9
    lambda_ = lambda_ if lambda_ >= 380e-9 else 380e-9

    I_source = I_source if I_source <= 1 else 1
    I_source = I_source if I_source >= 0 else 0

    arrow_v = arrow_v if arrow_v <= 320 - 38 else 320 - 38
    arrow_v = arrow_v if arrow_v >= - 19 else - 19


def draw_lightlines():  # 绘制光线
    # 主体
    pg.draw.aalines(screen, RED, False, [(pedestal_x + 50, pedestal_y - 200),
                                         (pedestal_x + 50, pedestal_y - 50 - d_c)], blend=1)
    pg.draw.aalines(screen, RED, False, [(pedestal_x + 100, pedestal_y - 200),
                                         (pedestal_x + 100, pedestal_y - 50 - d_c)], blend=1)
    pg.draw.aalines(screen, RED, False, [(pedestal_x + 150, pedestal_y - 200),
                                         (pedestal_x + 150, pedestal_y - 50 - d_c)], blend=1)
    pg.draw.aalines(screen, RED, False, [(pedestal_x + 200, pedestal_y - 200),
                                         (pedestal_x + 200, pedestal_y - 50 - d_c)], blend=1)
    pg.draw.aalines(screen, RED, False, [(pedestal_x + 250, pedestal_y - 200),
                                         (pedestal_x + 250, pedestal_y - 50 - d_c)], blend=1)


# 创建标题
title = pygame.freetype.Font(r"font\STXINGKA.TTF", 36)
titlesurf, titlerect = title.render("牛顿环实验仿真模拟", fgcolor=(0, 0, 0), size=50)

# 载入按钮
add = pg.image.load(r"image\add.png")
subtract = pg.image.load(r"image\subtract.png")
open_light_path = pg.image.load(r"image\light_path_open.png")
off_light_path = pg.image.load(r"image\light_path_off.png")
open_data = pg.image.load(r"image\data_open.png")
off_data = pg.image.load(r"image\data_off.png")

# 载入箭头
pic_arrow = pg.image.load(r"image\arrow.png")

# 载入光源
pic_light = pg.image.load(r"image\line_light.png")



# 绘制装置
pedestal_rect = pg.draw.rect(screen, BLUE, (pedestal_x, pedestal_y, 300, 75), 0)  # 底座
draw_circle()  # 圆
draw_shade()  # 遮罩

# 定义循环变量
light_judge = 1  # 光路状态
detail_judge = -1  # 显示详细信息

while True:
    # 数据
    data = pygame.freetype.Font(r"font\msyh.ttc", 36)
    data1 = pygame.freetype.Font(r"font\STXINGKA.TTF")
    lambda_surf, lambda_rect = data.render("波长 λ = {:.2f}nm".format(lambda_ * 1e9), fgcolor=(0, 0, 0), size=22)
    Rsurf, Rrect = data.render("曲率半径 R = {:.2f}m".format(R), fgcolor=(0, 0, 0), size=22)
    hsurf, hrect = data.render("镜座间隙 e = {:.2f}μm".format(h * 1e6), fgcolor=(0, 0, 0), size=22)
    nsurf, nrect = data.render("间隙物质折射率 n = {:.2f}".format(n), fgcolor=(0, 0, 0), size=22)
    Isurf, Irect = data.render("入射光强 I= {:.1f}".format(I_source), fgcolor=(0, 0, 0), size=22)
    sizesurf, sizerect = data.render("尺寸：{:.2f}cm * {:.2f}cm".format(size, size), fgcolor=(0, 0, 0), size=16)
    btitl_1_esurf, btitle_1_rect = data1.render("实验装置", fgcolor=(0, 0, 0), size=30)
    btitl_2_esurf, btitle_2_rect = data1.render("干涉图样", fgcolor=(0, 0, 0), size=30)
    btitl_3_esurf, btitle_3_rect = data1.render("相应数据", fgcolor=(0, 0, 0), size=30)

    # 绘制箭头
    arrow = screen.blit(pic_arrow, (picture_x + 320, picture_y + arrow_v))

    # 获取鼠标位置
    mouse_x, mouse_y = pg.mouse.get_pos()

    # 获取事件并逐类响应
    for event in pg.event.get():
        # 鼠标点击关闭按钮--关闭窗口
        if event.type == pg.QUIT:
            sys.exit()
        # 键盘按下事件
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                h += 5e-8
                refresh_circle(0, 5)
            elif event.key == pg.K_DOWN:
                h -= 5e-8
                refresh_circle(0, -5)
            elif event.key == pg.K_RIGHT:
                R += 0.1
                refresh_circle(100, 0)
            elif event.key == pg.K_LEFT:
                R -= 0.1
                refresh_circle(-100, 0)
        # 鼠标移动事件
        elif event.type == pg.MOUSEMOTION:
            if event.pos[0] > pedestal_rect.left and event.pos[0] < pedestal_rect.right \
                    and event.pos[1] > pedestal_rect.top and event.pos[1] < pedestal_rect.bottom \
                    and event.buttons[0] == 1:
                R += 0.005 * event.rel[0]
                refresh_circle(event.rel[0] * 5, 0)
            elif event.pos[0] > pedestal_rect.left and event.pos[0] < pedestal_rect.right \
                    and event.pos[1] > pedestal_rect.top - 50 - d_c and event.pos[1] < pedestal_rect.top - d_c \
                    and event.buttons[0] == 1:
                refresh_circle(0, -event.rel[1])
                h += -event.rel[1] * 1e-8
            elif arrow.collidepoint((mouse_x, mouse_y)) and event.buttons[0] == 1:
                arrow_v = mouse_y - 19 - picture_y
        # 鼠标按下事件
        elif event.type == pg.MOUSEBUTTONDOWN:
            if lambda_btn_a.collidepoint((mouse_x, mouse_y)) and event.button == 1:
                lambda_ += 10e-9
            elif R_btn_a.collidepoint((mouse_x, mouse_y)) and event.button == 1:
                R += 0.1
                refresh_circle(100, 0)
            elif h_btn_a.collidepoint((mouse_x, mouse_y)) and event.button == 1:
                h += 5e-8
                refresh_circle(0, 5)
            elif n_btn_a.collidepoint((mouse_x, mouse_y)) and event.button == 1:
                n += 0.01
            elif I_btn_a.collidepoint((mouse_x, mouse_y)) and event.button == 1:
                I_source += 0.05
            elif lambda_btn_s.collidepoint((mouse_x, mouse_y)) and event.button == 1:
                lambda_ -= 10e-9
            elif R_btn_s.collidepoint((mouse_x, mouse_y)) and event.button == 1:
                R -= 0.1
                refresh_circle(-100, 0)
            elif h_btn_s.collidepoint((mouse_x, mouse_y)) and event.button == 1:
                h -= 5e-8
                refresh_circle(0, -5)
            elif n_btn_s.collidepoint((mouse_x, mouse_y)) and event.button == 1:
                n -= 0.01
            elif I_btn_s.collidepoint((mouse_x, mouse_y)) and event.button == 1:
                I_source -= 0.05
            elif light_path.collidepoint((mouse_x, mouse_y)) and event.button == 1:
                light_judge = -light_judge

    number_check()  # 检查数据的正确性

    # 清空屏幕
    screen.fill(BACKGROUND)

    # 绘制装置
    pedestal_rect = pg.draw.rect(screen, BLUE, (pedestal_x, pedestal_y, 300, 75), 0)  # 底座
    draw_circle()  # 圆
    draw_shade()  # 遮罩

    # 绘制光源
    pic_light_d = screen.blit(pic_light, (pedestal_x, pedestal_y - 250))  # 绘制光源

    # 绘制光路图
    if light_judge < 0:
        light_path = screen.blit(off_light_path, (30, 50))
        draw_lightlines()
    else:
        light_path = screen.blit(open_light_path, (30, 50))

    #  计算图像
    pic1, pic2 = caculator_L(R, h)
    # 绘制干涉图样
    screen.blit(pic1, (picture_x, picture_y))
    # 绘制光强分布图
    screen.blit(pic2, ((picture_x - 57, picture_y + 300)))

    # 绘制箭头
    arrow = screen.blit(pic_arrow, (picture_x + 320, picture_y + arrow_v))

    # 绘制数据
    lambda_v = screen.blit(lambda_surf, (words_x, words_y))
    R_v = screen.blit(Rsurf, (words_x, words_y + 70))
    h_v = screen.blit(hsurf, (words_x, words_y + 140))
    n_v = screen.blit(nsurf, (words_x, words_y + 210))
    I_v = screen.blit(Isurf, (words_x, words_y + 280))
    # 绘制按钮
    lambda_btn_a = screen.blit(add, (lambda_v.left - 40, lambda_v.top - 5))
    R_btn_a = screen.blit(add, (R_v.left - 40, R_v.top - 5))
    h_btn_a = screen.blit(add, (h_v.left - 40, h_v.top - 5))
    n_btn_a = screen.blit(add, (n_v.left - 40, n_v.top - 5))
    I_btn_a = screen.blit(add, (I_v.left - 40, I_v.top - 5))
    lambda_btn_s = screen.blit(subtract, (lambda_v.right + 10, lambda_v.top - 5))
    R_btn_s = screen.blit(subtract, (R_v.right + 10, R_v.top - 5))
    h_btn_s = screen.blit(subtract, (h_v.right + 10, h_v.top - 5))
    n_btn_s = screen.blit(subtract, (n_v.right + 10, n_v.top - 5))
    I_btn_s = screen.blit(subtract, (I_v.right + 10, I_v.top - 5))

    # 绘制标题
    screen.blit(titlesurf, (title_x, title_y))

    # 绘制比例尺
    size_v = screen.blit(sizesurf, (picture_x + 100, picture_y - 25))

    # 绘制底部文字
    bt1 = screen.blit(btitl_1_esurf, (150, 550))
    bt2 = screen.blit(btitl_2_esurf, (525, 630))
    bt2 = screen.blit(btitl_3_esurf, (925, 575))

    # 刷新屏幕
    pg.display.update()
