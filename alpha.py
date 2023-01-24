import sys
import pygame as p
import numpy as np

p.init()
Width, Height = 1500, 800
Screen = p.display.set_mode((Width, Height), p.RESIZABLE)
ProtonList = []
PtontonTra = []
time = 0

# 常量
MouseState = -1
black = (0, 0, 0)


class Gold:
    def __init__(self):
        self.pos = [int(8 / 9 * Width), Height // 2]
        self.color = 'red'


gold = Gold()


class Proton:
    def __init__(self, x, y):
        self.pos = [x, y]
        self.color = (0, 222, 255)
        self.speed = [1.8, 0]
        self.Tra = []

    def move(self):
        self.pos = [self.pos[0] + self.speed[0], self.pos[1] + self.speed[1]]

    def report(self):
        self.Tra.append(self.pos)


def FirePronton():
    global ProtonList
    new = Proton(p.mouse.get_pos()[0], p.mouse.get_pos()[1])
    ProtonList.append(new)


def ProtonDie():
    global ProtonList
    for i in ProtonList:
        if 2000 <= i.pos[0] or i.pos[0] <= 10:
            ProtonList.remove(i)
        elif i.pos[1] >= 2000 or i.pos[1] <= -1000:
            ProtonList.remove(i)


def DisplayPronton():
    global ProtonList,time
    time+=1
    for i in ProtonList:
        p.draw.circle(Screen, i.color, i.pos, 10)
        axis = np.linspace(i.pos[1], Height // 2, 20)
        for x in range(0, len(axis) - 1, 2):
            p.draw.line(Screen, black, [i.pos[0], axis[x]], [i.pos[0], axis[x + 1]], 1)
        i.move()
        i.report()
        # if time%10==0:
        #     for y in range(0, len(i.Tra) - 1):
        #         p.draw.line(Screen, (0, 222, 255), i.Tra[y], i.Tra[y + 1], 1)


def Force():
    for i in ProtonList:
        r = np.sqrt((gold.pos[1] - i.pos[1]) ** 2 + (gold.pos[0] - i.pos[0]) ** 2)
        deltay = (gold.pos[1] - i.pos[1])
        deltax = (gold.pos[0] - i.pos[0])
        CosSeta = deltax / r * 0.001
        SinSeta = deltay / r * 0.001
        i.speed = [i.speed[0] - CosSeta, i.speed[1] - SinSeta]


def Event():
    global MouseState, Width, Height
    Width, Height = p.display.get_window_size()
    for i in p.event.get():
        if i.type == p.QUIT:
            sys.exit()
        elif i.type == p.MOUSEBUTTONDOWN:
            MouseState = 1
        elif i.type == p.MOUSEBUTTONUP:
            MouseState = -1


def ActiveProton():
    global MouseState
    if MouseState == 1:
        FirePronton()
        MouseState = -1
    DisplayPronton()
    ProtonDie()


def Init():
    global gold
    gold = Gold()
    p.draw.circle(Screen, gold.color, gold.pos, 10)
    axis = np.linspace(0, Width, Width // 20)
    for i in range(0, len(axis) - 1, 2):
        p.draw.line(Screen, black, [axis[i], Height // 2], [axis[i + 1], Height // 2], 1)
    Force()


def Update():
    p.display.update()
    Screen.fill((255, 255, 255))


while True:
    Init()
    Event()
    ActiveProton()
    Update()
