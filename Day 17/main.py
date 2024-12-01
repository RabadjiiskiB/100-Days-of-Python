import data,question_model as q
import quiz_brain

questions = []
for i in data.question_data:
    questions.append(q.Question(i["question"], i["correct_answer"]))

quiz = quiz_brain.Quiz(questions)
while quiz.still_has_question():
    quiz.next_question()




