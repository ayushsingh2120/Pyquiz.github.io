import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, master):
        # Initialize the main window
        self.master = master
        self.master.title("Python Quiz App")
        
        # List of questions 
        self.questions = [
            {
                "question": "What is the output of print(type([]))?",
                "options": ["<class 'list'>", "<class 'dict'>", "<class 'tuple'>", "<class 'set'>"],
                "answer": "<class 'list'>"
            },
            {
                "question": "Which of the following is a mutable data type?",
                "options": ["tuple", "list", "str", "int"],
                "answer": "list"
            },
            {
                "question": "What keyword is used to define a function in Python?",
                "options": ["function", "def", "define", "fun"],
                "answer": "def"
            },
            {
                "question": "Which of the following is used to handle exceptions in Python?",
                "options": ["try/except", "catch/throw", "error/handle", "if/else"],
                "answer": "try/except"
            }
        ]
        
        # Initialize score and question index
        self.score = 0
        self.question_index = 0
        
        # Label to display the question
        self.question_label = tk.Label(master, text="", wraplength=400)
        self.question_label.pack(pady=20)
        
        # Variable to store the selected answer
        self.var = tk.StringVar()
        self.options = []
        
        # Create radio buttons for answer options
        for i in range(4):
            option = tk.Radiobutton(master, variable=self.var, value="", text="")
            option.pack(anchor='w')
            self.options.append(option)
        
        # Button to submit the answer
        self.submit_button = tk.Button(master, text="Submit", command=self.submit_answer)
        self.submit_button.pack(pady=20)

        # Button to go to the next question
        self.next_button = tk.Button(master, text="Next", command=self.next_question)
        self.next_button.pack(pady=20)
        
        # Load the first question
        self.load_question()
    
    def load_question(self):
        """Load the current question and its options into the GUI."""
        if self.question_index < len(self.questions):
            question_data = self.questions[self.question_index]
            self.question_label.config(text=question_data["question"])
            self.var.set(None)  # Reset the selected option
            for i, option in enumerate(self.options):
                option.config(text=question_data["options"][i], value=question_data["options"][i])
            self.submit_button.config(state=tk.NORMAL)  # Enable the submit button
        else:
            self.end_quiz()  # End the quiz if there are no more questions
    
    def submit_answer(self):
        """Check the selected answer and update the score."""
        selected_option = self.var.get()
        if selected_option == self.questions[self.question_index]["answer"]:
            self.score += 1  # Increment score for correct answer
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", f"Wrong! The correct answer was: {self.questions[self.question_index]['answer']}")
        self.submit_button.config(state=tk.DISABLED)  # Disable the submit button after answering
    
    def next_question(self):
        """Move to the next question and load it."""
        self.question_index += 1
        self.load_question()
    
    def end_quiz(self):
        """Display the final score and close the application."""
        messagebox.showinfo("Quiz Complete", f"Your score: {self.score}/{len(self.questions)}")
        self.master.quit()  # Close the application

if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    app = QuizApp(root)  # Initialize the QuizApp
    root.mainloop()  # Start the Tkinter event loop