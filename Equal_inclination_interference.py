import pygame as pg
import sys
import numpy as np
import math
from PIL import Image
import pygame.freetype
import matplotlib.pyplot as plt

# 元素位置
slide_x, slide_y = 100, 450  # 波片位置
picture_x, picture_y = 425, 180  # 图像位置
title_x, title_y = 475, 50  # 标题位置
words_x, words_y = 875, 220  # 数据位置

# 元件属性的定义
slide_width = 200  # 波片宽度

# 元件相关量定义
d_c = 40
arrow_v = 160 - 19

# 图片相关量的定义
rho = 30  # 一厘米有多少个像素
px = 100  # 图片的宽度（像素）
size = px / rho  # 图片的尺寸（厘米）
RGBA = 0

# 相关物理量的定义
n = 1.3  # 折射率
lambda_ = 453e-9  # 波长
f = 0.8  # 透镜的焦距
I_source = 1.0  # 入射光强
d = 6e-3 + (d_c - 10) / 10 * 5e-5  # 波片厚度

# 颜色定义
BACKGROUND = 255, 255, 255
BLUE = 0, 132, 255
RED = 255, 0, 0

pg.init()  # 初始化窗体
icon = pg.image.load(r"image\logo.ico")  # 加载logo
pg.display.set_icon(icon)
screen = pg.display.set_mode((1180, 700))  # 设置主窗体的尺寸
pg.display.set_caption("Equal inclination interference")  # 设置窗体的标题
screen.fill(BACKGROUND)  # 将背景填充为白色

plt.figure(figsize=(4, 1.5))


def refresh(rect):
    pg.draw.rect(screen, BACKGROUND, rect, 0)


def matrix_creat(size):
    matrix = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            matrix[i, j] = np.sqrt((int(matrix.shape[0] / 2) - i) ** 2 + (int(matrix.shape[1] / 2) - j) ** 2)
    return matrix


def caculator_L(d):
    a = matrix_creat(px) / rho / 100  # 单位是米
    I_origin = 2 * I_source + 2 * I_source * np.cos(
        (2 * math.pi / lambda_) * (2 * d * np.sqrt(n ** 2 - (a ** 2) / (a ** 2 + f ** 2))))
    I_format = I_origin * (255 / 4)
    im = Image.fromarray(I_format)
    im = im.convert('L')
    im = im.resize((320, 320))
    im.save(r"image\Equal_inclination_interference.png")
    y = I_origin[int(arrow_v * px / 320 - 1), :][::1]
    x = np.linspace(1, y.size, y.size)

    plt.xlabel("location", fontsize=10)
    plt.ylabel("strength", fontsize=10)
    plt.xticks([])
    plt.yticks(fontsize=10)
    plt.plot(x, y)
    plt.savefig(r"image\Equal_inclination_interference_strength.png")
    plt.cla()

    img = Image.open(r"image\Equal_inclination_interference_strength.png")
    img = img.resize((425, 125))
    img.save(r"image\Equal_inclination_interference_strength.png")

    pic1 = pg.image.load(r"image\Equal_inclination_interference.png")
    pic2 = pg.image.load(r"image\Equal_inclination_interference_strength.png")
    return pic1, pic2


def draw_lightlines():
    pg.draw.aalines(screen, RED, False, [(slide_x - 5, slide_y - 50),
                                         (slide_x + 45, slide_y),
                                         (slide_x + 180, slide_y - 115),
                                         (slide_x + 232, slide_y - 111)], blend=1)
    pg.draw.aalines(screen, RED, False, [(slide_x + 145, slide_y),
                                         (slide_x + 224, slide_y - 66),
                                         (slide_x + 232, slide_y - 111)], blend=1)


def draw_btn_shade(btn):
    pg.draw.rect(screen, BACKGROUND, (btn.left, btn.top, btn.width, btn.height), 0)


def number_check():
    global d_c, temp, f, n, lambda_, I_source, arrow_v

    if temp == 5 or f == 1:
        temp = 0
        f = 0.5
    elif temp == -1 or f == 0.4:
        temp = 4
        f = 0.9

    d_c = d_c if d_c <= 80 else 80
    d_c = d_c if d_c >= 10 else 10

    n = n if n <= 2 else 2
    n = n if n >= 1.3 else 1.3

    lambda_ = lambda_ if lambda_ <= 760e-9 else 760e-9
    lambda_ = lambda_ if lambda_ >= 380e-9 else 380e-9

    I_source = I_source if I_source <= 1 else 1
    I_source = I_source if I_source >= 0.2 else 0.2

    arrow_v = arrow_v if arrow_v <= 320 - 38 else 320 - 38
    arrow_v = arrow_v if arrow_v >= - 19 else - 19


# 载入光源
pic_light = pg.image.load(r"image\light.png")

# 载入按钮
add = pg.image.load(r"image\add.png")
subtract = pg.image.load(r"image\subtract.png")
open_light_path = pg.image.load(r"image\light_path_open.png")
off_light_path = pg.image.load(r"image\light_path_off.png")
open_data = pg.image.load(r"image\data_open.png")
off_data = pg.image.load(r"image\data_off.png")

# 载入光屏
pic_screen = pg.image.load(r"image\screen1.png")
pic_screen = pg.transform.rotate(pic_screen, 130)

# 载入箭头
pic_arrow = pg.image.load(r"image\arrow.png")

# 载入透镜
pic_lens_0 = pg.image.load(r"image\ellipse0.png")
pic_lens_1 = pg.image.load(r"image\ellipse1.png")
pic_lens_2 = pg.image.load(r"image\ellipse2.png")
pic_lens_3 = pg.image.load(r"image\ellipse3.png")
pic_lens_4 = pg.image.load(r"image\ellipse4.png")
lens = [pic_lens_0, pic_lens_1, pic_lens_2, pic_lens_3, pic_lens_4]
pic_lens_s = pg.transform.rotate(pic_lens_2, -50)
pic_lens = screen.blit(pic_lens_s, (slide_x + 200, slide_y - 220))  # 绘制透镜

# 绘制标题
title = pygame.freetype.Font(r"font\STXINGKA.TTF", 36)
titlesurf, titlerect = title.render("等倾干涉", fgcolor=(0, 0, 0), size=50)

# 绘制波片
slide = pg.draw.rect(screen, BLUE, (slide_x, slide_y, slide_width, d_c), 0)

# 定义循环变量
temp = 2  # 用于切换透镜
light_judge = 1  # 光路状态

while True:
    # 数据
    data = pygame.freetype.Font(r"font\msyh.ttc")
    data1 = pygame.freetype.Font(r"font\STXINGKA.TTF")
    lambda_surf, lambda_rect = data.render("波长 λ = {:.2f}nm".format(lambda_ * 1e9), fgcolor=(0, 0, 0), size=22)
    fsurf, frect = data.render("透镜焦距 f = {:.2f}m".format(f), fgcolor=(0, 0, 0), size=22)
    dsurf, drect = data.render("波片厚度 d = {:.4f}mm".format(d * 1e3), fgcolor=(0, 0, 0), size=22)
    nsurf, nrect = data.render("波片折射率 n = {:.2f}".format(n), fgcolor=(0, 0, 0), size=22)
    Isurf, Irect = data.render("入射光强 I= {:.1f}".format(I_source), fgcolor=(0, 0, 0), size=22)
    sizesurf, sizerect = data.render("尺寸：{:.2f}cm * {:.2f}cm".format(size, size), fgcolor=(0, 0, 0), size=16)
    btitl_1_esurf, btitle_1_rect = data1.render("实验仪器", fgcolor=(0, 0, 0), size=30)
    btitl_2_esurf, btitle_2_rect = data1.render("干涉图样", fgcolor=(0, 0, 0), size=30)
    btitl_3_esurf, btitle_3_rect = data1.render("相应数据", fgcolor=(0, 0, 0), size=30)

    # 绘制箭头
    arrow = screen.blit(pic_arrow, (picture_x + 320, picture_y + arrow_v))

    # 获取鼠标位置
    mouse_x, mouse_y = pg.mouse.get_pos()
    # print(mouse_x - slide_x, mouse_y - slide_y)

    # 获取事件并逐类响应
    for event in pg.event.get():
        # 鼠标点击关闭按钮--关闭窗口
        if event.type == pg.QUIT:
            sys.exit()
        # 键盘按下事件
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                refresh(slide)
                d_c += 1
                d = 6e-3 + d_c * 5e-7
            elif event.key == pg.K_DOWN:
                refresh(slide)
                d_c -= 1
                d = 6e-3 + d_c * 5e-7
        # 鼠标移动事件
        elif event.type == pg.MOUSEMOTION:
            if event.pos[0] > slide.left and event.pos[0] < slide.right \
                    and event.pos[1] > slide.top + 10 and event.pos[1] < slide.top + 80 \
                    and event.buttons[0] == 1:
                refresh(slide)
                d_c = event.pos[1] - slide.top
                d = 6e-3 + d_c * 5e-7
            elif arrow.collidepoint((mouse_x, mouse_y)) and event.buttons[0] == 1:
                arrow_v = mouse_y - 19 - picture_y

        # 鼠标按下事件
        elif event.type == pg.MOUSEBUTTONDOWN:
            if pic_lens.collidepoint(event.pos):
                temp += 1
                f += 0.1
            elif lambda_btn_a.collidepoint((mouse_x, mouse_y)) and event.button == 1:
                lambda_ += 0.1e-10
            elif d_btn_a.collidepoint((mouse_x, mouse_y)) and event.button == 1:
                d_c += 1
                d = 6e-3 + d_c * 5e-7
                refresh(slide)
            elif f_btn_a.collidepoint((mouse_x, mouse_y)) and event.button == 1:
                f += 0.1
                temp += 1
            elif n_btn_a.collidepoint((mouse_x, mouse_y)) and event.button == 1:
                n += 0.05
            elif I_btn_a.collidepoint((mouse_x, mouse_y)) and event.button == 1:
                I_source += 0.05
            elif lambda_btn_s.collidepoint((mouse_x, mouse_y)) and event.button == 1:
                lambda_ -= 0.1e-10
            elif d_btn_s.collidepoint((mouse_x, mouse_y)) and event.button == 1:
                d_c -= 1
                d = 6e-3 + d_c * 5e-7
                refresh(slide)
            elif f_btn_s.collidepoint((mouse_x, mouse_y)) and event.button == 1:
                f -= 0.1
                temp -= 1
            elif n_btn_s.collidepoint((mouse_x, mouse_y)) and event.button == 1:
                n -= 0.05
            elif I_btn_s.collidepoint((mouse_x, mouse_y)) and event.button == 1:
                I_source -= 0.05
            elif light_path.collidepoint((mouse_x, mouse_y)) and event.button == 1:
                light_judge = -light_judge

    # 检查数据的正确性
    number_check()

    # 清空屏幕
    screen.fill(BACKGROUND)

    # 绘制标题
    screen.blit(titlesurf, (title_x, title_y))

    # 绘制波片
    slide = pg.draw.rect(screen, BLUE, (slide_x, slide_y, slide_width, d_c), 0)

    # 绘制光屏
    screen.blit(pic_screen, (slide_x + 190, slide_y - 170))

    # 绘制光路图开关
    if light_judge < 0:
        light_path = screen.blit(off_light_path, (30, 250))
        draw_lightlines()
    else:
        light_path = screen.blit(open_light_path, (30, 250))

    # 绘制透镜
    pic_lens_s = pg.transform.rotate(lens[temp], -50)  # 旋转
    pic_lens = screen.blit(pic_lens_s, (slide_x + 150, slide_y - 150))

    # 绘制光源
    pic_light_d = screen.blit(pic_light, (slide_x - 30 - 25, slide_y - 75 - 25))  # 绘制光源

    # 计算图像
    pic1, pic2 = caculator_L(d)

    # 绘制图像
    screen.blit(pic1, (picture_x, picture_y))
    # 绘制光强分布图
    screen.blit(pic2, ((picture_x - 57, picture_y + 300)))

    # 箭头
    arrow = screen.blit(pic_arrow, (picture_x + 320, picture_y + arrow_v))

    # 绘制数据
    lambda_v = screen.blit(lambda_surf, (words_x, words_y))
    d_v = screen.blit(dsurf, (words_x, words_y + 70))
    f_v = screen.blit(fsurf, (words_x, words_y + 140))
    n_v = screen.blit(nsurf, (words_x, words_y + 210))
    I_v = screen.blit(Isurf, (words_x, words_y + 280))

    # 绘制按钮
    lambda_btn_a = screen.blit(add, (lambda_v.left - 40, lambda_v.top - 5))
    d_btn_a = screen.blit(add, (d_v.left - 40, d_v.top - 5))
    f_btn_a = screen.blit(add, (f_v.left - 40, f_v.top - 5))
    n_btn_a = screen.blit(add, (n_v.left - 40, n_v.top - 5))
    I_btn_a = screen.blit(add, (I_v.left - 40, I_v.top - 5))
    lambda_btn_s = screen.blit(subtract, (lambda_v.right + 10, lambda_v.top - 5))
    d_btn_s = screen.blit(subtract, (d_v.right + 10, d_v.top - 5))
    f_btn_s = screen.blit(subtract, (f_v.right + 10, f_v.top - 5))
    n_btn_s = screen.blit(subtract, (n_v.right + 10, n_v.top - 5))
    I_btn_s = screen.blit(subtract, (I_v.right + 10, I_v.top - 5))

    # 绘制比例尺
    size_v = screen.blit(sizesurf, (picture_x + 100, picture_y - 25))

    # 绘制底部文字
    bt1 = screen.blit(btitl_1_esurf, (150, 550))
    bt2 = screen.blit(btitl_2_esurf, (525, 630))
    bt2 = screen.blit(btitl_3_esurf, (925, 575))

    # 刷新屏幕
    pg.display.update()
