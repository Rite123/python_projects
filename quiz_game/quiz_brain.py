
class QuizBrain:

    def questions(self):
        Q = self.question_list[self.question_no]
        self.question_no += 1
        user_input = input(f"Q:{self.question_no}.{Q.ques}(True/False):")

        if self.check_answer(user_input, Q.ans):
            self.score += 1
            print("you're right !!")
        else:
            print("you're Wrong !!")
        print(f"your current Score:{self.score}/{self.question_no}")
        print(f"The Correct answer is:{Q.ans}")

    def __init__(self, question_bank):
        self.question_no = 0
        self.score = 0
        self.question_list = question_bank

    def still_ques_left(self):
        return self.question_no<len(self.question_list)

    def check_answer(self,ans,user_ans):
        return ans.lower() == user_ans.lower()





