"""
Database Connection Utility

This module provides a utility function to establish a connection to a PostgreSQL database using SQLAlchemy
"""
from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

def get_engine():
    """
    Establish a connection to a PostgreSQL database using SQLAlchemy

    Parameters
    ----------
    credentials : dict
        A dictionary containing the database connection credentials

    Returns
    -------
    engine : sqlalchemy.engine.base.Engine
        A SQLAlchemy Engine object representing the established connection.

    Raises
    ------
    SQLAlchemyError: If there is an error establishing the database connection.

    """
    dialect = config('PGDIALECT')
    user = config('PGUSER')
    passwd = config('PGPASSWD')
    host = config('PGHOST')
    port = config('PGPORT')
    db = config('PGDB')

    url = f"{dialect}://{user}:{passwd}@{host}:{port}/{db}"
    try:
        engine = create_engine(url)
        print(f'Conected successfully to database {db}!')
        return engine
    except SQLAlchemyError as e:
        print(f'Error: {e}')


"""
 Make sure to replace the placeholder credentials with your actual database credentials.
"""
