from locust import TaskSet, task, HttpLocust
from random import randint

class ConverterTasks(TaskSet):
    @task
    def day_to_hour(self):
        self.client.get('/%d' % randint(1, 200), name='/alarme/[int]')

class ApiUser(HttpLocust):
    task_set = ConverterTasks
    min_wait = 1000
    max_wait = 3000