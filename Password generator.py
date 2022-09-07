from tkinter import*
import random
frame=Tk()
frame.geometry('400x400')
frame.configure(background= "skyblue")
frame.title("Password Generate")

def gen():
    n=en1.get()
    ct=len(n)
    if(ct<=6):
        a="Week Password"
        nn.set(a)
        en2=Label(textvariable=nn , bg='skyblue' ,fg='red',font=45)
        en2.place(x=90,y=170)

        
        
    elif(ct>=7 and ct<=9):
        b="strong Password"
        nn.set(b)
        en2=Label(textvariable=nn , bg='skyblue', fg='blue',font=45)
        en2.place(x=90,y=170)
        
    elif(ct>=10):
        c="Very Strong Password"
        nn.set(c)
        en2=Label(textvariable=nn , bg='skyblue',fg='green',font=45)
        en2.place(x=90,y=170)
        
        
        
nn=StringVar()

name=Label(text="Password Generate")
name.place(x=90,y=50)

en1=Entry()
en1.place(x=90,y=90)

btn=Button(text="Generate",command=gen)
btn.place(x=90,y=130)




