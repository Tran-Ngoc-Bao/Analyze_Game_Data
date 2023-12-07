from pyspark.sql.functions import udf
from pyspark.sql.types import *

@udf(returnType=StringType())
def extract_name(name):
	while " " in name:
		name = name.replace(" ", "_")
	while ":" in name:
		name = name.replace(":", "_")
	return name

@udf(returnType=StringType())
def extract_company(company):
	for i in range(len(company) - 1):
		if company[i] == " ":
			return company[:i]
	return company

@udf(returnType=FloatType())
def extract_rating(rating):
	if len(rating) == 0:
		return 0.0
	return float(rating[:3])

@udf(returnType=IntegerType())
def extract_reviews(reviews):
    if len(reviews) == 0:
        return 0
    h = ""
    for i in range(len(reviews)):
        if reviews[i] == " " or reviews[i] == "K" or reviews[i] == "M":
            h = reviews[i]
            reviews = reviews[:i]
            break
    if h == " ":
        return int(reviews)
    if h == "K":
        return int(float(reviews) * 1000)
    if h == "M":
        return int(float(reviews) * 1000000)
    
@udf(returnType=StringType())
def extract_ageLimit(ageLimit):
    return ageLimit[10:]
