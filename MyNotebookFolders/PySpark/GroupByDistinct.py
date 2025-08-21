df.groupBy("country").agg(sum("revenue"),count("state"),countDistinct("product"))

df.withColumn("roi",when(col("roi").isnull(),col("amount")*col("interest")*col("")).otherwise("roi"))