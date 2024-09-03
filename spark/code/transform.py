from pyspark.sql.session import SparkSession
from pyspark.context import SparkContext
from pyspark.sql.types import *
from pyspark.sql.functions import *
from bs4 import BeautifulSoup
from datetime import datetime

schema = StructType([
		StructField("url", StringType(), False),
		StructField("content", StringType(), False)
	])

run_time = "{:%d%m%Y}".format(datetime.now())

if __name__ == "__main__":
	sc = SparkContext("spark://spark-master:7077", "extract_load")
	spark = SparkSession(sc)

	df = spark.read.parquet("hdfs://namenode:9000/app_store/" + run_time)
	df.printSchema()