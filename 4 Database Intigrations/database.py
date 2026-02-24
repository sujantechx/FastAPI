from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


SQLALCHEMY_DATABASE_URL= "sqlite:///./test.db" #database name.db

engine= create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args= {'check_same_thread': False}
) 
SessionLocal= sessionmaker(autoflush=False, autocommit=False,bind=engine) # this line creates a session factory that will be used to create database sessions. The sessionmaker function is called with the engine as an argument, and it returns a new session factory that can be used to create sessions that are bound to the engine.

Base = declarative_base()