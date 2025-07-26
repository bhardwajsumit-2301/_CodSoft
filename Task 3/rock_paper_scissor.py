import random
import tkinter as tk
from tkinter import messagebox

game_options = ['rock', 'paper', 'scissors']
option_symbols = {
    'rock': '✊',
    'paper': '✋',
    'scissors': '✌️'
}

option_colors = {
    'rock': '#6EC1E4',        # Soft Blue
    'paper': '#A8E6CF',       # Mint Green
    'scissors': '#FF8C94'     # Rosy Red
}

active_colors = {
    'rock': '#4AA5C9',
    'paper': '#87D6BA',
    'scissors': '#FF6B7B'
}

exit_button_color = '#FFD166'  # Soft Yellow

class RockPaperScissorsApp:
    def __init__(self, root_window):
        self.root = root_window
        self.root.title("Rock, Paper, Scissors Game")

        self.player_score = 0
        self.cpu_score = 0

        self.title_label = tk.Label(self.root, text="Welcome to Rock, Paper, Scissors!", font=("Arial", 16))
        self.title_label.pack(pady=10)

        self.instruction_label = tk.Label(self.root, text="Choose rock, paper, or scissors to play.", font=("Arial", 12))
        self.instruction_label.pack(pady=5)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        self.rock_button = tk.Button(
            self.button_frame,
            text=f"{option_symbols['rock']} Rock",
            width=12,
            font=("Arial", 14, "bold"),
            bg=option_colors['rock'],
            activebackground=active_colors['rock'],
            command=lambda: self.play_round('rock')
        )
        self.rock_button.grid(row=0, column=0, padx=5)

        self.paper_button = tk.Button(
            self.button_frame,
            text=f"{option_symbols['paper']} Paper",
            width=12,
            font=("Arial", 14, "bold"),
            bg=option_colors['paper'],
            activebackground=active_colors['paper'],
            command=lambda: self.play_round('paper')
        )
        self.paper_button.grid(row=0, column=1, padx=5)

        self.scissors_button = tk.Button(
            self.button_frame,
            text=f"{option_symbols['scissors']} Scissors",
            width=12,
            font=("Arial", 14, "bold"),
            bg=option_colors['scissors'],
            activebackground=active_colors['scissors'],
            command=lambda: self.play_round('scissors')
        )
        self.scissors_button.grid(row=0, column=2, padx=5)

        self.player_choice_label = tk.Label(self.root, text="You chose: ", font=("Arial", 12))
        self.player_choice_label.pack(pady=2)

        self.cpu_choice_label = tk.Label(self.root, text="Computer chose: ", font=("Arial", 12))
        self.cpu_choice_label.pack(pady=2)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 14, "bold"))
        self.result_label.pack(pady=5)

        self.score_label = tk.Label(self.root, text="Score => You: 0 | Computer: 0", font=("Arial", 12))
        self.score_label.pack(pady=10)

        self.exit_button = tk.Button(
            self.root,
            text="Exit",
            width=10,
            bg=exit_button_color,
            font=("Arial", 12, "bold"),
            command=self.quit_game
        )
        self.exit_button.pack(pady=5)

        for button in [self.rock_button, self.paper_button, self.scissors_button]:
            button.bind("<Enter>", self.on_hover)
            button.bind("<Leave>", self.on_leave)

    def on_hover(self, event):
        event.widget.config(relief=tk.SUNKEN, bd=4)

    def on_leave(self, event):
        event.widget.config(relief=tk.RAISED, bd=2)

    def decide_winner(self, player_choice, cpu_choice):
        if player_choice == cpu_choice:
            return "tie"
        elif (player_choice == 'rock' and cpu_choice == 'scissors') or \
             (player_choice == 'scissors' and cpu_choice == 'paper') or \
             (player_choice == 'paper' and cpu_choice == 'rock'):
            return "player"
        else:
            return "cpu"

    def play_round(self, player_choice):
        cpu_choice = random.choice(game_options)

        self.player_choice_label.config(
            text=f"You chose: {option_symbols[player_choice]} {player_choice.capitalize()}"
        )
        self.cpu_choice_label.config(
            text=f"Computer chose: {option_symbols[cpu_choice]} {cpu_choice.capitalize()}"
        )

        result = self.decide_winner(player_choice, cpu_choice)

        if result == "tie":
            self.result_label.config(text="It's a tie!", fg="blue")
        elif result == "player":
            self.result_label.config(text="You win this round!", fg="green")
            self.player_score += 1
        else:
            self.result_label.config(text="Computer wins this round!", fg="red")
            self.cpu_score += 1

        self.score_label.config(
            text=f"Score => You: {self.player_score} | Computer: {self.cpu_score}"
        )

    def quit_game(self):
        final_message = f"Final Score:\nYou: {self.player_score} | Computer: {self.cpu_score}\nThanks for playing!"
        messagebox.showinfo("Game Over", final_message)
        self.root.destroy()


if __name__ == "__main__":
    app_window = tk.Tk()
    game_app = RockPaperScissorsApp(app_window)
    app_window.mainloop()
