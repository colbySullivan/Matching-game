
import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox
from PIL import ImageTk, Image  

root = Tk()
root.title('Tile Matching Game!')
root.geometry("500x550") 
global winner, matches
# Set winner counter to 0
winner = 0

# Photos for the Buttons
image_list = ["Mickey (2).png",
             "player.png",
             "goomba.png",
             "dannysprite.png",
             "Mickey (2).png",
             "Mickey (2).png"]


# Creating Matches
matches = [1,1,2,2,3,3,4,4,5,5,6,6]
random.shuffle(matches)
# Shuffles the Matches
print(matches)

string_list = {}
for x in matches:
    fname = "Mickey (2).png"
    image_tk = ImageTk.PhotoImage(Image.open(image_list[x-1]))
    string_list[x] = image_tk

# Create Button Frame
my_frame = Frame(root)
my_frame.pack(pady=10)

# Variables
count = 0 
answer_list = []
answer_dict = {}

# Reset the Game
def reset():
    global matches, winner
    winner = 0
    # Creating Matches
    matches = [1,1,2,2,3,3,4,4,5,5,6,6]
    random.shuffle(matches) 
    # Shuffles the Matches
    print(matches)

    # Reset label
    my_label.config(text="")

    # Reset Tiles
    my_label.config(text="You Win!!")
    button_list = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11]
    # Look Through Buttons and Change Colors
    for button in button_list:
        button.config(text= " ", bg="SystemButtonFace", state="normal")


    
# Create winner function
def win():
    my_label.config(text="You Win!!")
    button_list = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11]
    # Look Through Buttons and Change Colors
    for button in button_list:
        button.config(bg="blue")

     
# Function for Clicking Buttons
def button_click(b, number):
    global count, answer_list, answer_dict, winner, string_list

    if b["text"] == ' ' and count < 2:
        b.configure(image=string_list[matches[number]], height=60, width=60)
        b["text"] = matches[number]
        # Add number to answer list
        answer_list.append(number)
        # Add button and number to Answer Dictionary
        answer_dict[b] = matches[number]
        # Increment our Counter
        count += 1
        
    # Determines correct or not
    if len(answer_list) == 2:
        if matches[answer_list[0]] == matches[answer_list[1]]:
            # my_label.config(text="MATCH!")
            for key in answer_dict:
                key["state"] = "disabled"
            count = 0
            answer_list = []
            answer_dict = {}
            # Increment outr winner counter
            winner += 1
            if winner == 6:
                win()
        else:   
            # my_label.config(text="DOH!")
            count = 0
            answer_list = []
            # Pop up box
            messagebox.showinfo("Incorrect!", "Incorrect")

            # Reset Buttons
            for key in answer_dict:
                key.configure(image='', text=' ', font=("Helvetica", 20), height=3, width=6, relief="raised")
                key["text"] = " "

                answer_dict = {}


# Define Buttons
b0 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b0, 0), relief="raised")
b1 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b1, 1), relief="raised")
b2 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b2, 2), relief="raised")
b3 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b3, 3), relief="raised")
b4 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b4, 4), relief="raised")
b5 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b5, 5), relief="raised")
b6 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b6, 6), relief="raised")
b7 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b7, 7), relief="raised")
b8 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b8, 8), relief="raised")
b9 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b9, 9), relief="raised")
b10 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b10, 10), relief="raised")
b11 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(b11, 11), relief="raised")

# Grid our Buttons
b0.grid(row=0, column=0)
b1.grid(row=0, column=1)
b2.grid(row=0, column=2)
b3.grid(row=0, column=3)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)
b7.grid(row=1, column=3)

b8.grid(row=2, column=0)
b9.grid(row=2, column=1)
b10.grid(row=2, column=2)
b11.grid(row=2, column=3)

my_label = Label(root, text="")
my_label.pack(pady=20)

# Create Menu
my_menu = Menu(root)
root.config(menu = my_menu)

# Create an options drpodown Menu
option_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu= option_menu)
option_menu.add_command(label="Reset Game", command=reset)
option_menu.add_separator()
option_menu.add_command(label="Exit Game", command=root.quit)

root.mainloop()
