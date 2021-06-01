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


![image](https://user-images.githubusercontent.com/79819331/120372111-bcc08e00-c2e4-11eb-8f6a-6edfef1d2ed6.png)

Histogram of temperature in Hawaii

