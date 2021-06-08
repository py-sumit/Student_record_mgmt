from tkinter import*
from tkinter import ttk,messagebox
import time
import os
import pymysql
import getpass

#functions
def exit():
    register.destroy()

def wel():
    register.destroy()
    os.system('welcome.py')




register=Tk()
register.title('Register')
register.geometry("700x500")
register.config(bg='#c8c8c8')
lb=Label(register,text='Welcome',font=('Trebuchet MS',45),bg='#c8c8c8')
lb.place(x=220,y=20)

lb=Label(register,text='Admin register',font=('Trebuchet MS',25,'bold'),bg='#c8c8c8',fg='#6816FF')
lb.place(x=230,y=100)

#===============Entry Fields============


lblname = Label(register, text="Name:- ", bg="#c8c8c8", fg="black", font=("times new roman", 20, "bold"))
lblname.place(x=100,y=180)
txtname = Entry(register, bd=5, relief=GROOVE,width=15,font=("times new roman", 18))
txtname.place(x=300,y=180)

lblclass = Label(register, text="Class:- ", bg="#c8c8c8", fg="Black", font=("times new roman", 20, "bold"))
lblclass.place(x=100,y=230)
comboclass = ttk.Combobox(register,font=("times new roman", 18),width=12,state='readonly')
comboclass['values'] = ("I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII")
comboclass.set("Select Class")
comboclass.place(x=300,y=230)

lblusername = Label(register, text="User Name:- ", bg="#c8c8c8", fg="black", font=("times new roman", 20, "bold"))
lblusername.place(x=100,y=280)
txtusername = Entry(register, bd=5, relief=GROOVE,width=15,font=("times new roman", 18))
txtusername.place(x=300,y=280)

lblpass = Label(register, text="Password:- ", bg="#c8c8c8", fg="black", font=("times new roman", 20, "bold"))
lblpass.place(x=100,y=330)
txtpass = Entry(register,show="*", bd=5, relief=GROOVE,width=15,font=("times new roman", 18))
txtpass.place(x=300,y=330)

#==================Database=====================
def adduser():
    con=pymysql.connect(host="localhost",user="root",password="joshi",database="students")
    cur=con.cursor()
    cur.execute("insert into teacher values(%s,%s,%s,%s)",(
                                                        txtname.get(),
                                                        comboclass.get(),
                                                        txtusername.get(),
                                                        txtpass.get()
                                                        ))
    con.commit()
    con.close()
    messagebox.showinfo("register", "Registered Successfully!!!\nYou can Login now..", parent=register)
    register.destroy()
    os.system('Login.py')


#==============Buttons========================

bt=Button(register,text='Exit',height=1,width=8,font=('Trebuchet MS',12),bg='#000000',fg='white',command=exit)
bt.place(x=440,y=420)

bt=Button(register,text='Register',height=1,width=8,font=('Trebuchet MS',12),bg='#115DF4',fg='white',command=adduser)
bt.place(x=200,y=420)

bt=Button(register,text='Back',height=1,width=8,font=('Trebuchet MS',12),bg='#115DF4',fg='white',command=wel)
bt.place(x=320,y=420)

register.resizable(0,0);
register.mainloop()
