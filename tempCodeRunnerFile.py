from tkinter import *
import pymysql
from PIL import ImageTk
from tkinter import messagebox
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
def login_page():
    signup_window.destroy()
    import login
def admin_page():
    signup_window.destroy()
    import adminLogin
def clear():
    emailEntry.delete(0,END)
    userEntry.delete(0,END)
    PassEntry.delete(0,END)
    check.set(0)
    signup_window.destroy()
    import login
def connect_database():
    if (emailEntry.get()=='' or userEntry.get()=='' or PassEntry.get()=='' or ConfirmEntry.get()==''):
        messagebox.showerror('Error','All Fields Are Required')
    elif PassEntry.get()!=ConfirmEntry.get():
        messagebox.showerror('Error','Password Mismatch')
    elif check.get()==0:
        messagebox.showerror('Error', 'Please accept terms and conditions')
    else:
        try:
            con=pymysql.Connect(host='localhost',user='root',password='P2615')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Error, pLease try Again.')
            return
        try:
            query='create database userinfo;'
            mycursor.execute(query)
            query='use userinfo;'
            mycursor.execute(query)
            query='create table data (id int auto_increment primary key not null,Email varchar(70),UserName varchar(50),password varchar(20));'
            mycursor.execute(query)
        except:
            mycursor.execute('use userinfo')
        query='select * from data where UserName=%s'
        mycursor.execute(query,(userEntry.get()))
        row=mycursor.fetchone()
        if row!=None:
            messagebox.showerror('Error', 'UserName already exists')
        else:
            query='insert into data(Email,UserName,password) values(%s,%s,%s)'
            mycursor.execute(query,(emailEntry.get(),userEntry.get(),PassEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration is Successful')
            clear()
signup_window=Tk()
signup_window.geometry("1520x790+0+0");
signup_window.title('Sign Up Page')
# signup_window.resizable(False,False)
background=ImageTk.PhotoImage(file='/images/bg11.jpeg')
bg6label=Label(signup_window,image=background)
bg6label.grid()
frame=Frame(signup_window,bg='deepskyblue4')
frame.place(x=575,y=150)
heading=Label(frame,text='Create An Account',font=('calibri',31,'bold'),bg='deepskyblue4'
              ,fg='white')
heading.grid(row=0,column=0,padx=10,pady=10)

emailLabel=Label(frame,text='Email',font=("calibri",12,'bold'),bg='deepskyblue4',fg='white')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(8,0))
emailEntry=Entry(frame,width=30,font=('calibri',12,'bold'),fg='antiquewhite',bg='firebrick1')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

userLabel=Label(frame,text='User Name',font=("calibri",12,'bold'),bg='deepskyblue4',fg='white')
userLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(8,0))

userEntry=Entry(frame,width=30,font=('calibri',12,'bold'),fg='antiquewhite',bg='firebrick1')
userEntry.grid(row=4,column=0,sticky='w',padx=25)

PassLabel=Label(frame,text='Password',font=("calibri",12,'bold'),bg='deepskyblue4',fg='white')
PassLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(8,0))

PassEntry=Entry(frame,width=30,font=('calibri',12,'bold'),fg='antiquewhite',bg='firebrick1')
PassEntry.grid(row=6,column=0,sticky='w',padx=25)

ConfirmLabel=Label(frame,text='Confirm Password',font=("calibri",12,'bold'),bg='deepskyblue4',fg='white')
ConfirmLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(8,0))

ConfirmEntry = Entry(frame, width=30, font=('calibri', 12, 'bold'), fg='darkslategray1', bg='firebrick1')
ConfirmEntry.grid(row=8, column=0, sticky='w', padx=25)

check=IntVar()
termsAndConditions = Checkbutton(frame, text="I Agree To Terms And Conditions", font=('calibri', '12', 'bold'), bg='deepskyblue4', activeforeground='firebrick1', cursor='hand2',variable=check)
termsAndConditions.grid(row=9, column=0, pady=10, padx=15)

submit_but = Button(frame, text="SIGN UP", font=('open sans', 16, 'bold'), bd=0,fg='white',bg='firebrick1',activeforeground='white',activebackground='firebrick1',width=17,
                    command=connect_database,cursor='hand2')
submit_but.grid(row=11, column=0,pady=10) # Notice row 11 instead of 10

account_label = Label(frame, text="Don't have an account", font=('open sans', 9, 'bold'),fg='white',bg='deepskyblue4')
account_label.grid(row=13, column=0,sticky='w',padx=25,pady=10) # Notice row 11 instead of 10

login_but = Button(frame, text="LOG IN", font=('open sans', 10, 'bold underline'), bd=0,fg='yellow',bg='deepskyblue4',activeforeground='blue',cursor='hand2',command=login_page)
login_but.place(x=172, y=415)

Adminreg_but = Button(frame, text="Admin", font=('open sans', 10, 'bold underline'), bd=0,fg='yellow',bg='deepskyblue4',activeforeground='blue',cursor='hand2',command=admin_page)
Adminreg_but.place(x=270, y=415)

signup_window.mainloop()

