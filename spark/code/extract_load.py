from pyspark.sql.functions import *
from pyspark.sql.session import SparkSession
from pyspark.context import SparkContext
import requests
from bs4 import BeautifulSoup
from datetime import datetime

if __name__ == "__main__":
	sc = SparkContext("spark://spark-master:7077", "extract_load")
	spark = SparkSession(sc)

	a = requests.get("https://play.google.com/store/games?device=mobile")
	t = a.text
	b = sc.textFile(t)
	b.saveAsTextFile("hdfs://namenode:9000/test.txt")
	# soup = BeautifulSoup(t, "html.parser")
	# l = soup.find_all('a')
	# for i in l:
	# 	if str(i).find("/apps/details") != -1:
	# 		print(str(sum) + "abc" + "{:%d%m%Y}".format(datetime.now()))
	# 		t.saveAsTextFile("hdfs://namenode:9000/text.txt")

	# a = requests.get("https://play.google.com/store/games?device=tablet")
	# t = a.text

	# soup = BeautifulSoup(t, "html.parser")
	# l = soup.find_all('a')
	# for i in l:
	# 	if str(i).find("/apps/details") != -1:
	# 		print(str(sum) + "abc" + "{:%d%m%Y}".format(datetime.now()))