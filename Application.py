# Created by GastDev
import tkinter
from tkinter import Y, font
from tkinter import messagebox
from turtle import back

from matplotlib.pyplot import text

#Information about the customer saved into an array
clientInfo = [[]]

#Setup the window and it's properties
global total
total = 0.0
window = tkinter.Tk()
window.title("Gast's Outlet")
window.geometry("900x900")
window.configure(background="moccasin")
greetings = tkinter.Label(window, text="Welcome to Gast's Outlet!\nChoose an option!", fg="black",
                          background="moccasin", font=("Arial", 24))

#Functions
#Takeaway Function
def takeawayFunction():
    t = tkinter.Tk()
    t.title("Gast's Takeaway")
    t.geometry("900x900")
    t.configure(background="moccasin")
    address = tkinter.Entry(t, fg="Black", bg="white", width=15, font=("Arial", 12))
    file = open("logs.txt", "w")
    addy = address.get()
    file.write("Address: " + addy)

    file.close()
    address.pack()
    
#Menu Function
def orderFunction():
    m = tkinter.Tk()
    m.title("Order")
    m.geometry("900x900")
    m.configure(background="moccasin")
    e = "Total £" + str(total)

    #Functions for the buttons
    def pastaFunc():
        global total
        total += 9.99 
        bill.configure(text="Total £" + str(round(total, 2)))
    def burgerFunc():
        global total
        total += 29.99
        bill.configure(text="Total £" + str(round(total, 2)))
    def pizzaFunc():
        global total
        total += 39.99
        bill.configure(text="Total £" + str(round(total, 2)))

    #Buttons and packing everything in the function
    pasta = tkinter.Button(m, text="Pasta             £9.99", fg="Black", bg="cyan2", background="moccasin", command=pastaFunc,height=2, width=20,font=("Arial", 15))
    burger = tkinter.Button(m, text="Burger           £29.99", fg="Black", bg="cyan2", background="moccasin", command=burgerFunc,height=2, width=20,font=("Arial", 15))
    pizza = tkinter.Button(m, text="Pizza             £39.99", fg="Black", bg="cyan2", background="moccasin", command=pizzaFunc,height=2, width=20,font=("Arial", 15))
    bill = tkinter.Label(m, text=e, fg="black", background="moccasin", font=("Arial", 20))
    bill.pack()
    burger.pack()
    pizza.pack()
    pasta.pack()
    

#Buttons
takeaway = tkinter.Button(window, font=("Arial", 30), text="Takeaway", fg="Black", bg="cyan2", command=takeawayFunction, height=2, width=8)
order = tkinter.Button(window,font=("Arial", 30), text="Order", fg="Black", bg="cyan2", command=orderFunction, height=2, width=8)

#Pack everything here
greetings.pack()
takeaway.pack()
order.pack()



#Executes the window here
window.mainloop()
