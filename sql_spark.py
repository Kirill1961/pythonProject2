# from pyspark.sql import SparkSession
#
# spark = SparkSession.builder.appName("CRM_ETL").getOrCreate()
#
# # Создаём DataFrame
# df = spark.read.parquet("data/customers")
#
# # Регистрируем временное представление
# df.createOrReplaceTempView("customers")
#
# # Выполняем SQL
# result = spark.sql("""
#     SELECT
#         city,
#         COUNT(*) AS customers_count
#     FROM customers
#     GROUP BY city
# """)

import pandas as pd
from pyspark.sql.functions import count

df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": list("abbab")})

result = (
    df
    # .groupBy("B")
    .agg(count("*").alias("customers_count"))
)