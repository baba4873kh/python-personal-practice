flights table :  Q . 
 
id	arrival_airport	departure_airport	number_of_flights
1	JFK	LAX	300
2	ORD	JFK	250
3	LAX	ORD	200
4	ATL	JFK	150
5	LAX	ATL	350
6	JFK	ATL	100
7	ORD	ATL	400
 
 
 
Find the busiest airport 

 The airport with the highest total number of flights (arrivals + departures) should be returned
 
with arrival(
    select arrival airport,f1.number_of_flights a, f1.number_of_flights b from flights f1 join flights f2 on f1.arrival_airport = f2.arrival_airport and f1.departure_airport <> f2.departure_airport
    ),
    
    depearture as (
            select departure airport,f1.number_of_flights a, f1.number_of_flights b from flights f1 join flights f2 on f1.departure_airport = f2.departure_airport and f1.arrival_airport <> f2.arrival_airport
        )
        
select airport, a+b total from arrival union depearture

healthcare
scratch
aws databricks
glue, redshift,emr-ec2
managed



        
        
        
        
        
        
        
        