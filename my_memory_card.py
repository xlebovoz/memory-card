from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

q1 = Question('какой язык Бразилии?','Португальский','Испанский','Бразильский','Английский')
q2 = Question('Выбери  перевод слова переменная','variable','chanching','variant','variation')
q3 = Question('Какого цвета нет на флаге России?','Зелёного','Белого','синего','Красного')
question_list = [q1,q2,q3]











# app = QApplication([])
# window = QWidget()
# window.setWindowTitle('Memory Card')

# question = QLabel('Какой национальности не существует?')
# btnok = QPushButton('Ответить')

# radiogroupbox = QGroupBox('Варианты ответов')
# rbtn1 = QRadioButton('Энцы')
# rbtn2 = QRadioButton('Смурфы')
# rbtn3 = QRadioButton('Чулымцы')
# rbtn4 = QRadioButton('Алеуты')
# loyautans1 = QHBoxLayout()
# loyautans2 = QVBoxLayout()
# loyautans3 = QVBoxLayout()

# loyautans2.addWidget(rbtn1)
# loyautans2.addWidget(rbtn2)
# loyautans3.addWidget(rbtn3)
# loyautans3.addWidget(rbtn4)
# loyautans1.addLayout(loyautans2)
# loyautans1.addLayout(loyautans3)

# radiogroupbox.setLayout(loyautans1)

# loyautline1 = QHBoxLayout()
# loyautline2 = QHBoxLayout()
# loyautline3 = QHBoxLayout()

# loyautline1.addWidget(question)
# loyautline2.addWidget(radiogroupbox)
# loyautline3.addWidget(btnok)

# layoutmain = QVBoxLayout()

# layoutmain.addLayout(loyautline1)
# layoutmain.addLayout(loyautline2)
# layoutmain.addLayout(loyautline3)

# window.setLayout(layoutmain)

# window.show()
# app.exec_()



app = QApplication([])
lbquestion = QLabel('Самый сложный вопрос в мире!')
btnok = QPushButton('Ответить')
rgb = QGroupBox('Варианты ответов')
rbtn1 = QRadioButton('v1')
rbtn2 = QRadioButton('v2')
rbtn3 = QRadioButton('v3')
rbtn4 = QRadioButton('v4')

layoutans1 = QHBoxLayout()
layoutans2 = QVBoxLayout()
layoutans3 = QVBoxLayout()

layoutans2.addWidget(rbtn1)
layoutans2.addWidget(rbtn2)
layoutans3.addWidget(rbtn3)
layoutans3.addWidget(rbtn4)

layoutans1.addLayout(layoutans2)
layoutans1.addLayout(layoutans3)

rgb.setLayout(layoutans1)

ansgroupbox = QGroupBox('Результат теста')
lbresult = QLabel('Правильно/неправильно')
lbcorrect = QLabel('Правильный ответ')

layoutres = QVBoxLayout()

layoutres.addWidget(lbresult)
layoutres.addWidget(lbcorrect)

ansgroupbox.setLayout(layoutres)


layoutline1 = QHBoxLayout()
layoutline2 = QHBoxLayout()
layoutline3 = QHBoxLayout()

layoutline1.addWidget(lbquestion)
layoutline2.addWidget(rgb)
layoutline2.addWidget(ansgroupbox)
layoutline3.addWidget(btnok)

ansgroupbox.hide()

layoutmain = QVBoxLayout()
layoutmain.addLayout(layoutline1)
layoutmain.addLayout(layoutline2)
layoutmain.addLayout(layoutline3)

window = QWidget()
window.setLayout(layoutmain)

#.
def show_result():
    rgb.hide()
    ansgroupbox.show()
    btnok.setText('Следуюший вопрос')

def show_question():
    ansgroupbox.hide()
    rgb.show()
    btnok.setText('Ответить')
    radio_group.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    radio_group.setExclusive(True)

def start_test():
    if 'Ответить' == btnok.text():
        show_result()
    else:
        show_question()

# btnok.clicked.connect(start_test)

radio_group = QButtonGroup()
radio_group.addButton(rbtn1)
radio_group.addButton(rbtn2)
radio_group.addButton(rbtn3)
radio_group.addButton(rbtn4)

answers = [rbtn1, rbtn2, rbtn3, rbtn4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lbquestion.setText(q.question)
    lbcorrect.setText(q.right_answer)
    show_question()


def show_correct(res):
    lbresult.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        window.score += 1
        print('статистика')
        print('Всего вопросов',window.total)
        print('Правильных ответов:',window.score)
        print('Рейтинг:',window.score / window.total * 100)
    elif answers[1].isChecked():
        show_correct('Неправильно')
        print('Рейтинг:',window.score / window.total * 100)
    elif answers[2].isChecked():
        show_correct('Неправильно')
        print('Рейтинг:',window.score / window.total * 100)
    elif answers[3].isChecked():
        show_correct('Неправильно')
        print('Рейтинг:',window.score / window.total * 100)

# def next_question():
#     question_askt = []
#     window.total += 1
#     print('статистика')
#     print('Всего вопросов',window.total)
#     print('Правильных ответов:',window.score)
#     cur_question = randint(0, len(question_list) -1)
#     q = question_list[cur_question]
#     for i in range(len(question_list)):
#         q = question_list[i]
#         ask(q)
#     # if q in question_askt:
#         # question_list.remove(q)
#     # if window.cur_question >= len(question_list):
#     #     window.cur_question = 0
#     # q = question_list[window.cur_question]
#     # ask(q)
#     # question_askt.append(q)

question_order = list(range(len(question_list)))
shuffle(question_order)
question_index = 0

def next_question():
    window.total += 1
    global question_index
    if question_index >= len(question_list):
        print("All questions have been asked. Reshuffling...")
        shuffle(question_order)
        question_index = 0
    
    cur_question = question_order[question_index]
    q = question_list[cur_question]
    ask(q)
    
    question_index += 1


def click_ok():
    if btnok.text() == 'Ответить':
        check_answer()
    else:
        next_question()


# window.cur_question = -1

# q = Question('Выбери  перевод слова переменная','variable','chanching','variant','variation')

window.score = 0
window.total = 0

# ask(q)
btnok.clicked.connect(click_ok)
next_question()










window.show()
app.exec_()
