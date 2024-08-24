#!/usr/bin/env python

#来源:  https://gitlab.com/PySimpleGUI/pysimplegui/-/blob/4.60.5/DemoPrograms/Demo_Button_Click.py?ref_type=tags
import sys
import PySimpleGUI as sg


layout = [
          [sg.Button('Start', button_color=('white', 'black'), key='start'),
           sg.Button('Stop', button_color=('white', 'black'), key='stop'),
           sg.Button('Reset', button_color=('white', 'firebrick3'), key='reset'),
           sg.Button('Submit', button_color=('white', 'springgreen4'), key='submit')]
          ]

window = sg.Window("Button Click", layout, auto_size_buttons=False, default_button_element_size=(12,1), use_default_focus=False, finalize=True)

window['submit'].update(disabled=True)

recording = have_data = False
while True:
    event, values = window.read(timeout=100)
    if event == sg.WINDOW_CLOSED:  break
    if event == sg.TIMEOUT_EVENT:  continue
    print(f"event={event}, values={values}")
window.close()
