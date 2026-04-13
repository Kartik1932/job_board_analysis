from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("jobs").getOrCreate()

df = spark.read.json("data/raw/*.json")

jobs = df.selectExpr("explode(results) as job").select(
    col("job.id").alias("job_id"),
    col("job.title"),
    col("job.company.display_name").alias("company"),
    col("job.location.display_name").alias("location"),
    col("job.salary_min"),
    col("job.salary_max"),
    col("job.created")
)

jobs.write.mode("overwrite").parquet("data/processed/jobs")
