import tkinter as tk
import tkinter
import tkinter.messagebox
import os

os.system('title 恭喜你发现了彩蛋!')
window = tk.Tk()
window.title('常用软件安装小工具')
window.geometry("800x480")

def faq():		
    tkinter.messagebox.showinfo('提示','快速安装指使用本地的安装包安装,速度快,但版本可能不是最新的\n\n官网下载指下载软件官网的安装包安装,速度慢,但版本是最新的')
def runtime():		
    os.system('.\software\\runtime\\runtime.py')
def vscode():		
    os.system('.\software\\vscode\\vscode.py')
def vs():		
    os.system('.\software\\vs\\vs.py')
def python():		
    os.system('.\software\python\python.py')
def java():		
    os.system('.\software\java\java.py')
def powertoys():		
    os.system('.\software\powertoys\powertoys.py')
def tim():		
    os.system('.\software\\tim\\tim.py')
def wechat():		
    os.system('.\software\wechat\wechat.py')
def qq():		
    os.system('.\software\qq\qq.py')

line = tk.Label(window, text=' ')
line.pack()

tk.Button(window,width=30,height=2,text='点击查看快速安装和官网下载的区别',command=faq).pack()

line = tk.Label(window, text='---------------------------------------------------------必装软件---------------------------------------------------------')
line.pack()

tk.Button(window,width=30,height=2,text='运行库(必装)',command=runtime).pack()

line = tk.Label(window, text='---------------------------------------------------------代码编辑---------------------------------------------------------')
line.pack()

tk.Button(window,width=30,height=2,text='VS Code',command=vscode).pack()

tk.Button(window,width=30,height=2,text='VS(Visaul Studio)',command=vs).pack()

tk.Button(window,width=30,height=2,text='Python',command=python).pack()

tk.Button(window,width=30,height=2,text='Java',command=java).pack()

line = tk.Label(window, text='---------------------------------------------------------实用工具---------------------------------------------------------')
line.pack()

tk.Button(window,width=30,height=2,text='PowerToys',command=powertoys).pack()

line = tk.Label(window, text='---------------------------------------------------------即时通讯---------------------------------------------------------')
line.pack()

tk.Button(window,width=30,height=2,text='TIM',command=tim).pack()

tk.Button(window,width=30,height=2,text='微信',command=wechat).pack()

tk.Button(window,width=30,height=2,text='QQ',command=qq).pack()

tkinter.messagebox.showinfo('版权声明','本程序由该昵称已被占用____(Bilibili UID:1760935433)制作.\n\n本软件在GitHub上开源.\n\n另外,本软件完全免费,如果你通过付费获得,那么你肯定被骗了!')

window.mainloop()