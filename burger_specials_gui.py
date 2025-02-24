import tkinter as tk
from tkinter import messagebox

class BurgerOrderGUI:
    def __init__(self, root):
        # Setup the main window
        self.root = root
        self.root.title("Burger Specials")  # Window title
        self.root.geometry("400x400")  # Set window size

        # Label for burger selection
        self.burger_label = tk.Label(self.root, text="Choose Your Burger:", font=("Arial", 14))
        self.burger_label.grid(row=0, column=0, padx=10, pady=10)

        # Create a StringVar to store the selected burger type (Prime Beef or Veggie)
        self.burger_var = tk.StringVar(value="Prime Beef")  # Default selection

        # Radio buttons for burger types
        self.prime_beef_button = tk.Radiobutton(self.root, text="Prime Beef", variable=self.burger_var, value="Prime Beef", font=("Arial", 12))
        self.vegetarian_button = tk.Radiobutton(self.root, text="Veggie", variable=self.burger_var, value="Veggie", font=("Arial", 12))

        # Place radio buttons on grid
        self.prime_beef_button.grid(row=1, column=0, padx=10, pady=5)
        self.vegetarian_button.grid(row=2, column=0, padx=10, pady=5)

        # Label to display the burger image (if required)
        try:
            self.burger_image = tk.PhotoImage(file="burger.png")  # Replace with your image path
            self.image_label = tk.Label(self.root, image=self.burger_image)
            self.image_label.grid(row=3, column=0, padx=10, pady=10)
        except tk.TclError:
            self.image_label = None  # If no image, ignore it

        # Button to confirm the order
        self.confirm_button = tk.Button(self.root, text="Confirm Selection", command=self.confirm_order, font=("Arial", 14))
        self.confirm_button.grid(row=4, column=0, padx=10, pady=10)

    def confirm_order(self):
        """This function will handle the order confirmation when the button is clicked."""
        selection = self.burger_var.get()  # Get the selected burger type
        messagebox.showinfo("Order Confirmation", f"You selected the {selection} burger!")  # Display a confirmation message

# Main execution
if __name__ == "__main__":
    root = tk.Tk()  # Create the Tkinter window
    app = BurgerOrderGUI(root)  # Instantiate the GUI application
    root.mainloop()  # Run the main loop to display the window
