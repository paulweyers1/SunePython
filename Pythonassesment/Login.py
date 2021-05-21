#Login program

from tkinter import *
from tkinter import ttk
import tkinter.messagebox



# Class checks sets up the input boxes

class UserChecker:

        def __init__(self, parent):
            self.username_input = StringVar()
            self.password_input = StringVar()

            self.login_frame = ttk.LabelFrame(parent, text="Login")
            self.login_frame.grid(row=2, column=0, padx=10, pady=10, sticky="NSEW")

            self.title_label = Label(parent, font=('arial',20,'bold'), text="Kapiti college Canteen ", fg="maroon")
            self.title_label.grid(row=0)

            self.title_2_label = Label(parent, font=('arial', 18,'bold'), text="Order Login Page", fg="maroon")
            self.title_2_label.grid(row=1)

            self.label1 = Label(self.login_frame, font=('arial',10), text="Username:")
            self.label2 = Label(self.login_frame, font=('arial',10), text="Password:")
            self.label1.grid(row=0, column=0)
            self.label2.grid(row=1, column=0)

            self.entry1= Entry(self.login_frame, textvariable=self.username_input)
            self.entry2= Entry(self.login_frame, textvariable=self.password_input, show="*")
            self.entry1.grid(row=0, column=1)
            self.entry2.grid(row=1, column=1)

            self.login_button = Button(self.login_frame, text="Log in", command=self.login_check)
            self.login_button.grid(row=5, column=1)

        def login_and_order(self):
            root.destroy()
            import AssesmentV6
    
        def login_check(self):
                
            with open('accounts.txt', 'r') as accounts_file:

                for line in accounts_file:
                    first_name, last_name, username, password = line.strip().split(',')
                    if self.username_input.get() == username and self.password_input.get() == password:
                        tkinter.messagebox.showinfo("Welcome!")
                        self.login_and_order()
                    
                    else:
                        tkinter.messagebox.showinfo("Authentication  Failed")
                        self.username_input.set("")
                        self.password_input.set("")
                        break
    
#main Route
if __name__ == "__main__":
    root = Tk()   
    root.title("Login Page")
   

    checker=UserChecker(root)
    root.mainloop()
    
                    

