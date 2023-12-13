from pyspark.sql.functions import udf
from pyspark.sql.types import *

@udf(returnType = StringType())
def extract_alpha(str):
	result = ""
	for char in str:
		if (char.isalpha()):
			result += char
	return result

@udf(returnType = StringType())
def extract_numeric(str):
	result = ""
	for char in str:
		if (char.isnumeric()):
			result += char
	return result

@udf(returnType = StringType())
def extract_alpha_numeric(str):
	result = ""
	for char in str:
		if (char.isalnum()):
			result += char
	return result

@udf(returnType = StringType())
def extract_classify(ranking):
	result = ""
	for char in ranking:
		if (char.isalpha()):
			result += char
	return result[5:]

@udf(returnType = StringType())
def extract_rating(ratingAndReviews):
	if len(ratingAndReviews) != 0:
		return ratingAndReviews[:3]
	return ""

@udf(returnType = IntegerType())
def extract_reviews(ratingAndReviews):
	if len(ratingAndReviews) != 0:
		tmp = ""
		h = ""
		for char in ratingAndReviews[6:]:
			if (char.isnumeric()):
				tmp += char
			elif (char == ","):
				tmp += "."
			elif (char.isalpha()):
				h = char
				break

		if h == "N":
			return int(float(tmp) * 1000)
		if h == "T":
			return int(float(tmp) * 1000000)
		return int(tmp)
	return 0

@udf(returnType = IntegerType())
def extract_price(price):
	result = ""
	for char in price:
		if (char.isnumeric()):
			result += char
	if len(result) != 0:
		return int(result)
	return 0

@udf(returnType = DoubleType())
def extract_size(size):
	tmp = ""
	h = ""
	for char in size:
		if (char.isnumeric()):
			tmp += char
		elif (char == ","):
			tmp += "."
		elif (char.isalpha()):
			h = char
			break

	if h == "G":
		return float(tmp) * 1000
	return float(tmp)