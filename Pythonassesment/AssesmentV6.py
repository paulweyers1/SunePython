
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

root = Tk()
root.title("Kapiti College Canteen Order form")

GST_factor = 3/23
MAX = 10
order_list = []
order_number = 1

 
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
amount_list = []

title_label = Label(font=('arial',20,'bold'), text="Kapiti college Canteen Order Form ", fg="maroon")
title_label.grid(row=0)


"""
with open('food_menu.txt','r') as food_menu_file:

    for line in food_menu_file:
        name, group, price = line.strip().split(', ')
        #price_list.append([name, group, price])

    for i in range(len(price_list)):
        row = 4+2*i

        if price_list[i][0] == "sandwitches":
            label = ttk.Label(order_sandwitch_middle, text=price_list[i][0])
            label.grid(row=row, column=0, padx = 10, pady=10, sticky="WE")

            amount_input = ttk.Entry(order_sandwitch_middle)
            amount_input.grid(row=row, column= 1, padx=10, pady=10, sticky="WE")
            amount_list.append(amount_input)
            amount_input.insert(0,0)
"""      

customer_name = ttk.Label(root, text="Customer Name:")
customer_name.grid(row=2, column=0, padx=10, pady=3)
customer_input = ttk.Entry(root)
customer_input.grid(row=2, column=1, padx=10, pady=10, sticky="WE")

order_list.append(("Order Number", "Customer Name", "Total Cost", "GST"))


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
total_label = ttk.Label(root, text="Total Price (Includes GST):  $")
total_label.grid(row=100, column=0, padx=10, pady=3)

total1_label = ttk.Label(root, text="")
total1_label.grid(row=100, column=1, padx=10, pady=3)


#GST label box
GST_label = ttk.Label(root, text="Total GST:  $")
GST_label.grid(row=120, column=0, padx=10, pady=3)

GST1_label = ttk.Label(root, text="")
GST1_label.grid(row=120, column=1, padx=10, pady=3)



#Calculates the total price  based on the price_list (taken from the multidimentianl list) and from the user input of how much they want to order from amount_list
def take_order():
    total_price = 0
    global order_number
    reset_flag = 0
    
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
        total1_label.configure(text= total_string)
        GST_string = '%.2f' % GST
        GST1_label.configure(text= GST_string)

        # Append order to order list
        order_list.append(("Ord#" + str(order_number), str(customer_input.get()), str(total_string), str(GST_string)))
        order_number+=1
        t = Order_Table(root)

        # Clear the fields
        customer_input.delete(0,END)
        for i in range(len(price_list)):
            amount_list[i].delete(0,END)
            amount_list[i].insert(0,0)
                        

def open_menu():
    import Pictureslideshow

receipt_label = ttk.Label(root, text="Order List", foreground='blue', font=('Arial', 16))
receipt_label.grid(row=0, column=4, padx=20, pady=3)


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
                  
                ttk.e = Entry(root, width=20, fg='blue', font=('Arial',10))
                ttk.e.grid(row=(i*row_depth)+row_offset, column=j+column_offset)
                ttk.e.insert(END, order_list[i][j])

def check_value(value):  

    if not(value.isdigit()):
        tkinter.messagebox.showerror("Data Error", "Please only enter numerical values")
        return 1
    
    elif (int(value) > MAX):
        tkinter.messagebox.showinfo("Limit Exceeded", "Cannot order more than " + str(MAX) + " items. Please pick a number less than " + (str(MAX + 1)) + " and resubmit your order")
        return 1
    
    
    return 0

def check_customer_name(customer_name):  

    if (len(customer_name)  == 0 or customer_name.isdigit()):
        tkinter.messagebox.showerror("Data Error", "Please input alphabetic name value for Customer name ")
        return 1

    return 0

#Submit button
submit_button = ttk.Button(root, text="Submit order", command=take_order)
submit_button.grid(row=200, column=5, padx=10, pady=10)

#Menu Button
menu_button = ttk.Button(root, text="Menu", command=open_menu)
menu_button.grid(row=180, column=5, padx=10, pady=10)

#Exit button
exit_button = ttk.Button(root, text="Exit", command=exit)
exit_button.grid(row=220, column=5, padx=10, pady=10)

root.mainloop()
