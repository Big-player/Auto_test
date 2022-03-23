import pytest
import os
import requests
@pytest.fixture(scope="session",autouse=True)
def login():
    header = {
        'Cookie': 'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217d02e598cd625-09a2c9e5e7c4ce-1c306851-1296000-17d02e598ced2e%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22http%3A%2F%2F10.2.2.84%3A29001%2F%22%7D%2C%22%24device_id%22%3A%2217d02e598cd625-09a2c9e5e7c4ce-1c306851-1296000-17d02e598ced2e%22%7D; SESSION=NjU4ODU2YTMtMzg4MS00MDdjLTk5YmMtZWFlYjE0MTU1ODU5; aops-sessionId=658856a3-3881-407c-99bc-eaeb14155859'
        , 'Content-Type': 'application/json'}
    s=requests.session()
    s.headers=header
    return s
