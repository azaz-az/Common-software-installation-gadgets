import tkinter as tk
import os

window = tk.Tk()
window.title('VS Code')
window.geometry("800x480")

def fast():		
    os.system('start .\software\\vscode\\vscode.exe')
def link():		
    os.system('start https://code.visualstudio.com/')

tk.Button(window,width=30,height=2,text='快速安装(推荐)',command=fast).pack()

tk.Button(window,width=30,height=2,text='官网下载',command=link).pack()

window.mainloop()