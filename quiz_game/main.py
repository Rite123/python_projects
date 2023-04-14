# from question_model import Question
# from quiz_brain import QuizBrain
# from data import question_data as qd
#
# question_bank = []
# for i in qd:
#     question_bank.append(Question(i["text"], i["answer"]))
#
# brain = QuizBrain(question_bank)
#
#
# while brain.still_ques_left():
#     brain.questions()
#
#     print("\n\n")

import numpy as np
class Mast:
    def __init__(self,name,ph_no):
        self.name= name
        self.phone= ph_no


temp=Mast(input("Enter your name:"),int(input("enter your phone no:")))
print(temp.name, temp.phone)
print(np.size(float))