from tkinter import *
from tkinter import ttk
from tkinter import messagebox,simpledialog
from tkinter import filedialog
from PIL import ImageTk,Image
import os

win=Tk()
win.resizable(width=False,height=True)
win.state('zoomed')
bgclr='#00ff80'
win.configure(bg=bgclr)
title=Label(win,text='Review Analysis',font=('',50,'bold'),fg='black',bg=bgclr)
title.pack()



def adminhomescreen(prvfrm=None):
    if(prvfrm!=None):
        prvfrm.destroy()
    frm=Frame(win)
    frm.place(x=0,y=100,relwidth=1,relheight=1)

    user_lbl=Label(frm,text='Username:',font=('',20,''),fg='blue')
    user_lbl.place(x=400,y=100)
    
    pass_lbl=Label(frm,text='Password:',font=('',20,''),fg='blue')
    pass_lbl.place(x=400,y=150)


    user_entry=Entry(frm,bd=5,width=15,font=('',15,''))
    user_entry.place(x=580,y=100)
    user_entry.focus()
    
    pass_entry=Entry(frm,show='*',bd=5,width=15,font=('',15,''))
    pass_entry.place(x=580,y=150)

    login_btn=Button(frm,text='Login',command=lambda:nextscreen(frm,user_entry,pass_entry),width=10,font=('',12,''),bg='powder blue',bd=5)
    login_btn.place(x=600,y=220) 

def nextscreen(frm,eu,ep):
    u=eu.get()
    p=ep.get()
    if(u=='admin' or p=='1234'):
        messagebox.showinfo('Succesful',"Succesful ,Go to next page")
        welcome(frm)
        
    else:
       messagebox.showwarning('Wrong',"Retry")
    
def welcome(prvfrm):
    prvfrm.destroy()
    frm=Frame(win)
    frm.place(x=0,y=100,relwidth=1,relheight=1)

    single_btn=Button(frm,text='Single Review',command=lambda:single(frm),width=15,font=('',12,''),bg='powder blue',bd=5)
    single_btn.place(x=600,y=50)

    bulk_btn=Button(frm,text='Bulk Review',command=lambda:bulk(frm),width=15,font=('',12,''),bg='powder blue',bd=5)
    bulk_btn.place(x=600,y=120)

    back_b=ImageTk.PhotoImage(Image.open("backarow.png").resize((50,30)))
    b_back=Button(frm,image=back_b,command=lambda:adminhomescreen(frm))
    b_back.image=back_b
    b_back.place(x=10,y=10)

def single(prvfrm):
    prvfrm.destroy()
    frm=Frame(win)
    frm.place(x=0,y=100,relwidth=1,relheight=1)

    feedback_lbl=Label(frm,text='Your Feedback:',font=('',20,''),fg='blue')
    feedback_lbl.place(x=400,y=100)

    user_entry=Entry(frm,bd=5,width=20,font=('',15,''))
    user_entry.place(x=600,y=100)
    user_entry.focus()


    pridct_btn=Button(frm,text='Prediction',command=lambda:single(frm),width=15,font=('',12,''),bg='powder blue',bd=5)
    pridct_btn.place(x=600,y=200)

    back_b=ImageTk.PhotoImage(Image.open("backarow.png").resize((50,30)))
    b_back=Button(frm,image=back_b,command=lambda:welcome(frm))
    b_back.image=back_b
    b_back.place(x=10,y=10)

    back_b=ImageTk.PhotoImage(Image.open("backarow.png").resize((50,30)))
    b_back=Button(frm,image=back_b,command=lambda:bulk(frm))
    b_back.image=back_b
    b_back.place(x=30,y=30)

def bulk(prvfrm):
    prvfrm.destroy()
    frm=Frame(win)
    frm.place(x=0,y=100,relwidth=1,relheight=1)

    

    feedback_lbl=Label(frm,text='Browse File:',font=('',20,''),fg='blue')
    feedback_lbl.place(x=400,y=100)

    user_entry=Entry(frm,bd=5,width=20,font=('',15,''))
    user_entry.place(x=600,y=100)
    user_entry.focus()

    fileopen_btn=Button(frm,text='File Browse',command=lambda:file(),width=15,font=('',12,''),bg='powder blue',bd=5)
    fileopen_btn.place(x=750,y=200)


    pridct_btn=Button(frm,text='Prediction',command=lambda:bulk(frm),width=15,font=('',12,''),bg='powder blue',bd=5)
    pridct_btn.place(x=600,y=200)

    back_b=ImageTk.PhotoImage(Image.open("backarow.png").resize((50,30)))
    b_back=Button(frm,image=back_b,command=lambda:welcome(frm))
    b_back.image=back_b
    b_back.place(x=10,y=10)

def file():
    dd=filedialog.askopenfilename()
    print(dd)
    
    




adminhomescreen()
win.mainloop()
