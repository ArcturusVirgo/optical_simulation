import pygame as p
import sys
import numpy as np

Width, Height = 1500, 800
LineRate = 0.1
FocalLength = 120
LeftFocal = [Width // 2 - FocalLength, Height // 2]
RightFocal = [Width // 2 + FocalLength, Height // 2]
LineLegth = 4 // 5 * Width
black = (0, 0, 0)
red = (255, 0, 0)
purple = (255, 0, 255)
GuideLine = 1  # 'show'
Beita = 0

# event
MouseState = 'up'
MouseStateList = ['up', 'up']



p.init()
Screen = p.display.set_mode((Width, Height),p.RESIZABLE)
p.display.set_caption("凹透镜")
Screen.fill((236, 163, 239))
# font = p.font.SysFont('华文楷体', 20)
# font2 = p.font.SysFont('华文楷体', 30)
font = p.font.Font('font/华文楷体.TTF', 30)
font2 = p.font.Font('font/华文楷体.TTF', 30)
# TextBg = p.image.load('参数2.png')
TextBgBg = p.image.load('image/lens/参数gb.png')
# bg = p.image.load('bg.png')
LPos = [Height//2-300, Height//2+300]
TextBgPos = (1220, 20)
TextBPos = (1230, 40)
TextSPos = (1230, 90)
TextS1Pos = (1230, 140)
TextLPos = (1230, 190)
TextColor = (156, 0, 255)
AddPos = (TextSPos[0] + 130, TextSPos[1])
SubPos = (TextSPos[0] + 130 + 60, TextSPos[1])
TextLightPos = (1230, 240)
TextSwithPos = (TextLightPos[0] + 120, TextLightPos[1])
AddImage = p.image.load('image/lens/add.png')
SubImage = p.image.load('image/lens/subtract.png')
LightOn = p.image.load('image/lens/LightOn.png')
LightOff = p.image.load('image/lens/LightOff.png')

def UpdataPos():
    global Width,Height,LPos,TextBgPos,TextBPos,TextS1Pos,TextLPos,AddPos,SubPos,TextSwithPos,TextLightPos,TextSPos
    Width, Height = p.display.get_window_size()
    LPos = [Height // 2 - 300, Height // 2 + 300]
    TextBgPos = (Width-280, 20)
    TextBPos = (Width-270, 40)
    TextSPos = (Width-270, 90)
    TextS1Pos = (Width-270, 140)
    TextLPos = (Width-270, 190)
    AddPos = (TextSPos[0] + 130, TextSPos[1])
    SubPos = (TextSPos[0] + 130 + 60, TextSPos[1])
    TextLightPos = (Width-270, 240)
    TextSwithPos = (TextLightPos[0] + 120, TextLightPos[1])

def LoadImage():
    global MouseState
    Screen.blit(AddImage, (AddPos))
    Screen.blit(SubImage, (SubPos))
    if MouseState == 'down' and 0 <= light.pos[0] <= Width // 2 - 1:
        if AddPos[0] <= p.mouse.get_pos()[0] <= AddPos[0] + 32 and AddPos[1] <= p.mouse.get_pos()[1] <= AddPos[1] + 32:
            light.pos[0] -= 1
            MouseState = 'up'
        elif SubPos[0] <= p.mouse.get_pos()[0] <= SubPos[0] + 32 and SubPos[1] <= p.mouse.get_pos()[1] <= SubPos[
            1] + 32:
            light.pos[0] += 1
            MouseState = 'up'


class Light:
    def __init__(self):
        self.pos = [Width // 4, Height // 3]
        self.color = (255, 10, 0)
        self.radius = 10


light = Light()


def DrawInit():
    p.draw.line(Screen, (0, 0, 0), (int(LineRate * Width), Height // 2), (int((1 - LineRate) * Width), Height // 2), 3)
    p.draw.line(Screen, (0, 0, 0), (Width // 2, Height//2 - 300), (Width // 2, Height//2 + 300), 3)
    DrawArrow(Width // 2, Height//2 - 300, black, 'down')
    DrawArrow(Width // 2, Height//2 + 300, black, 'up')


def DrawLight():
    p.draw.line(Screen, light.color, light.pos, (light.pos[0], Height // 2), 10)
    if light.pos[1] <= Height // 2:
        DrawArrow(light.pos[0], light.pos[1], light.color, 'up')
    else:
        DrawArrow(light.pos[0], Height // 2, light.color, 'up')
    DrawLine()


def DrawArrow(x, y, color, dir):
    if dir == 'up':
        p.draw.line(Screen, color, (x - 10, y + 10), (x, y - 2), 10)
        p.draw.line(Screen, color, (x + 10, y + 10), (x, y - 2), 10)
    elif dir == 'down':
        p.draw.line(Screen, color, (x - 10, y - 10), (x, y + 2), 10)
        p.draw.line(Screen, color, (x + 10, y - 10), (x, y + 2), 10)


def OutputLine():
    k = (light.pos[1] - Height // 2) / (FocalLength)
    b = light.pos[1] - k * (Width // 2)
    x = LineRate * Width + Width // 2
    y = k * x + b
    return x, y


def DrawLine():
    if GuideLine == 1:
        FocalLengthList1 = [[Width // 2 - FocalLength, i] for i in range(Height // 2 - 200, Height // 2 + 201, 10)]
        FocalLengthList2 = [[Width // 2 + FocalLength, i] for i in range(Height // 2 - 200, Height // 2 + 201, 10)]
        for i in range(0, len(FocalLengthList1) - 1, 2):
            p.draw.line(Screen, (0, 0, 0), FocalLengthList1[i], FocalLengthList1[i + 1], 1)
            p.draw.line(Screen, (0, 0, 0), FocalLengthList2[i], FocalLengthList2[i + 1], 1)
        p.draw.line(Screen, red, light.pos,
                    (Width // 2 + (Width // 2 - light.pos[0]), Height // 2 + (Height // 2 - light.pos[1])), 3)
        p.draw.line(Screen, red, light.pos, (Width // 2, light.pos[1]), 3)
        p.draw.line(Screen, red, (Width // 2, light.pos[1]), OutputLine(), 3)
        line1 = np.linspace(150, Width // 2, 30)
        line2 = np.linspace(LPos[0], LPos[1], 20)
        for i in range(0, len(line1) - 1, 2):
            p.draw.line(Screen, (0, 255, 48), (line1[i], LPos[0]), (line1[i + 1], LPos[0]), 2)
            p.draw.line(Screen, (0, 255, 48), (line1[i], LPos[1]), (line1[i + 1], LPos[1]), 2)
        for i in range(0, len(line2) - 1, 2):
            p.draw.line(Screen, (0, 255, 48), (150, line2[i]), (150, line2[i + 1]), 2)


def DrawText():
    Screen.blit(TextBgBg, (TextBgPos[0] - 10, TextBgPos[1] - 10))
    # Screen.blit(TextBg, TextBgPos)
    p.draw.circle(Screen, (0, 0, 0), (Width // 2, Height // 2), 5)
    Screen.blit(font.render('O', True, (0, 0, 0)), (Width // 2 - 10 - 5, Height // 2 + 10))
    p.draw.circle(Screen, (0, 0, 0), (Width // 2 - FocalLength, Height // 2), 8)
    Screen.blit(font.render('f\'', True, (0, 0, 0)), (Width // 2 - FocalLength, Height // 2 + 10))
    p.draw.circle(Screen, (0, 0, 0), (Width // 2 + FocalLength, Height // 2), 8)
    Screen.blit(font.render('f', True, (0, 0, 0)), (Width // 2 + FocalLength - 5, Height // 2 + 10))
    p.draw.circle(Screen, (0, 0, 0), (Width // 2 - 2 * FocalLength, Height // 2), 8)
    Screen.blit(font.render('2f\'', True, (0, 0, 0)), (Width // 2 - 2 * FocalLength - 5, Height // 2 + 10))
    p.draw.circle(Screen, (0, 0, 0), (Width // 2 + 2 * FocalLength, Height // 2), 8)
    Screen.blit(font.render('2f', True, (0, 0, 0)), (Width // 2 + 2 * FocalLength - 5, Height // 2 + 10))
    Screen.blit(font2.render('S : {}'.format(-round(Width // 2 - light.pos[0], 3)), True, TextColor),
                (TextSPos))
    Screen.blit(font2.render('L:{}'.format(FocalLength), True, TextColor), TextLPos)
    if light.pos[1] <= Height // 2:
        Screen.blit(font.render('S', True, red), (light.pos[0] - 5, Height // 2 + 15))
    else:
        Screen.blit(font.render('S', True, red), (light.pos[0] - 5, Height // 2 - 25))
    B = -round((Width // 2 - Image()[0]), 3) / -round(Width // 2 - light.pos[0], 3) if -round(Width // 2 - light.pos[0],
                                                                                              3) != 0 else 1
    Screen.blit(font2.render('B : {}'.format(round(B, 3)), True, TextColor), TextBPos)
    Screen.blit(font2.render('S\' : {}'.format(round(-(Width // 2 - Image()[0]), 3)), True, TextColor), TextS1Pos)
    Screen.blit(font2.render('Light:', True, (255, 0, 84)), TextLightPos)
    if GuideLine == 1:
        Screen.blit(LightOn, TextSwithPos)
    else:
        Screen.blit(LightOff, TextSwithPos)


def GetLines(x1, y1, x2, y2):
    k = (y2 - y1) / (x2 - x1)
    b = y1 - k * x1
    return [[i, i * k + b] for i in np.arange(min(x1, x2), max(x1, x2), 5)]


def Image():
    k1 = (light.pos[1] - Height // 2) / (FocalLength)
    k2 = -(Height // 2 - light.pos[1]) / (Width // 2 - light.pos[0]) if Width // 2 - light.pos[0] != 0 else 1000
    DeltaX = (light.pos[1] - Height // 2) / (k1 + k2) if k1 + k2 != 0 else 1000
    b = light.pos[1] - k1 * (Width // 2)
    x = Width // 2 - DeltaX
    y = k1 * x + b
    return x, y


def DrawImage():
    x, y = Image()
    p.draw.line(Screen, (255, 0, 255), (x, y), (x, Height // 2), 10)  # 像
    if light.pos[1] <= Height // 2:
        Screen.blit(font.render('S‘', True, (255, 0, 255)), (x - 5, Height // 2 + 15))
    else:
        Screen.blit(font.render('S\'', True, (255, 0, 255)), (x - 5, Height // 2 - 25))
    if light.pos[1] <= Height // 2:
        DrawArrow(x, y, (255, 0, 255), 'up')
    else:
        DrawArrow(x, Height // 2, (255, 0, 255), 'up')
    if GuideLine == 1:
        line = GetLines(x, y, Width // 2, light.pos[1])
        for i in range(0, len(line) - 1, 2):
            p.draw.line(Screen, (0, 0, 0), (line[i][0], line[i][1]), (line[i + 1][0], line[i + 1][1]), 3)


def Draw():
    DrawLight()
    DrawImage()
    DrawInit()
    DrawText()
    LoadImage()


def Event():
    global MouseState, MouseStateList
    for i in p.event.get():
        if i.type == p.QUIT:
            sys.exit()
        elif i.type == p.MOUSEBUTTONDOWN:
            MouseState = 'down'
            MouseStateList.append('down')
        elif i.type == p.MOUSEBUTTONUP:
            MouseState = 'up'
            MouseStateList.append('up')


def Update():
    global GuideLine, MouseStateList
    if MouseState == 'down':
        if 150 <= p.mouse.get_pos()[0] <= Width // 2 and LPos[0] <= p.mouse.get_pos()[1] <= LPos[1]:
            light.pos = [p.mouse.get_pos()[0], p.mouse.get_pos()[1]]
    elif MouseState == 'up':
        pass
    if MouseStateList[-1] == 'up' and MouseStateList[-2] == 'down':
        MouseStateList = ['up', 'up']
        if TextSwithPos[0] <= p.mouse.get_pos()[0] <= TextSwithPos[0] + 82 and TextSwithPos[1] <= p.mouse.get_pos()[
            1] <= TextSwithPos[1] + 35:
            GuideLine = -GuideLine
    p.display.update()
    UpdataPos()
    Screen.fill((255,255,255))
    # Screen.blit(bg,(0,0))


while True:
    Event()
    Draw()
    Update()
