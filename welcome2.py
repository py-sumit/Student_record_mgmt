from tkinter import*
from tkinter import ttk,messagebox
import time
import os
import pymysql


#functions
def exit():
    win.destroy()
    os.system('Main.py')

def open():
    win.destroy()
    os.system('Stulogin.py')

def reg():
    win.destroy()
    os.system('sturegister.py')

#===============Tkinter===============


win=Tk()
win.title('Welcome Student')
win.geometry("650x400")
win.config(bg='#c8c8c8')
lb=Label(win,text='Welcome',font=('Trebuchet MS',45),bg='#c8c8c8')
lb.place(x=200,y=20)


#==============Label and entry fields====================

lb=Label(win,text='To',font=('Trebuchet MS',28,'bold'),bg='#c8c8c8')
lb.place(x=310,y=120)

lb=Label(win,text='Student Management System',font=('Trebuchet MS',32,'bold'),bg='#c8c8c8',fg='#6816FF')
lb.place(x=48,y=190)

#================Buttons===========================

bt=Button(win,text='Back',height=2,width=9,font=('Trebuchet MS',12),bg='#000000',fg='white',command=exit)
bt.place(x=500,y=300)

bt=Button(win,text='LogIn',height=2,width=12,font=('Trebuchet MS',12),bg='#115DF4',fg='white',command=open)
bt.place(x=60,y=300)

bt=Button(win,text='Register',height=2,width=16,font=('Trebuchet MS',12),bg='#00ABC1',fg='white',command=reg)
bt.place(x=260,y=300)
win.resizable(0,0);
win.mainloop()
