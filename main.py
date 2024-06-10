import tkinter as tk
from tkinter import messagebox

# Questions, options, and answers
questions = ["Which planet is known as the red planet?",
             "What is the currency of Japan?",
             "What has a face and two hands, but no arms or legs?",
             "What is the tallest land animal in the world?",
             "What do you call a baby cat?"]

options = [["A. Earth", "B. Mars", "C. Neptune", "D. Mercury"],
           ["A. Japanese Yen", "B. Euro", "C. Dollars", "D. Rupay"],
           ["A. Chair", "B. Table", "C. Coconut", "D. Clock"],
           ["A. giraffe", "B. elephant", "C. lion", "D. tiger"],
           ["A. Cub", "B. Baby cat", "C. Kitten", "D. Puppy"]]

answers = ["B", "A", "D", "A", "C"]

# Initialize the quiz state
question_number = 0
score = 0
guesses = []


# Function to handle the answer submission
def submit_answer():
    global question_number, score

    guess = var.get()
    guesses.append(guess)

    if guess == answers[question_number]:
        score += 1

    question_number += 1

    if question_number < len(questions):
        update_question()
    else:
        show_results()


# Function to update the question and options
def update_question():
    question_label.config(text=questions[question_number])
    for i, option in enumerate(options[question_number]):
        option_buttons[i].config(text=option)


# Function to display the results
def show_results():
    result_text = f"Your score is: {int(score / len(questions) * 100)}%\n"
    result_text += "Answers: " + " ".join(answers) + "\n"
    result_text += "Guesses: " + " ".join(guesses)
    messagebox.showinfo("Results", result_text)
    root.destroy()


# Set up the main application window
root = tk.Tk()
root.title("Quiz Application")

question_label = tk.Label(root, text=questions[question_number], wraplength=400, justify="center")
question_label.pack(pady=20)

var = tk.StringVar()
option_buttons = []
for i in range(4):
    btn = tk.Radiobutton(root, text="", variable=var, value="ABCD"[i], indicatoron=0, width=20)
    btn.pack(pady=5)
    option_buttons.append(btn)

submit_button = tk.Button(root, text="Submit", command=submit_answer)
submit_button.pack(pady=20)

update_question()
root.mainloop()