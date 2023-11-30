import pyspark
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.session import SparkSession
from pyspark.context import SparkContext

import extract, queries

schema = StructType([
    StructField("tên", StringType(), True), 
    StructField("mô tả", StringType(), True), 
    StructField("có gì mới", StringType(), True), 
    StructField("xếp hạng", StringType(), True), 
    StructField("nhà cung cấp", StringType(), True), 
    StructField("kích cỡ", StringType(), True), 
    StructField("giá", IntegerType(), True)
    ])

if __name__ == "__main__":
	sc = SparkContext("spark://10.0.2.15:7077", "AnalyzeGameData")
	spark = SparkSession(sc)
    
	raw_game_df = spark.read.schema(schema).option("multiline", "true").json("hdfs://namenode:9000/appstore/*")

	extracted_game_df = raw_game_df.select(
        
        )

    ##========make some query==========================================


	##========save some df to hdfs========================


