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

  def __init__(self,  id:int,  name:str,  _type:str,  path:str) -> None:
    self.id=id
    self.name=name
    self._type=_type
    self.path=path
    self.cad_ver=''