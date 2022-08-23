from email.mime import application
from os import curdir
from sqlite3 import Row
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from tokenize import String
from turtle import bgcolor
from unittest import result  # กล่องโต้ตอบ
import pymysql
import random  

class MemberConnect:

    def __init__(self, root):
        self.root = root
        blank_space = " "
        self.root.title(180 * blank_space + "MySql Connector")
        self.root.geometry("1360x700+0+0")

        MemID = StringVar()
        Firstname = StringVar()
        Surname = StringVar()
        Address = StringVar()
        PoBox = StringVar()    # รหัสไปรษณีย์
        Gender = StringVar()
        MType = StringVar()   # ประเภทสมาชิก
        Mobile = StringVar()
        Email = StringVar()
        Search = StringVar()
        MemIDBar = StringVar()   # บาร์โค๊ด

        # ================================================================================================

        MainFrame = Frame(self.root, bd=10,width=1350,height=700,relief=RIDGE,bg="cadetblue")
        MainFrame.grid()

        TitleFrames = Frame(MainFrame, bd=7,width=1340,height=100,relief=RIDGE)
        TitleFrames.grid(row=0, column=0)

        SearchFrame = Frame(MainFrame, bd=5,padx=5,width=1340,height=50,relief=RIDGE)
        SearchFrame.grid(row=1, column=0)

        MidFrame = Frame(MainFrame, bd=5,width=1340,height=500,relief=RIDGE)
        MidFrame.grid(row=2, column=0)

        MemberDetailsFrm = Frame(MidFrame, bd=5,width=1340,height=180,padx=6,pady=4, relief=RIDGE)
        MemberDetailsFrm.grid(row=0, column=0)

        TreeviewFrm = Frame(MidFrame, bd=5,padx=2,width=1340,height=400, relief=RIDGE)
        TreeviewFrm.grid(row=1, column=0)

        ButtonFrame = Frame(MidFrame, bd=7,width=1340,height=50,bg="cadetblue", relief=RIDGE)
        ButtonFrame.grid(row=2, column=0)

        # ================================================================================================
        self.lbltitle = Label(TitleFrames,font=('arial',40,'bold'),text="MySQL Connection",bd=7)
        self.lbltitle.grid(row=0, column=0, padx=420)
        # ================================================================================================
        self.lblmemberID = Label(MemberDetailsFrm,font=('arial',12,'bold'),text="Member ID",bd=7,anchor='w',justify=LEFT)
        self.lblmemberID.grid(row=0, column=0, padx=5, sticky=W)

        self.txtmemberID = Entry(MemberDetailsFrm,font=('arial',12,'bold'),textvariable=MemID,bd=5,width=36, justify=LEFT)
        self.txtmemberID.grid(row=0, column=1,)

        self.lblFirstname = Label(MemberDetailsFrm,font=('arial',12,'bold'),text="Firstname",bd=7,anchor='w',justify=LEFT)
        self.lblFirstname.grid(row=1, column=0, padx=5, sticky=W)

        self.txtFirstname = Entry(MemberDetailsFrm,font=('arial',12,'bold'),textvariable=Firstname,bd=5,width=36, justify=LEFT)
        self.txtFirstname.grid(row=1, column=1,)

        self.lblSurname = Label(MemberDetailsFrm,font=('arial',12,'bold'),text="Surname",bd=7,anchor='w',justify=LEFT)
        self.lblSurname.grid(row=2, column=0, padx=5, sticky=W)

        self.txtSurname = Entry(MemberDetailsFrm,font=('arial',12,'bold'),textvariable=Surname,bd=5,width=36, justify=LEFT)
        self.txtSurname.grid(row=2, column=1,)
        # ================================================================================================
        self.lblAddress = Label(MemberDetailsFrm,font=('arial',12,'bold'),text="Address",bd=7)
        self.lblAddress.grid(row=0, column=2, padx=5, sticky=W)

        self.txtAddress = Entry(MemberDetailsFrm,font=('arial',12,'bold'),textvariable=Address,bd=5,width=40, justify=LEFT)
        self.txtAddress.grid(row=0, column=3,)

        self.lblGender = Label(MemberDetailsFrm,font=('arial',12,'bold'),text="Gender",bd=5)
        self.lblGender.grid(row=1, column=2, padx=5, sticky=W)

        self.cboGender = ttk.Combobox(MemberDetailsFrm,font=('arial',12,'bold'),textvariable=Gender,width=38,state='readonly')
        self.cboGender['values']=('','Female','Male')
        self.cboGender.current(0)
        self.cboGender.grid(row=1, column=3,)

        self.lblMobile = Label(MemberDetailsFrm,font=('arial',12,'bold'),text="Surname",bd=5)
        self.lblMobile.grid(row=2, column=2, padx=5, sticky=W)

        self.txtMobile = Entry(MemberDetailsFrm,font=('arial',12,'bold'),textvariable=Mobile,bd=5,width=40)
        self.txtMobile.grid(row=2, column=3,)

        # ================================================================================================
        self.lblPOBox = Label(MemberDetailsFrm,font=('arial',12,'bold'),text="PO Box",bd=7)
        self.lblPOBox.grid(row=0, column=4, padx=5, sticky=W)

        self.txtPOBox = Entry(MemberDetailsFrm,font=('arial',12,'bold'),textvariable=PoBox,bd=5,width=35, justify=LEFT)
        self.txtPOBox.grid(row=0, column=5,)

        self.lblEmail = Label(MemberDetailsFrm,font=('arial',12,'bold'),text="Email",bd=5)
        self.lblEmail.grid(row=1, column=4, padx=5, sticky=W)

        self.txtEmail = Entry(MemberDetailsFrm,font=('arial',12,'bold'),textvariable=Email,bd=5,width=35)
        self.txtEmail.grid(row=1, column=5,)

        self.lblType = Label(MemberDetailsFrm,font=('arial',12,'bold'),text="Type",bd=5)
        self.lblType.grid(row=2, column=4, padx=5, sticky=W)

        self.cboType = ttk.Combobox(MemberDetailsFrm,font=('arial',12,'bold'),textvariable=MType,width=33,state='readonly')
        self.cboType['values']=('Member Type','Annual Member','Quarterly','Monthly')
        self.cboType.current(0)
        self.cboType.grid(row=2, column=5,)

         # ============================== Function ==========================================================
        def addNew():
            if MemID.get() == "" or Firstname.get() == "" or Surname.get() == "":
                tkinter.messagebox.showerror("Error check input", "Enter correct members details")
            else:
                sqlCon = pymysql.connect(host="localhost", user="root", passwd="Ying_4449", database="member")
                cur = sqlCon.cursor()
                cur.execute("insert into member values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    
                MemID.get(),
                Firstname.get(),
                Surname.get(),
                Address.get(),
                PoBox.get(),
                Gender.get(),
                Mobile.get(),
                Email.get(),
                MType.get(),
                ))

                sqlCon.commit()
                ShowRecord()
                sqlCon.close()
                tkinter.messagebox.showinfo("Data Entry Form", "Record Entered Successfully")

        def ShowRecord():
            sqlCon = pymysql.connect(host="localhost", user="root", passwd="Ying_4449", database="member")
            cur = sqlCon.cursor()
            cur.execute("select * from member")
            result = cur.fetchall()
            if len(result) != 0:
                self.member_records.delete(*self.member_records.get_children())
                for row in result:
                    self.member_records.insert('',END,values=row)
                sqlCon.commit()
            sqlCon.close()


         # ================================================================================================

        scroll_y=Scrollbar(TreeviewFrm, orient=VERTICAL)

        self.member_records=ttk.Treeview(TreeviewFrm,height=12,columns=("memid","firstname","surname","address",
                                        "pobox","gender","mobile","email","mtype"),yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.member_records.heading("memid",text="MemberID")
        self.member_records.heading("firstname",text="Firstname")
        self.member_records.heading("surname",text="Surname")
        self.member_records.heading("address",text="Address")
        self.member_records.heading("pobox",text="PO Box")
        self.member_records.heading("gender",text="Gender")
        self.member_records.heading("mobile",text="Mobile")
        self.member_records.heading("email",text="Email")
        self.member_records.heading("mtype",text="Member Type")

        self.member_records['show']='headings'

        self.member_records.column("memid", width=120)
        self.member_records.column("firstname",width=140)
        self.member_records.column("surname",width=140)
        self.member_records.column("address",width=212)
        self.member_records.column("pobox",width=120)
        self.member_records.column("gender",width=120)
        self.member_records.column("mobile",width=120)
        self.member_records.column("email",width=212)
        self.member_records.column("mtype",width=120)

        self.member_records.pack(fill=BOTH,expand=1)

        # ================================================================================================
        self.lblBarCode = Label(SearchFrame,font=('arial',12,'bold'),text="Bar Code")
        self.lblBarCode.grid(row=0, column=0,sticky=W,padx=4)
        self.txtBarcode = Entry(SearchFrame,font=('CCode39',13,'bold'),bd=5,width=26,justify='center',textvariable=MemIDBar)
        self.txtBarcode.grid(row=0,column=1,padx=39)

        self.txtSearch = Entry(SearchFrame,font=('arial',16,'bold'),width=33,justify='right',textvariable=Search)
        self.txtSearch.grid(row=0,column=2)
        self.btnSearch = Button(SearchFrame,pady=1,padx=29,width=9,height=1, bd=4,font=('arial',16,'bold'), text="Search",bg="cadetblue").grid(row=0,column=3,padx=1)

        # ================================================================================================
        self.btnAddNew = Button(ButtonFrame,pady=1,padx=29,width=11,height=1, bd=4,font=('arial',16,'bold'), text="Add New",command=addNew).grid(row=0,column=0,padx=2)
        self.btnShowRecord = Button(ButtonFrame,pady=1,padx=29,width=11,height=1, bd=4,font=('arial',16,'bold'), text="Show Record",command=ShowRecord).grid(row=0,column=1,padx=2)
        self.btnUpdate = Button(ButtonFrame,pady=1,padx=29,width=11,height=1, bd=4,font=('arial',16,'bold'), text="Update").grid(row=0,column=2,padx=2)
        self.btnDelete = Button(ButtonFrame,pady=1,padx=29,width=11,height=1, bd=4,font=('arial',16,'bold'), text="Delete").grid(row=0,column=3,padx=2)
        self.btnReset = Button(ButtonFrame,pady=1,padx=29,width=11,height=1, bd=4,font=('arial',16,'bold'), text="Reset").grid(row=0,column=4,padx=2)
        self.btnExit = Button(ButtonFrame,pady=1,padx=29,width=11,height=1, bd=4,font=('arial',16,'bold'), text="Exit").grid(row=0,column=5,padx=2)
        
        # ================================================================================================




if __name__ == '__main__':
      root = Tk()
      application = MemberConnect(root)
      root.mainloop()





