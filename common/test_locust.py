from locust import HttpUser, task, TaskSet
import jsonpath
import os

class Test1(TaskSet):
    @task
    def my_task(self):
        with self.client.get(url='/v2/zoho/getZohoNetwork', catch_response=True) as re:
            # print(re.text)
            if '研发' in re.text:
                re.success()
            else:
                re.failure()

    # def my_task1(self):
    #     with self.client.get('/room/getList',catch_response=True,name="1") as re:
    #         s=re.json()
    #         if jsonpath.jsonpath(s,'$..message')==['成功!']:
    #             re.success()
    #         else:
    #             re.failure()

    # def ces(self):
    #     self.my_task1()
    #     self.my_task()

class Test(HttpUser):
    tasks = [Test1]
    min_wait = 100
    max_wait = 1000

# if __name__ == '__main__':
#     os.system("locust -f ces.py --host=http://10.2.2.84:8087")
