import tkinter as tk
import random

# Initialize scores
user_score = 0
computer_score = 0

# Game logic
def play(user_choice):
    global user_score, computer_score

    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)

    result = ""
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper') or \
         (user_choice == 'Paper' and computer_choice == 'Rock'):
        user_score += 1
        result = "You win!"
    else:
        computer_score += 1
        result = "Computer wins!"

    result_label.config(
        text=f"Your choice: {user_choice}\nComputer's choice: {computer_choice}\n{result}"
    )
    score_label.config(
        text=f"Score - You: {user_score} | Computer: {computer_score}"
    )

# Reset scores
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Make your move!")
    score_label.config(text="Score - You: 0 | Computer: 0")

# GUI setup
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x300")
root.resizable(False, False)
root.configure(bg="lightgreen")  # Main background

# Title label
tk.Label(
    root, text="Rock, Paper, Scissors",
    font=("Helvetica", 16, "bold"),
    bg="yellow"
).pack(pady=10)

# Button frame
button_frame = tk.Frame(root, bg="lightgray")
button_frame.pack(pady=10)

# Colored buttons
tk.Button(button_frame, text="Rock", width=10, bg="saddlebrown", fg="white",
          command=lambda: play("Rock")).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Paper", width=10, bg="purple", fg="white",
          command=lambda: play("Paper")).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Scissors", width=10, bg="orange", fg="white",
          command=lambda: play("Scissors")).grid(row=0, column=2, padx=5)

# Result label
result_label = tk.Label(
    root, text="Make your move!",
    font=("Helvetica", 12),
    bg="red", fg="white"
)
result_label.pack(pady=20)

# Score label
score_label = tk.Label(
    root, text="Score - You: 0 | Computer: 0",
    font=("Helvetica", 12, "bold"),
    bg="blue", fg="white"
)
score_label.pack(pady=5)

# Reset button with color
tk.Button(root, text="Reset Game", bg="skyblue", command=reset_game).pack(pady=10)

root.mainloop()
