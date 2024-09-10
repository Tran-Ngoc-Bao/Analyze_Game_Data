from airflow import DAG
from airflow.operators.bash_operator import BashOperator # type: ignore
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 9, 1),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes = 5),
    # "queue": "bash_queue",
    # "pool": "backfill",
    # "priority_weight": 10,
    # "end_date": datetime(2016, 1, 1),
}

dag = DAG("main", default_args = default_args, schedule_interval = timedelta(30))

extract_load_task = BashOperator(
    task_id = "extract_load_task",
    bash_command = "spark-submit /opt/aitflow/code/extract_load.py", 
    dag = dag
)

transform_app_store_task = BashOperator(
    task_id = "transform_app_store_task",
    bash_command = "spark-submit --driver-class-path /opt/code/postgresql-42.2.5.jar /opt/code/transform_app_store.py", 
    dag = dag
)

transform_google_play_task = BashOperator(
    task_id = "transform_google_play_task",
    bash_command = "spark-submit --driver-class-path /opt/code/postgresql-42.2.5.jar /opt/code/transform_google_play.py", 
    dag = dag
)

extract_load_task >> [transform_app_store_task, transform_google_play_task]