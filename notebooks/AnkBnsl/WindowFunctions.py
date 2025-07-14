from pyspark.sql.window import Window
from pyspark.sql.functions import *

w = Window.partitionBy(col("id")).orderBy(col("value")).desc()

df.withColumn("cumulative_sum",sum(col("value")).over(w).rowsBetween(unboundedPreceding(),currentRow()))