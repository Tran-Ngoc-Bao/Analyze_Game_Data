from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator # type: ignore
import json
import redis
import os
from airflow import DAG
from airflow.operators.python_operator import PythonOperator # type: ignore
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

dag = DAG("tutorial", default_args = default_args, schedule_interval = timedelta(30))

submit_task = SparkSubmitOperator(
    application='/opt/code/hello.py',
    conn_id='spark_default',
    task_id='submit_task',
    dag=dag
)