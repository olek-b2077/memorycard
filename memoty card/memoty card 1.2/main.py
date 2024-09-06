from random import choice, shuffle
from time import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

app = QApplication([])

from main_widow import *
from menu_window import *

class Question():
    def __init__(self,question, answer, wrong_answer1, wrong_answer2,wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.caunt_ark = 0
        self.caunt_right = 0
    def got_right (self):
        self.caunt_ark +=1
        self.caunt_right +=1
    def got_wrong(self):
        self.caunt_ark +=0

qvest1 = Question("Ми вивчаємо","pyton","C#","C++","Java")
qvest2 = Question("Де ростути чорниці","в лісі","в полі","африці","марсі")
qvest3 = Question("Де розташований еверест ","Азія","Європа","Африці","Америці")
qvest4 = Question("Де розташований карпати ","Україна","США","Німечина","Китаї")
qvest5 = Question("Скільки областей в Україні","27","28","24","37")
qvest6 = Question("Скільки лап в кита","-_-","2","4","0")
qvest7 = Question("Бескінечний цикл ","while True","for i in range(100)","while False","for True")

qvestion_list = [qvest1,qvest2,qvest3,qvest4,qvest5,qvest6,qvest7]
radio_list = [ansver1,ansver2,ansver3,ansver4]
qvestion_list_1 = qvestion_list

shuffle(radio_list)


def new_question():
    global cur_q, ansver_right
    cur_q = choice(qvestion_list)
    qvestion_text.setText(cur_q.question)

    answers = [cur_q.wrong_answer1, cur_q.wrong_answer2, cur_q.wrong_answer3, cur_q.answer]
    shuffle(answers)

    ansver_right = cur_q.answer
    
    for i in range(4):
        radio_list[i].setText(answers[i])
    
new_question()

def cheak():
    RadioButtonGroup.setExclusive(False)
    for answer in radio_list:
        if answer.isChecked() and answer.text() == ansver_right:
            cur_q.got_right()
            answer.setChecked(False)
            print("+1")
            break
    else:
        cur_q.got_wrong()
        print("-1")
    answer.setChecked(False)
    RadioButtonGroup.setExclusive(True)

def clic_ok():
    cheak()
    new_question()

def rest():
    win.hide()
    sleep(5)
    win.show()

def menu_gn():
    win.hide()
    menu.show()

def menu_bekc():
    menu.hide()
    win.show()
    


Respond.clicked.connect(clic_ok)
Sleep.clicked.connect(rest)
Menu.clicked.connect(menu_gn)

bakc.clicked.connect(menu_bekc)



app.exec_()



