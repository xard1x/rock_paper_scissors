from PyQt5.QtCore import Qt
import random
from PyQt5.QtWidgets import *
from pygame import mixer
from PyQt5.QtGui import *

app = QApplication([]) # создание окна
win = QWidget()

result_3 = '' #переменные для статистики
result_2 = ''
result = ''
player = '' #переменная для выбора игрока

counter =  0  #переменная счетчик(общий)
counter_win = 0 #переменная счетчик(побед)
counter_defeat = 0 #переменная счетчик(поражений)
counter_draw = 0 #переменная счетчик(ничьих)

win.setWindowTitle('Камень-ножницы-бумага') 
win.setMinimumSize(400, 400)
win.setMaximumSize(400, 400)

main_layout = QVBoxLayout() #создание основного лайаута

vertical_layout1 = QHBoxLayout() #создание горизонтальный лайаутов
vertical_layout2 = QHBoxLayout()
vertical_layout3 = QHBoxLayout()
vertical_layout4 = QHBoxLayout()

select = QLabel('Выберите:') #создание надписи выберите и присваивание ее лайауту  
select.setFont(QFont('Arial', 20)) 
vertical_layout1.addWidget(select,alignment = Qt.AlignCenter)

stone = QPushButton('Камень') #создание кнопок  и присваивание их лайауту  
stone.setFont(QFont('Arial', 15))
scissors = QPushButton('Ножницы') 
scissors.setFont(QFont('Arial', 15))
paper =  QPushButton('Бумага')
paper.setFont(QFont('Arial', 15))
counter_button = QPushButton('Статистика')
counter_button.setFont(QFont('Arial', 17))
but_music = QPushButton('Музыка')
but_music.setFont(QFont('Arial', 17))
but_pause = QPushButton('Стоп')
but_pause.setFont(QFont('Arial', 17))
vertical_layout2.addWidget(stone, alignment = Qt.AlignCenter)
vertical_layout2.addWidget(scissors, alignment = Qt.AlignCenter)
vertical_layout2.addWidget(paper, alignment = Qt.AlignCenter)
vertical_layout4.addWidget(counter_button, alignment = Qt.AlignCenter)
vertical_layout4.addWidget(but_music, alignment= Qt.AlignCenter)
vertical_layout4.addWidget(but_pause, alignment= Qt.AlignCenter)
but_pause.hide()

main_layout.addLayout(vertical_layout1) #присваивании гориз лайаутов основному
main_layout.addLayout(vertical_layout2)
main_layout.addLayout(vertical_layout3)
main_layout.addLayout(vertical_layout4)

def click_stone(): #нажатие разных кнопок
    global player
    player = 'камень'
    proverka()
def click_scissors():
    global player
    player = 'ножницы'
    proverka()
def click_paper():
    global player
    player = 'бумага'
    proverka()

def proverka(): #сравнение выбора игрока и бота
    global counter
    global counter_win
    global counter_defeat
    global counter_draw
    global player
    global choice
    global result
    list = ['камень', 'ножницы', 'бумага']
    choice = random.choice(list)
    if choice == player:
        result = 'Ничья'
        counter_draw += 1
        result_msg()
    if player == 'камень' and choice == 'ножницы' or player == 'ножницы' and choice == 'бумага' or player == 'бумага' and choice =='камень':
        result = 'Победа'
        counter += 1
        counter_win += 1
        result_msg()
    if choice == 'камень' and player == 'ножницы' or choice == 'ножницы' and player == 'бумага' or choice == 'бумага' and player =='камень':
        result = 'Поражение'
        counter -= 1
        counter_defeat += 1
        result_msg()

def result_msg(): #окно с результатом
    global choice
    msg_kk = QMessageBox()
    msg_kk.setWindowTitle(result)
    msg_kk.setInformativeText(choice)
    msg_kk.setText("Бот выбрал:         ")
    msg_kk.setIcon(QMessageBox.Information)
    msg_kk.exec_()
def okno(): #окно для статистики
    global result
    global result_2
    global result_3
    msg_kk = QMessageBox()
    msg_kk.setWindowTitle(result)
    msg_kk.setInformativeText(result_2)
    msg_kk.setText(result_3)
    msg_kk.setIcon(QMessageBox.Question)
    msg_kk.exec_()
def stats(): #вывод статистики
    global result
    global result_2
    global result_3
    result = 'Статистика'
    result_2 = str(counter)
    result_3 = 'Общий счет:'
    okno()
    result_2 = str(counter_win)
    result_3 = '    Победы:'
    okno()
    result_2 = str(counter_draw)
    result_3 = '     Ничьи:'
    okno()
    result_2 = str(counter_defeat)
    result_3 = ' Поражения:'
    okno()
def play_music(): #проигрывание музыки
    volume = 1
    mixer.init()
    mixer.music.load('music.wav')
    mixer.music.play(-1)
    mixer.music.set_volume(volume)
    but_music.hide()
    but_pause.show()
def pause(): #остановка музыки
    but_music.show()
    mixer.music.pause()
    but_pause.hide()
but_music.clicked.connect(play_music)
but_pause.clicked.connect(pause)    
paper.clicked.connect(click_paper) #заключение
stone.clicked.connect(click_stone)
scissors.clicked.connect(click_scissors)
counter_button.clicked.connect(stats)
win.setLayout(main_layout)
win.show()
app.exec()