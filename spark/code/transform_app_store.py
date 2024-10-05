from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
from bs4 import BeautifulSoup
from datetime import datetime

# run_time = "{:%d%m%Y}".format(datetime.now())
run_time ="09092024"

def extract_alpha(str):
	str = str.strip()
	result = ""
	for char in str:
		if char.isalpha() or char == ' ':
			result += char
	return result

def extract_numeric(str):
	result = ""
	for char in str:
		if char.isnumeric():
			result += char
	return result

def extract_alpha_numeric(str):
	str = str.strip()
	result = ""
	for char in str:
		if char.isalnum() or char == ' ':
			result += char
	return result

def extract_ageLimit(nameAndAge):
	result = ""
	for char in nameAndAge[(len(nameAndAge) - 5):]:
		if char.isnumeric():
			result += char
	return int(result)

def extract_classify(ranking):
	ranking = ranking.strip()
	result = ""
	for char in ranking:
		if char.isalpha() or char == ' ':
			result += char
	return result[7:]

def extract_rating(ratingAndReviews):
	if len(ratingAndReviews) != 0:
		return float(ratingAndReviews[:3].replace(",", "."))
	return 0.0

def extract_reviews(ratingAndReviews):
	if len(ratingAndReviews) != 0:
		tmp = ""
		h = ""
		for char in ratingAndReviews[6:]:
			if char.isnumeric():
				tmp += char
			elif char == ",":
				tmp += "."
			elif char.isalpha():
				h = char
				break

		if h == "N":
			return int(float(tmp) * 1000)
		if h == "T":
			return int(float(tmp) * 1000000)
		return int(float(tmp))
	return 0

def extract_price(price):
	result = ""
	for char in price:
		if char.isnumeric():
			result += char
	if len(result) != 0:
		return int(result)
	return 0

def extract_size(size):
	tmp = ""
	h = ""
	for char in size:
		if char.isnumeric():
			tmp += char
		elif (char == ","):
			tmp += "."
		elif char.isalpha():
			h = char
			break

	if h == "G":
		return float(tmp) * 1000
	return float(tmp)

if __name__ == "__main__":
	spark = SparkSession.builder.config("spark.jars", "/opt/code/postgresql-42.2.5.jar").master("spark://spark:7077").appName("transform_app_store").getOrCreate()

	df = spark.read.parquet("hdfs://namenode:9000/app_store/" + run_time + "/*.parquet")
	list_url = df.select("url").collect()
	list_content = df.select("content").collect()

	data = []
	for i in range(len(list_url)):
		soup = BeautifulSoup(list_content[i].content, 'html.parser')
          
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
          
		if len(company) == 0:
			continue
		tmp['company'] = extract_alpha_numeric(company[0].text)
		tmp['link'] = list_url[i].url
		tmp['name'] = extract_alpha(nameAndAge[0].text)
		tmp['age'] = extract_ageLimit(nameAndAge[0].text)
		tmp['ranking'] = int(extract_numeric(raking[0].text))
		tmp['classify'] = extract_classify(raking[0].text)
		if len(ratingAndReviews) == 0:
			tmp['rating'] = ""
			tmp['reviews'] = 0
		else:
			tmp['rating'] = extract_rating(ratingAndReviews[0].text)
			tmp['reviews'] = extract_reviews(ratingAndReviews[0].text)
		tmp['price'] = extract_price(price[0].text)
		if len(availablity) == 0:
			tmp['availablity'] = ""
		else:
			tmp['availablity'] = extract_alpha_numeric(availablity[0].text)
		tmp['describe'] = extract_alpha_numeric(describe[0].text)
		if len(new) == 0:
			tmp['new'] = ""
		else:
			tmp['new'] = extract_alpha_numeric(new[0].text)

		tmp['configuration'] = extract_alpha_numeric(configurationAndSize[3].text)
		tmp['size'] = extract_size(configurationAndSize[1].text)
		tmp['language'] = extract_alpha_numeric(language[4].text)

		data.append(tmp)
	
	df_ = spark.createDataFrame(data)
	url = "jdbc:postgresql://data-warehouse:5432/datawarehouse"
	properties = {"user": "datawarehouse","password": "datawarehouse"}
	df_.write.mode("overwrite").jdbc(url=url, table="app_store_" + run_time, properties=properties)