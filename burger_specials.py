
import tkinter as tk
from tkinter import messagebox

# Initialize main window
root = tk.Tk()
root.title("Burger Specials")
root.geometry("400x400")

# Function to update label with burger info
def show_burger(burger_type):
    label.config(text=f"{burger_type} selected")

# Function for confirmation
def confirm_selection():
    messagebox.showinfo("Confirmation", "Burger selected successfully!")

# Function to exit
def exit_app():
    root.destroy()

# Buttons for selecting burgers
btn_prime = tk.Button(root, text="Prime Beef", command=lambda: show_burger("Prime Beef"))
btn_prime.pack()

btn_veggie = tk.Button(root, text="Veggie", command=lambda: show_burger("Veggie"))
btn_veggie.pack()

# Label to display selected burger info
label = tk.Label(root, text="Select a burger")
label.pack()

# Confirm and Exit buttons
btn_confirm = tk.Button(root, text="Confirm", command=confirm_selection)
btn_confirm.pack()

btn_exit = tk.Button(root, text="Exit", command=exit_app)
btn_exit.pack()

root.mainloop()


