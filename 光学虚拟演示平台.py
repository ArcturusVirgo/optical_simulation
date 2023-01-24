# -*- coding: utf-8 -*-
'''
 @Time : 2021/3/8 18:10
 @Author : Angus-拾壹
 @Institution: Northwest Normal University, China
 @E-mail: angusli736@163.com
 @File : 项目主页（新）.py
 @Software: PyCharm 
'''
import tkinter as tk
import sys
import os
import subprocess

window = tk.Tk()

def mainwindow():
    global myfont, zifont,window,logoimage
    window.geometry("1920x1080+0+0")
    window.attributes("-fullscreen", True)
    window.iconphoto(True, tk.PhotoImage(file='image/UI/光学图标.png'))  # 设置窗口图标,True表示子窗口也显示图标
    window.title('')

    # 设置标签是否被选中参数
    window_status = {"wave": 0, "geo": 0, "express": 0}

    # 设置宽度高度
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()

    # 主页介绍
    homepagelabeldemoimage = tk.PhotoImage(file='image/UI/主页改.png')
    homepagelabeldemo = tk.Label(window,
                                image=homepagelabeldemoimage)
    homepagelabeldemo.place(relx=255 / width, rely=28 / height,
                           relheight=(height - 28) / height,
                           relwidth=(width - 255) / width
                           )

    #总标题标签
    logoimage = tk.PhotoImage(file='image/UI/UI标题改.png')
    logolabel = tk.Label(window,
                         image=logoimage
                         )
    logolabel.place(relx=0, rely=0, relheight=180/ height, relwidth=247 / width) #宽高之比11：8  * 28

    # 波动光学标签
    wavelabelimage1 = tk.PhotoImage(file='image/UI/波动光学开始.png')
    wavelabel = tk.Label(window,
                         image=wavelabelimage1
                         )
    wavelabel.place(relx=0, rely=180/ height, relheight=68/ height, relwidth=247/ width)  # 宽高之比11：3

    # 波动光学鼠标指示变图片
    def wavelabel_enter(event):
        global wavelabelimage2
        if not window_status["wave"]:
            wavelabelimage2 = tk.PhotoImage(file='image/UI/波动光学enter.png')
            wavelabel.configure(image=wavelabelimage2)

    wavelabel.bind('<Enter>', wavelabel_enter)

    def wavelabel_leave(event):
        global wavelabelimage1
        if not window_status["wave"]:
            wavelabelimage1 = tk.PhotoImage(file='image/UI/波动光学开始.png')
            wavelabel.configure(image=wavelabelimage1)

    wavelabel.bind('<Leave>', wavelabel_leave)

    # 波动光学标签按下状态
    def wavelabel_sink(event):
        global wavelabelimage3, Younglabelimage, Newtonlabelimage, Equalinlabelimage, wavefigurelabelimage
        wavelabelimage3 = tk.PhotoImage(file='image/UI/波动光学最后.png')

        # 是否选中参数设置
        window_status["wave"] = 1
        window_status["geo"] = 0
        window_status["express"] = 0

        # 波动光学变化
        wavelabel.configure(image=wavelabelimage3)

        # 几何光学不变
        geolabel.configure(image = geolabelimage1)

        # 鸣谢不变
        expresslabel.configure(image=expresslabelimage1)

        # 杨氏双缝干涉部分（三等分）
        Younglabelimage = tk.PhotoImage(file='image/UI/杨氏双缝干涉开始.png')
        Younglabel = tk.Label(window,
                              image=Younglabelimage
                              )
        Younglabel.place(relx=255 / width, rely=28 / height,
                         relheight=180 / height - 28 / height,
                         relwidth=(width - 255) / width / 3)

        # 杨氏双缝鼠标指示变图片
        def Younglabel_enter(event):
            global Younglabelimage2
            Younglabelimage2 = tk.PhotoImage(file='image/UI/杨氏双缝干涉最后.png')
            Younglabel.configure(image=Younglabelimage2)

        Younglabel.bind('<Enter>',Younglabel_enter)

        def Younglabel_leave(event):
            global Younglabelimage1
            Younglabelimage1 = tk.PhotoImage(file='image/UI/杨氏双缝干涉开始.png')
            Younglabel.configure(image=Younglabelimage1)

        Younglabel.bind('<Leave>',Younglabel_leave)

        # 杨氏双缝标签按下状态
        def Younglabel_sink(event):
            # os.system("python Double_slit_interference.py")
            subprocess.Popen('.\\subprogram\\Double_slit_interference.exe')

        Younglabel.bind('<ButtonPress-1>', Younglabel_sink)

        # 牛顿环部分（三等分）
        Newtonlabelimage = tk.PhotoImage(file='image/UI/牛顿环开始.png')
        Newtonlabel = tk.Label(window,
                              image=Newtonlabelimage
                              )
        Newtonlabel.place(relx=682 / width , rely=28 / height,
                          relheight=180 / height - 28 / height,
                          relwidth=(width - 255) / width / 3)

        # 牛顿环鼠标指示变图片
        def Newtonlabel_enter(event):
            global Newtonlabelimage2
            Newtonlabelimage2 = tk.PhotoImage(file='image/UI/牛顿环最后.png')
            Newtonlabel.configure(image=Newtonlabelimage2)

        Newtonlabel.bind('<Enter>', Newtonlabel_enter)

        def Newtonlabel_leave(event):
            global Newtonlabelimage1
            Newtonlabelimage1 = tk.PhotoImage(file='image/UI/牛顿环开始.png')
            Newtonlabel.configure(image=Newtonlabelimage1)

        Newtonlabel.bind('<Leave>', Newtonlabel_leave)

        # 牛顿环标签按下状态
        def Newtonlabel_sink(event):
            # os.system("python Newton_Ring.py")
            subprocess.Popen('.\\subprogram\\Newton_Ring.exe')

        Newtonlabel.bind('<ButtonPress-1>', Newtonlabel_sink)

        # 等倾干涉部分（三等分）
        Equalinlabelimage = tk.PhotoImage(file='image/UI/等倾干涉开始.png')
        Equalinlabel = tk.Label(window,
                               image=Equalinlabelimage
                               )
        Equalinlabel.place(relx=1109 / width, rely=28 / height,
                          relheight=180 / height - 28 / height,
                          relwidth=(width - 255) / width / 3)

        # 等倾干涉鼠标指示变图片
        def Equalinlabel_enter(event):
            global Equalinlabelimage2
            Equalinlabelimage2 = tk.PhotoImage(file='image/UI/等倾干涉最后.png')
            Equalinlabel.configure(image=Equalinlabelimage2)

        Equalinlabel.bind('<Enter>', Equalinlabel_enter)

        def Equalinlabel_leave(event):
            global Equalinlabelimage1
            Equalinlabelimage1 = tk.PhotoImage(file='image/UI/等倾干涉开始.png')
            Equalinlabel.configure(image=Equalinlabelimage1)

        Equalinlabel.bind('<Leave>', Equalinlabel_leave)

        # 等倾干涉标签按下状态
        def Equalinlabel_sink(event):
            # os.system("python Equal_inclination_interference.py")
            subprocess.Popen(".\\subprogram\\Equal_inclination_interference.exe")

        Equalinlabel.bind('<ButtonPress-1>', Equalinlabel_sink)

        # 波动光学人物介绍卡
        wavefigurelabelimage = tk.PhotoImage(file='image/UI/波动光学.png')
        wavefigurelabel = tk.Label(window,
                                   image=wavefigurelabelimage
                                   )
        wavefigurelabel.place(relx=255 / width, rely=180 / height,
                          relheight= (height - 180) / height,
                          relwidth=(width - 255) / width)

    wavelabel.bind('<ButtonPress-1>', wavelabel_sink)

    # 几何光学标签
    geolabelimage1 = tk.PhotoImage(file='image/UI/几何光学开始.png')
    geolabel = tk.Label(window,
                        image =geolabelimage1
                    )
    geolabel.place(relx=0, rely=247 / height, relheight=68 / height,relwidth=247 / width)


    # 几何光学鼠标指示变图片
    def geolabel_enter(event):
        global geolabelimage2
        if not window_status["geo"]:
            geolabelimage2 = tk.PhotoImage(file='image/UI/几何光学enter.png')
            geolabel.configure(image = geolabelimage2)

    geolabel.bind('<Enter>', geolabel_enter)

    def geolabel_leave(event):
        global geolabelimage1
        if not window_status["geo"]:
            geolabelimage1 = tk.PhotoImage(file='image/UI/几何光学开始.png')
            geolabel.configure(image = geolabelimage1)

    geolabel.bind('<Leave>', geolabel_leave)

    # 几何光学标签按下状态
    def geolabel_sink(event):
        global geolabelimage3, convexlabelimage, concavelabelimage, geofigurelabelimage
        geolabelimage3 = tk.PhotoImage(file='image/UI/几何光学最后.png')
        geolabel.configure(image=geolabelimage3)

        # 是否选中参数设置
        window_status["wave"] = 0
        window_status["geo"] = 1
        window_status["express"] = 0

        # 波动光学不变
        wavelabel.configure(image=wavelabelimage1)

        # 鸣谢不变
        expresslabel.configure(image=expresslabelimage1)

        # 凸透镜部分（二等分）
        convexlabelimage = tk.PhotoImage(file='image/UI/凸透镜开始.png')
        convexlabel = tk.Label(window,
                              image=convexlabelimage
                              )
        convexlabel.place(relx=255 / width, rely=28 / height,
                         relheight=180 / height - 28 / height,
                         relwidth=(width - 257) / width / 2)

        # 凸透镜指示变图片
        def convexlabel_enter(event):
            global convexlabelimage2
            convexlabelimage2 = tk.PhotoImage(file='image/UI/凸透镜最后.png')
            convexlabel.configure(image=convexlabelimage2)

        convexlabel.bind('<Enter>', convexlabel_enter)

        def convexlabel_leave(event):
            global convexlabelimage1
            convexlabelimage1 = tk.PhotoImage(file='image/UI/凸透镜开始.png')
            convexlabel.configure(image=convexlabelimage1)

        convexlabel.bind('<Leave>', convexlabel_leave)

        # 凸透镜标签按下状态
        def convexlabel_sink(event):
            # os.system("python convex_lens.py")
            subprocess.Popen(".\\subprogram\\convex_lens.exe")

        convexlabel.bind('<ButtonPress-1>', convexlabel_sink)

        # 凹透镜部分（二等分）
        concavelabelimage = tk.PhotoImage(file='image/UI/凹透镜开始.png')
        concavelabel = tk.Label(window,
                               image=concavelabelimage
                               )
        concavelabel.place(relx=895 / width, rely=28 / height,
                          relheight=180 / height - 28 / height,
                          relwidth=(width - 257) / width / 2)

        # 凹透镜鼠标指示变图片
        def concavelabel_enter(event):
            global concavelabelimage2
            concavelabelimage2 = tk.PhotoImage(file='image/UI/凹透镜最后.png')
            concavelabel.configure(image=concavelabelimage2)

        concavelabel.bind('<Enter>', concavelabel_enter)

        def concavelabel_leave(event):
            global concavelabelimage1
            concavelabelimage1 = tk.PhotoImage(file='image/UI/凹透镜开始.png')
            concavelabel.configure(image=concavelabelimage1)

        concavelabel.bind('<Leave>', concavelabel_leave)

        # 凹透镜标签按下状态
        def concavelabel_sink(event):
            # os.system("python concave_lens.py")
            subprocess.Popen(".\\subprogram\\concave_lens.exe")

        concavelabel.bind('<ButtonPress-1>', concavelabel_sink)

        # 几何光学人物介绍卡
        geofigurelabelimage = tk.PhotoImage(file='image/UI/几何光学.png')
        geofigurelabel = tk.Label(window,
                                   image=geofigurelabelimage
                                   )
        geofigurelabel.place(relx=255 / width, rely=180 / height,
                              relheight=(height - 180) / height,
                              relwidth=(width - 255) / width)

    geolabel.bind('<ButtonPress-1>', geolabel_sink)

    # 分界线标签
    boundarylabelimage1 = tk.PhotoImage(file='image/UI/分割线最终2.png')
    boundarylabel = tk.Label(window,
                            image=boundarylabelimage1
                            )
    boundarylabel.place(relx=0, rely=314 / height, relheight=68/ height, relwidth=247/ width)  # 宽高之比11：3

    # 鸣谢标签
    expresslabelimage1 = tk.PhotoImage(file='image/UI/鸣谢开始.png')
    expresslabel = tk.Label(window,
                         image=expresslabelimage1
                         )
    expresslabel.place(relx=0, rely=(381)/ height, relheight=68/ height, relwidth=247/ width)  # 宽高之比11：3

    # 鸣谢鼠标指示变图片
    def expresslabel_enter(event):
        global expresslabelimage2
        if not window_status["express"]:
            expresslabelimage2 = tk.PhotoImage(file='image/UI/鸣谢enter.png')
            expresslabel.configure(image=expresslabelimage2)

    expresslabel.bind('<Enter>', expresslabel_enter)

    def expresslabel_leave(event):
        global expresslabelimage1
        if not window_status["express"]:
            expresslabelimage1 = tk.PhotoImage(file='image/UI/鸣谢开始.png')
            expresslabel.configure(image=expresslabelimage1)

    expresslabel.bind('<Leave>', expresslabel_leave)

    # 鸣谢标签按下状态
    def expresslabel_sink(event):
        global expresslabelimage3, expresslabeldemoimage
        expresslabelimage3 = tk.PhotoImage(file='image/UI/鸣谢最后.png')
        expresslabel.configure(image=expresslabelimage3)


        # 是否选中参数设置
        window_status["wave"] = 0
        window_status["geo"] = 0
        window_status["express"] = 1

        # 几何光学不变
        geolabel.configure(image=geolabelimage1)

        # 波动光学不变
        wavelabel.configure(image=wavelabelimage1)

        # 鸣谢页面介绍
        expresslabeldemoimage = tk.PhotoImage(file='image/UI/鸣谢改.png')
        expresslabeldemo = tk.Label(window,
                                    image=expresslabeldemoimage)
        expresslabeldemo.place(relx=255 / width, rely=28 / height,
                                    relheight=(height - 28) / height,
                                    relwidth=(width - 255) / width
                                    )

    expresslabel.bind('<ButtonPress-1>', expresslabel_sink)



    # 关闭标签
    closelabelimage1 = tk.PhotoImage(file='image/UI/关闭成品.png')
    closelabel = tk.Label(window,
                          image=closelabelimage1
                            )
    closelabel.place(relx=1489 / width, rely=0, relheight=28/ height, relwidth=48 / width)

    # 关闭鼠标指示变图片
    def closelabel_enter(event):
        global closelabelimage2
        closelabelimage2 = tk.PhotoImage(file='image/UI/关闭成品enter.png')
        closelabel.configure(image=closelabelimage2)

    closelabel.bind('<Enter>', closelabel_enter)

    def closelabel_leave(event):
        global closelabelimage1
        closelabelimage1 = tk.PhotoImage(file='image/UI/关闭成品.png')
        closelabel.configure(image=closelabelimage1)

    closelabel.bind('<Leave>', closelabel_leave)

    # 按下关闭
    def closelabel_sink(event):
        global closelabelimage1
        sys.exit()

    closelabel.bind('<ButtonPress-1>', closelabel_sink)

    # 最小化标签
    minlabelimage1 = tk.PhotoImage(file='image/UI/最小化成品.png')
    minlabel = tk.Label(window,
                          image=minlabelimage1
                          )
    minlabel.place(relx=1442 / width, rely=0, relheight=28 / height, relwidth=48 / width)

    # 最小化鼠标指示变图片
    def minlabel_enter(event):
        global minlabelimage2
        minlabelimage2 = tk.PhotoImage(file='image/UI/最小化成品enter.png')
        minlabel.configure(image=minlabelimage2)

    minlabel.bind('<Enter>', minlabel_enter)

    def minlabel_leave(event):
        global minlabelimage1
        minlabelimage1 = tk.PhotoImage(file='image/UI/最小化成品.png')
        minlabel.configure(image=minlabelimage1)

    minlabel.bind('<Leave>', minlabel_leave)

    # 按下最小化
    def minlabel_sink(event):
        global minlabelimage1
        window.iconify() #窗口图标化

    minlabel.bind('<ButtonPress-1>', minlabel_sink)

    # 竖直分割线
    linelabelimage1 = tk.PhotoImage(file='image/UI/竖直分割线.png')
    linelabel = tk.Label(window,
                         image=linelabelimage1
                         )
    linelabel.place(relx=247 / width, rely=0, relheight=864 / height,
                    relwidth=8 / width)

    # 关闭左边旁白
    whitelabelimage1 = tk.PhotoImage(file='image/UI/关闭左边.png')
    whitelabel = tk.Label(window,
                          image=whitelabelimage1


                          )
    whitelabel.place(relx=255 / width, rely=0, relheight=28 / height,
                     relwidth=1188 / width)

    # 剩余部分
    spacelabelimage1 = tk.PhotoImage(file='image/UI/剩余部分.png')
    spacelabel = tk.Label(window,
                          image=spacelabelimage1
                          )
    spacelabel.place(relx=0, rely=448 / height, relheight=416 / height,
                     relwidth=247 / width)

    window.mainloop()

mainwindow()