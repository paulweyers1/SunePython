from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Kapiti College Canteen Order form")

#GST = 3/23

class order:

    def __init__(self, parent)
    
    #List of food items and their prices (In $)
    #CHECK PRICE OF FOOD
    price_list = [
        ["BLT",3.80],
        ["Ham salad sandwich",4.50],
        ["veggie Sandwich",4.50],
        ["Chicken panini",4.80],
        ["Hawaiian panini",4.50],
        ["Breakfast burrito",4.80],
        ["Nachos",3.50],
        ["Wedges",3.00],
        ["Hash Browns",1.20],
        ["Garlic Bread",1.50]
        ]
    amount_list = []

    customer_name = ttk.Label(root, text="Customer Name:")
    customer_name.grid(row=1, column=0, padx=10, pady=3)
    customer_input = ttk.Entry(root)
    customer_input.grid(row=1, column=1, padx=10, pady=10, sticky="WE")

    #This 'for' loop that allows for input of amount for each item, items are gotten from the price list (multidimentinal list) Price is 1 and item is 0 
    for i in range(len(price_list)):
        row = 4+2*i
        label = ttk.Label(root, text=price_list[i][0])
        label.grid(row=row, column=0, padx=10,pady=3)

     # adds the user input into the 'amount_list"
        amount_input = ttk.Entry(root)
        amount_input.grid(row=row, column=1, padx=10, pady=10, sticky="WE")
        amount_list.append(amount_input)

        amount_input.insert (0, 0)

    # Label and entry box to display the total at the end of the code
    total_label = ttk.Label(root, text="Total:")
    total_label.grid(row=100, column=0, padx=10, pady=3)

    total_input = ttk.Entry(root)
    total_input.grid(row=100, column=1, padx=10, pady=10, sticky="WE")


    #Calculates the total price  based on the price_list (taken from the multidimentianl list) and from the user input of how much they want to order from amount_list
    def take_order(self):
        total_price = 0
        for i in range(len(price_list)):
            value = amount_list[i].get()
            total_price += int(value) * float(price_list[i][1])
                                        
        total_input.insert(0, total_price)

    def open_menu(self):
        import Pictureslideshow

    submit_button = ttk.Button(root, text="Submit order", command=take_order)
    submit_button.grid(row=200, column=5, padx=10, pady=10)

    menu_button = ttk.Button(root, text="Menu", command=open_menu)
    menu_button.grid(row=180, column=5, padx=10, pady=10)

    exit_button = ttk.Button(root, text="Exit", command=exit)
    exit_button.grid(row=220, column=5, padx=10, pady=10)  

#WHEN DOING GST: Set GST as a constent 


root = Tk()
Order_form = order(root)
root.mainloop()
