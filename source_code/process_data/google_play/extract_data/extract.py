from pyspark.sql.functions import udf
from pyspark.sql.types import *

@udf(returnType = StringType())
def extract_alpha_numeric(str):
	result = ""
	for char in str:
		if (char.isalnum()):
			result += char
	return result

@udf(returnType = IntegerType())
def extract_downloads(downloads):
	if len(downloads) != 0:
		tmp = ""
		h = ""
		for char in downloads:
			if (char.isnumeric()):
				tmp += char
			elif (char.isalpha()):
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

@udf(returnType = IntegerType())
def extract_reviews(reviews):
	if len(reviews) != 0:
		tmp = ""
		h = ""
		for char in reviews:
			if (char.isnumeric()) or (char == "."):
				tmp += char
			elif (char.isalpha()):
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

@udf(returnType = StringType())
def extract_ranking(classify):
	if classify[0] == "#":
		result = ""
		for char in classify:
			if (char.isalnum()):
				if (char.isupper()):
					break
				result += char
		return result
	return ""

@udf(returnType = StringType())
def extract_classify(classify):
	start = 0
	for i in range(len(classify)):
		if (classify[i].isupper()):
			start = i
			break
	result = classify[start]
	for i in range(start + 1, len(classify)):
		if (classify[i].isalpha()):
			if (classify[i].isupper()) and (classify[i - 1].isalpha()):
				break
			result += classify[i]
	return result