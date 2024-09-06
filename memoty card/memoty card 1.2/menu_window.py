from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
menu=QWidget()
menu.resize(800,200)
menu.setWindowTitle("Menu")

question_lb = QLabel("Запитаня")
ansver_right_lb = QLabel("Правельна відповіть")
ansver_lb1 = QLabel("Відповідь"+"1")
ansver_lb2 = QLabel("Відповідь"+"2")
ansver_lb3 = QLabel("Відповідь"+"3")

question = QLineEdit("")
ansver_right = QLineEdit("")
ansver1_le = QLineEdit("")
ansver2_le = QLineEdit("")
ansver3_le = QLineEdit("")

clear = QPushButton("clear")
add_q = QPushButton("add_question")
bakc = QPushButton("bakc")

row_lb = QVBoxLayout()
row_le = QVBoxLayout()

col_lb_le = QHBoxLayout()
col_buton = QHBoxLayout()

main_line = QVBoxLayout()

row_lb.addWidget(question_lb)
row_lb.addWidget(ansver_right_lb)
row_lb.addWidget(ansver_lb1)
row_lb.addWidget(ansver_lb2)
row_lb.addWidget(ansver_lb3)

row_le.addWidget(question)
row_le.addWidget(ansver_right)
row_le.addWidget(ansver1_le)
row_le.addWidget(ansver2_le)
row_le.addWidget(ansver3_le)

col_buton.addWidget(clear)
col_buton.addWidget(add_q)
col_lb_le.addLayout(row_lb)
col_lb_le.addLayout(row_le)

main_line.addLayout(col_lb_le)
main_line.addLayout(col_buton)
main_line.addWidget(bakc)

menu.setLayout(main_line)



