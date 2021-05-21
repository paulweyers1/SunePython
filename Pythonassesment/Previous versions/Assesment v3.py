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

class UserChecker:
    def __init__(self, parent):
        self.username_input = StringVar()
        self.password_input = StringVar()

        self.login_frame = ttk.LabelFrame(parent, text="Login")
        self.login_frame.grid(row=2, column=0, padx=10, pady=10, sticky="NSEW")

        self.title_label = Label(parent, font=('arial',20,'bold'), text="Kapiti Sunshine Sushi", fg="maroon")
        self.title_label.grid(row=0)

        self.title_2_label = Label(parent, font=('arial', 18,'bold'), text="Order Login Page", fg="maroon")
        self.title_2_label.grid(row=1)

        self.label1 = Label(self.login_frame, font=('arial',10), text="Username:")
        self.label2 = Label(self.login_frame, font=('arial',10), text="Password:")
        self.label1.grid(row=0, column=0)
        self.label2.grid(row=1, column=0)

        self.entry1= Entry(self.login_frame, textvariable=self.username_input)
        self.entry2= Entry(self.login_frame, textvariable=self.password_input)
        self.entry1.grid(row=0, column=1)
        self.entry2.grid(row=1, column=1)

        self.login_button = Button(self.login_frame, text="Log in", command=self.login_check)
        self.login_button.grid(row=5, column=1)

    def login_check(self):
        root.destroy()
        import order










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
def take_order():
    total_price = 0
    for i in range(len(price_list)):
        value = amount_list[i].get()
        total_price += int(value) * float(price_list[i][1])
                                           


    total_input.insert(0, total_price)
        

submit_button = ttk.Button(root, text="Submit order", command=take_order)
submit_button.grid(row=200, column=5, padx=10, pady=10)

exit_button = ttk.Button(root, text="Exit", command=exit)
exit_button.grid(row=220, column=5, padx=10, pady=10)  

checker=UserChecker(root)
root.mainloop()

