# list_reverso = (input("Вставте свої слова скопійовані з Reverso: ")).split()
#
# list_quizlet = []
#
# print(list_reverso)
import re

import PySimpleGUI as sg
layout = [
    [sg.Text('Text'), sg.InputText(size=(100, 20)), sg.Submit()],
    [sg.Output(size=(120, 30))],
    [sg.Cancel()]
]
window = sg.Window('Formatting for quizlet(reverso)', layout)
while True:                             # The Event Loop
    event, values = window.read()
    # print(event, values) #debug
    if event in (None, 'Exit', 'Cancel'):
        break
    if event == 'Submit':
        text_1 = values[0].split('\n\n\n')
        text_2 = []

        for i in text_1:
            text_2.append(i.split('\n')[:-3])
        text_res = str()
        text_for = str()
        for item in text_2:
            text_res += f'{text_for}\n'
            text_for = str()
            if len(item) != 1:
                for j, k in enumerate(item):
                    if j == 0:
                        text_for += f'{k}    '
                    else:
                        text_for += f'{k}, '
        print(text_res)
