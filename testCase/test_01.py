from locust import HttpUser, task, TaskSet, SequentialTaskSet
import os


class Test1(SequentialTaskSet):
    @task
    def test01(self):
        print("测试01")
    @task
    def test02(self):
        print("测试02")
    @task
    def test03(self):
        print("测试03")
    @task
    def my_task(self):
        with self.client.get('/v2/zoho/getZohoNetwork', catch_response=True) as re:
            # print(re.text)
            if '研发' in re.text:
                re.success()
            else:
                re.failure('fail')


class Test(HttpUser):
    tasks = [Test1]
    # min_wait = 100
    # max_wait = 1000

# if __name__ == '__main__':
#     os.system("locust -f test_01.py --host=http://10.2.2.84:8087")
