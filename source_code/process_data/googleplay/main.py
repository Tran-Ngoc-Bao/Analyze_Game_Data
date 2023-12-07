import pyspark
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql.session import SparkSession
from pyspark.context import SparkContext

import extract, queries

schema = StructType([
    StructField("url", StringType(), True), 
    StructField("wallVideo", StringType(), True), 
    StructField("trailer", StringType(), True), 
    StructField("name", StringType(), True), 
    StructField("company", StringType(), True), 
    StructField("companyURL", StringType(), True), 
    StructField("avatar", StringType(), True),
    StructField("rating", StringType(), True),
    StructField("reviews", StringType(), True),
    StructField("downloads", StringType(), True),
    StructField("ageLimit", StringType(), True),
    StructField("imageList", ArrayType(StringType()), True),
    StructField("about", StringType(), True),
    StructField("categoryList", MapType(StringType(), StringType()), True),
    StructField("price", StringType(), True),
    StructField("isAvailable", StringType(), True),
    StructField("update", StringType(), True),
    ])

if __name__ == "__main__":
	sc = SparkContext("spark://10.0.2.15:7077", "AnalyzeGameData")
	spark = SparkSession(sc)
    
	raw_game_df = spark.read.schema(schema).option("multiline", "true").json("hdfs://namenode:9000/googleplay/*")

	extracted_game_df = raw_game_df.select(
        extract.extract_name("name").alias("GameName"),
        extract.extract_company("company").alias("CompanyName"),
        extract.extract_rating("rating").alias("Rating"),
        extract.extract_reviews("reviews").alias("Reviews"),
        extract.extract_ageLimit("ageLimit").alias("AgeLimit")
        )

    ##========make some query==========================================
	df_distinct = queries.get_distinct(extracted_game_df)
	#df_reviews_company = queries.get_sum_reviews_company(df_distinct)  
	#df_most_company = queries.get_most_of_company(df_reviews_company)
	#df_game_ageLimit = queries.get_count_game_ageLimit(df_distinct)

	##========save some df to hdfs========================
	df_distinct.write.json("hdfs://namenode:9000/extracteddata/googleplay/distinct")
	#df_most_company.write.json("hdfs://namenode:9000/extracteddata/googleplay/mostCompany")
	#df_game_ageLimit.write.json("hdfs://namenode:9000/extracteddata/googleplay/gameAgeLimit")

