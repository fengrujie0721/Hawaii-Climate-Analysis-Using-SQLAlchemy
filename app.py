import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#create engine
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
measurement=Base.classes.measurement
station=Base.classes.station

# Flask Setup

app = Flask(__name__)



# Flask Routes


@app.route("/")
def welcome():
    """List all routes that are availabel."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/stations2<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all passenger names"""
    # Query date and prcp
    dates = session.query(measurement.date).all()
    prcp=session.query(measurement.prcp).all()
    #close the session
    session.close()

    # Convert list of tuples into dictionary
    all_dates=list(np.ravel(dates))
    all_prcp=list(np.ravel(prcp))
    
    dictionary=dict(zip(all_dates,all_prcp))
        
    
    return jsonify(dictionary)
@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session=Session(engine)
    # Query station from the dataset of station
    results=session.query(station.station).all()
    #close the session
    session.close()

    #convert list of tuples into normal list
    all_station=list(np.ravel(results))
    return jsonify(all_station)
@app.route("/api/v1.0/stations2")
def stations2():
    # Create our session (link) from Python to the DB
    session=Session(engine)
    #query station from the dataset of measurement
    results=session.query(measurement.station).distinct().all()
    #close the session
    session.close()

    #convert list of tuples into normal list
    all_station2=list(np.ravel(results))
    return jsonify(all_station2)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session=Session(engine)
    #query dates
    dates=session.query(measurement.date).filter(measurement.date>="2016-08-23").filter(measurement.station=="USC00519281").all()
    #query temperature
    temp=session.query(measurement.tobs).filter(measurement.date>="2016-08-23").filter(measurement.station=="USC00519281").all()
    #close the session
    session.close()

    #convert list of tuples into dictionary
    all_dates=list(np.ravel(dates))
    all_tobs=list(np.ravel(temp))
    dictionary=dict(zip(all_dates,all_tobs))
    return jsonify(dictionary)
@app.route("/api/v1.0/start")
def start():
    #input start date
    start=input("Please input start date of year-month-date as xxxx-xx-xx:")
    if "2010-01-01"<=start<"2017-08-24":
        # Create our session (link) from Python to the DB
        session=Session(engine)
        #query minimal temperature
        min_temp=session.query(func.min(measurement.tobs)).filter(measurement.date>=start).all()[0][0]
        #query average temprature
        avg_temp=session.query(func.avg(measurement.tobs)).filter(measurement.date>=start).all()[0][0]
        #query maximal temperature
        max_temp=session.query(func.max(measurement.tobs)).filter(measurement.date>=start).all()[0][0]
        #close the session
        session.close()

        #convert into dictionary
        keys={"minimal temperature": min_temp,"average temperature":avg_temp,"maximal temperature":max_temp}
    
    
        return jsonify(keys)
    if start>="2017-08-24" or start<"2010-01-01":
        return "Date input error. Please input another date between 2010-01-01 and 2017-08-24."
@app.route("/api/v1.0/start/end")
def start_end():
    #input start date
    start=input("Please input start date of year-month-day as xxxx-xx-xx:")
    #input end date
    end=input("Please input end date of year-month-date as xxxx-xx-xx:")
    if end>start and end<="2017-08-24" and start>="2010-01-01":
        # Create our session (link) from Python to the DB
        session=Session(engine)
        #query minimal temperature
        min_temp=session.query(func.min(measurement.tobs)).filter(measurement.date>=start).filter(measurement.date<=end).all()[0][0]
        #query average temperature
        avg_temp=session.query(func.avg(measurement.tobs)).filter(measurement.date>=start).filter(measurement.date<=end).all()[0][0]
        #query maximal temperature
        max_temp=session.query(func.max(measurement.tobs)).filter(measurement.date>=start).filter(measurement.date<=end).all()[0][0]
        #close the session
        session.close()

        #convert into dictionary
        keys={"minimal temperature": min_temp,"average temperature":avg_temp,"maximal temperature":max_temp}
    
        return jsonify(keys)
    if end<=start or end>"2017-08-24" or start<"2010-01-01":
        return "Date input error. Please input start date and end date between 2010-01-01 and 2017-08-24.And make sure end date is after start date."

if __name__ == '__main__':
    app.run(debug=True)


