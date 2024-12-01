import question_model as q
class Quiz():
    def __init__(self, questions):
        self.questions = questions
        self.question_number = 0
        self.score = 0

    def next_question(self):
        currentquestion = self.questions[self.question_number]
        self.question_number += 1
        userAnswer = input(f"{self.question_number}: {currentquestion.question} (True/False): ")
        self.check_answer(userAnswer, currentquestion.answer)

    def still_has_question(self):
        return self.question_number < len(self.questions)-1

    def check_answer(self, user, answer):
        if user == answer:
            self.score += 1
            print("You got it right!")
        if self.still_has_question():
            print(f"Your score is {self.score}/{self.question_number}")
        else:
            print(f"Your final score is {self.score}/{self.question_number}")