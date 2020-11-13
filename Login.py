#building a calculator

from tkinter import *

window=Tk()
window.title("Log in")
window.configure(background="pink", relief="solid")
window.geometry("700x200")


lbh=Label(window,text="Log In Page:", font="arial 18 bold")
lbh.pack()

lb1=Label(window,text="First number:", font="arial 18 bold")
lb1.pack(pady=20)

en1=Entry(window)
en1.pack(pady=20)

lb2=Label(window,text="Second number:", font="arial 18 bold")
lb2.pack(pady=20)

en2=Entry(window)
en2.pack(pady=20)

lb3=Label(window,text="Result:", font="arial 18 bold")
lb3.pack(pady=20)

mytexbox= Label(window, width=30)#never make results a textbox
mytexbox.pack(pady=20)

my_button=Button(window, text="Add")
my_button.pack(pady=20)

my_clearbutton=Button(window,text="Clear")
my_clearbutton.pack(pady=20)


#first establish your window

window.mainloop()
