# coding=utf-8
from locust import HttpLocust, TaskSet, task
import json

class WebsitTasks(TaskSet):

    @task
    # 调用登陆接口
    def login(self):
        # 设置登陆名和密码
        payload = {"username":"123","password":"123"}

        with self.client.post("/demo/user/v1/login", json=payload, catch_response=True) as response:
            if response.status_code == 200:
                pass
            else:
                response.failure(response)

    @task
    # 调用结算接口
    def buy(self):

        header = {"token": "666"}
        payload = [{"productId":1,"count":2},{"productId":2,"count":1}]
        with self.client.post("/demo/product/v1/products/buy", headers=header, json=payload, catch_response=True) as response:
            if response.status_code == 200:
                pass
            else:
                response.failure(response)

    @task
    # 调用查看订单接口
    def order(self):

        header = {"token": "666"}
        with self.client.get("/demo/order/v1/user/1/orders", headers=header, catch_response=True) as response:
            if response.status_code == 200:
                pass
            else:
                response.failure(response)


class WebsiteUser(HttpLocust):
    task_set = WebsitTasks
    # 设置daoshop的host(形式为ip：port)
    host = "http://172.16.20.104:30677"
    min_wait = 0
    max_wait = 0