FROM apache/airflow:2.10.0
USER root
RUN apt update
RUN apt install -y default-jdk
USER airflow
RUN pip install pyspark