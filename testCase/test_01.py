import pytest
from common.handler_yaml import read_yaml

@pytest.mark.parametrize("case,http,result", read_yaml('data/search_list_api.yaml'))
def test_api(login, case, http, result):
    s = login.request(url=http['path'], method=http['method'], headers=http['headers'], json=http['body'])
    print(s.text)
    assert s.status_code == result['response']['code']
