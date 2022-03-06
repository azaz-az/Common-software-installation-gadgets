import tkinter as tk
import os

window = tk.Tk()
window.title('运行库')
window.geometry("800x480")

def fast():		
    os.system('start .\software\\runtime\\runtime.exe')
def link():		
    os.system('start https://docs.microsoft.com/zh-cn/cpp/windows/latest-supported-vc-redist?view=msvc-170')

tk.Button(window,width=30,height=2,text='快速安装(推荐)',command=fast).pack()

tk.Button(window,width=30,height=2,text='官网下载',command=link).pack()

window.mainloop()