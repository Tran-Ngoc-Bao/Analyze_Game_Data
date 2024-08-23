from airflow import DAG
from airflow.operators.bash_operator import BashOperator # type: ignore
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 8, 1),
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

crawl_app_store = BashOperator(
    task_id = "crawl_app_store",
    bash_command = "python3 /usr/local/airflow/code/hello.py",
    dag = dag,
)

# crawl_google_play_mobile = BashOperator(
#     task_id = "crawl_google_play_mobile",
#     bash_command = "ls -la",
#     dag = dag,
# )

# crawl_google_play_tablet = BashOperator(
#     task_id = "crawl_google_play_tablet",
#     bash_command = "ls -la",
#     dag = dag,
# )

crawl_app_store
# crawl_google_play_mobile
# crawl_google_play_tablet