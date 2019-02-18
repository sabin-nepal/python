from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk
win = Tk()
def validation(name,passw,mail):
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', mail)
    username=re.match("^[\d_a-z]+$", name) 
    if match==None:
        error = Label(win,text="Email Invalid")
        error.grid()
        return
    if username==None:
        error = Label(win,text="Username must be lowercase and be digit")
        error.grid()
        return
    else:
        nextWin()
def nextWin():
    next = Toplevel(win)
    next.geometry("400x400")
    notebook = ttk.Notebook(next)
    tab1 = tk.Frame(notebook,)
    tab2 = tk.Frame(notebook)
    notebook.add(tab1,text="Encrypted Data")
    notebook.add(tab2,text="Decrypt Data")
    notebook.grid()
    file = Entry(tab1, font=("", 10))
    file.grid(row="2",column="1")
    fileButton = Button(tab1, text="Browse File",bg="blue", command=lambda :BrowseFile(file))
    fileButton.grid(row="3",column="1")
    uploadButton = Button(tab1,text="Upload File",bg="red",command=lambda:UploadFile(file.get))
    uploadButton.grid(row="2",column="2")
    Emessage = Entry(tab1,font=("",15))
    Emessage.grid(row="4",column="1")
    send = Button(tab1,text="Send")
    send.grid(row="4",column="2")


def BrowseFile(file):
    filename = filedialog.askopenfilename()
    file.insert(0,filename)

win.geometry("400x400")
registerLabel = Label(win,text="Register Here")
registerLabel.grid()
name = Entry(win,font=("",20))
name.insert(0,'username')
name.grid(padx="30",pady="10")
password = Entry(win,show="*",font=("",20))
password.insert(0,'password')
password.grid(padx="30")
email = Entry(win,font=("",20))
email.insert(0,'email')
email.grid(padx="30",pady="10")
register = Button(win,text="Register",command=lambda: validation(name.get(),password.get(),email.get()))
register.grid()

##next Window

win.mainloop()