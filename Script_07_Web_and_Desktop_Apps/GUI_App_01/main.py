# Sentence Maker App

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtWidgets import QLabel, QPushButton, QLineEdit

def make_sentence():
    input_text = text.text()
    outout_label.setText(input_text.capitalize() + '.')


app = QApplication([])
window = QWidget()
window.setWindowTitle('Sentence Maker')


layout  = QVBoxLayout()

text = QLineEdit()
layout.addWidget(text)

btn = QPushButton('Make')
layout.addWidget(btn)
btn.clicked.connect(make_sentence)

outout_label = QLabel('')
layout.addWidget(outout_label)

window.setLayout(layout)
window.show()
app.exec()