from tkinter import *
from tkinter import ttk, messagebox
import time
import os
import pymysql


class Student:
    def logout(self):
        self.root.destroy()
        os.system('main.py')

    def __init__(self, root):
        self.root = root
        self.root.geometry("1900x1000+0+0")
        self.root.title("Student Management System")
        self.root.config(bg="#074463")
        title = Label(self.root, pady=5, bg="white", fg="navy", text="Student Management System",font=("times new roman", 30, "bold"), bd=5, relief=GROOVE)
        title.pack(side=TOP, fill=X)
        self.root.focus_force()
        # ====================All Variables======================================
        self.class_ = StringVar()
        self.roll = StringVar()
        self.name = StringVar()
        self.email = StringVar()
        self.gender = StringVar()
        self.contact = StringVar()
        self.dob = StringVar()
        self.Address = StringVar()
        self.marks = StringVar()
        self.tmarks = StringVar()
        self.Attendance = StringVar()

        butt = Button(self.root,text="Logout",bg='red',fg='white', command=self.logout, width=10,font=("times new roman", 12, "bold"))
        butt.place(x=1400,y=20)

        # =======================Student Frame=======================================================

        self.StudentDetail_Frame = Frame(self.root, bd=5, relief=GROOVE, bg="crimson")
        self.StudentDetail_Frame.place(x=20, y=70, width=1490, height=700)

        self.SearchKeyword = StringVar()
        self.searchtxt = StringVar()
        lblSearchBy = Label(self.StudentDetail_Frame, bg="crimson", fg="white", text="Search By",font=("times new roman", 20, "bold")).grid(row=0, column=0, padx=10, pady=10)

        self.comboSearchBy = ttk.Combobox(self.StudentDetail_Frame, textvariable=self.SearchKeyword, width=12,font=("times new roman", 13), state='readonly')
        self.comboSearchBy["values"] = ("Roll", "Name", "Email", "Contact", "Marks", "Attendance")
        self.comboSearchBy.set("Select Options")
        self.comboSearchBy.grid(row=0, column=1, padx=10, pady=10)

        txtSearch = Entry(self.StudentDetail_Frame, textvariable=self.searchtxt, width=15, bd=4, relief=GROOVE,font=("times new roman", 12)).grid(row=0, column=2, padx=10)

        btnsearch = Button(self.StudentDetail_Frame, command=self.SearchBy, text="Search", width=12,font=("times new roman", 12, "bold")).grid(row=0, column=3, padx=5)

        btnShow = Button(self.StudentDetail_Frame, text="Show All", command=self.showDetails, width=12,font=("times new roman", 12, "bold")).grid(row=0, column=4, padx=5)

        EmptTableFrame = Frame(self.StudentDetail_Frame, bd=4, relief=GROOVE)
        EmptTableFrame.place(x=30, y=60, width=1420, height=620)

        scroll_x = Scrollbar(EmptTableFrame, orient=HORIZONTAL)
        scroll_y = Scrollbar(EmptTableFrame, orient=VERTICAL)

        self.StudentTable = ttk.Treeview(EmptTableFrame, columns=("Roll", "Name", "Email", "Dob", "Gender", "Contact", "Marks Obt", "tmarks", "Address", "Attendance"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_x.config(command=self.StudentTable.xview)
        scroll_y.config(command=self.StudentTable.yview)
        self.StudentTable.heading("Roll", text="Roll No.")
        self.StudentTable.heading("Name", text="Name")
        self.StudentTable.heading("Email", text="Email")
        self.StudentTable.heading("Dob", text="Dob")
        self.StudentTable.heading("Gender", text="Gender")
        self.StudentTable.heading("Contact", text="Contact")
        self.StudentTable.heading("Marks Obt", text="Marks Obt")
        self.StudentTable.heading("tmarks", text="Total Marks")
        self.StudentTable.heading("Address", text="Address")
        self.StudentTable.heading("Attendance", text="Attendance")

        self.StudentTable['show'] = 'headings'
        self.StudentTable.column("Roll", width=50)
        self.StudentTable.column("Name", width=100)
        self.StudentTable.column("Email", width=100)
        self.StudentTable.column("Dob", width=100)
        self.StudentTable.column("Gender", width=100)
        self.StudentTable.column("Contact", width=100)
        self.StudentTable.column("Marks Obt", width=100)
        self.StudentTable.column("tmarks", width=100)
        self.StudentTable.column("Address", width=100)
        self.StudentTable.column("Attendance", width=100)
        self.StudentTable.pack(fill=BOTH, expand=1)
        self.showDetails()

    def SearchBy(self):
        con = pymysql.connect(host="localhost", user='Joshi', password="", database="students")
        cur = con.cursor()
        try:
            if self.SearchKeyword.get() == "Select Options":
                messagebox.showerror("Error", "Please select any search by option", parent=self.root)
            elif self.searchtxt.get() == "":
                messagebox.showerror("Error", "Search Area should not be emplty", parent=self.root)
            else:
                cur.execute(
                    "select * from students where " + self.SearchKeyword.get() + " LIKE '%" + self.searchtxt.get() + "%'")
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.StudentTable.delete(*self.StudentTable.get_children())
                    for row in rows:
                        self.StudentTable.insert('', END, values=row)
                    con.commit()
                    con.close()
                    messagebox.showinfo("Student", "Search Complete!!!", parent=self.root)
                else:
                    messagebox.showerror("Error", "No record Found !!!", parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"error due to {str(es)}", parent=self.root)
    def showDetails(self):
        con = pymysql.connect(host="localhost", user='root', password="joshi", database="students")
        cur = con.cursor()
        try:
            cur.execute("select * from students")
            rows = cur.fetchall()
            if rows != None:
                self.StudentTable.delete(*self.StudentTable.get_children())
                for row in rows:
                    self.StudentTable.insert('', END, values=row)
                con.close()
        except Exception as es:
            messagebox.showerror("Error", f"error due to {str(es)}", parent=self.root)
root = Tk()
ob = Student(root)
root.mainloop()
