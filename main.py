from cProfile import label
from cgitb import text
from importlib.metadata import PathDistribution
from json import detect_encoding
import tkinter as tk
from tkinter import *
from turtle import title, width
from tkinter import messagebox
from tkinter import ttk


class Application(tk.Frame):
    def __init__(self, window):
        super().__init__(window)
        self.master = window
        self.pack()
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        self.schoolName = tk.StringVar()
        self.intWind()
        window.geometry("255x195")
        window.iconbitmap()
        window.title('程序')
        window.resizable(0,0)

    def buttonActive(self):
        u = self.username.get()
        p = self.password.get()

        if len(u) == 0 or len(p) == 0:
            messagebox.showinfo('提示','输入不能为空')
            return


        #messagebox.showinfo('提示:','输入的账号:%s\n密码:%s' % (u, p))    


    def selectorLinstener(self,*args):
        print(self.selector.get())

    def intWind(self):

        frame4 = Frame(self)
        Label(frame4,text='登入方式:').grid(row=0, column=0)
        self.selector = ttk.Combobox(frame4,values=('手机号登入','学号登入'),width=14)
        self.selector.grid(row=0,column=1)
        self.selector.current(0)
        self.selector.bind('<<ComboboxSelected>>',self.selectorLinstener) #监听选择

        frame5 = Frame(self)
        Label(frame5,text="学校:").grid(row=0, column=0)
        Entry(frame5,textvariable = self.schoolName).grid(row=0, column=1)
        
        frame1 = Frame(self)
        Label(frame1,text="账号:").grid(row=0, column=0)
        Entry(frame1,textvariable = self.username).grid(row=0, column=1)

        frame2 = Frame(self)
        Label(frame2,text="密码:").grid(row=0, column=0)
        Entry(frame2,show='*',textvariable = self.password).grid(row=0, column=1)

        frame3 = Frame(self)
        Button(frame3,text="登入",width=10,command=self.buttonActive).grid(row=0,column=0)


        frame4.grid(pady=5)
        frame5.grid(pady=5)
        frame1.grid(pady=5)
        frame2.grid(pady=5)
        frame3.grid(pady=5)


if __name__ == '__main__':
    window = tk.Tk()
application = Application(window=window)
application.mainloop()
