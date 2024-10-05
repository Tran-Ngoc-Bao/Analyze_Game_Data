from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
from bs4 import BeautifulSoup
from datetime import datetime

# run_time = "{:%d%m%Y}".format(datetime.now())
run_time ="09092024"

def extract_alpha_numeric(str):
	result = ""
	for char in str:
		if char.isalnum() or char == ' ':
			result += char
	return result

def extract_downloads(downloads):
	if len(downloads) != 0:
		tmp = ""
		h = ""
		for char in downloads:
			if char.isnumeric():
				tmp += char
			elif char.isalpha():
				h = char
				break

		if h == "K":
			return int() * 1000
		if h == "M":
			return int(tmp) * 1000000
		if h == "B":
			return int(tmp) * 1000000000
		return int(tmp)
	return 0

def extract_reviews(reviews):
	if len(reviews) != 0:
		tmp = ""
		h = ""
		for char in reviews:
			if char.isnumeric() or char == ".":
				tmp += char
			elif char.isalpha():
				h = char
				break

		if h == "K":
			return int(float(tmp) * 1000)
		if h == "M":
			return int(float(tmp) * 1000000)
		if h == "B":
			return int(float(tmp) * 1000000000)
		return int(tmp)
	return 0

def extract_ranking(classify):
	if classify[0] == "#":
		result = ""
		for char in classify:
			if char.isnumeric():
				if char.isupper():
					break
				result += char
		return int(result)
	return 1000000000

def extract_classify(classify):
	start = 0
	for i in range(len(classify)):
		if classify[i].isupper():
			start = i
			break
	result = classify[start]
	for i in range(start + 1, len(classify)):
		if classify[i].isalpha():
			if classify[i].isupper() and classify[i - 1].isalpha():
				break
			result += classify[i]
	return result

def solution(classification):
    df = spark.read.parquet("hdfs://namenode:9000/" + classification +"/" + run_time + "/*.parquet")
    list_url = df.select("url").collect()
    list_content = df.select("content").collect()

    data = []
    for i in range(len(list_url)):
        soup = BeautifulSoup(list_content[i].content, 'html.parser')
        name = soup.find_all('h1')
        company = soup.find_all(class_ = 'Vbfug')
        ratingAndDownloads = soup.find_all(class_ = 'ClM7O')
        reviewsAndAge = soup.find_all(class_ = 'g1rdde')
        descirbe = soup.find_all(class_ = 'bARER')
        lastVersion = soup.find_all(class_ = 'xg1aie')
        classify = soup.find_all(class_ = 'Uc6QCc')
        privacy = soup.find_all(class_ = 'WpHeLc')
        
        tmp = {}

        if len(name) == 0:
            continue
        tmp['name'] = extract_alpha_numeric(name[0].text)
        tmp['link'] = list_url[i].url
        tmp['company'] = extract_alpha_numeric(company[0].text)
        if len(ratingAndDownloads) == 1:
            tmp['rating'] = 0.0
            tmp['downloads'] = 0
        elif len(ratingAndDownloads) == 2:
            tmp['rating'] = 0.0
            tmp['downloads'] = extract_downloads(ratingAndDownloads[0].text)
        else:
            tmp['rating'] = float(ratingAndDownloads[0].text[:3])
            tmp['downloads'] = extract_downloads(ratingAndDownloads[1].text)
        if len(reviewsAndAge) == 1:
            tmp['reviews'] = 0
            tmp['age'] = reviewsAndAge[0].text
        elif len(reviewsAndAge) == 2:
            tmp['reviews'] = 0
            tmp['age'] = reviewsAndAge[1].text
        else:
            tmp['reviews'] = extract_reviews(reviewsAndAge[0].text)
            tmp['age'] = reviewsAndAge[2].text
        tmp['describe'] = descirbe[0].text
        tmp['lastVersion'] = lastVersion[0].text
        tmp['ranking'] = extract_ranking(classify[0].text)
        tmp['classify'] = extract_classify(classify[0].text)
        tmp['privacy'] = "https://play.google.com" + privacy[1].get('href')

        data.append(tmp)

    df_ = spark.createDataFrame(data)
    url = "jdbc:postgresql://data-warehouse:5432/datawarehouse"
    properties = {"user": "datawarehouse","password": "datawarehouse"}
    df_.write.mode("overwrite").jdbc(url=url, table=classification + "_" + run_time, properties=properties)

if __name__ == "__main__":
	spark = SparkSession.builder.config("spark.jars", "/opt/code/postgresql-42.2.5.jar").master("spark://spark:7077").appName("transform_google_play").getOrCreate()

	solution("google_play_phone")
	solution("google_play_tablet")