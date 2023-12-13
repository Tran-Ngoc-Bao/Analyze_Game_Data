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
    
	raw_game_df = spark.read.schema(schema).option("multiline", "true").json("hdfs://namenode:9000/raw_data/app_store/December_2023_4_10/*")

	extracted_game_df = raw_game_df.select(
		raw_game_df['link'].alias("Link"),
        extract.extract_alpha("nameAndAge").alias("GameName"),
        extract.extract_numeric("nameAndAge").alias("AgeLimit"),
        extract.extract_alpha_numeric("company").alias("CompanyName"),
		extract.extract_alpha_numeric("ranking").alias("Raking"),
		extract.extract_classify("ranking").alias("Classify"),
        extract.extract_rating("ratingAndReviews").alias("Rating"),
        extract.extract_reviews("reviews").alias("Reviews"),
		extract.extract_price("price").alias("Price"),
		extract.extract_alpha_numeric("availablity").alias("Availablity"),
		extract.extract_alpha_numeric("describe").alias("Describe"),
		extract.extract_alpha_numeric("new").alias("New"),
		extract.extract_alpha_numeric("configuration").alias("Configuration"),
		extract.extract_size("size").alias("Size"),
        extract.extract_alpha_numeric("language").alias("Language")
        )
	
    # extracted_game_df.write.json("hdfs://namenode:9000/extracted_data/app_store/December_2023_4_10.json")