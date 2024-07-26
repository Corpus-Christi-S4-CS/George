#Import the library
from tkinter import *
import time

#Create an instance of tkinter frame
win= Tk()

#Define the geometry of window
win.geometry("800x600")

#Create a canvas object
c= Canvas(win,width=800, height=600, bg = "white")
c.pack()

# positions starts from top left corner
light_1 = c.create_rectangle(600,300,700,550,fill='black')
light_2 = c.create_rectangle(450,300,550,550,fill='black')

#Draw an Oval in the canvas
radius = 25 
x_center_top = 650
x_center_left = 500
y_center_top = 350
y_center_middle = 425
y_center_bottom = 500


while True:
    
    top_light = c.create_oval(x_center_top-radius,y_center_top-radius,
                        x_center_top+radius,y_center_top+radius, fill = "red")
    top_light = c.create_oval(x_center_top-radius,y_center_middle-radius,
                        x_center_top+radius,y_center_middle+radius, fill = "black")
    op_light = c.create_oval(x_center_top-radius,y_center_bottom-radius,
                        x_center_top+radius,y_center_bottom+radius, fill = "black")
    
    top_light = c.create_oval(x_center_left-radius,y_center_top-radius,
                        x_center_left+radius,y_center_top+radius, fill = "black")
    top_light = c.create_oval(x_center_left-radius,y_center_middle-radius,
                        x_center_left+radius,y_center_middle+radius, fill = "black")
    top_light = c.create_oval(x_center_left-radius,y_center_bottom-radius,
                        x_center_left+radius,y_center_bottom+radius, fill = "green")
    
    win.update()
    time.sleep(3)

    top_light = c.create_oval(x_center_top-radius,y_center_top-radius,
                        x_center_top+radius,y_center_top+radius, fill = "red")
    top_light = c.create_oval(x_center_top-radius,y_center_middle-radius,
                        x_center_top+radius,y_center_middle+radius, fill = "black")
    op_light = c.create_oval(x_center_top-radius,y_center_bottom-radius,
                        x_center_top+radius,y_center_bottom+radius, fill = "black")
    
    top_light = c.create_oval(x_center_left-radius,y_center_top-radius,
                        x_center_left+radius,y_center_top+radius, fill = "black")
    top_light = c.create_oval(x_center_left-radius,y_center_middle-radius,
                        x_center_left+radius,y_center_middle+radius, fill = "orange")
    top_light = c.create_oval(x_center_left-radius,y_center_bottom-radius,
                        x_center_left+radius,y_center_bottom+radius, fill = "black")
    
    win.update()
    time.sleep(1)

    top_light = c.create_oval(x_center_top-radius,y_center_top-radius,
                        x_center_top+radius,y_center_top+radius, fill = "black")
    top_light = c.create_oval(x_center_top-radius,y_center_middle-radius,
                        x_center_top+radius,y_center_middle+radius, fill = "black")
    op_light = c.create_oval(x_center_top-radius,y_center_bottom-radius,
                        x_center_top+radius,y_center_bottom+radius, fill = "green")
    
    top_light = c.create_oval(x_center_left-radius,y_center_top-radius,
                        x_center_left+radius,y_center_top+radius, fill = "red")
    top_light = c.create_oval(x_center_left-radius,y_center_middle-radius,
                        x_center_left+radius,y_center_middle+radius, fill = "black")
    top_light = c.create_oval(x_center_left-radius,y_center_bottom-radius,
                        x_center_left+radius,y_center_bottom+radius, fill = "black")
    
    win.update()
    time.sleep(3)

    top_light = c.create_oval(x_center_top-radius,y_center_top-radius,
                        x_center_top+radius,y_center_top+radius, fill = "black")
    top_light = c.create_oval(x_center_top-radius,y_center_middle-radius,
                        x_center_top+radius,y_center_middle+radius, fill = "orange")
    op_light = c.create_oval(x_center_top-radius,y_center_bottom-radius,
                        x_center_top+radius,y_center_bottom+radius, fill = "black")
    
    top_light = c.create_oval(x_center_left-radius,y_center_top-radius,
                        x_center_left+radius,y_center_top+radius, fill = "red")
    top_light = c.create_oval(x_center_left-radius,y_center_middle-radius,
                        x_center_left+radius,y_center_middle+radius, fill = "black")
    top_light = c.create_oval(x_center_left-radius,y_center_bottom-radius,
                        x_center_left+radius,y_center_bottom+radius, fill = "black")
    
    win.update()
    time.sleep(1)

win.mainloop()