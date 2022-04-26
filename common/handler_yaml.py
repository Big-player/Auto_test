import yaml
from common.handler_path import ab_path
from common.replace_yaml import replace_yaml


#私有方法，读取yaml文件，返回数据。
def __read_yml(file_name):
    with open(file_name, encoding="UTF-8") as f:
        data = yaml.load(f.read(), Loader=yaml.SafeLoader)
    return data

#读取用例文件和替换数据文件，返回易于使用的列表。filename：数据文件；config_file:替换数据文件，文件读取结果为字典。
def read_yaml(filename, autos=True, config_file='config/application-dev.yml'):
    case = []  # 存储测试用例名称
    http = []  # 存储请求对象
    expected = []  # 存储预期结果
    file_name = ab_path(filename)
    if autos == True:
        dat = __read_yml(file_name)
        test = dat['tests']
        for td in test:
            case.append(td.get('case'))
            http.append(td.get('http'))
            expected.append(td.get('expected'))
        datas = zip(case, http, expected)
        config = __read_yml(config_file)
        parameters = replace_yaml(list(datas), config)
    else:
        dat = __read_yml(file_name)
        test = dat['tests']
        for td in test:
            case.append(td.get('case'))
            http.append(td.get('http'))
            expected.append(td.get('expected'))
        datas = zip(case, http, expected)

        parameters=list(datas)

    return parameters

#写入yaml文件的方法
def write_yaml(filename):
    file_name = ab_path(filename)
    with open(file_name, "w", encoding="utf-8") as f:
        yaml.dump(file_name, f, allow_unicode=True)

