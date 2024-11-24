# Python Quiz App

## Overview
The **Python Quiz App** is a desktop application developed using Python and the `tkinter` library. It offers a series of multiple-choice questions focused on Python programming concepts. Users can test their Python knowledge interactively, track their scores, and restart the quiz to play again.

---

## Features
- **Python-Focused Questions**:  
  Questions cover Python syntax, operations, and basic programming concepts.
- **Dynamic Question Updates**:  
  The app dynamically updates the question and options as the quiz progresses.
- **Score Tracking**:  
  Displays the user's score in a pop-up message at the end of the quiz.
- **Restart Option**:  
  Allows users to restart the quiz after completion.

---

## Requirements
- Python 3.x
- Tkinter (comes pre-installed with Python)

---

## Installation and Setup
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Salil16440/quiz.github.io

2. **Navigate to Directory**
   ```bash
    cd quiz.github.io
3. **Run the Application**
   ```bash
   python quiz_app.py
## How to Use
1. Launch the application using the above instructions.

2. The quiz will start, and you will be presented with a question and multiple-choice options.

3. Select an answer by clicking on the radio button next to your choice and click the "Submit" button.

4. After submitting, you will receive feedback on your answer. Click the "Next" button to move to the next question.

5. At the end of the quiz, your total score will be displayed in a message box.

## Code Explanation
The application is structured in a single class, QuizApp, which handles the GUI and quiz logic. Key components include:

**Questions:** A list of dictionaries containing questions, answer options, and the correct answer.

**Methods:**
load_question(): Loads the current question and its options into the GUI.
submit_answer(): Checks the selected answer and updates the score.
next_question(): Moves to the next question.
end_quiz(): Displays the final score and closes the application.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## Acknowledgments

Thanks to the Python community for providing resources and support.
Tkinter documentation for GUI development.

## Contact

For any inquiries, please reach out to **salil.16440@stu.upes.ac.in**.


