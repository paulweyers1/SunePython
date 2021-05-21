from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Test")

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

for i in range(len(price_list)):
    row = 1+10*i
    label = ttk.Label(root, text=price_list[i][0])
    label.grid(row=row, column=0, padx=10,pady=3)

    amount_input = ttk.Entry(root)
    amount_input.grid(row=row, column=1, padx=10, pady=10, sticky="WE")
    amount_list.append(amount_input)

total_label = ttk.Label(root, text="Total $:")
total_label.grid(row=100, column=0, padx=10, pady=3)

total_input = ttk.Entry(root)
total_input.grid(row=100, column=1, padx=10, pady=10, sticky="WE")

def take_order():
    total_price = 0
    for i in range(len(price_list)):
        value = amount_list[i].get()
        total_price += int(value) * float(price_list[1][1])

            

    total_input.insert(0, total_price)

submit_button = ttk.Button(root, text="Submit order", command=take_order)
submit_button.grid(row=1, column=5, padx=10, pady=10)

root.mainloop()

