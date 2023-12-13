from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.session import SparkSession
from pyspark.context import SparkContext

import extract

schema = StructType([
    StructField("link", StringType(), True), 
    StructField("name", StringType(), True), 
    StructField("company", StringType(), True), 
    StructField("rating", StringType(), True), 
    StructField("downloads", StringType(), True), 
    StructField("reviews", StringType(), True), 
    StructField("age", StringType(), True),
    StructField("describe", StringType(), True),
    StructField("lastVersion", StringType(), True),
    StructField("classify", StringType(), True),
    StructField("privacy", StringType(), True)
    ])

if __name__ == "__main__":
	sc = SparkContext("spark://10.0.2.15:7077", "ExtractDataGooglePlay")
	spark = SparkSession(sc)
    
	raw_game_df = spark.read.schema(schema).option("multiline", "true").json("hdfs://namenode:9000/raw_data/google_play/December_2023_4_10/*")

	extracted_game_df = raw_game_df.select(
		raw_game_df['link'].alias("Link"),
        extract.extract_alpha_numeric("name").alias("GameName"),
		extract.extract_alpha_numeric("company").alias("CompanyName"),
		raw_game_df['rating'].alias("Rating"),
		extract.extract_downloads("downloads").alias("Downloads"),
		extract.extract_reviews("reviews").alias("Reviews"),
        raw_game_df['age'].alias("AgeLimit"),
		raw_game_df['describe'].alias("Describe"),
		raw_game_df['lastVersion'].alias("LastVersion"),
		extract.extract_ranking("classify").alias("Raking"),
		extract.extract_classify("classify").alias("Classify"),
        raw_game_df['privacy'].alias("LinkPrivacy")
        )
	
    # extracted_game_df.write.json("hdfs://namenode:9000/extracted_data/google_play/December_2023_4_10.json")