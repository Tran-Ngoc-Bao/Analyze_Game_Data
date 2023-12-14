from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.session import SparkSession
from pyspark.context import SparkContext

import query

schema = StructType([
    StructField("Link", StringType(), True), 
    StructField("GameName", StringType(), True), 
    StructField("AgeLimit", StringType(), True), 
    StructField("CompanyName", StringType(), True), 
    StructField("Raking", StringType(), True), 
    StructField("Classify", StringType(), True), 
    StructField("Rating", StringType(), True),
    StructField("Reviews", IntegerType(), True),
    StructField("Price", IntegerType(), True),
    StructField("Availablity", StringType(), True),
    StructField("Describe", StringType(), True),
	StructField("New", StringType(), True),
	StructField("Configuration", StringType(), True),
	StructField("Size", DoubleType(), True),
	StructField("Language", StringType(), True)
    ])

if __name__ == "__main__":
	sc = SparkContext("spark://10.0.2.15:7077", "QueryDataAppStore")
	spark = SparkSession(sc)
    
	extracted_data_df1 = spark.read.schema(schema).option("multiline", "true").json("hdfs://namenode:9000/extracted_data/app_store/December_2023_4_10/*")
	extracted_data_df2 = spark.read.schema(schema).option("multiline", "true").json("hdfs://namenode:9000/extracted_data/app_store/December_2023_11_17/*")

	extracted_data_df = (extracted_data_df1, extracted_data_df2, )