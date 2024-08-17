from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.session import SparkSession
from pyspark.context import SparkContext

import extract, query

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
	sc = SparkContext("spark://10.0.2.15:7077", "ProcessDataGooglePlay")
	spark = SparkSession(sc)
	
	date = "/December_2023_18_24"
    
	raw_data_df = spark.read.schema(schema).option("multiline", "true").json("hdfs://namenode:9000/raw_data/google_play" + date + "/*")

	# Extract raw data
	extracted_data_df = raw_data_df.select(
		raw_data_df['link'].alias("Link"),
        extract.extract_alpha_numeric("name").alias("GameName"),
		extract.extract_alpha_numeric("company").alias("CompanyName"),
		raw_data_df['rating'].alias("Rating"),
		extract.extract_downloads("downloads").alias("Downloads"),
		extract.extract_reviews("reviews").alias("Reviews"),
        raw_data_df['age'].alias("AgeLimit"),
		raw_data_df['describe'].alias("Describe"),
		raw_data_df['lastVersion'].alias("LastVersion"),
		extract.extract_ranking("classify").alias("Raking"),
		extract.extract_classify("classify").alias("Classify"),
        raw_data_df['privacy'].alias("LinkPrivacy")
        )
	
	# Save extracted dataframe to hdfs
	extracted_data_df.write.json("hdfs://namenode:9000/extracted_data/google_play" + date)
	
	# Begin query data
	df_necessary = query.get_df_necessary(extracted_data_df)
	df_distinct = query.get_df_distinct(df_necessary)
	
	df_count_company = query.get_count_company(df_distinct)
	df_order_downloads_game = query.get_order_downloads_game(df_distinct)
	df_order_downloads_company = query.get_oder_downloads_company(df_distinct)
	df_order_reviews_game = query.get_order_reviews_game(df_distinct)
	df_order_reviews_company = query.get_oder_reviews_company(df_distinct)
	df_count_classify = query.get_count_classify(df_distinct)

	# Save some queried dataframes to hdfs
	path = "hdfs://namenode:9000/queried_data/google_play" + date

	df_count_company.write.json(path + "/count_company")
	df_order_downloads_game.write.json(path + "/order_downloads_game")
	df_order_downloads_company.write.json(path + "/order_downloads_company")
	df_order_reviews_game.write.json(path + "/order_reviews_game")
	df_order_reviews_company.write.json(path + "/order_reviews_company")
	df_count_classify.write.json(path + "/count_classify")
