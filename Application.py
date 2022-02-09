# Created by GastDev
import tkinter
from tkinter import Y, font
from tkinter import messagebox
from turtle import back

from matplotlib.pyplot import text

#Information about the customer saved into an array
clientInfo = [[]]

#Setup the window and it's properties
total = 0.0
window = tkinter.Tk()
window.title("Gast's Outlet")
window.geometry("900x900")
window.configure(background="moccasin")
greetings = tkinter.Label(window, text="Welcome to Gast's Outlet!\nChoose an option!", fg="black",
                          background="moccasin", font=("Arial", 24))

#Functions
def takeawayFunction():
    t = tkinter.Tk()
    t.title("Gast's Takeaway")
    t.geometry("900x900")
    t.configure(background="moccasin")

def pFunc():
    
#Menu Function
def orderFunction():
    m = tkinter.Tk()
    m.title("Order")
    m.geometry("900x900")
    m.configure(background="moccasin")
    e = "Total £" + str(total)

    pasta = tkinter.Button(m, text="Pasta             £9.99", fg="Black", bg="cyan2", background="moccasin", command=,height=2, width=20,font=("Arial", 15))
    burger = tkinter.Button(m, text="Burger           £29.99", fg="Black", bg="cyan2", background="moccasin", command=,height=2, width=20,font=("Arial", 15))
    pizza = tkinter.Button(m, text="Pizza             £39.99", fg="Black", bg="cyan2", background="moccasin", command=,height=2, width=20,font=("Arial", 15))

    bill = tkinter.Label(m, textvariable=e, fg="black", background="moccasin", font=("Arial", 20))
    bill.pack()
    burger.pack()
    pizza.pack()
    pasta.pack()
    

#Buttons
takeaway = tkinter.Button(window, font=("Arial", 30), text="Tip", fg="Black", bg="cyan2", command=takeawayFunction, height=3, width=8)
order = tkinter.Button(window,font=("Arial", 30), text="Order", fg="Black", bg="cyan2", command=orderFunction, height=2, width=5)

#Pack everything here
greetings.pack()
takeaway.pack()
order.pack()



#Executes the window here
window.mainloop()
