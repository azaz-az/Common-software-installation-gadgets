import tkinter as tk
import os
import tkinter.messagebox

window = tk.Tk()
window.title('Java')
window.geometry("800x480")

def fast():		
    tkinter.messagebox.showinfo('提示','该软件安装包体积过大,超过了GitHub的最大限制(100MB).\n\n故本软件不提供快速安装功能,敬请谅解.')
def link():		
    os.system('start https://www.oracle.com/java/technologies/downloads/#jdk17-windows')

tk.Button(window,width=30,height=2,text='快速安装(推荐)',command=fast).pack()

tk.Button(window,width=30,height=2,text='官网下载',command=link).pack()

window.mainloop()