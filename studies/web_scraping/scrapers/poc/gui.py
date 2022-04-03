#!/usr/bin/env python
import PySimpleGUI as sg

layout = [
    [sg.Text('Some text on row 1')],
    [sg.Text('Enter Something on row 2'), sg.InputText()],
    [sg.Button('Ok'), sg.Button('Cancel')],
]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    print('You entered ', values[0])

window.close()
