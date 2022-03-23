import yaml
from common.handler_path import ab_path
from string import Template
def read_yaml(filename):
    file_name = ab_path(filename)
    with open(file_name, encoding="UTF-8") as f:
        result = yaml.load(f, Loader=yaml.FullLoader)
    # 返回读取结果
    return result

def write_yaml(filename):
    file_name = ab_path(filename)
    with open(file_name, "w", encoding="utf-8") as f:
        yaml.dump(file_name, f,allow_unicode=True)
