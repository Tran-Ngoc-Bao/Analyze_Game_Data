from pyspark.sql.functions import udf
from pyspark.sql.types import *

@udf(returnType = StringType())
def extract_name(nameAndAge):
	result = ""
	for char in nameAndAge:
		if (char.isalpha()):
			result += char
	return result

@udf(returnType = StringType())
def extract_age(nameAndAge):
	result = ""
	for char in nameAndAge:
		if (char.isnumeric()):
			result += char
	return result

@udf(returnType = StringType())
def extract_company(company):
	result = ""
	for char in company:
		if (char.isalpha()):
			result += char
	return result

@udf(returnType = StringType())
def extract_raking(ranking):
	result = ""
	for char in ranking:
		if (char.isalnum()):
			result += char
	return result

@udf(returnType = StringType())
def extract_classify(ranking):
	result = ""
	for char in ranking:
		if (char.isalpha()):
			result += char
	return result