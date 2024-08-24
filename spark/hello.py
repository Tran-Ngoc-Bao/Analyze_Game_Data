from pyspark.sql.functions import *
from pyspark.sql.session import SparkSession
from pyspark.context import SparkContext

if __name__ == "__main__":
	sc = SparkContext("spark://spark-master:7077", "test")
	
	spark = SparkSession(sc)
	df_ds = spark.read.csv("/opt/code/test.csv")
	df_ds.write.option("header", "true").option("delimiter", ",").mode("overwrite").csv("hdfs://namenode:9000/test")