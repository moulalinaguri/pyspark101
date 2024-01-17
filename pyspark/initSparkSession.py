from pyspark.sql import SparkSession

if __name__ == "__main__":
    print("Spark application started....")

    spark = SparkSession \
        .builder \
        .appName("Getting started with PySpark") \
        .master("local[*]") \
        .getOrCreate()

    print(spark)
