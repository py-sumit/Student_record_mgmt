from tkinter import*
from tkinter import ttk,messagebox
import time
import os
import pymysql


#functions
def exit():
    main.destroy()

def open():
    main.destroy()
    os.system('welcome.py')

def reg():
    main.destroy()
    os.system('welcome2.py')

#===============Tkinter===============


main=Tk()
main.title('Welcome Interface')
main.geometry("650x400")
main.config(bg='#c8c8c8')
lb=Label(main,text='Welcome',font=('Trebuchet MS',45),bg='#c8c8c8')
lb.place(x=200,y=20)


#==============Label and entry fields====================

lb=Label(main,text='To',font=('Trebuchet MS',28,'bold'),bg='#c8c8c8')
lb.place(x=310,y=120)

lb=Label(main,text='Student Management System',font=('Trebuchet MS',32,'bold'),bg='#c8c8c8',fg='#6816FF')
lb.place(x=48,y=190)

#================Buttons===========================

bt=Button(main,text='Exit',height=2,width=9,font=('Trebuchet MS',12),bg='#000000',fg='white',command=exit)
bt.place(x=500,y=300)

bt=Button(main,text='Admin',height=2,width=12,font=('Trebuchet MS',12),bg='#115DF4',fg='white',command=open)
bt.place(x=60,y=300)

bt=Button(main,text='Student',height=2,width=16,font=('Trebuchet MS',12),bg='#00ABC1',fg='white',command=reg)
bt.place(x=260,y=300)
main.resizable(0,0);
main.mainloop()
