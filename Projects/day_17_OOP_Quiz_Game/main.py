from question_model import Question
from data import question_data
from quiz_brain import QuizGame


questions_to_ask = []

for question in question_data:

    text = question["question"]
    answer = question["correct_answer"]
    new_question = Question(text, answer)
    questions_to_ask.append(new_question)


quiz = QuizGame(questions_to_ask)

while quiz.still_has_questions:
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your finale score was: {quiz.score}/{quiz.question_number}")



