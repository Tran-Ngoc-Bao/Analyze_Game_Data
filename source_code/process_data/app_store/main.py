from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.session import SparkSession
from pyspark.context import SparkContext

import extract, query

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
	sc = SparkContext("spark://10.0.2.15:7077", "ProcessDataAppStore")
	spark = SparkSession(sc)
	
	date = "/December_2023_18_24"

	raw_data_df = spark.read.schema(schema).option("multiline", "true").json("hdfs://namenode:9000/raw_data/app_store" + date + "/*")

	# Extract raw data
	extracted_data_df = raw_data_df.select(
		raw_data_df['link'].alias("Link"),
        extract.extract_alpha("nameAndAge").alias("GameName"),
        extract.extract_numeric("nameAndAge").alias("AgeLimit"),
        extract.extract_alpha_numeric("company").alias("CompanyName"),
		extract.extract_alpha_numeric("ranking").alias("Raking"),
		extract.extract_classify("ranking").alias("Classify"),
        extract.extract_rating("ratingAndReviews").alias("Rating"),
        extract.extract_reviews("ratingAndReviews").alias("Reviews"),
		extract.extract_price("price").alias("Price"),
		extract.extract_alpha_numeric("availablity").alias("Availablity"),
		extract.extract_alpha_numeric("describe").alias("Describe"),
		extract.extract_alpha_numeric("new").alias("New"),
		extract.extract_alpha_numeric("configuration").alias("Configuration"),
		extract.extract_size("size").alias("Size"),
        extract.extract_alpha_numeric("language").alias("Language")
        )
	
	# Save extracted dataframe to hdfs
	extracted_data_df.write.json("hdfs://namenode:9000/extracted_data/app_store" + date)
	
	# Begin query data
	df_necessary = query.get_df_necessary(extracted_data_df)
	df_distinct = query.get_df_distinct(df_necessary)
	
	df_count_ageLimit = query.get_count_ageLimit(df_distinct)
	df_count_company = query.get_count_company(df_distinct)
	df_count_classify = query.get_count_classify(df_distinct)
	df_order_reviews_game = query.get_order_reviews_game(df_distinct)
	df_order_reviews_company = query.get_oder_reviews_company(df_distinct)
	df_count_price = query.get_count_price(df_distinct)
	df_count_size = query.get_count_size(df_distinct)

	# Save some queried dataframes to hdfs
	path = "hdfs://namenode:9000/queried_data/app_store" + date
	
	df_count_ageLimit.write.json(path + "/count_ageLimit")
	df_count_company.write.json(path + "/count_company")
	df_count_classify.write.json(path + "/count_classify")
	df_order_reviews_game.write.json(path + "/order_reviews_game")
	df_order_reviews_company.write.json(path + "/order_reviews_company")
	df_count_price.write.json(path + "/count_price")
	df_count_size.write.json(path + "/count_size")