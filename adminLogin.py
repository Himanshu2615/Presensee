from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
import datetime
import tkinter as tk
from check import FaceIdentificationSystem
import pytz
from check import FaceIdentificationSystem
# Function part
def login_use():
    if UserName.get()=='' or Password=='P2615':
        messagebox.showerror('Error','All fields are required')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='P2615')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error', 'Connection not established properly')
            return
    query = 'use admininfo'
    mycursor.execute(query)
    query='select * from data where UserName=%s and password=%s'
    mycursor.execute(query,(UserName.get(),Password.get()))
    row=mycursor.fetchone()
    if row==None:
        messagebox.showerror('Error','Invalid username and password')
    else:
        messagebox.showinfo('Success','Login is Successfull')
        check2_window = tk.Toplevel(rootlw)
        check2_app = FaceIdentificationSystem(check2_window)
def hide():
    openeye.config(file='/images/closeye.png')
    Password.config(show='*')
    eyeButton.config(command=show)
def show():
    openeye.config(file='/images/openeye.png')
    Password.config(show='')
    eyeButton.config(command=hide)
def User_enter(event):
    if UserName.get()=='Username':
        UserName.delete(0,END)
def Password_enter(event):
    if Password.get()=='Password':
        Password.delete(0,END)
def admin_page():
    rootlw.destroy()
    import admin_signup
def home_page():
    home_window= tk.Toplevel(rootlw)
    home_app =FaceIdentificationSystem(home_window)
def forget_pass():
    rootlw.destroy()
    import forgetp
def update_cloc():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%H:%M:%S  %Y-%m-%d")
    time_label.config(text="Time:- " + formatted_time)
    rootlw.after(1000, update_cloc)
rootlw=Tk()
rootlw.geometry("1520x790+0+0")
rootlw.title('Sign UP  Page')
bgImage=ImageTk.PhotoImage(file='/images/bg7.webp')
bg4Label=Label(rootlw,image=bgImage)
bg4Label.grid()
frame=Frame(rootlw,bg='deepskyblue4')
frame.place(x=575,y=150)
heading=Label(frame,text='ADMIN LOGIN',font=('calibri',31,'bold'),bg='deepskyblue4'
              ,fg='white')
heading.grid(row=0,column=0,padx=10,pady=10)
UserName=Entry(frame,width=25,font=("calibri",14,'bold'),bd=0,fg='deepskyblue4',bg='white')
UserName.grid(row=2,column=0,sticky='w',padx=25,pady=(8,0))
UserName.insert(0,'Username')
UserName.bind('<FocusIn>',User_enter)
Password=Entry(frame,width=25,font=("calibri",14,'bold'),bd=0,fg='deepskyblue4',bg='white')
Password.grid(row=4,column=0,sticky='w',padx=25,pady=(8,0))
Password.insert(0,'Password')
Password.bind('<FocusIn>',Password_enter)
frame2=Frame(frame,width=250,height=2,bg='firebrick1')
frame2.place(x=600,y=350)
openeye=PhotoImage(file='/images/openeye.png')
eyeButton=Button(frame,image=openeye,bd=0,bg='White',activebackground='white',cursor='hand2',command=hide)
eyeButton.grid(row=4,column=0,sticky='e',padx=25,pady=(8,0))
forgetbtn=Button(frame,text='Forget Password?',bd=0,bg='deepskyblue4',activebackground='white',cursor='hand2',font=("calibri",14,'bold'),fg='yellow',activeforeground='firebrick1',command=forget_pass)
forgetbtn.grid(row=8,column=0,sticky='e',padx=25,pady=(8,0))
Login_but = Button(frame,text="Login", font=('open sans', 16, 'bold'),fg='white',bg='firebrick1',cursor='hand2',activeforeground='white',activebackground='firebrick1',bd=0,width=19,command=login_use)
Login_but.grid(row=10,column=0,sticky='w',padx=25,pady=(8,0))
orlabel=Label(frame,text='**************OR*************',font=('Open Sans','16'),fg='firebrick1',bg='deepskyblue4')
orlabel.grid(row=12,column=0)
facebook_logo=PhotoImage(file='/images/facebook.png')
fblabel=Label(frame,image=facebook_logo,bg='white')
fblabel.grid(row=14,column=0,sticky='w',padx=60)
google_logo=PhotoImage(file='/images/google.png')
golabel=Label(frame,image=google_logo,bg='white')
golabel.grid(row=14,column=0,sticky='e',padx=60)
linkedlogo=PhotoImage(file='/images/linked.png')
lnlabel=Label(frame,image=linkedlogo,bg='white')
lnlabel.grid(row=14,column=0)

sign_btn=Label(frame,text='Dont Have An Account',cursor='hand2',font=('Microsoft Yahei UI Light',9,'bold'),fg='yellow',bg='deepskyblue4')
sign_btn.grid(row=16,column=0,sticky='w',padx=20,pady=(10,0))
newa_but = Button(frame,text="Create New", font=('open sans', 12, 'bold underline'),fg='orange',bg='deepskyblue4',cursor='hand2',activeforeground='white',activebackground='firebrick1',bd=0,command=admin_page)
newa_but.grid(row=16,column=0,sticky='e',padx=25,pady=(10,0))
time_label = tk.Label(frame, font=("Helvetica", 11, "bold"), fg="white", bg="deepskyblue4")
time_label.grid(row=20, column=0,sticky='w' ,padx=25,pady=(10,0))
update_cloc()
rootlw.mainloop()
