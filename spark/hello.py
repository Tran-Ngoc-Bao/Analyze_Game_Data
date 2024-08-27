from pyspark.sql.functions import *
from pyspark.sql.session import SparkSession
from pyspark.context import SparkContext

if __name__ == "__main__":
	sc = SparkContext("spark://spark-master:7077", "test")

	dataDictionary = [
        ('James',{'hair':'black','eye':'brown'}),
        ('Michael',{'hair':'brown','eye':None}),
        ('Robert',{'hair':'red','eye':'black'}),
        ('Washington',{'hair':'red','eye':'grey'}),
        ('Jefferson',{'hair':'red','eye':''})
        ]
	
	spark = SparkSession(sc)
	df = spark.createDataFrame(data=dataDictionary, schema = ["name","properties"])
	df.write.save('hdfs://namenode:9000/test', format='parquet', mode='append')