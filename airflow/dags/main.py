import json, requests
import redis
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 5, 1),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    # "queue": "bash_queue",
    # "pool": "backfill",
    # "priority_weight": 10,
    # "end_date": datetime(2016, 1, 1),
}

dag = DAG("main", default_args = default_args, schedule_interval = timedelta(30))

def crawl_app_store():
    main_page = requests.get("https://apps.apple.com/vn/genre/ios-tr%C3%B2-ch%C6%A1i/id6014?l=vi")
    soup = BeautifulSoup(main_page.content.decode("utf-8"), "html.parser")
    list = soup.find_all('a')
    client = InsecureClient('hdfs://namenode:9000', user='root')
    for i in list:
        if i['href'].find('/vn/app/') != -1:
            game = requests.get(i['href']).content
            client.write("app_store", game)

crawl_app_store = PythonOperator(
    task_id = "crawl_app_store",
    python_callable = crawl_app_store,
    provide_context = True,
    dag = dag,
)

crawl_app_store