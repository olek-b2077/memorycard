from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

win=QWidget()
win.resize(400,200)
win.setWindowTitle("0w0")

HLayver1 = QHBoxLayout()
HLayver2 = QHBoxLayout()
HLayver3 = QHBoxLayout()
HLayver4 = QHBoxLayout()
HLayver5 = QHBoxLayout()
VLayver1 = QVBoxLayout()
VLayver2 = QVBoxLayout()


#h1
Menu = QPushButton("Menu")
Sleap = QPushButton("Sleap")
HLayver1.addWidget(Menu)
HLayver1.addWidget(Sleap)


#h2
Box_Qvestion = QGroupBox("запитання")
HLayver2.addWidget(Box_Qvestion)

#h3

#h4
Box_Ansver = QGroupBox("відповіді")
#v1
RadioButtonGroup=QButtonGroup()
ansver1 = QRadioButton('1')
ansver2 = QRadioButton('2')
ansver3 = QRadioButton('3')
ansver4 = QRadioButton('4')

RadioButtonGroup.addButton(ansver1)
RadioButtonGroup.addButton(ansver2)
RadioButtonGroup.addButton(ansver3)
RadioButtonGroup.addButton(ansver4)

HLayver3.addWidget(ansver1,alignment=Qt.AlignCenter)
HLayver3.addWidget(ansver2,alignment=Qt.AlignCenter)
HLayver4.addWidget(ansver3,alignment=Qt.AlignCenter)
HLayver4.addWidget(ansver4,alignment=Qt.AlignCenter)

v_main=QVBoxLayout()

v_main.addLayout(HLayver3)
v_main.addLayout(HLayver4)

Box_Ansver.setLayout(v_main)

HLayver4.addWidget(Box_Ansver)

#h5
Respond = QPushButton("Відповсти")
HLayver5.addWidget(Respond)



VLayver1.addLayout(HLayver1)
VLayver1.addWidget(Box_Ansver)






win.setLayout(VLayver1)



win.show()