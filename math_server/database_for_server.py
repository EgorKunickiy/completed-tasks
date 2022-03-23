from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from math_server.data_for_db import user, password, database, host, port


engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')

Session = sessionmaker(bind=engine)

Base = declarative_base()
