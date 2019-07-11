# coding:UTF-8

from tkinter import *
from tkinter import messagebox
import random

def no_close():
    return

#关闭所有窗口
def close_all_window():
    window.destroy()

#关闭窗口提示
def close_window():
    messagebox.showinfo(title="不要嘛~", message="不选对不让走！")

#“好的”窗口
def Love():
    love = Toplevel(window)
    love.geometry("300x100+580+250")
    love.title("爱你么么哒~")
    btn = Button(love, text="我爱你哟！", width=10, height=2, command=close_all_window)
    btn.place(x=100, y=30)
    love.protocol("WM_DELETE_WINDOW", no_close)

window = Tk()
window.title("亲爱的小宝宝") #窗口标题
window.geometry("360x640+550+50") #窗口大小
window.protocol("WM_DELETE_WINDOW", close_window) #窗口关闭
label = Label(window, text="我们在一起两周年啦", font=("微软雅黑", 18))
label.place(x=90, y=50)
label = Label(window, text="期待下一个两周年吗？", font=("微软雅黑", 24))
label.place(x=40, y=100)
btn1 = Button(window, text="非常期待", width=15, height=2, command=Love)
btn1.place(x=110, y=200)
# “不期待”按钮
pos = [110, 300]
btn2 = Button(window, text="期待", width=15, height=2)
btn2.place(x=pos[0], y=pos[1])
def on_enter(e):
    global pos
    dx = random.randint(100, 200)
    dy = random.randint(100, 300)
    print(pos,dx,dy)
    pos = (pos[0] + dx) % 200, (pos[1] - 250 + dy) % 350 + 250
    btn2.place(x=pos[0], y=pos[1])
btn2.bind("<Enter>", on_enter)
#显示窗口，消息循坏
window.mainloop()