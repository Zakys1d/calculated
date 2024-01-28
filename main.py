from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,
                             QPushButton, QListWidget, QVBoxLayout,QLineEdit, QHBoxLayout)
from PyQt5.QtCore import Qt
from random import randint

app = QApplication([])
window = QWidget()
window.resize(250,250) # розміри
window.move(250,250)

line = QLineEdit()
button1 = QPushButton('1')
button2 = QPushButton('2')
button3 = QPushButton('3')
button4 = QPushButton('4')
button5 = QPushButton('5')
button6 = QPushButton('6')
button7 = QPushButton('7')
button8 = QPushButton('8')
button9 = QPushButton('9')
button0 = QPushButton('0')
slash = QPushButton('/')
clear = QPushButton('clear')
res = QPushButton('=')
plus = QPushButton('+')
min = QPushButton('-')
mnozh = QPushButton('*')

result = QLabel('Результат')
label = QLabel('Максим')


h1 = QHBoxLayout()
h1.addWidget(button1)
h1.addWidget(button2)
h1.addWidget(button3)
h1.addWidget(plus)

h2 = QHBoxLayout()
h2.addWidget(button4)
h2.addWidget(button5)
h2.addWidget(button6)
h2.addWidget(min)

h3 = QHBoxLayout()
h3.addWidget(button7)
h3.addWidget(button8)
h3.addWidget(button9)
h3.addWidget(mnozh)

h4 = QHBoxLayout()
h4.addWidget(button0)
h4.addWidget(slash)
h4.addWidget(clear)
h4.addWidget(res)

h5 = QHBoxLayout()
h5.addWidget(result)
h5.addWidget(label)

v = QVBoxLayout()
v.addWidget(line)
v.addLayout(h1)
v.addLayout(h2)
v.addLayout(h3)
v.addLayout(h4)
v.addLayout(h5)

window.setLayout(v)
window.show()
app.exec_()