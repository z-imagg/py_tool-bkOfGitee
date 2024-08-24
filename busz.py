import typing

from entity import Remain

#TODO 寻找文件残留们
def find_fileRemain()->typing.List[Remain]:
  remain_ls:typing.List[Remain]=[]
  remain_ls.append(Remain(1,"AUTOCAD2022","type1","c:/Program Files/AUTOCAD2022"))
  return remain_ls

#TODO 寻找注册表残留们
def find_regTabRemain()->typing.List[Remain]:
  remain_ls:typing.List[Remain]=[]
  remain_ls.append(Remain(1,"注册表残留1","type1","xxx注册表项目路径"))
  return remain_ls
