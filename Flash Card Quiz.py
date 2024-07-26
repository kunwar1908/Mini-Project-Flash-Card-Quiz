import tkinter as tk

# Sample questions and answers
questions = ["What is the capital of France?", "Which planet is known as the Red Planet?", "What is the largest ocean in the world?"]
answers = ["Paris", "Mars", "Pacific Ocean"]

# Initialize the score and current question index
score = 0
current_question = 0

# Function to check the user's answer
def check_answer():
    global score, current_question
    user_answer = entry.get()
    if user_answer.lower() == answers[current_question].lower():
        feedback_label.config(text="Correct!", fg="green")
        score += 1
    else:
        feedback_label.config(text=f"Incorrect! The correct answer was {answers[current_question]}.", fg="red")
    entry.delete(0, tk.END)
    current_question += 1
    root.after(2000, show_question)  # Show the next question after 2 seconds

# Function to display the next question
def show_question():
    if current_question < len(questions):
        question_label.config(text=questions[current_question])
        feedback_label.config(text="")
    else:
        question_label.config(text=f"Quiz completed! Your score is {score}/{len(questions)}")
        entry.config(state='disabled')
        submit_button.config(state='disabled')
        feedback_label.config(text="")

# Create the GUI
root = tk.Tk()
root.title("Flashcard Quiz")
root.configure(bg="lightblue")

question_label = tk.Label(root, text="", font=("Arial", 16), bg="lightblue", fg="darkblue")
question_label.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 14), bg="white", fg="black")
entry.pack(pady=10)

submit_button = tk.Button(root, text="Submit", command=check_answer, font=("Arial", 14), bg="darkblue", fg="white")
submit_button.pack(pady=20)

feedback_label = tk.Label(root, text="", font=("Arial", 14), bg="lightblue")
feedback_label.pack(pady=10)

show_question()

root.mainloop()