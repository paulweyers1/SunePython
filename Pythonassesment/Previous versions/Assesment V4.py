from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Test")


#List of food items and their prices (In $)
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

image_list=[
    PhotoImage(file="images/%d.png" % i)
    for i in range(0,6)
]

customer_name = ttk.Label(root, text="Customer Name:")
customer_name.grid(row=1, column=0, padx=10, pady=3)
customer_input = ttk.Entry(root)
customer_input.grid(row=1, column=1, padx=10, pady=10, sticky="WE")
#check_validity()
#if len(customer_name) == 0:
    #for char in customer_name:
      #if not char.isalpha():
          #Label(main_window, fg="red", text="*Name Required").grid(column=2, row=2)
       

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


for i in range(len(price_list)):
    image_label = Label(root, image=image_list[i], height=150, width=200, padx=20)
    image_label.grid(row=4+2*i, column=2)

# Label and entry box to display the total at the end of the code
total_label = ttk.Label(root, text="Total:")
total_label.grid(row=100, column=0, padx=10, pady=3)

total_input = ttk.Entry(root)
total_input.grid(row=100, column=1, padx=10, pady=10, sticky="WE")






#Calculates the total price  based on the price_list (taken from the multidimentianl list) and from the user input of how much they want to order from amount_list
def take_order():
    total_price = 0
    for i in range(len(price_list)):
        value = amount_list[i].get()
        total_price += int(value) * float(price_list[i][1])
                                           


    total_input.insert(0, total_price)




def check_validity():
    if len(customer_name) == 0:
        for char in customer_name:
              if not char.isalpha():
                  Label(main_window, fg="red", text="*Name Required").grid(column=2, row=2)

submit_button = ttk.Button(root, text="Submit order", command=take_order)
submit_button.grid(row=200, column=5, padx=10, pady=10)

exit_button = ttk.Button(root, text="Exit", command=exit)
exit_button.grid(row=220, column=5, padx=10, pady=10)  

root.mainloop()
