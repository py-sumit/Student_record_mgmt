from tkinter import*
from tkinter import ttk,messagebox
import time
import os
import pymysql


#functions
def exit():
    stulogin.destroy()

def wel():
    stulogin.destroy()
    os.system('welcome2.py')


#=================Tkinter==============


stulogin=Tk()
stulogin.title('Log In')
stulogin.geometry("700x500")
stulogin.config(bg='#c8c8c8')
lb=Label(stulogin,text='Welcome',font=('Trebuchet MS',45),bg='#c8c8c8')
lb.place(x=220,y=20)

#==============Labels And Entry fields=================

global txtid,txtpass

lb=Label(stulogin,text='Student Login',font=('Trebuchet MS',25,'bold'),bg='#c8c8c8',fg='#6816FF')
lb.place(x=250,y=100)

lblid = Label(stulogin, text="User Name:- ", bg="#c8c8c8", fg="black", font=("times new roman", 20, "bold"))
lblid.place(x=100,y=200)
txtid = Entry(stulogin, bd=5, relief=GROOVE,width=15,font=("times new roman", 18))
txtid.place(x=300,y=200)

lblpass = Label(stulogin, text="Password:- ", bg="#c8c8c8", fg="black", font=("times new roman", 20, "bold"))
lblpass.place(x=100,y=250)
txtpass = Entry(stulogin,show="*", bd=5, relief=GROOVE,width=15,font=("times new roman", 18))
txtpass.place(x=300,y=250)


#================Database===========


def log():
    con=pymysql.connect(host="localhost",user="root",password="joshi",database="students")
    cur=con.cursor()
    try:
        cur.execute("select username from stu where password=%s",txtpass.get())
        for i in cur:
            getstuloginID = i[0]
        cur.execute("select password from stu where password=%s",txtpass.get())
        for i in cur:
            getPass = i[0]

        if (getstuloginID == txtid.get() and getPass == txtpass.get()):
            messagebox.showinfo("SUCCESS", "You have successfully logged in")
            stulogin.destroy()
            os.system('student.py')
        else:
            messagebox.showerror("Failure", "Can't log in, check your username and password..")
    except:
        messagebox.showinfo("FAILED", "Please check your credentials")




#===============Buttons======================


bt=Button(stulogin,text='Exit',height=1,width=8,font=('Trebuchet MS',12),bg='#000000',fg='white',command=exit)
bt.place(x=440,y=420)

bt=Button(stulogin,text='login',height=1,width=8,font=('Trebuchet MS',12),bg='#115DF4',fg='white',command=log)
bt.place(x=200,y=420)

bt=Button(stulogin,text='Back',height=1,width=8,font=('Trebuchet MS',12),bg='#115DF4',fg='white',command=wel)
bt.place(x=320,y=420)

stulogin.resizable(0,0);
stulogin.mainloop()
