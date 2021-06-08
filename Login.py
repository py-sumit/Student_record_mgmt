from tkinter import*
from tkinter import ttk,messagebox
import time
import os
import pymysql


#functions
def exit():
    login.destroy()

def wel():
    login.destroy()
    os.system('welcome.py')


#=================Tkinter==============


login=Tk()
login.title('Log In')
login.geometry("700x500")
login.config(bg='#c8c8c8')
lb=Label(login,text='Welcome',font=('Trebuchet MS',45),bg='#c8c8c8')
lb.place(x=220,y=20)

#==============Labels And Entry fields=================

global txtid,txtpass

lb=Label(login,text='Admin LogIn',font=('Trebuchet MS',25,'bold'),bg='#c8c8c8',fg='#6816FF')
lb.place(x=250,y=100)

lblid = Label(login, text="User Name:- ", bg="#c8c8c8", fg="black", font=("times new roman", 20, "bold"))
lblid.place(x=100,y=200)
txtid = Entry(login, bd=5, relief=GROOVE,width=15,font=("times new roman", 18))
txtid.place(x=300,y=200)

lblpass = Label(login, text="Password:- ", bg="#c8c8c8", fg="black", font=("times new roman", 20, "bold"))
lblpass.place(x=100,y=250)
txtpass = Entry(login,show="*", bd=5, relief=GROOVE,width=15,font=("times new roman", 18))
txtpass.place(x=300,y=250)


#================Database===========


def log():
    con=pymysql.connect(host="localhost",user="root",password="joshi",database="students")
    cur=con.cursor()
    try:
        cur.execute("select username from teacher where password=%s",txtpass.get())
        for i in cur:
            getLoginID = i[0]
        cur.execute("select password from teacher where password=%s",txtpass.get())
        for i in cur:
            getPass = i[0]

        if (getLoginID == txtid.get() and getPass == txtpass.get()):
            messagebox.showinfo("SUCCESS", "You have successfully logged in")
            login.destroy()
            os.system('Student_Management.py')
        else:
            messagebox.showerror("Failure", "Can't log in, check your username and password..")
    except:
        messagebox.showinfo("FAILED", "Please check your credentials")




#===============Buttons======================


bt=Button(login,text='Exit',height=1,width=8,font=('Trebuchet MS',12),bg='#000000',fg='white',command=exit)
bt.place(x=440,y=420)

bt=Button(login,text='LogIn',height=1,width=8,font=('Trebuchet MS',12),bg='#115DF4',fg='white',command=log)
bt.place(x=200,y=420)

bt=Button(login,text='Back',height=1,width=8,font=('Trebuchet MS',12),bg='#115DF4',fg='white',command=wel)
bt.place(x=320,y=420)

login.resizable(0,0);
login.mainloop()
