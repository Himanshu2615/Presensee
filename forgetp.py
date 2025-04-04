from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql
def User_enter2(event):
    if UserName1.get() == 'User Name':
        UserName1.delete(0, END)

def Password_enter2(event):
    if NEWpass.get() == 'NEW PASSWORD':
        NEWpass.delete(0, END)


def Password_enter3(event):
    if ConfirmEntry2.get() == 'RENTER YOUR PASS':
        ConfirmEntry2.delete(0, END)


def forget_pass1():
    if NEWpass.get() != ConfirmEntry2.get():
        messagebox.showerror('Error', 'Passwords are not matching ')
    elif NEWpass.get() == '' or ConfirmEntry2.get == '' or UserName1.get == '':
        messagebox.showerror('Error', 'All fields are mendatory')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='P2615')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Connection not established properly')
            return
        query = 'use userinfo'
        mycursor.execute(query)
        query = 'update data set password=%s where UserName=%s;'
        mycursor.execute(query, (NEWpass.get(), UserName1.get()))
        con.commit()
        con.close()
        messagebox.showinfo("Success", 'Password Changed Successfully')
window = Tk()
window.title('Change Password')
bgpic = ImageTk.PhotoImage(file='.vscode/images/bg14.webp')
bglabel = Label(window, image=bgpic)
bglabel.grid()
frame=Frame(window,bg='orange')
frame.place(x=300,y=150)
headingf = Label(frame, text='RESET PASSWORD', font=("calibri", 20, 'bold'), bg='deepskyblue4', fg='white')
headingf.grid(row=0,column=0,padx=10,pady=10)
UserName1 = Entry(frame, width=25, font=('calibri', 12, 'bold'), bd=0, fg='white', bg='deepskyblue4')
UserName1.grid(row=1,column=0,padx=10,pady=10)
UserName1.insert(0, 'User Name')
UserName1.bind('<FocusIn>', User_enter2)
frame4 = Frame(frame, width=200, height=2, bg='white')
frame4.grid(row=2,column=0,padx=10)
NEWpass = Entry(frame, width=25, font=('calibri', 12, 'bold'), bd=0, fg='white',bg='deepskyblue4')
NEWpass.grid(row=3,column=0,padx=10,pady=10)
NEWpass.insert(0, 'NEW PASSWORD')
NEWpass.bind('<FocusIn>', Password_enter2)
frame5 = Frame(frame, width=200, height=2, bg='white')
frame5.grid(row=4,column=0,padx=10)

ConfirmEntry2 = Entry(frame, width=25, font=('calibri', 12, 'bold'), fg='white', bd=0, bg='deepskyblue4')
ConfirmEntry2.grid(row=5,column=0,padx=10,pady=10)
ConfirmEntry2.insert(0, 'RENTER YOUR PASS')
ConfirmEntry2.bind('<FocusIn>', Password_enter3)
frame6 = Frame(frame, width=200, height=2, bg='white')
frame6.grid(row=6,column=0,padx=10)
confirmbtn = Button(frame, text="CONFIRM", font=('open sans', 16, 'bold'), fg='white', bg='red', cursor='hand2',
                    activeforeground='white', activebackground='magenta', bd=0, width=15, command=forget_pass1)
confirmbtn.grid(row=6,column=0,padx=10,pady=10)

window.mainloop()



