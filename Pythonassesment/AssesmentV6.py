# import the libraries i need to complete this window
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

# create the window and give it a title
root = Tk()
root.title("Kapiti College Canteen Order form")

# Global variables and constant values
GST_factor = 3/23  # Factor to help calculate GST
MAX = 10           # Maximum number of items allowed
order_list = []    # list of submitted orders
order_number = 1   # Unique order number for all orders
amount_list = []   # list of amount fields

#List of food items and their prices (In $)
#CHECK PRICE OF FOOD
price_list = [
    ["BLT",  3.80, "sandwitch"],
    ["Ham salad sandwich" ,4.50],
    ["veggie Sandwich",4.50 ],
    ["Chicken panini",4.80],
    ["Hawaiian panini",4.50],
    ["Breakfast burrito",4.80],
    ["Nachos",3.50],
    ["Wedges",3.00],
    ["Hash Browns",1.20],
    ["Garlic Bread",1.50]
    ]

# Order Form Heading
title_label = Label(font=('arial',20,'bold'), text="Kapiti College Canteen Order Form ", fg="maroon")
title_label.grid(row=0)

# Order List Heading
receipt_label = ttk.Label(root, text="Order List", foreground='maroon', font=('Arial', 12))
receipt_label.grid(row=0, column=4, padx=20, pady=3)

# Customer Name Field
customer_name = ttk.Label(root, text="Customer Name:")
customer_name.grid(row=2, column=0, padx=10, pady=3)
customer_input = ttk.Entry(root)
customer_input.grid(row=2, column=1, padx=10, pady=10, sticky="WE")

# Label and entry box to display the total at the end of the code
total_label = ttk.Label(root, text="Total Price (Includes GST):  $")
total_label.grid(row=24, column=0, padx=10, pady=3)

total1_label = ttk.Label(root, text="")
total1_label.grid(row=24, column=1, padx=10, pady=3)

# GST label box
GST_label = ttk.Label(root, text="Total GST:  $")
GST_label.grid(row=26, column=0, padx=10, pady=3)

GST1_label = ttk.Label(root, text="")
GST1_label.grid(row=26, column=1, padx=10, pady=3)

# class to create the order table
class Order_Table:
    def __init__(self,root):

        # code for creating a order table
        total_rows = len(order_list)
        total_columns = len(order_list[0])
        column_offset = 4
        row_offset = 2
        row_depth = 2

        for i in range(total_rows):
            for j in range(total_columns):
                ttk.e = Label(root, text=str(order_list[i][j]), foreground='maroon', font=('Arial', 10))
                ttk.e.grid(row=(i*row_depth)+row_offset, column=j+column_offset)

# Calculates the total price  based on the price_list (taken from the multidimentianl list) and from the user input of how much they want to order from amount_list
def take_order():
    total_price = 0
    global order_number
    reset_flag = 0

    # validate fields and calculate total price for order
    if check_customer_name(customer_input.get()) == 0:
        for i in range(len(price_list)):
            value = amount_list[i].get()
            if check_value(value) == 0:
                reset_flag = 1
                total_price += int(value) * float(price_list[i][1])
            else:
                reset_flag = 0
                break

    # If the order was added clear the fields else leave them
    if reset_flag == 1:

        # Calculate total and GST
        GST =  total_price*GST_factor
        total_string = '%.2f' % total_price
        total1_label.configure(text= str("$ "+total_string))
        GST_string = '%.2f' % GST
        GST1_label.configure(text= str("$ "+GST_string))

        # construct an order number
        order_no = str(order_number).zfill(3)

        # Append new order to order list
        order_list.append(("ord-"+order_no, str(customer_input.get()), str("$ "+total_string), str("$ "+GST_string)))
        order_number+=1
        t = Order_Table(root)

        # Reset the fields for next order
        customer_input.delete(0,END)
        total1_label.configure(text= "")
        GST1_label.configure(text= "")
        for i in range(len(price_list)):
            amount_list[i].delete(0,END)
            amount_list[i].insert(0,0)

# Event to calculate the total cost and GST everytime more items are added
def focus_out(event = None):
    total_price = 0

    # Validate fields and calculate total price for order
    for i in range(len(price_list)):
        value = amount_list[i].get()
        total_price += int(value) * float(price_list[i][1])

    # Calculate total and GST
    GST =  total_price*GST_factor
    total_string = '%.2f' % total_price
    total1_label.configure(text= str("$ "+total_string))
    GST_string = '%.2f' % GST
    GST1_label.configure(text= str("$ "+GST_string))

def setup_stuff():
    # Headings for the order list table
    order_list.append(("Order No.", "Customer", "Total Cost", "GST"))

    # This 'for' loop that allows for input of amount for each item, items are gotten from the price list (multidimentinal list) Price is 1 and item is 0
    for i in range(len(price_list)):
        row = 4+2*i
        label = ttk.Label(root, text=price_list[i][0])
        label.grid(row=row, column=0, padx=10,pady=3)

        # adds the user input into the 'amount_list"
        amount_input = ttk.Entry(root)
        amount_input.grid(row=row, column=1, padx=10, pady=10, sticky="WE")

        # set event to calculate total when someone has updated an item amount
        amount_input.bind('<FocusOut>', focus_out)
        amount_list.append(amount_input)
        amount_input.insert (0, 0)

# open the food item slideshow
def open_menu():
    import Pictureslideshow

# validation to check that item amounts are numeric and less that the maximum limit
def check_value(value):

    if not(value.isdigit()):
        tkinter.messagebox.showerror("Data Error", "Please only enter numerical values")
        return 1

    elif (int(value) > MAX):
        tkinter.messagebox.showinfo("Limit Exceeded", "Cannot order more than " + str(MAX) + " items. Please pick a number less than " + (str(MAX + 1)) + " and resubmit your order")
        return 1

    return 0

# validation to check the customer name has been added and is not numeric
def check_customer_name(customer_name):

    if (len(customer_name)  == 0 or customer_name.isdigit()):
        tkinter.messagebox.showerror("Data Error", "Please input a non numeric name value for Customer name")
        return 1

    return 0

# Menu Button
menu_button = ttk.Button(root, text="Menu", command=open_menu)
menu_button.grid(row=30, column=1, padx=10, pady=10)

# Submit button
submit_button = ttk.Button(root, text="Submit order", command=take_order)
submit_button.grid(row=32, column=1, padx=10, pady=10)

# Exit button
exit_button = ttk.Button(root, text="Exit", command=exit)
exit_button.grid(row=34, column=1, padx=10, pady=10)

setup_stuff()
root.mainloop()
