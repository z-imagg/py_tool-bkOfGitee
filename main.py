#!/usr/bin/env python

#来源:  https://gitlab.com/PySimpleGUI/pysimplegui/-/blob/4.60.5/DemoPrograms/Demo_Button_Click.py?ref_type=tags
import typing
import sys
import PySimpleGUI as sg

from busz_clean import clean_cadVer
from busz_find import find_fileRemain, find_regTabRemain
from entity import Remain
from sys_init import sys_init


def find_fileRemain_wrap(ui_remainList:sg.Table):
    remain_ls:typing.List[Remain]=find_fileRemain()
    ui_table:typing.List[typing.Tuple[int,str,str,str,str]]=Remain.toUiTable(remain_ls)
    ui_remainList.update(values=ui_table)
    return
    #end_func


def find_regTbRemain_wrap(ui_remainList:sg.Table):
    remain_ls:typing.List[Remain]=find_regTabRemain()
    ui_table:typing.List[typing.Tuple[int,str,str,str,str]]=Remain.toUiTable(remain_ls)
    ui_remainList.update(values=ui_table)
    return
    #end_func

def _ui_main():
  layout = [
            [sg.Button('搜索文件残留', button_color=('white', 'black'), key='btnId_fileRemain'),
            sg.Button('搜索注册表残留', button_color=('white', 'black'), key='btnId_regTbRemain'),],
            [[sg.Combo(['autocad2021', 'autocad2022', 'autocad2000', 'autocad2001'], default_value='cad版本', key='comboId_cadVer')],
              sg.Button('清理选中版本', button_color=('white', 'firebrick3'), key='btnId_cleanSelectVersion'),],
  [
    sg.Table([["-1..........", "名1..........", "类别1.........", "全路径1...........", "cad2005"],  ], 
    headings=[Remain._name_id, Remain._name_name, Remain._name__type, Remain._name_path, Remain._name_cad_ver],
    max_col_width=100,auto_size_columns=True, justification='right',
    key='tableId_remainList'
    ),
  ],

  [sg.Button('退出', button_color=('white', 'springgreen4'), key='btnId_quit')],
  ]#end_layout

  window:sg.Window = sg.Window("CAD卸载清理工具", layout, size=(600,300),auto_size_buttons=True,   use_default_focus=True, finalize=True)

  # window['btnId_cleanSelectVersion'].update(disabled=True)

  #变量类型声明
  event:str
  values:typing.Dict

  #本工具软件(系统)初始化
  sys_init()

  #ui事件循环
  recording = have_data = False
  while True:
      event, values = window.read(timeout=100)
      if event == sg.WINDOW_CLOSED:  break
      if event == 'btnId_quit':  break
      if event == sg.TIMEOUT_EVENT:  continue
      print(f"event={event}, values={values}")
      #搜索文件残留
      if event == 'btnId_fileRemain': find_fileRemain_wrap(window["tableId_remainList"])
      #搜索注册表残留
      if event == 'btnId_regTbRemain': find_regTbRemain_wrap(window["tableId_remainList"])
      #清理给定版本的cad
      if event == 'btnId_cleanSelectVersion': clean_cadVer(cadVer=values["comboId_cadVer"])
  #end_while
  window.close()


if __name__=="__main__": _ui_main()