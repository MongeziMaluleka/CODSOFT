import tkinter as tk
from PIL import Image, ImageTk
import random

# Paths to image files for the game buttons
image_paths = [
    "/home/shinigami/CODSOFT/CODSOFT/RPSgame/images/paper.png",
    "/home/shinigami/CODSOFT/CODSOFT/RPSgame/images/rock.png",
    "/home/shinigami/CODSOFT/CODSOFT/RPSgame/images/scissors.png"
]
# Labels for each game button
button_texts = ["paper", "rock", "scissors"]

class WelcomeWindow:
    def __init__(self, master, show_page):
        self.frame = tk.Frame(master)  # Container for widgets
        self.label = tk.Label(self.frame, text="Welcome to Rock Paper Scissors")
        self.label.pack(pady=10)  # Place label in frame with padding
        self.start_game_button = tk.Button(self.frame, text="START GAME", command=lambda: show_page(1))
        self.start_game_button.pack()  # Start button
        self.instructions_button = tk.Button(self.frame, text="VIEW INSTRUCTIONS", command=lambda: show_page(2))
        self.instructions_button.pack()  # Instruction button

    def pack(self):
        self.frame.pack()  # Display the frame

    def pack_forget(self):
        self.frame.pack_forget()  # Hide the frame

class GameSelectionWindow:
    def __init__(self, master, show_page):
        self.master = master
        self.show_page = show_page
        self.frame = tk.Frame(master)
        self.label = tk.Label(self.frame, text="Make your choice:")
        self.label.pack(pady=10)
        self.buttons = []
        for i, text in enumerate(button_texts):
            image = Image.open(image_paths[i])  # Open image file
            photo = ImageTk.PhotoImage(image)  # Convert to PhotoImage
            # Create a button with an image and text on top
            button = tk.Button(self.frame, image=photo, text=text, compound="top", command=lambda idx=i: self.make_choice(idx))
            button.image = photo  # Keep a reference to avoid garbage collection
            button.pack(side="left", padx=10)
            self.buttons.append(button)

    def make_choice(self, player_choice):
        comp_choice = random.randint(0, 2)  # Computer random choice
        result = compare_choices(button_texts[player_choice], button_texts[comp_choice])
        self.show_page(3, player_choice, comp_choice, result)

    def pack(self):
        self.frame.pack()

    def pack_forget(self):
        self.frame.pack_forget()

class InstructionsWindow:
    def __init__(self, master, show_page):
        self.frame = tk.Frame(master)
        instructions_text = (
            "Welcome to Rock Paper Scissors!\n\n"
            "Instructions:\n"
            "- Choose one of the three options: Rock, Paper, or Scissors.\n"
            "- Rock crushes Scissors, Scissors cut Paper, and Paper covers Rock.\n"
            "- The computer will also choose one of the three options at random.\n"
            "- The winner is determined by comparing your choice and the computer's choice.\n\n"
            "How to Play:\n"
            "- Click on the image of Rock, Paper, or Scissors to make your choice.\n"
            "- After selecting, you will see the computer's choice and the result of the match.\n"
            "- You can play as many times as you like by pressing 'Play Again'.\n"
            "- Press 'BACK' to return to the main menu at any time.\n\n"
            "Good luck and have fun!"
        )
        self.label = tk.Label(self.frame, text=instructions_text, justify=tk.LEFT)
        self.label.pack(pady=20)
        self.back_button = tk.Button(self.frame, text="BACK", command=lambda: show_page(0))
        self.back_button.pack()

    def pack(self):
        self.frame.pack()

    def pack_forget(self):
        self.frame.pack_forget()

class ResultWindow:
    def __init__(self, master, show_page):
        self.frame = tk.Frame(master)
        self.label = tk.Label(self.frame)
        self.label.pack(pady=20)
        self.back_button = tk.Button(self.frame, text="Play Again", command=lambda: show_page(1))
        self.back_button.pack()

    def update_result(self, player_choice, comp_choice, result):
        self.label.config(text=f"Your choice: {button_texts[player_choice]}\nComputer's choice: {button_texts[comp_choice]}\nResult: {result}")

    def pack(self):
        self.frame.pack()

    def pack_forget(self):
        self.frame.pack_forget()

def compare_choices(player, computer):
    # Determine the winner based on the game rules
    if player == computer:
        return "It's a tie!"
    elif (player == "rock" and computer == "scissors") or \
         (player == "paper" and computer == "rock") or \
         (player == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    root = tk.Tk()
    root.title("Rock Paper Scissors Game")
    root.geometry("750x330")  # Set initial window size

    windows = [
        WelcomeWindow(root, lambda idx: show_page(idx)),
        GameSelectionWindow(root, lambda idx, p=None, c=None, r=None: show_page(idx, p, c, r)),
        InstructionsWindow(root, lambda idx: show_page(idx)),
        ResultWindow(root, lambda idx: show_page(idx))
    ]

    def show_page(index, player_choice=None, comp_choice=None, result=None):
        for window in windows:
            window.pack_forget()  # Hide all windows
        if index == 3 and player_choice is not None and comp_choice is not None and result is not None:
            windows[index].update_result(player_choice, comp_choice, result)
        windows[index].pack()  # Show the current window

    show_page(0)  # Start at the welcome page
    root.mainloop()

if __name__ == "__main__":
    main()
