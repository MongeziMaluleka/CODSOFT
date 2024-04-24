import tkinter as tk
from tkinter import messagebox
import random

class FinalWindow(tk.Toplevel):
    """A popup window that displays the generated password."""
    def __init__(self, parent, password):
        super().__init__(parent)
        self.title("Final")
        self.geometry("300x150")
        self.password = password

        # Label to display the generated password
        password_label = tk.Label(self, text=f"Generated Password:\n{self.password}")
        password_label.pack(pady=20)

        # Button for copying the password to the clipboard
        copy_button = tk.Button(self, text="Copy to Clipboard", command=self.copy_to_clipboard)
        copy_button.pack()

    def copy_to_clipboard(self):
        """Copy the generated password to the clipboard and display confirmation."""
        self.clipboard_clear()  # Clear the clipboard contents
        self.clipboard_append(self.password)  # Append new password to the clipboard
        messagebox.showinfo("Clipboard", "Password copied to clipboard!")

class InputWindow(tk.Toplevel):
    """A window for user input to specify password generation criteria."""
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Password Length")
        self.geometry("300x250")
        self.parent = parent

        # Setup user input fields for password criteria
        length_label = tk.Label(self, text="Enter password length:")
        length_label.pack()
        self.length_input = tk.Entry(self)
        self.length_input.pack()

        alphabets_label = tk.Label(self, text="Enter number of alphabets:")
        alphabets_label.pack()
        self.alphabets_entry = tk.Entry(self)
        self.alphabets_entry.pack()

        symbols_label = tk.Label(self, text="Enter number of symbols:")
        symbols_label.pack()
        self.symbols_entry = tk.Entry(self)
        self.symbols_entry.pack()

        numbers_label = tk.Label(self, text="Enter number of numbers:")
        numbers_label.pack()
        self.numbers_entry = tk.Entry(self)
        self.numbers_entry.pack()

        # Button to generate password based on the specified criteria
        generate_button = tk.Button(self, text="Generate Password", command=self.validate_input)
        generate_button.pack()

    def validate_input(self):
        """Validate inputs and generate password if valid, else show error."""
        try:
            # Convert entries from string to integer and validate total length
            alphabets = int(self.alphabets_entry.get())
            symbols = int(self.symbols_entry.get())
            length = int(self.length_input.get())
            numbers = int(self.numbers_entry.get())
            if alphabets + symbols + numbers != length:
                messagebox.showwarning("Invalid Input", "Sum of numbers, symbols, and alphabets should equal the total length.")
            else:
                password = generate_password(length, alphabets, symbols, numbers)
                self.open_final_window(password)
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter valid numbers for symbols, numbers, and alphabets.")

    def open_final_window(self, password):
        """Open the final window displaying the generated password and hide this window."""
        self.withdraw()
        final_window = FinalWindow(self.parent, password)
        final_window.grab_set()

def generate_password(length, alphabets_count, symbols_count, numbers_count):
    """Generate a random password based on specified criteria."""
    alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%^&*()-_=+[{]}|;:',<.>/?`~"
    chosen_alphabets = "".join(random.choice(alphabets) for _ in range(alphabets_count))
    chosen_numbers = "".join(random.choice(numbers) for _ in range(numbers_count))
    chosen_symbols = "".join(random.choice(symbols) for _ in range(symbols_count))
    easy_password = list(chosen_numbers + chosen_alphabets + chosen_symbols)
    random.shuffle(easy_password)
    return "".join(easy_password)

class WelcomeScreen(tk.Tk):
    """Initial welcome screen with an option to start password generation."""
    def __init__(self):
        super().__init__()
        self.title("Welcome to PassGen")
        self.geometry("450x500")
        self.configure(background="#3498db")

        # Display labels and setup the interface
        welcome_label1 = tk.Label(self, text="Welcome to", font=("Arial", 30, "bold"), foreground="white", background="#3498db")
        welcome_label1.pack()

        passgen_label1 = tk.Label(self, text="PassGen!", font=("Arial", 40, "bold"), foreground="white", background="#3498db")
        passgen_label1.pack()

        description_label1 = tk.Label(self, text="Your Secure Password Generator", font=("Arial", 20), foreground="white", background="#3498db")
        description_label1.pack()

        # Button to transition to password generation
        generate_button = tk.Button(self, text="START", command=self.transition_to_genpass)
        generate_button.pack()

    def transition_to_genpass(self):
        """Transition to the password generation window and hide this window."""
        input_window = InputWindow(self)
        self.withdraw()
        self.wait_window(input_window)
        self.deiconify()

if __name__ == "__main__":
    # Main execution loop that creates the welcome screen and starts the application
    welcome_screen = WelcomeScreen()
    welcome_screen.mainloop()
