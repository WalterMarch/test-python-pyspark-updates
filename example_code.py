from pyspark import SparkConf
from pyspark.sql import SparkSession

def setup_SparkSession(name):
    spark_config = SparkConf().setAppName(name)
    spark_session = SparkSession.builder.appName(name).config(
        "spark.some.config.option", spark_config).getOrCreate()
    spark_session.sparkContext.setLogLevel("ERROR")
    return spark_session


def setup_sparkContext(spark_session):
    spark_context = spark_session.sparkContext
    spark_context._jsc.hadoopConfiguration().set(
        "mapreduce.fileoutputcommitter.marksuccessfuljobs",
        "false")

    return spark_context

def df_from_file(in_file):
    spark = setup_SparkSession("sparky")
    sc = setup_sparkContext(spark)

    rdd = sc.textFile(in_file)
    print(rdd.collect())
    df = spark.read.json(rdd)

    # return df


df_from_file("part-states")