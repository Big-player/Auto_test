import pytest
import os
import requests
from common.replace_yaml import replace_yaml
from common.handler_yaml import read_yaml
@pytest.fixture(scope='session',autouse=True)
def login():
    s=requests.session()
    Cookie='SESSION=ZTdkM2JkMjQtYTg3YS00ZWQxLWEyYmQtOTJhMGVhMmRiN2Yx;aops-sessionId=e7d3bd24-a87a-4ed1-a2bd-92a0ea2db7f1;JSESSIONID=300DCDB6BC3AFABF4E27BD979B50283A'
    s.headers.update({'Cookie': Cookie})
    return s
@pytest.fixture(scope='function')
def host():
    config=read_yaml("config/application-dev.yml")
    return config['host']


