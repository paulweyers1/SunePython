from tkinter import *

class SlideShowItem:
    """ Stores the information for one image - title, caption and the image itself as a PhotoImage. """
    def __init__(self, title, photo_file, caption):
        self.title = title
        self.photo = PhotoImage(master=root, file = photo_file)
        self.caption = caption


class SlideShowGUI:

    def __init__(self, parent):
        self.slide_items = []

        self.slide_items.append(SlideShowItem("BLT", "images/0.png", "$3.80"))
        self.slide_items.append(SlideShowItem("Ham Salad sandwich", "images/1.png", "4.50"))
        self.slide_items.append(SlideShowItem("Veggie sandwich", "images/2.png", "4.50"))       
        self.slide_items.append(SlideShowItem("Chicken Panini", "images/3.png", "4.50"))
        self.slide_items.append(SlideShowItem("Hawaiian panini", "images/4.png", "4.50"))
        self.slide_items.append(SlideShowItem("Breakfast Burrito", "images/5.png", "4.50"))
        self.slide_items.append(SlideShowItem("Nachos", "images/6.png", "4.50"))
        self.slide_items.append(SlideShowItem("Wedges", "images/7.png", "4.50"))
        self.slide_items.append(SlideShowItem("Hash Browns", "images/8.png", "4.50"))
        self.slide_items.append(SlideShowItem("Garlic Bread", "images/9.png", "4.50"))
       
        self.btn_left = Button(parent, text = "<", command = self.moveLeft)
        self.btn_right = Button(parent, text = ">", command = self.moveRight)
        self.target = 0
        self.title_label = Label(parent, text = self.slide_items[0].title, font = ("Times", "10", "bold"))
        self.image_label = Label(parent, image = self.slide_items[0].photo, height = 150,
                                                                 width = 200, padx = 20)
        self.caption_label = Label(parent, text = self.slide_items[0].caption, font = ("Times", "12", "bold"))
        self.title_label.grid(row = 0, columnspan = 2)
        self.image_label.grid(row = 1, columnspan = 2)
        self.caption_label.grid(row = 2, columnspan = 2)
        self.btn_left.grid(row = 3, column = 0, sticky = W)
        self.btn_right.grid(row = 3, column = 1, sticky = E)
        parent.configure(bg = "white")

    def moveLeft(self):
        self.target -= 1
        if self.target < 0:
            self.target = len(self.slide_items)- 1
        self.title_label.configure(text = self.slide_items[self.target].title)
        self.image_label.configure(image = self.slide_items[self.target].photo)
        self.caption_label.configure(text = self.slide_items[self.target].caption)

    def moveRight(self):
        self.target += 1
        if self.target >= len(self.slide_items):
                self.target = 0
        self.title_label.configure(text = self.slide_items[self.target].title)
        self.image_label.configure(image = self.slide_items[self.target].photo)
        self.caption_label.configure(text = self.slide_items[self.target].caption)
        
        
#Main routine


root = Tk()
slide_show = SlideShowGUI(root)
root.geometry("200x245+0+0")
root.mainloop()

        
        
        
        
                                                    
                                
    
