
from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup

class Question():
    def __init__(
        self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer =right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

total = 0
right = 0


questions = []
questions.append(Question('Как зовут предподавателя?',
                        'Джимми',
                        'Влад',
                        'Никита',
                        'Даниил'))                
questions.append(Question('Где проходят занятия?',
                        'в клубе',
                        'В здании',
                        'В магазине',
                        'В зоопарке'))
questions.append(Question('Какой сейчас год?',
                        '1701',
                        '2023',
                        '2020',
                        '2024'))
questions.append(Question('Сколько ноутбуков в классе?',
                        '10',
                        '14',
                        '20',
                        '9'))
questions.append(Question('Дополни. Минск-',
                        'бедный посёлок',
                        'город-герой',
                        'заброшенный город',
                        'город-мир'))
questions.append(Question('На каком этаже проходят занятия?',
                        'на 20',
                        'на 8',
                        'на 4',
                        'на 15'))

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Конкурс от Crazy People')
main_win.resize(600, 300)
box = QGroupBox()
box_answer = QGroupBox()
layout_box = QVBoxLayout()
answer_text = QLabel('Прав ты или нет!')
layout_box.addWidget(answer_text, alignment=Qt.AlignCenter)
box_answer.setLayout(layout_box)
question = QLabel('В каком году канал получил «золотую кнопку» от YouTube?')
group_btn = QButtonGroup()
btn_answer1 = QRadioButton('2005')
btn_answer2 = QRadioButton('2010')
btn_answer3 = QRadioButton('2015')
btn_answer4 = QRadioButton('2020')
group_btn.addButton(btn_answer1)
group_btn.addButton(btn_answer2)
group_btn.addButton(btn_answer3)
group_btn.addButton(btn_answer4)
layout_main = QVBoxLayout()
layoutH1 = QHBoxLayout()
layoutH2 = QHBoxLayout()
layoutH3 = QHBoxLayout()
layoutH1.addWidget(question, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layoutH2.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layoutH3.addWidget(btn_answer4, alignment = Qt.AlignCenter)
layoutV1 = QVBoxLayout()
layoutV1.addLayout(layoutH2)
layoutV1.addLayout(layoutH3)
box.setLayout(layoutV1)
btn = QPushButton('Ответить')
layout_main.addLayout(layoutH1)
layout_main.addStretch(1)
layout_main.addWidget(box)
layout_main.addWidget(box_answer)
box_answer.hide()
layout_main.addStretch(1)
layout_main.addWidget(btn)
main_win.setLayout(layout_main)
 
def show_answer():
    box.hide()
    box_answer.show()
    btn.setText('Следующий вопрос')
    
def show_question():
    box.show()
    box_answer.hide()
    btn.setText('Ответить')
    group_btn.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    group_btn.setExclusive(True)

btn_list = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]
def ask(q: Question):
    shuffle(btn_list)
    btn_list[0].setText(q.right_answer)
    btn_list[1].setText(q.wrong1)
    btn_list[2].setText(q.wrong2)
    btn_list[3].setText(q.wrong3)
    answer_text.setText(q.right_answer)
    question.setText(q.question)
    show_question()

def show_result(result):
    answer_text.setText(result)
    show_answer()

def check_answer():
    global right
    if btn_list[0].isChecked():
        show_result('Правильно!')
        right = right + 1 
    else:
        if btn_list[1].isChecked() or btn_list[2].isChecked() or btn_list[3].isChecked():
            show_result('Неверно!')
current_q = 0
def next_question():
    global current_q, total, right
    current_q += 1
    total = total + 1
    print('Статистика')
    print('Всего')
    print('Правильных ответов:', right)
    print('Рейтинг:', (right/total)*100, '%')
    if current_q >= len(questions):
        current_q = 0
    q = questions[current_q]
    ask(q)

def change():
    if btn.text() == 'Ответить':
        check_answer()
    else:
        next_question()
    
btn.clicked.connect(change)
main_win.show()
app.exec_()




В этоту программу 

я посветила 

4 часа своей жизни!

И я рада что у меня 

всё получилось. 

Ах да, я сделала 

это на языке програм-

мирования.

Жилаю хорошего просмотра! 







