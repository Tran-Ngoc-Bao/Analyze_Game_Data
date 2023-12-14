from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.session import SparkSession
from pyspark.context import SparkContext

import query

schema = StructType([
    StructField("Link", StringType(), True), 
    StructField("GameName", StringType(), True), 
    StructField("CompanyName", StringType(), True), 
    StructField("Rating", StringType(), True), 
    StructField("Downloads", IntegerType(), True), 
    StructField("Reviews", IntegerType(), True), 
    StructField("AgeLimit", StringType(), True),
    StructField("Describe", StringType(), True),
    StructField("LastVersion", StringType(), True),
    StructField("Raking", StringType(), True),
    StructField("Classify", StringType(), True),
	StructField("LinkPrivacy", StringType(), True)
    ])

if __name__ == "__main__":
	sc = SparkContext("spark://10.0.2.15:7077", "ExtractDataAppStore")
	spark = SparkSession(sc)
    
	extracted_data_df1 = spark.read.schema(schema).option("multiline", "true").json("hdfs://namenode:9000/raw_data/google_play/December_2023_4_10/*")
	extracted_data_df2 = spark.read.schema(schema).option("multiline", "true").json("hdfs://namenode:9000/raw_data/google_play/December_2023_11_17/*")
	
	extracted_data_df = (extracted_data_df1, extracted_data_df2, )