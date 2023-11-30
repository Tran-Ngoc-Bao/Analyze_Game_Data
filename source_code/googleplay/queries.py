import pyspark
from pyspark.sql.functions import *

def get_distinct(extracted_game_df):
	return extracted_game_df.distinct()

def get_sum_reviews_company(df_distinct):
	return df_distinct.groupBy("CompanyName").agg(sum("Reviews").alias("TotalReviews"))

def get_most_of_company(df_reviews_company):
	return df_reviews_company.where("TotalReviews > 10000000")

def get_count_game_ageLimit(df_distinct):
	return df_distinct.groupBy("AgeLimit").agg(count("GameName").alias("Games"))

def get_count_game_category(df_distinct):
	return df_distinct.groupBy("Category").agg(count("GameName").alias("Games"))
