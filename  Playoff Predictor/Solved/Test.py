# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd


def get_data():
    #Create engine using Playoffs.sqlite database file
    engine = create_engine("sqlite:///../Playoffs.sqlite")
    # Declare a Base using `automap_base()`
    Base = automap_base()

    # Use the Base class to reflect the database tables
    Base.prepare(autoload_with=engine)
    #Assign the dow class to a variable called 'Playoffs'
    Playoffs = Base.classes.Playoffs
    #Create a session
    session = Session(engine)
    data = session.query(Playoffs.BK, Playoffs.CG_y, Playoffs.Ch, Playoffs.GF, Playoffs.SB, Playoffs.cSho, Playoffs.playoffs).all()
    #'BK', 'CG_y', 'Ch', 'GF', 'SB', 'cSho', 'playoffs'
    data_df = pd.DataFrame(data=data, columns=['BK', 'CG_y', 'Ch', 'GF', 'SB', 'cSho', 'playoffs'])
    return data_df
