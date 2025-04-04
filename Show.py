from tkinter import *
from PIL import Image,ImageTk

class Show:
   def __init__(self,root):
     self.root=root
     self.root.title("Edit")
     screen_width = root.winfo_screenwidth()
     screen_height = root.winfo_screenheight()
     self.root.geometry(f"{screen_width}x{screen_height}+0+0")

     self.main_frame=Frame(self.root,bg='powder blue',width=screen_width,height=screen_height)
     self.main_frame.pack()
    
     img_chat=Image.open(r".vscode/showpic.png")
     img_chat=img_chat.resize((190,78),Image.LANCZOS)
     self.photoimg=ImageTk.PhotoImage(img_chat)

     Title_label=Label(self.main_frame,bd=3,relief=RAISED,anchor='nw',width=1200,compound=LEFT,image=self.photoimg,text='               User Queries',font=('arial',30,'bold'),fg='black',bg='#06beb6')
     Title_label.pack(side=TOP)

     self.text=Text(self.main_frame,width=screen_width,height=screen_height,bd=3,relief=RAISED,font=('arial',14),wrap='word')
     self.scroll_y=Scrollbar(self.main_frame,orient=VERTICAL,command=self.text.yview)
     self.scroll_y.pack(side=RIGHT,fill=Y)
     self.text.pack()
     self.text.config(yscrollcommand=self.scroll_y.set)

     f=open(".vscode\saved_queries.txt","r")
     self.text.insert(END, f.read())
     self.text.config(state=DISABLED)

if __name__ == '__main__':
  root=Tk()
  obj=Show(root)
  root.mainloop()