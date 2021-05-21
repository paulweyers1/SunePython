from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Test")


class Food_order:

    def __init__(self, parent):

        self.price_list = [["Chicken panini", 4.80], ["Veggie panini", 4.80] , ["Chicken burger",4.50] , ["turkish  warp" , 4.50]]
        amount_list = []
    
       
    def take_order(self):
        total_price = 0
        for i in range(len(self.price_list)):
            value = amount_list[i].get()
            total_price += int(value) * float(price_list[i][1])

        total_input.insert(0, total_price)

    submit_button = ttk.Button(root, text="Submit Order", command=take_order)
    submit_button.grid(row=3, column=0, padx=10, pady=10)


            #try:
                #if self.hot_food_entry.get() == "":
                    #self.miso_cost = 0
               # else:
                  #  self.hot_food_cost = int(self.hot_food_entry.get())*float(self.price_list[0][1])
            #except:
                #tkinter.messagebox.showinfo('Error')

            #try:
               # if self.roll_entry.get() == "":
                    #self.roll_cost = 0
               # else:
                    #self.roll_cost = int(self.roll_entry.get())*float(self.price_list[1][1])
           # except:
                #tkinter.messagebox.showinfo('Error')

        #self.cost_of_food = self.hot_food_cost + self.roll_cost
        
        #Print is testing the calculation in shell, will remove after the programm finished
       # print(self.customer_entry.get(), self.cost_of_food)
       # ttk.Entry.insert(self.total_entry, 0, self.cost_of_food)


#Run the mainloop
root = Tk()
root.title("Food Order App")
food_order = Food_order(root)
root.mainloop()
