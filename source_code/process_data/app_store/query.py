from pyspark.sql.functions import *
from pyspark.sql.types import StringType

def get_df_necessary(df):
    return df.select(
        df["GameName"],
        df["AgeLimit"],
        df["CompanyName"],
        df["Raking"],
        df["Classify"],
        df["Rating"],
        df["Reviews"],
        classify_by_price("Price").alias("Price"),
        classify_by_size("Size").alias("Size")
        )

@udf(returnType = StringType())
def classify_by_price(price):
    if price == 0:
        return "Free"
    if price < 50000:
        return "LowPrice"
    if price < 100000:
        return "MediumPrice"
    return "HighPrice"

@udf(returnType = StringType())
def classify_by_size(size):
    if size < 100:
        return "LowSize"
    if size < 500:
        return "MediumSize"
    if size < 1000:
        return "HighSize"
    return "VeryHighSize"

def get_df_distinct(df):
    return df.distinct()

def get_count_ageLimit(df):
    return df.groupBy("AgeLimit").select("AgeLimit", count("GameName").alias("Games"))

def get_count_company(df):
    return df.select(countDistinct("CompanyName").alias("Companies"))

def get_count_classify(df):
    return df.groupBy("Classify").select("Classify", count("GameName").alias("Games"))

def get_order_reviews_game(df):
    return df.where("Reviews >= 1000000").select("GameName", "Reviews")

def get_oder_reviews_company(df):
    df_tmp = df.groupBy("Companyname").select("CompanyName", sum("Reviews").alias("Reviews"))
    return df_tmp.where("Reviews >= 5000000")

def get_count_price(df):
    return df.groupBy("Price").select("Price", count("GameName").alias("Games"))

def get_count_size(df):
    return df.groupBy("Size").select("Size", count("GameName").alias("Games"))