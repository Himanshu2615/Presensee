from tkinter import *
import json
from PIL import Image,ImageTk 

class Edit:
   def __init__(self,root):
     self.root=root
     self.root.title("Edit")
     root.config(bg="light yellow")
     screen_width = root.winfo_screenwidth()
     screen_height = root.winfo_screenheight()
     self.root.geometry(f"{screen_width}x{screen_height}+0+0")

     self.main_frame=Frame(self.root,bg='powder blue',width=screen_width,height=screen_height)
     self.main_frame.pack()
    
     img_chat=Image.open(r"editpic.png")
     img_chat=img_chat.resize((200,78),Image.LANCZOS)
     self.photoimg=ImageTk.PhotoImage(img_chat)

     Title_label=Label(self.main_frame,bd=3,relief=RAISED,anchor='nw',width=1200,compound=LEFT,image=self.photoimg,text='               Edit ChatBot Queries',font=('arial',30,'bold'),fg='black',bg='pink')
     Title_label.pack(side=TOP)

     q_label=Label(self.root,text="Query",font=('arial',20,'bold'),fg='black',bg='sky blue',width=50,bd=3)
     q_label.place(x=300,y=200)
     self.q_entry=Entry(self.root,fg='black',bg='white',width=77,bd=3,font=('arial',15))
     self.q_entry.place(x=300,y=250)

     r_label=Label(self.root,text="Response",font=('arial',20,'bold'),fg='black',bg='light green',width=50,bd=3)
     r_label.place(x=300,y=350)
     self.r_entry=Entry(self.root,fg='black',bg='white',width=77,bd=3,font=('arial',15))
     self.r_entry.place(x=300,y=400)

     add_button=Button(self.root,text="Add",font=('arial',15),width=20,bg="light grey",command=self.add)
     add_button.place(x=610,y=500)

     self.ack_label=Label(self.root,text="",font=('arial',20,'bold'),fg='red',width=50,bg="light yellow")
     self.ack_label.place(x=300,y=550)


   def convert(self,s):
    r=''
    for i in s:
      if(i.isalpha()):
        r=r+i
    return r

   def add(self):
    if (self.q_entry.get()!='' and self.r_entry.get()!=''):
     with open(r"Queries.json","r") as file:
       qs=json.load(file)
     #k=self.convert(self.q_entry.get())
     v=self.r_entry.get()
     qs[self.q_entry.get()]=v

     with open("Queries.json","w") as file:
       json.dump(qs,file,indent=2)

     self.ack_label.config(text="Query added !")
    elif(self.q_entry.get()=='' and self.r_entry.get()==''):
     self.ack_label.config(text="Please enter query and response.")
    elif (self.q_entry.get()==''):
     self.ack_label.config(text="Please enter query.")
    elif (self.r_entry.get()==''):
     self.ack_label.config(text="Please enter response.")
    


if __name__ == '__main__':
  root=Tk()
  obj=Edit(root)
  root.mainloop()