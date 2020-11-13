from tkinter import *
from tkinter import filedialog
from tkinter import simpledialog ,messagebox


window=Tk()
window.title("File Handling")
window.configure(background="pink", relief="solid")
window.geometry("700x500")

def qualify():
    try:
        amount = int(entry1.get())

        if amount < 3000:
            raise ValueError

    except ValueError as e:
       messagebox.showerror("Insufficient Funds:","You do not qualify for a trip to Malaysia. Please add more funds.")

    else:
        messagebox.showinfo("Congratulations!","You qualify for a trip to Malaysia!")

    finally:
        messagebox.showinfo("Completed.","Your transaction has been completed.")

    amount = int(entry1.get())


def clear_function():
    entry1.delete(0,END)


def close_window():
    sure = messagebox.askyesno(title="Alert",message="Are you sure that you want to exit this app?")
    if sure==True:
        window.destroy()
    else:
        return  None



lb1=Label(window,text="Flights to Malayisa:", font="arial 18 bold")
lb1.pack()

lb3=Label(window,text="Please enter deposit amount below.", font="arial 12")
lb3.pack(pady=20)

entry1=Entry(window)
entry1.pack(pady=20)

open_button=Button(window, text="Qualify", command=qualify)
open_button.pack(pady=20)


exit_button = Button (text = "Exit", command = close_window)
exit_button.place(x=600, y=370)

clear_button = Button (text = "Clear", command = clear_function)
clear_button.pack(pady=20)

window.mainloop()



