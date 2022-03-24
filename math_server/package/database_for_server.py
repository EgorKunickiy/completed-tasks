from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from data_for_db import USER, PORT, PASSWORD, DATABASE, HOST


engine = create_engine(f'postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}')

Session = sessionmaker(bind=engine)

Base = declarative_base()
