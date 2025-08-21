user. action transcation.    

 user1, action1, 2025-06-18 3:20:25

 user2, action2, 2025-06-18 3:24:25

 user1, action3, 2025-06-18 3:30:25

 user2, action4, 2025-06-18 3:32:25

 user2, action5, 2025-06-18 3:34:25

 user1, action6, 2025-06-18 3:37:25

 user1, action7, 2025-06-18 3:40:25
 
 from pyspark.sql.window import Window
 from pyspark.sql.functions import lag
 
 w = partitionBy(col("user")).orderBy("transcation")
 
 df.withColumn("lag",lag("transcation",-1,0).over(w)).withColumn("Tag",when(col(lag) < "5","Invalid").otherwise("Valid"))
 
 
 