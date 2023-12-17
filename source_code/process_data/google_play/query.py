from pyspark.sql.functions import *

def get_df_necessary(df):
    return df.select(
        df["GameName"],
        df["CompanyName"],
        df["Rating"],
        df["Downloads"],
        df["Reviews"],
        df["Raking"],
        df["Classify"]
        )

def get_df_distinct(df):
    return df.distinct()

def get_count_company(df):
    return df.select(countDistinct("CompanyName").alias("Companies"))

def get_order_downloads_game(df):
    return df.where("Downloads >= 100000000").select("GameName", "Downloads")

def get_oder_downloads_company(df):
    df_tmp = df.groupBy("Companyname").agg(sum("Downloads").alias("Downloads"))
    return df_tmp.where("Downloads >= 200000000")

def get_order_reviews_game(df):
    return df.where("Reviews >= 10000000").select("GameName", "Reviews")

def get_oder_reviews_company(df):
    df_tmp = df.groupBy("Companyname").agg(sum("Reviews").alias("Reviews"))
    return df_tmp.where("Reviews >= 20000000")

def get_count_classify(df):
    return df.groupBy("Classify").agg(count("GameName").alias("Games"))