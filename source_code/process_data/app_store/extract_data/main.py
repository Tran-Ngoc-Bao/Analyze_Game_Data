from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.session import SparkSession
from pyspark.context import SparkContext

import extract

schema = StructType([
    StructField("link", StringType(), True), 
    StructField("nameAndAge", StringType(), True), 
    StructField("company", StringType(), True), 
    StructField("ranking", StringType(), True), 
    StructField("ratingAndReviews", StringType(), True), 
    StructField("price", StringType(), True), 
    StructField("availablity", StringType(), True),
    StructField("describe", StringType(), True),
    StructField("new", StringType(), True),
    StructField("configuration", StringType(), True),
    StructField("size", StringType(), True),
	StructField("language", StringType(), True)
    ])

if __name__ == "__main__":
	sc = SparkContext("spark://10.0.2.15:7077", "ExtractDataAppStore")
	spark = SparkSession(sc)
    
	raw_game_df = spark.read.schema(schema).option("multiline", "true").json("hdfs://namenode:9000/app_store/December_2023_4_10/*")

	extracted_game_df = raw_game_df.select(
		raw_game_df['link'].alias("Link"),
        extract.extract_name("nameAndAge").alias("GameName"),
        extract.extract_age("nameAndAge").alias("AgeLimit"),
        extract.extract_company("company").alias("CompanyName"),
		extract.extract_raking("ranking").alias("Raking"),
		extract.extract_classify("ranking").alias("Classify"),
        extract.extract_rating("rating").alias("Rating"),
        extract.extract_reviews("reviews").alias("Reviews")
        )