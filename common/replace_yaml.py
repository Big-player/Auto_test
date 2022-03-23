from string import Template

def typeof(variate,replace):
      type=None
      result=None
      if isinstance(variate,int):
            type = "int"
            print(type)
            result=int(replace)
      elif isinstance(variate,str):
            type = "str"
            print(type)
            result=str(replace)
      elif isinstance(variate,float):
            type = "float"
            print(type)
            result = float(replace)
      elif isinstance(variate,list):
            type = "list"
            print(type)
            result = eval(replace)
      elif isinstance(variate,tuple):
            type = "tuple"
            print(type)
            result = eval(replace)
      elif isinstance(variate,dict):
            type = "dict"
            print(type)
            result = eval(replace)
      elif isinstance(variate,set):
            type = "set"
            print(type)
            result = eval(replace)

      return result
"""
:param old_result 要被替换的结果,列表或者字典;data为要替换的字典值
"""
def replace_yaml(old_result,data):
    dat=dict(data)
    old_str=str(old_result)
    replace= Template(old_str).substitute(dat)

    result=typeof(old_result,replace)
    return result

