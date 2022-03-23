from locust import HttpUser, task, TaskSet,SequentialTaskSet
import os
import jsonpath
class Test1(TaskSet):
    def on_start(self):
        print("on_stop")
    def on_stop(self):
        print("end..")
    @task
    def my_task(self):
        with self.client.get('/v2/zoho/getZohoNetwork', catch_response=True) as re:
            print(1)
            if '研发' in re.text:
                re.success()
            else:
                re.failure("faile")
    # @task(1)
    # def my_task1(self):
    #     with self.client.get('/room/getList', catch_response=True) as re:
    #         print(2)
    #         s = re.json()
    #         if jsonpath.jsonpath(s, '$..message') == ['成功!']:
    #             re.success()
    #         else:
    #             re.failure("失败")
    #





class Test(HttpUser):
    tasks = [Test1]
    min_wait = 100
    max_wait = 1000

if __name__ == '__main__':
    os.system("locust -f ces.py --host=http://10.2.2.84:8087")

