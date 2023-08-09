from tkinter import *


# from tkinter.ttk import *

def dataHandle(fname, lname):
    error = Label(master, text="Error : Enter a valid name")
    if fname.get().isspace() or len(fname.get()) == 0 or lname.get().isspace() or len(lname.get()) == 0:
        error.grid(row=3, column=0, columnspan=2)
    else:
        error.grid_remove()
        print("Hello", fname.get(), lname.get())
    fname.delete(0, len(fname.get()))
    lname.delete(0, len(lname.get()))


master = Tk()
labelFirstName = Label(
    master,
    text="Enter first name",
    fg="black",
)
labelSecondName = Label(
    master,
    text="Enter second name",
    fg="black",
)

entryFirstName = Entry(
    master,
)
entrySecondName = Entry(
    master,
)
buttonSend = Button(
    master,
    text="Send",
    command=lambda: dataHandle(entryFirstName, entrySecondName)
)
buttonQuit = Button(
    master,
    text="Quit",
    command=lambda: master.quit()
)
labelFirstName.grid(row=0, column=0)
labelSecondName.grid(row=1, column=0)
entryFirstName.grid(row=0, column=1)
entrySecondName.grid(row=1, column=1)
buttonSend.grid(row=2, column=0)
buttonQuit.grid(row=2, column=1)
master.mainloop()
