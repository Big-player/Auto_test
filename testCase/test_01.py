import allure
import pytest
import requests

class Test_b():
    req=[]
    def test_m1(self,login):
        url = 'https://docp5-ops.cloudwise.com/gateway/dosm/api/v1/dosm_activiti/workOrder/list/all/filter?currentPage=1&pageSize=30&searchKey=&language=zh&timestamp=1646987147252'
        data={"createdTime_":{"value":["1639152000~1647014399"],"key":"createdTime","process":"","type":""},"orderTypeList_":{"key":"orderTypeList","process":"","value":["CHANGE"],"type":""}}
        self.req.append(login)
        s=login.post(url=url,json=data )
        print(s.status_code)

    def test_m2(self):
        url = 'https://docp5-ops.cloudwise.com/gateway/dosm/api/v1/dosm_activiti/workOrder/list/all/filter?currentPage=1&pageSize=30&searchKey=&language=zh&timestamp=1646987147252'
        data={"createdTime_":{"value":["1639152000~1647014399"],"key":"createdTime","process":"","type":""},"orderTypeList_":{"key":"orderTypeList","process":"","value":["CHANGE"],"type":""}}
        s=self.req[0].post(url=url,json=data )
        print(s.json())