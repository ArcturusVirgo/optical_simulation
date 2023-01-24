import pygame as p
import sys
import matplotlib.pyplot as plt
import math as m
import numpy as np
from PIL import Image
import pandas as pd
#设置双缝位置
#参数设置
p.init()
InitSlitDentence = 20  #初始光标停在离中心20mm处
Mouse_down = False
TipHandMove = -1
TipHandMove2 = -1
TipHandMoveUp = -1
sleeptime = 5
sleeptimeInit = 5
ClearanceTime = 0.2
Width, Height = 700, 700
HandImg = p.image.load("image/Double_slit_interference/hand.png")
UpHandImg = p.image.load("image/Double_slit_interference/uphand.png")
NullImage = p.image.load("image/Double_slit_interference/nullimage.png")
screen = p.display.set_mode((Width + 480, Height)) #窗口
p.display.set_caption('双缝干涉')
# font = p.font.SysFont('华文楷体', 15)
font = p.font.Font('font/华文楷体.TTF', 15)
color = (255,255,255)
r = 1
DistanceR = '1'
LastImage = NullImage
PrintData = False
ListKey = [p.K_1,p.K_2,p.K_3,p.K_4,p.K_5,p.K_6,p.K_7,p.K_8,p.K_9,p.K_0]
ListKey2 = [p.K_KP0,p.K_KP1,p.K_KP2,p.K_KP3,p.K_KP4,p.K_KP5,p.K_KP6,p.K_KP7,p.K_KP8,p.K_KP9]

def OutputData(data):
    df = pd.DataFrame(data=data)
    df.to_excel("output/interfrence.xlsx")

def image():
    global InitSlitDentence,r,PrintData
    d = InitSlitDentence * 1e-3
    S1 = (0,+d)
    S2 = (0,-d)
    A0 = A1 = 1 #振幅
    lambdas = 500e-9 #500nm的绿光
    k1 = k2 = 2*m.pi/lambdas
    #计算两点之间的距离
    def dentist(a,b):
        dx = r*(a[0]-b[0])
        dy = r*(a[1]-b[1])
        return dx**2 + dy**2  #返回两点直接按的距离

    def I(a,b):
        i = 4*A0**2*(m.cos((a-b)/2))**2  #光强计算公式
        return i

    def covert(a):
        return a/4*255  #将值转化为255的标准值
    data = [[r,i] for i in np.linspace(-0.5,0.5,100)]
    x_y_i = [[i[0],i[1],covert(I(k1*dentist(i,S1),k2*dentist(i,S2)))] for i in data] #x=1，y的位置，光强
    temp = [x_y_i[i][2] for i in range(len(x_y_i))] #光强
    if PrintData:
        OutputData(temp)
        PrintData = False
    temp = [255-i for i in temp]     #将灰度值与光强匹配
    plt.figure()
    plt.subplot(211)
    plt.plot(temp)
    plt.ylabel('$light intensity$')
    plt.subplot(212)
    temp=(temp,temp)*15
    plt.imshow(temp,cmap=plt.cm.gray,interpolation='bilinear')
    plt.savefig('image/Double_slit_interference/temp.png')
    plt.close()
    img = Image.open('image/Double_slit_interference/temp.png')
    img = img.rotate(90)
    img = img.resize((640,480))
    img.save('image/Double_slit_interference/temp.png')

def HelpTip():
    global TipHandMove,TipHandMove2,TipHandMoveUp
    x = 703 // 3 + 20
    if sleeptime<=0 and ClearanceTime==0.2:
        y = [i for i in range(60,271,10)]
        if TipHandMove>-21:
            screen.blit(HandImg, (x, y[TipHandMove]))
            TipHandMove -=1
        else:
            TipHandMove=-1
    elif sleeptime <=0 and ClearanceTime !=0.2:
        y = [i for i in range(60,271)]
        if TipHandMove2>-210:
            screen.blit(HandImg,(x,y[TipHandMove2]))
            TipHandMove2 -= 1
        else:
            TipHandMove2 = -1
    if sleeptime<=0:
        x1 = 555
        y = [i for i in range(360,401,5)]
        if TipHandMoveUp >-8:
            screen.blit(UpHandImg,(x1,y[TipHandMoveUp]))
            TipHandMoveUp -=1
        else:
            TipHandMoveUp = -1


def TextLoad():
    screen.blit(font.render("狭缝到光屏的距离为：R = {}m".format(r),True,(0,0,0)),(400,320))
    screen.blit(font.render("导出光强数据",True,(0,0,0),(0,255,255)),(10,0))

def GetInputNum():
    pass
def TransfNum(strnum):
    global r,DistanceR
    if strnum == '':
        r = 0
    elif strnum != '':
        r = float(strnum)
        image()
    if len(DistanceR)>=2 and DistanceR[0] == 0:
        DistanceR = DistanceR[1:]

def basic(): #绘制基本框架
    d_y1 = Height // 2 - InitSlitDentence
    d_y2 = Height // 2 + InitSlitDentence - 10
    screen.fill(color)
    p.draw.rect(screen, (252, 131, 12), (702 // 3, 50, 10, Height - 2 * 50))  # 绘制光屏1
    p.draw.rect(screen,(255,255,255),(702//3,d_y1,10,10))    #屏1
    p.draw.rect(screen, (255,255,255), (702//3,d_y2,10,10))  #屏2
    p.draw.line(screen, (0, 0, 0,), (20, Height // 2), (700, Height // 2))  # 中心线
    p.draw.circle(screen, (255, 0, 0), (20, Height // 2), 10)  # 点光源
    thing = font.render('d = {}mm'.format(InitSlitDentence), True, (0, 0, 0)) #加载文字
    screen.blit(thing,(702//3+15,d_y1))

def up_kong():
    global InitSlitDentence,PrintData
    if Mouse_down and 702//3-20<=p.mouse.get_pos()[0]<=702//3+20:
        InitSlitDentence = Height // 2 - p.mouse.get_pos()[1]
    elif Mouse_down:
        if 10<=p.mouse.get_pos()[0]<=100 and 0<=p.mouse.get_pos()[1]<=20:
            PrintData = True

def Event():
    global  Mouse_down,sleeptime,DistanceR,r
    for i in p.event.get():
        if i.type==p.QUIT:
            p.quit()
            sys.exit()
        elif i.type == p.MOUSEBUTTONDOWN:
            Mouse_down = True
            sleeptime = sleeptimeInit
        elif i.type == p.MOUSEBUTTONUP:
            Mouse_down = False
            sleeptime = sleeptimeInit
        elif i.type == p.KEYDOWN:
            sleeptime = sleeptimeInit
            if i.key in ListKey:
                DistanceR += str(i.key-48)
            elif i.key in ListKey2:
                DistanceR += str(i.key-208-48)
            elif i.key == 46:
                DistanceR +='.'
            elif i.key == p.K_BACKSPACE and DistanceR !='':
                DistanceR = DistanceR[:-1]
    TransfNum(DistanceR)
    sleeptime -= ClearanceTime


def PrintImg():
    global LastImage,ClearanceTime
    InterImage = p.image.load('image/Double_slit_interference/temp.png')
    if r != 0:
        LastImage =InterImage
        ClearanceTime = 0.2
    else:
        LastImage = NullImage
        ClearanceTime = 0.01
    screen.blit(LastImage,(600, 110))
    HelpTip()

while True:
    Event()
    up_kong()
    basic()
    TextLoad()
    PrintImg()
    p.display.update()