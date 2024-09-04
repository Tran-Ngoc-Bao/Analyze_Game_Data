from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

run_time = "{:%d%m%Y}".format(datetime.now())
run_time ="03092024"

if __name__ == "__main__":
	spark = SparkSession.builder.config("spark.jars", "/opt/code/postgresql-42.2.5.jar").master("spark://spark-master:7077").appName("transform_app_store").getOrCreate()

	df = spark.read.parquet("hdfs://namenode:9000/app_store/" + run_time + "/*.parquet")
	pd_df = df.toPandas()
	list_url = pd_df["url"].tolist()
	list_content = pd_df["content"].tolist()

	data = []
	for i in range(2):
		soup = BeautifulSoup(list_content[i], 'html.parser')
          
		nameAndAge = soup.find_all('h1')
		company = soup.find_all(class_ = 'product-header__identity')
		raking = soup.find_all(class_ = 'product-header__list__item')
		ratingAndReviews = soup.find_all(class_ = 'we-rating-count')
		price = soup.find_all(class_ = 'app-header__list__item--price')
		availablity = soup.find_all(class_ = 'gallery-nav__items')
		describe = soup.find_all(class_ = 'we-truncate')
		new = soup.find_all(class_ = 'whats-new__content')
		configurationAndSize = soup.find_all(class_ = 'information-list__item__definition')
		language = soup.find_all(class_ = 'information-list__item')

		tmp = {}
          
		tmp['link'] = list_url[i]
		tmp['nameAndAge'] = nameAndAge[0].text
		if len(company) == 0:
			continue
		tmp['company'] = company[0].text
		tmp['ranking'] = raking[0].text
		if len(ratingAndReviews) == 0:
			tmp['ratingAndReviews'] = ""
		else:
			tmp['ratingAndReviews'] = ratingAndReviews[0].text
		tmp['price'] = price[0].text
		if len(availablity) == 0:
			tmp['availablity'] = ""
		else:
			tmp['availablity'] = availablity[0].text
		tmp['describe'] = describe[0].text
		if len(new) == 0:
			tmp['new'] = ""
		else:
			tmp['new'] = new[0].text

		tmp['configuration'] = configurationAndSize[3].text
		tmp['size'] = configurationAndSize[1].text
		tmp['language'] = language[4].text

		data.append(tmp)
	
	df_ = pd.DataFrame(data)
	print(df_)