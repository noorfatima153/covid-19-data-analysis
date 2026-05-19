from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("COVID Analysis").getOrCreate()
