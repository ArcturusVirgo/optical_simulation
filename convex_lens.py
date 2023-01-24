import pygame as p
import sys
import math as m
import numpy as np

p.init()
size = (width, height) = (1500, 800)
screen = p.display.set_mode(size, p.RESIZABLE)
p.display.set_caption("凸透镜")
LinesLenth = 4500  # 线段的长度
jiaoju = 120  # 设置透镜的焦距
font = p.font.Font('font/华文楷体.TTF', 30)
FontTiger = p.font.Font('font/华文楷体.TTF', 30)
LineRate = 0.9
LinesLight = []
LinesLightStete = -1  # 控制光路是否可见
MouseState = False
Width, Height = width, height
FocalLength = jiaoju
Screen = screen
LPos = [200, 600]
ListJiaoju = [[int(width / 2 - jiaoju), int(height / 2)], [int(width / 2 + jiaoju), int(height / 2)]]
Lines = [[(0, 0, 0), ((1 - LineRate) * width, height // 2), (LineRate * width, height // 2)],
         [(0, 0, 0), (width // 2, LPos[0]), (width // 2, LPos[1])]]  # 颜色，起点坐标和目标坐标

font2 = p.font.Font('font/华文楷体.TTF', 40)
# TextBg = p.image.load('参数2.png')
TextBgBg = p.image.load('image/lens/参数gb.png')
# bg = p.image.load('bg.png')
TextBgPos = (1220, 20)
TextBPos = (1230, 40)
TextSPos = (1230, 90)
TextS1Pos = (1230, 140)
TextLPos = (1230, 190)
TextColor = (156, 0, 255)
AddPos = (TextSPos[0] + 145, TextSPos[1])
SubPos = (TextSPos[0] + 130 + 60, TextSPos[1])
TextLightPos = (1230, 240)
TextSwithPos = (TextLightPos[0] + 120, TextLightPos[1])
AddImage = p.image.load('image/lens/add.png')
SubImage = p.image.load('image/lens/subtract.png')
LightOn = p.image.load('image/lens/LightOn.png')
LightOff = p.image.load('image/lens/LightOff.png')
b = 0
LPos = [200, 600]
red = (255, 0, 0)
purple = (255, 0, 255)


def UpdataPos():
    global Width, Height, LPos, TextBgPos, TextBPos, TextS1Pos, TextLPos, AddPos, SubPos, TextSwithPos, TextLightPos, TextSPos, height, width, Lines, ListJiaoju
    Width, Height = p.display.get_window_size()
    width, height = p.display.get_window_size()
    LPos = [Height // 2 - 300, Height // 2 + 300]
    TextBgPos = (Width - 280, 20)
    TextBPos = (Width - 270, 40)
    TextSPos = (Width - 270, 90)
    TextS1Pos = (Width - 270, 140)
    TextLPos = (Width - 270, 190)
    AddPos = (TextSPos[0] + 130, TextSPos[1])
    SubPos = (TextSPos[0] + 130 + 60, TextSPos[1])
    TextLightPos = (Width - 270, 240)
    TextSwithPos = (TextLightPos[0] + 120, TextLightPos[1])
    Lines = [[(0, 0, 0), ((1 - LineRate) * width, height // 2), (LineRate * width, height // 2)],
             [(0, 0, 0), (width // 2, LPos[0]), (width // 2, LPos[1])]]  # 颜色，起点坐标和目标坐标
    ListJiaoju = [[int(width / 2 - jiaoju), int(height / 2)], [int(width / 2 + jiaoju), int(height / 2)]]


def LoadImage():
    global MouseState
    screen.blit(AddImage, (AddPos))
    screen.blit(SubImage, (SubPos))
    if MouseState and 0 <= dot.pos[0] < Width // 2 - 1:
        if AddPos[0] <= p.mouse.get_pos()[0] <= AddPos[0] + 32 and AddPos[1] <= p.mouse.get_pos()[1] <= AddPos[1] + 32:
            dot.pos[0] -= 0.1
            MouseState = False
        elif SubPos[0] <= p.mouse.get_pos()[0] <= SubPos[0] + 32 and SubPos[1] <= p.mouse.get_pos()[1] <= SubPos[
            1] + 32:
            dot.pos[0] += 0.1
            MouseState = False


class Dot():
    def __init__(self):
        self.pos = [width // 2 - 80, Height // 2 - 100]  # 初始光源位置


def arr(x, y, up=0, down=0, color=(123, 0, 123)):  # 绘制箭头
    if up == 1:
        p.draw.line(screen, color, (x, y), (int(x - 10), int(y + 10)), 10)
        p.draw.line(screen, color, (x, y), (int(x + 10), int(y + 10)), 10)
    elif down == 1:
        p.draw.line(screen, color, (x, y), (int(x - 10), int(y - 10)), 10)
        p.draw.line(screen, color, (x, y), (int(x + 10), int(y - 10)), 10)


def DesDot(x1, y1, x2, y2):  # 计算两点的距离
    xiebian = m.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    x = x1 + LinesLenth * (x2 - x1) / xiebian
    y = y1 + LinesLenth * (y2 - y1) / xiebian
    return x, y


def Intersection(x1, y1, x2, y2):  # 计算成像的交点
    k = (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else 1000
    b = y1 - k * x1
    y3 = k * (fuhao() + width // 2) + b
    return fuhao() + width // 2, y3


def XieLv(x, y, k):  # 起始的坐标和斜率
    b = y - k * x
    x1 = width + 300
    y1 = k * x1 + b
    return x1, y1


dot = Dot()


def AddLines():
    global Lines
    LinesLight.append([(255, 0, 0), (dot.pos[0], dot.pos[1]), (int(width / 2), dot.pos[1])])
    # 过焦距的光线
    LinesLight.append([(255, 0, 0), (int(width / 2), dot.pos[1]),
                       (DesDot(int(width / 2), dot.pos[1], width / 2 + jiaoju, height / 2))])
    LinesLight.append(
        [(255, 0, 0), (dot.pos[0], dot.pos[1]), (DesDot(dot.pos[0], dot.pos[1], width / 2, height / 2))])  # 过光心的光线
    if int(dot.pos[1]) == int(height // 2):
        LinesLight.append([(255, 0, 0), (dot.pos[0], dot.pos[1]), (width / 2, height / 2 - (width / 2 - dot.pos[0]))])
        x, y = width // 2 - jiaoju, height // 2 - (width // 2 - jiaoju - dot.pos[0])  # 光线与物方焦平面的交点
        k = (y - Height / 2) / (x - Width / 2)
        LinesLight.append([(255, 0, 0), (width / 2, height / 2 - (width / 2 - dot.pos[0])),
                           (XieLv(width / 2, height / 2 - (width / 2 - dot.pos[0]), k))])
    line1 = np.linspace(150, Width // 2, 30)
    line2 = np.linspace(LPos[0], LPos[1], 20)
    for i in range(0, len(line1) - 1, 2):
        p.draw.line(Screen, (0, 255, 48), (line1[i], LPos[0]), (line1[i + 1], LPos[0]), 2)
        p.draw.line(Screen, (0, 255, 48), (line1[i], LPos[1]), (line1[i + 1], LPos[1]), 2)
    for i in range(0, len(line2) - 1, 2):
        p.draw.line(Screen, (0, 255, 48), (150, line2[i]), (150, line2[i + 1]), 2)


def init_bg():  # 初始化背景和获得鼠标点击的位置
    screen.fill((255, 255, 255))
    # screen.blit(bg, (0, 0))
    if MouseState == True:
        if 150 <= p.mouse.get_pos()[0] <= Width // 2 and LPos[0] <= p.mouse.get_pos()[1] <= LPos[1]:
            dot.pos = [p.mouse.get_pos()[0], p.mouse.get_pos()[1]]


def event():
    global MouseState, LinesLightStete
    for i in p.event.get():
        if i.type == p.QUIT:
            p.quit()
            sys.exit()
        elif i.type == p.MOUSEBUTTONDOWN:
            MouseState = True
        elif i.type == p.MOUSEBUTTONUP:
            MouseState = False
            if TextSwithPos[0] <= p.mouse.get_pos()[0] <= TextSwithPos[0] + 82 and TextSwithPos[1] <= p.mouse.get_pos()[
                1] <= TextSwithPos[1] + 35:
                LinesLightStete = -LinesLightStete


def DrawDot():
    global jiaoju
    # p.draw.circle(screen,(222,0,0),dot.pos,1) #光源的绘制
    p.draw.circle(screen, (0, 0, 0), ListJiaoju[0], 8)
    p.draw.circle(screen, (0, 0, 0), ListJiaoju[1], 8)
    p.draw.circle(screen, (0, 0, 0), (width // 2, height // 2), 5)
    p.draw.circle(screen, (0, 0, 0), (width // 2 - 2 * jiaoju, height // 2), 8)
    p.draw.circle(screen, (0, 0, 0), (width // 2 + 2 * jiaoju, height // 2), 8)


def GetLines(x1, y1, x2, y2):
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    return [[i, i * k + b] for i in np.arange(min(x1, x2), max(x1, x2), 5)]


def DrawLines():
    global Lines, b
    for i in Lines:
        p.draw.line(screen, i[0], i[1], i[2], 3)
    for i in LinesLight:
        p.draw.line(screen, i[0], i[1], i[2], 3)
        LinesLight.remove(i)
    arr(width // 2, LPos[0], up=1, color=(0, 0, 0))  # 绘制两个箭头
    arr(width // 2, LPos[1], down=1, color=(0, 0, 0))
    p.draw.line(screen, (255, 0, 0), dot.pos, (dot.pos[0], height // 2), 6)  # 物体
    TempBule = 30 if fuhao() > 0 else 255
    if dot.pos[1] <= height // 2:
        x1, y1 = dot.pos[0], dot.pos[1]
    else:
        x1, y1 = dot.pos[0], Height // 2
    arr(x1, y1, up=1, color=(255, 0, 0))
    up, down = 0, 0
    delta = (dot.pos[0] - width // 2) if (dot.pos[0] - width // 2) != 0 else 1000
    x2, y2 = Intersection(dot.pos[0], dot.pos[1], width // 2, height // 2)
    if width // 2 - jiaoju - 0.1 < dot.pos[0] < width // 2 - jiaoju + 0.1:
        b = 'inf'
    else:
        p.draw.line(screen, (255, 0, TempBule), (width // 2 + fuhao(), height // 2), (x2, y2), 6)  # 像
        if fuhao() / delta >= 0:
            up = 1
        else:
            down = 1
        if up == 1:
            y2 = min(y2, height // 2)
        elif down == 1:
            y2 = max(y2, height // 2)
        arr(x2, y2, up=up, down=down, color=(255, 0, TempBule))
    x2, y2 = Intersection(dot.pos[0], dot.pos[1], width // 2, height // 2)
    if LinesLightStete == -1:
        FocalLengthList1 = [[Width // 2 - FocalLength, i] for i in range(Height // 2 - 200, Height // 2 + 201, 10)]
        FocalLengthList2 = [[Width // 2 + FocalLength, i] for i in range(Height // 2 - 200, Height // 2 + 201, 10)]
        for i in range(0, len(FocalLengthList1) - 1, 2):
            p.draw.line(Screen, (0, 0, 0), FocalLengthList1[i], FocalLengthList1[i + 1], 1)
            p.draw.line(Screen, (0, 0, 0), FocalLengthList2[i], FocalLengthList2[i + 1], 1)
        if width // 2 - jiaoju < dot.pos[0] < width // 2:
            line = GetLines(dot.pos[0], dot.pos[1], x2, y2)
            for i in range(0, len(line) - 1, 2):
                p.draw.line(screen, (0, 0, 0), (line[i][0], line[i][1]), (line[i + 1][0], line[i + 1][1]), 3)
            line = GetLines(width // 2, dot.pos[1], x2, y2)
            for i in range(0, len(line) - 1, 2):
                p.draw.line(screen, (0, 0, 0), (line[i][0], line[i][1]), (line[i + 1][0], line[i + 1][1]), 3)


def fuhao():  # 符号法则，计算出的是相对长度，相对于顶点的
    s = -(abs(width / 2 - dot.pos[0]))
    f1 = jiaoju
    if s != 0:
        s1 = 1 / (1 / s + 1 / f1) if (1 / s + 1 / f1) != 0 else 1000
    else:
        s1 = 1000
    return s1


def Text():
    global b
    Screen.blit(TextBgBg, (TextBgPos[0] - 10, TextBgPos[1] - 10))
    # screen.blit(TextBg, TextBgPos)
    screen.blit(font.render('O', True, (0, 0, 0)), (width // 2 - 20, height // 2 + 10))
    screen.blit(font.render('f', True, (0, 0, 0)), (width // 2 - jiaoju, height // 2 + 10))
    screen.blit(font.render('f\'', True, (0, 0, 0)), (width // 2 + jiaoju, height // 2 + 10))
    screen.blit(font.render('2f', True, (0, 0, 0)), (width // 2 - 2 * jiaoju, height // 2 + 10))
    screen.blit(font.render('2f\'', True, (0, 0, 0)), (width // 2 + 2 * jiaoju, height // 2 + 10))
    screen.blit(font2.render('S : {}'.format(-round(width // 2 - dot.pos[0], 3)), True, TextColor), TextSPos)
    screen.blit(font2.render('L :{}'.format(jiaoju), True, TextColor), TextLPos)
    x2, y2 = Intersection(dot.pos[0], dot.pos[1], width // 2, height // 2)
    S1 = round(-(Width // 2 - x2), 3) if round(-(Width // 2 - x2), 3) != 1000 else 'inf'
    Screen.blit(font2.render('S'' : {}'.format(S1), True, TextColor), TextS1Pos)
    Screen.blit(font2.render('Light:', True, (255, 0, 84)), TextLightPos)
    if LinesLightStete == -1:
        Screen.blit(LightOn, TextSwithPos)
    else:
        Screen.blit(LightOff, TextSwithPos)
    if fuhao() == 1000:
        b = 'inf'
    else:
        b = round((Width // 2 - x2) / round(width // 2 - dot.pos[0], 3), 3) if -round(width // 2 - dot.pos[0],
                                                                                      3) != 0 else 'Inf'
    wen = font2.render("B : {:}".format(b), True, TextColor)  # 横向放大率
    screen.blit(wen, TextBPos)
    if dot.pos[1] >= Height // 2:
        screen.blit(font.render('S', True, red), (dot.pos[0] - 5, Height // 2 - 20))
    else:
        screen.blit(font.render('S', True, red), (dot.pos[0] - 5, Height // 2 + 10))
    if y2 > Height // 2:
        screen.blit(font.render('S\'', True, purple), (x2 - 5, Height // 2 - 20))
    else:
        screen.blit(font.render('S\'', True, purple), (x2 - 5, Height // 2 + 10))


def Update():
    DrawLines()
    DrawDot()
    Text()
    LoadImage()
    UpdataPos()
    p.display.update()


while True:
    event()
    init_bg()
    if LinesLightStete == -1:
        AddLines()
    Update()
