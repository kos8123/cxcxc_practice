from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://admin:Abcd1234!@18.205.20.36:3306/cxcxc_DB")
SessionLocal = sessionmaker(bind=engine)
database = declarative_base()

class User(database):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    height = Column(Float, nullable=False)
    weight = Column(Float, nullable=False)

    
database.metadata.create_all(bind=engine)
    
