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


![image](https://user-images.githubusercontent.com/79819331/120374430-89cbc980-c2e7-11eb-9c4b-9c580b137976.png)


Precipitation of Hawaii


Design a query to retrieve the last 12 months of temperature observation data (TOBS).


![image](https://user-images.githubusercontent.com/79819331/120372111-bcc08e00-c2e4-11eb-8f6a-6edfef1d2ed6.png)


Histogram of temperature in Hawaii


Design a Flask API based on the queries that you have just developed. Use Flask to create your routes.


Home page: List all routes that are available.


![image](https://user-images.githubusercontent.com/79819331/120373353-40c74580-c2e6-11eb-815d-1b795ede0409.png)



Convert the query results to a dictionary using `date` as the key and `prcp` as the value. Return the JSON representation of your dictionary.


![image](https://user-images.githubusercontent.com/79819331/120373394-4de43480-c2e6-11eb-9d55-00a4f673ee07.png)


Return a JSON list of stations from the dataset.


![image](https://user-images.githubusercontent.com/79819331/120374557-af58d300-c2e7-11eb-87da-014bd554e992.png)



Query the dates and temperature observations of the most active station for the last year of data. Return a JSON list of temperature observations (TOBS) for the previous year.


![image](https://user-images.githubusercontent.com/79819331/120374248-525d1d00-c2e7-11eb-8a01-d9cdd3d1b162.png)





When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive. Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

![image](https://user-images.githubusercontent.com/79819331/120373730-b3382580-c2e6-11eb-8406-847769c87635.png)


Use pandas to identify the average temperature in June at all stations across all available years in the dataset. Do the same for December temperature. Use the t-test to determine whether the difference in the means, if any, is statistically significant. A paired t-test or an unpaired t-test should be used? Why?

![image](https://user-images.githubusercontent.com/79819331/120375015-458cf900-c2e8-11eb-9674-3a06de2ba103.png)

Get June data.

![image](https://user-images.githubusercontent.com/79819331/120375205-8422b380-c2e8-11eb-9ffa-e3f1eff4858e.png)


Get December data.

![image](https://user-images.githubusercontent.com/79819331/120375425-ca781280-c2e8-11eb-8603-38cda3fca83a.png)

There is significant difference between June temperature and December temperature.
Unpaired t-test is used because the two groups are independent. The number of two groups is different. One is 1700 and the other is 1517.



Plot the min, avg, and max temperature from your previous query as a bar chart.


![image](https://user-images.githubusercontent.com/79819331/120376212-9b15d580-c2e9-11eb-83f7-c567fd79014c.png)

Average temperature of Hawaii from 2016-08-01 to 2017-08-01.




Use Pandas to plot an area plot for the daily temperature normals.

![image](https://user-images.githubusercontent.com/79819331/120376987-86860d00-c2ea-11eb-90e0-6a2cdac28307.png)

Daily minimal, average, and maximal temperature of Hawaii during the period between 2017-08-01 and 2017-08-07.



