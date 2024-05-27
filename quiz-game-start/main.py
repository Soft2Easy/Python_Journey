from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

bank_size = len(question_data)
question_bank = []

for data_ in question_data:
    q_text = data_['question']
    answer_ = data_['correct_answer']
    new_quiz = Question(q_text, answer_)
    question_bank.append(new_quiz)

q_brain = QuizBrain(question_bank)

while q_brain.still_has_question():
    q_brain.next_question()

print('You have completed your quiz.')
print(f'Your final score was: {q_brain.score}/{q_brain.question_number}.')

# You can use TRIVIA DATABASE to renew the questions https://opentdb.com/api_config.php
