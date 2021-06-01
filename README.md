# sqlalchemy-challenge
 To help with trip planning, some climate analysis on the area of Hawaii needs to be done.
 
 Use SQLAlchemy create_engine to connect to your sqlite database.
 
 # create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite",echo=False)


Use SQLAlchemy automap_base() to reflect your tables into classes and save a reference to those classes called Station and Measurement.

# reflect an existing database into a new model

Base=automap_base()

# reflect the tables

Base.prepare(engine,reflect=True)

# Save references to each table

measurement=Base.classes.measurement

station=Base.classes.station


Link Python to the database by creating an SQLAlchemy session.

# Create our session (link) from Python to the DB

session=Session(engine)


