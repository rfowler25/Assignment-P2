import tkinter as tk
from tkinter import messagebox

class PayrollCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Payroll Calculator")
        self.root.geometry("400x300")

        # Labels and Entry
        tk.Label(root, text="Gross Pay:").grid(row=0, column=0, padx=10, pady=10)
        self.gross_pay_entry = tk.Entry(root)
        self.gross_pay_entry.grid(row=0, column=1, padx=10, pady=10)
        
        # Labels for results
        self.fica_label = tk.Label(root, text="FICA: ")
        self.fica_label.grid(row=1, column=0, padx=10, pady=5)
        
        self.federal_label = tk.Label(root, text="Federal Tax: ")
        self.federal_label.grid(row=2, column=0, padx=10, pady=5)
        
        self.state_label = tk.Label(root, text="State Tax: ")
        self.state_label.grid(row=3, column=0, padx=10, pady=5)
        
        self.net_income_label = tk.Label(root, text="Net Paycheck Income: ")
        self.net_income_label.grid(row=4, column=0, padx=10, pady=5)
        
        # Buttons
        self.compute_button = tk.Button(root, text="Compute Taxes", command=self.compute_taxes)
        self.compute_button.grid(row=5, column=0, pady=10)
        
        self.clear_button = tk.Button(root, text="Clear", command=self.clear_fields)
        self.clear_button.grid(row=5, column=1, pady=10)
        
        self.exit_button = tk.Button(root, text="Exit", command=root.quit)
        self.exit_button.grid(row=6, column=0, columnspan=2, pady=10)

    def compute_taxes(self):
        try:
            cdecFica = 0.0765
            cdecFed = 0.22
            cdecState = 0.04
            
            gross_pay = float(self.gross_pay_entry.get())
            if gross_pay < 0:
                raise ValueError("Gross Pay must be a positive number.")
            
            fica = gross_pay * cdecFica
            federal = gross_pay * cdecFed
            state = gross_pay * cdecState
            net_income = gross_pay - (fica + federal + state)
            
            self.fica_label.config(text=f"FICA: ${fica:.2f}")
            self.federal_label.config(text=f"Federal Tax: ${federal:.2f}")
            self.state_label.config(text=f"State Tax: ${state:.2f}")
            self.net_income_label.config(text=f"Net Paycheck Income: ${net_income:.2f}")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid numeric value for Gross Pay.")
            self.clear_fields()
    
    def clear_fields(self):
        self.gross_pay_entry.delete(0, tk.END)
        self.fica_label.config(text="FICA: ")
        self.federal_label.config(text="Federal Tax: ")
        self.state_label.config(text="State Tax: ")
        self.net_income_label.config(text="Net Paycheck Income: ")
        self.gross_pay_entry.focus()

if __name__ == "__main__":
    root = tk.Tk()
    app = PayrollCalculator(root)
    root.mainloop()
