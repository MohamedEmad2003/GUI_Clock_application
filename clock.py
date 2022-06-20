import time
import sys
from tkinter import *

def times():
    current_time=time.strftime("%H : %M : %S")
    clock.configure(text=current_time)
    clock.after(200,times)

root = Tk()
root.geometry("500x250")
root.configure(bg='#142045')
clock = Label(root,font=("times",50,'bold'),bg='#b9def0',fg='#8c1230')
clock.grid(row=2,column=2,pady=25,padx=100)
times()

digi = Label(root,text="Digital Clock",bg='#142045',fg='white',font='times 24 bold')
digi.grid(row=1,column=2)

nota=Label(root,fg='white',bg='#8c1230',text='      hours            minutes             seconds    ',font='times 15 bold')
nota.grid(row=3,column=2)

root.mainloop()



































































