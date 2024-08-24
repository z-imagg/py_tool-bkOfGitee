import typing

from entity import Remain
from sqlite3db_wrap import select_remain_by_cadVer

def clean_cadVer(cadVer:str)->None:
  print(f"执行残留清理,cadVer={cadVer}")
  clean_fileRemain(cadVer)
  clean_regTabRemain(cadVer)
  return

#TODO 清理文件残留们
def clean_fileRemain(cadVer:str)->None:
  fileRemain_list:typing.List[Remain]=select_remain_by_cadVer(cadVer)
  # print(f"执行文件残留清理,{fileRemain_list}")
  return  

#TODO 清理注册表残留们
def clean_regTabRemain(cadVer:str )->None:
  regTabRemain_list:typing.List[Remain]=select_remain_by_cadVer(cadVer)
  # print(f"执行注册表残留清理,{regTabRemain_list}")
  return  