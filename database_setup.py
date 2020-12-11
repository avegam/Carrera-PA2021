import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine



Base = declarative_base()




class Corredor(Base):
	__tablename__ = 'corredor'

	id = Column(Integer, primary_key=True)
	nombre = Column(String(40),nullable=False)
	apellido = Column(String(50), nullable=False)
	marca = Column(String(50), nullable=False)
	sexo = Column(String(250), nullable=False)
	t1 = Column(Integer, nullable=False)
	t2 = Column(Integer, nullable=False)
	mejor_tiempo = Column(Integer, nullable=False)
	promedio = Column(Integer, nullable=False)



engine = create_engine('sqlite:///blog.db')
Base.metadata.create_all(engine)
