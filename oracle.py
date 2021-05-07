from tkinter import *
from functools import partial


def register_user(Email, Password):
    print("Email entered:", Email.get())
    print("Password entered:", Password.get())

    if Email.get() == 'Emre@gmail.com':
        if Password.get() == 'Java&PythonProgram':
            print("Welcome Emre!")
    else:
        print("Wrong Email address or Password please try again!")


    return

tkWindow = Tk()
tkWindow.geometry('300x100')
tkWindow.title('GittiGidiyor.com')

EmailLabel = Label(tkWindow, text="Email").grid(row=0, column=0)
Email = StringVar()
EmailEntry = Entry(tkWindow, textvariable=Email).grid(row=0, column=1)

PasswordLabel = Label(tkWindow, text="Password").grid(row=1, column=0)
Password = StringVar()
PasswordEntry = Entry(tkWindow, textvariable=Password, show='*').grid(row=1,column=1)

validateLogin = partial(register_user, Email, Password)

loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)


tkWindow.mainloop()

