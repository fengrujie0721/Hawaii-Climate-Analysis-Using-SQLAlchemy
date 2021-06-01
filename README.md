# SQLAlchemy-Challenge
 To help with trip planning, some climate analysis on the area of Hawaii needs to be done.
 
 Use SQLAlchemy create_engine to connect to your sqlite database.
 
 
engine = create_engine("sqlite:///Resources/hawaii.sqlite",echo=False)


Use SQLAlchemy automap_base() to reflect your tables into classes and save a reference to those classes called Station and Measurement.



Base=automap_base()



Base.prepare(engine,reflect=True)



measurement=Base.classes.measurement

station=Base.classes.station


Link Python to the database by creating an SQLAlchemy session.



session=Session(engine)


Exploratory Precipitation Analysis


![image](https://user-images.githubusercontent.com/79819331/120371820-589dca00-c2e4-11eb-9ffa-fb7fb154697c.png)


Precipitation of Hawaii


Design a query to retrieve the last 12 months of temperature observation data (TOBS).


![image](https://user-images.githubusercontent.com/79819331/120372111-bcc08e00-c2e4-11eb-8f6a-6edfef1d2ed6.png)


Histogram of temperature in Hawaii


Design a Flask API based on the queries that you have just developed. Use Flask to create your routes.


Home page: List all routes that are available.


![image](https://user-images.githubusercontent.com/79819331/120373353-40c74580-c2e6-11eb-815d-1b795ede0409.png)



Convert the query results to a dictionary using `date` as the key and `prcp` as the value. Return the JSON representation of your dictionary.


![image](https://user-images.githubusercontent.com/79819331/120373394-4de43480-c2e6-11eb-9d55-00a4f673ee07.png)


When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive. Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

![image](https://user-images.githubusercontent.com/79819331/120373730-b3382580-c2e6-11eb-8406-847769c87635.png)
