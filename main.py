from questions import questions
import random
from prettytable import PrettyTable

def run_quiz(questions):
    """
    Runs an interactive quiz.

    Args:
        questions: a list of tuples, where each tuple represents a question and its possible answers.
                   Each tuple should have the following structure:
                   (question, answer_1, answer_2, answer_3, answer_4, correct_answer_index)

    Returns:
        The user's final score as a percentage (a number between 0 and 100).
    """

    # Randomise the order of the questions each time the function executes
    random.shuffle(questions)
    score = 0
    summary = []

    # Loop through the questions that were imported 
    for i, (question, answer_1, answer_2, answer_3, answer_4, correct_answer_index) in enumerate(questions):
        print(f"\nQuestion {i + 1}: {question}")
        print(f"\n1. {answer_1}")
        print(f"2. {answer_2}")
        print(f"3. {answer_3}")
        print(f"4. {answer_4}")

        valid_input = False
        while not valid_input:
            user_answer = input("Enter your answer (1-4): ")
            if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
                valid_input = True
                user_answer_index = int(user_answer)
            else:
                print("Invalid input. Please enter a number between 1 and 4.")

        if user_answer_index == correct_answer_index:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {correct_answer_index}.")

        # Create summary of the user's answers to be used in the output
        summary.append((question, [answer_1, answer_2, answer_3, answer_4], correct_answer_index, user_answer_index))
        
    # Create a table object to be used in the output
    table = PrettyTable()
    table.field_names = ["Question", "Answer 1", "Answer 2", "Answer 3", "Answer 4", "Correct Answer", "Your Answer"]
    for i, (question, answers, correct_answer_index, user_answer_index) in enumerate(summary):
        table.add_row([question, answers[0], answers[1], answers[2], answers[3], answers[correct_answer_index - 1], answers[user_answer_index - 1]])

    print("\nSummary of Questions and Answers:")
    # print(table)
    print(table.get_string(fields=["Question", "Correct Answer", "Your Answer"]))

    final_score = (score / len(questions)) * 100
    print(f"You scored {score} out of {len(questions)} ({final_score:.2f}%).")

run_quiz(questions)