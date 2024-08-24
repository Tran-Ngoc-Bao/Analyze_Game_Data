import pendulum
from airflow.decorators import dag, task
import requests
from bs4 import BeautifulSoup
import redis

@dag(
    schedule = None,
    start_date = pendulum.datetime(2024, 8, 1, tz="UTC"),
    catchup = False,
    tags = ["example"],
)
def tutorial_taskflow_api():
    @task()
    def extract_load_redis():
        req = requests.get("https://apps.apple.com/vn/genre/ios-tr%C3%B2-ch%C6%A1i/id6014?l=vi")
        t = req.text
        soup = BeautifulSoup(t, "html.parser")
        l = soup.find_all('a')
        output = ""
        for i in l:
            if str(i).find("/vn/app/") != -1:
                output += i["href"]
        r = redis.Redis(host = "redis", port = 6379, db = 0)
        r.set("test", output)
        
    
    # @task(multiple_outputs = True)
    # def transform(order_data_dict: dict):
    #     total_order_value = 0
    #     for value in order_data_dict.values():
    #         total_order_value += value
    #     return {"total_order_value": total_order_value}
    
    # @task()
    # def load(total_order_value: float):
    #     print(f"Total order value is: {total_order_value:.2f}")

    order_data = extract_load_redis()

tutorial_taskflow_api()