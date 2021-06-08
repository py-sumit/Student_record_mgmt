from tkinter import*
from tkinter import ttk,messagebox
import time
import os
import pymysql


class Student:
    def logout(self):
        self.root.destroy()
        os.system('main.py')
    def __init__(self,root):
        self.root=root
        self.root.geometry("1200x700+0+0")
        self.root.title("Student Management System")
        self.root.config(bg="#074463")
        title=Label(self.root,pady=5,bg="white",fg="navy",text="Student Management System",font=("times new roman",30,"bold"),bd=5,relief=GROOVE)
        title.pack(side=TOP,fill=X)
        self.root.focus_force()
        #====================All Variables======================================
        self.class_=StringVar()
        self.roll=StringVar()
        self.name=StringVar()
        self.email=StringVar()
        self.gender=StringVar()
        self.contact=StringVar()
        self.dob=StringVar()
        self.Address=StringVar()
        self.marks=StringVar()
        self.tmarks=StringVar()
        self.Attendance=StringVar()

        butt = Button(self.root, text="Logout", bg='red',fg='white', command=self.logout, width=10,font=("times new roman", 12, "bold"))
        butt.place(x=1400, y=20)
        
#=======================================================================
        fg_e="white"
        bg_e="crimson"
        fg_btn_e="white"
        bg_btn_e="#074463"
        Student_Manage_Frame=Frame(self.root,bd=4,relief=GROOVE,bg="crimson" )#"#074463")
        Student_Manage_Frame.place(x=20,y=70,width=550,height=700)

        lbl=Label(Student_Manage_Frame,text="Manage Students",bg=bg_e,fg=fg_e,font=("Comic Sans MS",20,"bold"),pady=0).grid(row=0,columnspan=5,pady=20)

        lblId=Label(Student_Manage_Frame,text="Roll No.:- ",bg=bg_e,fg=fg_e,font=("times new roman",20,"bold"))
        lblId.grid(row=2,column=0,padx=30,pady=3,sticky="w")
        txtId=Entry(Student_Manage_Frame,bd=5,relief=GROOVE,textvariable=self.roll,width=20,font=("times new roman",18))
        txtId.grid(row=2,column=1,padx=20,pady=3)
        
        lblName=Label(Student_Manage_Frame,text="Name:- ",bg=bg_e,fg=fg_e,font=("times new roman",20,"bold"))
        lblName.grid(row=3,column=0,padx=30,pady=3,sticky="w")
        txtName=Entry(Student_Manage_Frame,bd=5,relief=GROOVE,textvariable=self.name,width=20,font=("times new roman",18))
        txtName.grid(row=3,column=1,padx=20,pady=3)

        lblEmail=Label(Student_Manage_Frame,text="Email:- ",bg=bg_e,fg=fg_e,font=("times new roman",20,"bold"))
        lblEmail.grid(row=4,column=0,padx=30,pady=3,sticky="w")
        txtEmail=Entry(Student_Manage_Frame,bd=5,relief=GROOVE,width=20,textvariable=self.email,font=("times new roman",18))
        txtEmail.grid(row=4,column=1,padx=20,pady=3)

        lblgender=Label(Student_Manage_Frame,text="Gender:- ",bg=bg_e,fg=fg_e,font=("times new roman",20,"bold"))
        lblgender.grid(row=5,column=0,padx=30,pady=3,sticky="w")
        combogender=ttk.Combobox(Student_Manage_Frame,textvariable=self.gender,font=("times new roman",18),width=19,state='readonly')
        combogender['values']=("Male","Female","Other")
        combogender.set("Select Gender")
        combogender.grid(row=5,column=1,padx=20,pady=3)

        lblContact=Label(Student_Manage_Frame,text="Contact No.:- ",bg=bg_e,fg=fg_e,font=("times new roman",20,"bold"))
        lblContact.grid(row=6,column=0,padx=30,pady=3,sticky="w")

        txtContact=Entry(Student_Manage_Frame,bd=5,textvariable=self.contact,relief=GROOVE,width=20,font=("times new roman",18))
        txtContact.grid(row=6,column=1,padx=20,pady=3)

        lblDob=Label(Student_Manage_Frame,text="D.O.B:- ",bg=bg_e,fg=fg_e,font=("times new roman",20,"bold"))
        lblDob.grid(row=7,column=0,padx=30,pady=3,sticky="w")
        txtDob=Entry(Student_Manage_Frame,textvariable=self.dob,bd=5,relief=GROOVE,width=20,font=("times new roman",18))
        txtDob.grid(row=7,column=1,padx=20,pady=3)

        lblmarks=Label(Student_Manage_Frame,text="Marks Obt.:- ",bg=bg_e,fg=fg_e,font=("times new roman",20,"bold"))
        lblmarks.grid(row=11,column=0,padx=30,pady=3,sticky="w")
        txtmarks=Entry(Student_Manage_Frame,bd=5,relief=GROOVE,textvariable=self.marks,width=20,font=("times new roman",18))
        txtmarks.grid(row=11,column=1,padx=20,pady=3)

        lbltmarks=Label(Student_Manage_Frame,text="Total Marks:- ",bg=bg_e,fg=fg_e,font=("times new roman",20,"bold"))
        lbltmarks.grid(row=12,column=0,padx=30,pady=3,sticky="w")
        txttmarks=Entry(Student_Manage_Frame,bd=5,relief=GROOVE,textvariable=self.tmarks,width=20,font=("times new roman",18))
        txttmarks.grid(row=12,column=1,padx=20,pady=3)


        lblattn=Label(Student_Manage_Frame,text="Attendance\nin %:- ",bg=bg_e,fg=fg_e,font=("times new roman",20,"bold"))
        lblattn.grid(row=13,column=0,padx=30,pady=3,sticky="w")
        txtattn=Entry(Student_Manage_Frame,bd=5,relief=GROOVE,textvariable=self.Attendance,width=20,font=("times new roman",18))
        txtattn.grid(row=13,column=1,padx=20,pady=3)

        lblAddress=Label(Student_Manage_Frame,text="Address:- ",bg=bg_e,fg=fg_e,font=("times new roman",20,"bold"))
        lblAddress.grid(row=14,column=0,padx=30,pady=3,sticky="nw")
        self.txtAddress=Text(Student_Manage_Frame,width=28,height=3,font=("",13))
        self.txtAddress.grid(row=14,column=1,padx=20,pady=3,sticky="w")
        
        OptionBtn=Frame(Student_Manage_Frame,bd=2,relief=GROOVE,bg="white")
        OptionBtn.place(x=40,y=620,width=445)

        AddBtn=Button(OptionBtn,text="Add",width=8,bg=bg_btn_e,fg=fg_btn_e ,cursor="hand2",command=self.Add_Student,font=("times new roman",13,"bold"),pady=4)
        AddBtn.grid(row=0,column=0,padx=10,pady=5)

        UpdateBtn=Button(OptionBtn,text="Update",bg=bg_btn_e,fg=fg_btn_e ,cursor="hand2",command=self.update_details,width=8,font=("times new roman",13,"bold"),pady=4)
        UpdateBtn.grid(row=0,column=1,padx=10,pady=5)

        DeleteBtn=Button(OptionBtn,text="Delete",bg=bg_btn_e,fg=fg_btn_e ,cursor="hand2",command=self.delete_details,width=8,font=("times new roman",13,"bold"),pady=4)
        DeleteBtn.grid(row=0,column=2,padx=10,pady=5)

        ClearBtn=Button(OptionBtn,text="Clear",bg=bg_btn_e,fg=fg_btn_e ,cursor="hand2",command=self.clear_details,width=8,font=("times new roman",13,"bold"),pady=4)
        ClearBtn.grid(row=0,column=3,padx=10,pady=5)

        
#=======================Student Frame=======================================================

        self.StudentDetail_Frame=Frame(self.root,bd=5,relief=GROOVE,bg="crimson")
        self.StudentDetail_Frame.place(x=600,y=70,width=900,height=700)

        self.SearchKeyword=StringVar()
        self.searchtxt=StringVar()
        lblSearchBy=Label(self.StudentDetail_Frame,bg="crimson",fg="white",text="Search By",font=("times new roman",20,"bold")).grid(row=0,column=0,padx=10,pady=10)

        self.comboSearchBy=ttk.Combobox(self.StudentDetail_Frame,textvariable=self.SearchKeyword,width=12,font=("times new roman",13),state='readonly')
        self.comboSearchBy["values"]=("Roll","Name","Email","Contact","Marks","Attendance")
        self.comboSearchBy.set("Select Options")
        self.comboSearchBy.grid(row=0,column=1,padx=10,pady=10)
        
        txtSearch=Entry(self.StudentDetail_Frame,textvariable=self.searchtxt,width=15,bd=4,relief=GROOVE,font=("times new roman",12)).grid(row=0,column=2,padx=10)

        btnsearch=Button(self.StudentDetail_Frame,command=self.SearchBy,text="Search",width=12,font=("times new roman",12,"bold")).grid(row=0,column=3,padx=5)
        btnShow=Button(self.StudentDetail_Frame,text="Show All",command=self.showDetails,width=12,font=("times new roman",12,"bold")).grid(row=0,column=4,padx=5)


        EmptTableFrame=Frame(self.StudentDetail_Frame,bd=4,relief=GROOVE)
        EmptTableFrame.place(x=30,y=60,width=850,height=620)

        scroll_x=Scrollbar(EmptTableFrame,orient=HORIZONTAL)
        scroll_y=Scrollbar(EmptTableFrame,orient=VERTICAL)

        self.StudentTable=ttk.Treeview(EmptTableFrame,columns=("Roll","Name","Email","Dob","Gender","Contact","Marks Obt","tmarks","Address","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_x.config(command=self.StudentTable.xview)
        scroll_y.config(command=self.StudentTable.yview)
        self.StudentTable.heading("Roll",text="Roll No.")
        self.StudentTable.heading("Name",text="Name")
        self.StudentTable.heading("Email",text="Email")
        self.StudentTable.heading("Dob",text="Dob")
        self.StudentTable.heading("Gender",text="Gender")
        self.StudentTable.heading("Contact",text="Contact")
        self.StudentTable.heading("Marks Obt",text="Marks Obt")
        self.StudentTable.heading("tmarks",text="Total Marks")
        self.StudentTable.heading("Address",text="Address")
        self.StudentTable.heading("Attendance",text="Attendance")
        
        self.StudentTable['show']='headings'
        self.StudentTable.column("Roll",width=50)
        self.StudentTable.column("Name",width=100)
        self.StudentTable.column("Email",width=100)
        self.StudentTable.column("Dob",width=100)
        self.StudentTable.column("Gender",width=100)
        self.StudentTable.column("Contact",width=100)
        self.StudentTable.column("Marks Obt",width=100)
        self.StudentTable.column("tmarks",width=100)
        self.StudentTable.column("Address",width=100)
        self.StudentTable.column("Attendance",width=100)
        self.StudentTable.pack(fill=BOTH,expand=1)
        self.showDetails()
        self.StudentTable.bind("<ButtonRelease-1>",self.get_cursor)

    def get_cursor(self,ev):
        cursor_row=self.StudentTable.focus()
        contents=(self.StudentTable.item(cursor_row))
        row = contents['values']
        con=pymysql.connect(host="localhost",user='sumit',password="12345",database="students")
        cur=con.cursor()
        try:
            cur.execute("select * from students where roll=%s",str(row[0]))
            rows=cur.fetchone()
            self.roll.set(rows[0])
            self.name.set(rows[1])
            self.email.set(rows[2])
            self.dob.set(rows[3])
            self.gender.set(rows[4])
            self.contact.set(rows[5])
            self.marks.set(row[6])
            self.tmarks.set(row[7])
            self.txtAddress.delete('1.0',END)
            self.txtAddress.insert(END,rows[8])
            self.Attendance.set(row[9])
            con.close()
        except Exception as es:
            messagebox.showerror("Error",'No record selected')
    
    def SearchBy(self):
        con=pymysql.connect(host="localhost",user='sumit',password="12345",database="students")
        cur=con.cursor()
        try:
            if self.SearchKeyword.get()=="Select Options":
                messagebox.showerror("Error","Please select any search by option",parent=self.root)
            elif self.searchtxt.get()=="":
                messagebox.showerror("Error","Search Area should not be emplty",parent=self.root)
            else:
                cur.execute("select * from students where "+self.SearchKeyword.get()+" LIKE '%"+self.searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.StudentTable.delete(*self.StudentTable.get_children())
                    for row in rows:
                        self.StudentTable.insert('',END,values=row)
                    con.commit()
                    con.close()
                    messagebox.showinfo("Student", "Search Complete!!!", parent=self.root)
                else:
                    messagebox.showerror("Error","No record Found !!!",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"error due to {str(es)}",parent=self.root)
    


    def Add_Student(self):
        con=pymysql.connect(host="localhost",user='sumit',password="12345",database="students")
        cur=con.cursor()
        try:
            if self.roll.get()==""or self.class_.get()=="Select Class" or self.email.get()=="" or self.gender.get()=="Select Gender" or self.name.get()=="" or self.dob.get()=="" or self.marks.get()=="" or self.tmarks.get()==""  or self.txtAddress.get('1.0',END)=="" or self.Attendance.get()=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("select * from students where roll=%s",self.roll.get())
                emp_exist=cur.fetchone()
                if emp_exist!=None:
                    messagebox.showerror("Error","Student Id Already Exists",parent=self.root)
                else:
                    cur.execute("insert into Students values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                    self.roll.get(),
                                                                                    self.name.get(),
                                                                                    self.email.get(),
                                                                                    self.dob.get(),
                                                                                    self.gender.get(),
                                                                                    self.contact.get(),
                                                                                    self.marks.get(),
                                                                                    self.tmarks.get(),
                                                                                    self.txtAddress.get('1.0',END),
                                                                                    self.Attendance.get()
                                                                                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Student","Record  added Successfully!!!",parent=self.root)
                    self.clear_details()

        except Exception as es:
            messagebox.showerror("Error",f"error due to {str(es)}",parent=self.root)

    def showDetails(self):
        con=pymysql.connect(host="localhost",user='root',password="joshi",database="students")
        cur=con.cursor()
        try:
            cur.execute("select * from students")
            rows=cur.fetchall()
            if rows!=None:
                self.StudentTable.delete(*self.StudentTable.get_children())
                for row in rows:
                    self.StudentTable.insert('',END,values=row)
                con.close()
        except Exception as es:
            messagebox.showerror("Error",f"error due to {str(es)}",parent=self.root)

    def update_details(self):
        con=pymysql.connect(host="localhost",user='root',password="joshi",database="students")
        cur=con.cursor()
        try:
            if self.roll.get()==""or self.class_.get()=="Select Class" or self.email.get()=="" or self.gender.get()=="Select Gender" or self.dob.get()=="" or self.Attendance.get()=="" or self.marks.get()=="" or self.tmarks.get()=="" or self.txtAddress.get('1.0',END)=="":
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cur.execute("Select * from students where roll=%s ",self.roll.get())
                fetch_e=cur.fetchone()
                if fetch_e!=None:
                    cur.execute("update students set name=%s,Email=%s,Dob=%s,Gender=%s,Contact=%s,marks=%s,tmarks=%s,Address=%s,Attendance=%s where roll=%s",(
                                                                                                                    self.name.get(),
                                                                                                                    self.email.get(),
                                                                                                                    self.dob.get(),
                                                                                                                    self.gender.get(),
                                                                                                                    self.contact.get(),
                                                                                                                    self.marks.get(),
                                                                                                                    self.tmarks.get(),
                                                                                                                    self.txtAddress.get('1.0',END),
                                                                                                                    self.Attendance.get(),
                                                                                                                    self.roll.get()
                                                                                                                    ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Student","Record  updated Successfully!!!",parent=self.root)
                    self.showDetails()
                else:
                    messagebox.showerror("Error","Invalid Student Id ",parent=self.root)
        except Exception as es:
            con.close()
            messagebox.showerror("Error",f"error due to {str(es)}",parent=self.root)
    def clear_details(self):
        self.roll.set("")
        self.name.set("")
        self.email.set("")
        self.dob.set("")
        self.gender.set("Select Gender")
        self.contact.set("")
        self.marks.set("")
        self.tmarks.set("")
        self.txtAddress.delete('1.0',END)
        self.Attendance.set("")
        self.showDetails()
    
    def delete_details(self):
        con=pymysql.connect(host="localhost",user='root',password="joshi",database="students")
        cur=con.cursor()
        try:
            if self.roll.get()=="":
                messagebox.showerror("Error","Student Id must be required",parent=self.root)
            else:
                cur.execute("select * from students where roll=%s",self.roll.get())
                row=cur.fetchone()
                if row!=None:
                    yes_no=messagebox.askyesno("Delete Record",f"Are you sure do Delete the Record of \nEmploye ID : {self.roll.get()}\nName : {str(row[1])}",parent=self.root)
                    if yes_no>0:
                        cur.execute("delete from students where roll=%s",self.roll.get())    
                        con.commit()
                        con.close()
                        messagebox.showinfo("Student","Record  deleted Successfully!!!",parent=self.root)
                        self.clear_details()
                        self.showDetails()
                    else:
                        return
                else:
                    con.close()
                    messagebox.showerror("Error","Invalid Student ID",parent=self.root)
        except Exception as es:
            con.close()
            messagebox.showerror("Error",f"error due to {str(es)}")
root=Tk()
ob=Student(root)
root.mainloop()
