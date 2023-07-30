from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create your models here.

Base = declarative_base()

class RealEstateAgent(Base):
    __tablename__ = 'real_estate_agent'
    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    address = Column(String)
    age = Column(Integer)

    def __init__(self, id, name, email, phone, address, age):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.age = age

    def __str__(self):
        return self.name + " " + self.email + " " + self.phone + " " + self.address + " " + str(self.age)