# Created by GastDev
import tkinter
from tkinter import messagebox

#Array to hold the order data
orderData = [[]]

#Setup the window and it's properties
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
    
    
#Menu Function
def orderFunction():
    m = tkinter.Tk()
    m.title("Order")
    m.geometry("900x900")
    m.configure(background="moccasin")
    e = "Total £" + str(total)

    #Close listener
    def on_closing():
        if messagebox.askokcancel("Quit", "Are you sure you want to cancel your order?"):
            orderData.clear()
            m.destroy()
    m.protocol("WM_DELETE_WINDOW", on_closing)

    #Functions for the buttons
    def pastaFunc():
        global total
        total += 9.99 
        bill.configure(text="Total £" + str(round(total, 2)))
        global orderData
        orderData.append(9.99)
    def burgerFunc():
        global total
        total += 19.99
        bill.configure(text="Total £" + str(round(total, 2)))
        global orderData
        orderData.append(19.99)
    def pizzaFunc():
        global total
        total += 29.99
        bill.configure(text="Total £" + str(round(total, 2)))
        global orderData
        orderData.append(29.99)
    
    def friesFunc():
        global total
        total += 3.99
        bill.configure(text="Total £" + str(round(total, 2)))
        global orderData
        orderData.append(3.99)
    def guacemoliFunc():
        global total
        total += 5.99
        bill.configure(text="Total £" + str(round(total, 2)))
        global orderData
        orderData.append(5.99)
    def breadFunc():
        global total
        total += 6.99
        bill.configure(text="Total £" + str(round(total, 2)))
        global orderData
        orderData.append(6.99)
    
    #Function to loop through the list and get the last value, this removes the last item bought
    def getLastIndex():
        return orderData[-1]
    def removeLastItem():
        global total
        try:
            total -= getLastIndex()
            orderData.remove(getLastIndex())
            bill.configure(text="Total £" + str(round(total, 2)))
        except IndexError:
            print("[ERROR] ---> Caught IndexError. Order list has no values.")
        except TypeError:
            print("[ERROR] ---> Caught TypeError. Unsupported operator for float and list.")
    def submitOrderFunc():
        file = open("orders.txt", 'w')
        file.write("Order List\n")
        if 9.99 in orderData:
            pCount = orderData.count(9.99)
            file.write(str(pCount) + " Pastas ---> Total Pasta Price: " + str((round(pCount * 9.99, 2))) + "\n")
        if 19.99 in orderData:
            bCount = orderData.count(19.99)
            file.write(str(bCount) + " Burgers ---> Total Burger Price: " + str((round(bCount * 19.99, 2))) + "\n")
        if 29.99 in orderData:
            pCount = orderData.count(29.99)
            file.write(str(pCount) + " Pizzas ---> Total Pizza Price: " + str((round(pCount * 29.99, 2))) + "\n")
        if 3.99 in orderData:
            fCount = orderData.count(3.99)
            file.write(str(fCount) + " Fries ---> Total Fries Price: " + str((round(fCount * 3.99, 2))) + "\n")
        if 5.99 in orderData:
            gCount = orderData.count(5.99)
            file.write(str(gCount) + " Guacemolis ---> Total Guacemoli Price: " + str((round(gCount * 5.99, 2))) + "\n")
        if 6.99 in orderData:
            brCount = orderData.count(6.99)
            file.write(str(brCount) + " Breads ---> Total Bread Price: " + str((round(brCount * 6.99, 2))) + "\n")
        orderData.clear()
        total = 0
        file.close()

    #Defining the buttons and labels properties
    pasta = tkinter.Button(m, text="Pasta             £9.99", fg="Black", bg="cyan2", background="moccasin", command=pastaFunc,height=2, width=20,font=("Arial", 15))
    burger = tkinter.Button(m, text="Burger           £19.99", fg="Black", bg="cyan2", background="moccasin", command=burgerFunc,height=2, width=20,font=("Arial", 15))
    pizza = tkinter.Button(m, text="Pizza             £29.99", fg="Black", bg="cyan2", background="moccasin", command=pizzaFunc,height=2, width=20,font=("Arial", 15))
    
    fries = tkinter.Button(m, text="Fries             £3.99", fg="Black", bg="cyan2", background="moccasin", command=friesFunc,height=2, width=20,font=("Arial", 15))
    guacemoli = tkinter.Button(m, text="Guacemoli     £5.99", fg="Black", bg="cyan2", background="moccasin", command=guacemoliFunc,height=2, width=20,font=("Arial", 15))
    bread = tkinter.Button(m, text="Bread             £6.99", fg="Black", bg="cyan2", background="moccasin", command=breadFunc,height=2, width=20,font=("Arial", 15))

    removeItem = tkinter.Button(m, text="Remove Last Item Purchased", fg="Black", bg="moccasin", command=removeLastItem, height=2, width=24,font=("Arial", 15))
    submitOrder = tkinter.Button(m, text="Submit Order", fg="Black", bg="moccasin", command=submitOrderFunc, height=2, width=24,font=("Arial", 15))

    bill = tkinter.Label(m, text=e, fg="black", background="moccasin", font=("Arial", 20))
    item = tkinter.Label(m, text="Main Courses", background="moccasin", font=("Arial", 20))
    item2 = tkinter.Label(m, text="Sides", background="moccasin", font=("Arial", 20))

    #Packing all the buttons and labels
    item.pack() # Main Courses
    item2.pack() # Sides
    bill.pack() # Bill
    removeItem.pack()
    submitOrder.pack() # Submit Order
    burger.pack() # Burger
    pizza.pack() # Pizza
    pasta.pack() # Pasta
    fries.pack() # Fries
    guacemoli.pack() # Guacemoli
    bread.pack() # Bread
    
    #Positioning the buttons and labels
    item.place(x=22, y=45)
    pasta.place(x=22, y=88)
    burger.place(x=22, y= 155)
    pizza.place(x=22, y=225)

    item2.place(x=22, y=300)
    fries.place(x=22, y=340)
    guacemoli.place(x=22, y=410)
    bread.place(x=22, y=480)
    removeItem.place(x=600, y=50)
    submitOrder.place(x=600, y=120)
    

#Buttons
takeaway = tkinter.Button(window, font=("Arial", 30), text="Takeaway", fg="Black", bg="cyan2", command=takeawayFunction, height=2, width=8)
order = tkinter.Button(window,font=("Arial", 30), text="Order", fg="Black", bg="cyan2", command=orderFunction, height=2, width=8)

#Pack everything here
greetings.pack()
takeaway.pack()
order.pack()


#Executes the window here
window.mainloop()
