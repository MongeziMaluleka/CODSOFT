import tkinter as tk

class BasicCalculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Basic Calculator")
        self.master.geometry("300x300")  # Increased the size of the window

        # Entry field for numbers
        self.entry = tk.Entry(master, font=('Arial', 14), width=22)  # Bigger font and slightly wider
        self.entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Button for addition
        self.add_button = tk.Button(master, text="+", font=('Arial', 14), width=8, height=2, command=lambda: self.append_operator('+'))
        self.add_button.grid(row=1, column=0, padx=10, pady=5)

        # Button for subtraction
        self.subtract_button = tk.Button(master, text="-", font=('Arial', 14), width=8, height=2, command=lambda: self.append_operator('-'))
        self.subtract_button.grid(row=1, column=1, padx=10, pady=5)

        # Button for multiplication
        self.multiply_button = tk.Button(master, text="*", font=('Arial', 14), width=8, height=2, command=lambda: self.append_operator('*'))
        self.multiply_button.grid(row=2, column=0, padx=10, pady=5)

        # Button for division
        self.divide_button = tk.Button(master, text="/", font=('Arial', 14), width=8, height=2, command=lambda: self.append_operator('/'))
        self.divide_button.grid(row=2, column=1, padx=10, pady=5)

        # Button to evaluate the expression
        self.equal_button = tk.Button(master, text="=", font=('Arial', 14), width=17, height=2, command=self.calculate_result)
        self.equal_button.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

        # Label to display the result
        self.label_result = tk.Label(master, text="Result: ", font=('Arial', 14))
        self.label_result.grid(row=4, column=0, columnspan=2, pady=10)

    def append_operator(self, operator):
        """Append an operator to the entry field."""
        current = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, f"{current}{operator}")

    def calculate_result(self):
        """Calculate the expression in the entry field."""
        try:
            result = eval(self.entry.get())
            self.label_result.config(text=f"Result: {result}")
        except Exception as e:
            self.label_result.config(text=f"Error: {str(e)}")
            self.entry.delete(0, tk.END)  # Clear the entry widget if there's an error

if __name__ == "__main__":
    root = tk.Tk()
    app = BasicCalculator(root)
    root.mainloop()
