from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('postgresql+psycopg2://postgres:pass@localhost:5432/Math_expression')

Session = sessionmaker(bind=engine)

Base = declarative_base()
