from pyspark.sql.session import SparkSession
from pyspark.sql.types import *
import requests
from bs4 import BeautifulSoup
from datetime import datetime

schema = StructType([
		StructField("url", StringType(), False),
		StructField("content", StringType(), False)
	])

run_time = "{:%d%m%Y}".format(datetime.now())

def extract_load(link, find_con, url_header, classification):
	t = requests.get(link).content
	soup = BeautifulSoup(t, "html.parser")
	l = soup.find_all('a')
	data = []

	for i in l:
		if str(i).find(find_con) != -1:
			url = url_header + i["href"]
			
			try:
				content = requests.get(url, timeout = 5).content
			except requests.exceptions.Timeout:
				try:
					content = requests.get(url, timeout = 5).content
				except requests.exceptions.Timeout:
					try:
						content = requests.get(url, timeout = 5).content
					except requests.exceptions.Timeout:
						continue

			tmp = tuple((url, content.decode("utf-8")))
			data.append(tmp)

	df = spark.createDataFrame(data = data, schema = schema)
	df.write.mode("overwrite").parquet("hdfs://namenode:9000/" + classification + "/" + run_time)

if __name__ == "__main__":
	spark = SparkSession.builder.appName("extract_load").getOrCreate()

	extract_load("https://play.google.com/store/games?device=phone", "/apps/details", "https://play.google.com", "google_play_phone")
	extract_load("https://play.google.com/store/games?device=tablet", "/apps/details", "https://play.google.com", "google_play_tablet")
	# extract_load("https://apps.apple.com/vn/genre/ios-tr%C3%B2-ch%C6%A1i/id6014?l=vi", "/vn/app/", "", "app_store")