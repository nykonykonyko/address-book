from tkinter import * 
from tkinter.ttk import * 
screen = Tk()
screen.geometry("600x800")
screen.config(background="darkgreen",border=10,borderwidth=10,relief="raised")
screen.title("Address Book")

a = Label(screen,text="Welcome to the address book")
a.grid(row=0,column=1,pady=10,columnspan=3)
#open addressbook
OpenButton = Button(screen,text="Open Address Book")
OpenButton.grid(row=0,column=3,pady=10,columnspan=3)
ContactList = Listbox(screen,font="Arial 15 bold")
ContactList.grid(row=2,column=0,columnspan=3,rowspan=5)


screen.mainloop()