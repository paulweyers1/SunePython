#Login program

from tkinter import *
from tkinter import ttk
import tkinter.messagebox

# Class checks sets up the input boxes, verfiese the user and password and opens the order window
class UserChecker:

        def __init__(self, parent):
            self.username_input = StringVar()
            self.password_input = StringVar()

            self.login_frame = tkinter.LabelFrame(parent, text="", fg="white", bg="white", bd=4)

            self.login_frame.grid(row=2, column=0, padx=10, pady=10, sticky="NSEW")

            self.title_label = Label(parent, font=('arial',20,'bold'), text="Kapiti College Canteen ", fg="maroon", bg="white")
            self.title_label.grid(row=0)

            self.title_2_label = Label(parent, font=('arial', 18,'bold'), text="Order Login", fg="maroon", bg="white")
            self.title_2_label.grid(row=1)

            self.label1 = Label(self.login_frame, font=('arial',10), text="Username:", bg="white", fg="grey")
            self.label2 = Label(self.login_frame, font=('arial',10), text="Password:", bg="white", fg="grey")
            self.label1.grid(row=0, column=0)
            self.label2.grid(row=1, column=0)

            self.entry1= Entry(self.login_frame, textvariable=self.username_input, bg="grey", fg="white")
            self.entry2= Entry(self.login_frame, textvariable=self.password_input, show="*", bg="grey", fg="white")
            self.entry1.grid(row=0, column=1)
            self.entry2.grid(row=1, column=1)

            self.login_button = Button(self.login_frame, text="Login", command=self.login_check, bg="white")
            self.login_button.grid(row=5, column=1)

            self.entry1.focus_set()

        # open the order window
        def login_and_order(self):
            root.destroy()
            import AssesmentV6

        # Check for a valid user and password
        def login_check(self):
            success = 0
            with open('accounts.txt', 'r') as accounts_file:

                for line in accounts_file:
                    first_name, last_name, username, password = line.strip().split(',')
                    if self.username_input.get() == username and self.password_input.get() == password:
                        success = 1
                        break

            if success == 1:
                tkinter.messagebox.showinfo("Welcome!", "Welcome to Kapiti College Canteen App. Click Ok, add your name and select items for your order")
                self.login_and_order()

            else:
                tkinter.messagebox.showinfo("Authentication Failed", "Either the user name or password you have entered is incorrect. please try again.")
                self.username_input.set("")
                self.password_input.set("")
                self.entry1.focus_set()


# Main Routine
if __name__ == "__main__":
    root = Tk()
    root.title("Order Login Page")
    root.configure(background="white")
    checker=UserChecker(root)
    root.mainloop()
