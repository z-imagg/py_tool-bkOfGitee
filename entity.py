import typing

class Remain:
  id:int
  name:str
  _type:str
  path:str
  cad_ver:str

  _name_id:str="编号"
  _name_name:str="名称"
  _name__type:str="类型"
  _name_path:str="路径"
  _name_cad_ver:str="版本"

  def __init__(self,  id:int,  name:str,  _type:str,  path:str) -> None:
    self.id=id
    self.name=name
    self._type=_type
    self.path=path
    self.cad_ver=''

  def toUiTableRow(self)->typing.Tuple[int,str,str,str,str]:
    return (self.id,self.name,self._type,self.path,self.cad_ver)
  
  @staticmethod
  def toUiTable(remainLs:typing.List['Remain'])->typing.List[typing.Tuple[int,str,str,str,str]]:
    k:Remain
    ui_table:typing.List[typing.Tuple[int,str,str,str,str]]=[k.toUiTableRow() for k in remainLs]
    return ui_table
