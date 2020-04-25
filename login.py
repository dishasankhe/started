from tkinter import *
import tkinter.messagebox

root = Tk()
root.geometry("420x220+0+0")
root.title("Login Page")

name_inp = StringVar()
password_inp = StringVar()


def enter():
    if name_inp.get() == "harry" and password_inp.get() == "1234":
        root.destroy()
        import bill
    else:
        tkinter.messagebox.showinfo('Error', 'Authentication Failed')
        name_inp.set("")
        password_inp.set("")


def destroy():
    root.destroy()


label = Label(root, font=('arial', 50, 'bold'), text="Login", fg="steel blue", bd=10, anchor='w')
label.grid(row=0)

label1 = Label(root, text="Username")
label2 = Label(root, font=('slant', 10, 'bold'), text="Pin")

entry1 = Entry(root, textvariable=name_inp)
entry2 = Entry(root, textvariable=password_inp)

label1.grid(row=1, sticky=E)
label2.grid(row=2, sticky=E)
entry1.grid(row=1, column=1)
entry2.grid(row=2, column=1)

enter_btn = Button(root, text="Enter", command=enter)
enter_btn.grid(row=3, column=1)

exit_btn = Button(root, padx=1, text="Exit", command=destroy)
exit_btn.grid(row=3, column=2)

root.mainloop()
