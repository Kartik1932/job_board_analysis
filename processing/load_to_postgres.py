from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("load_to_postgres").getOrCreate()

jobs = spark.read.parquet("data/processed/jobs")

jobs.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://localhost:5432/jobsdb") \
    .option("dbtable", "jobs") \
    .option("user", "postgres") \
    .option("password", "password") \
    .option("driver", "org.postgresql.Driver") \
    .mode("overwrite") \
    .save()