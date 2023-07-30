from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from agents.models import RealEstateAgent

# Create your models here.

Base = declarative_base()

class RealEstateAd(Base):
    __tablename__ = 'real_estate_ad'
    id = Column(Integer, primary_key = True, autoincrement = True)
    title = Column(String)
    description = Column(String)
    address = Column(String)
    date_of_creation = Column(Date)
    negotiable = Column(Boolean)
    price = Column(Integer)
    area = Column(Integer)
    agent_id = Column('agent_id', Integer, ForeignKey(RealEstateAgent.id), primary_key = True)

    def __init__(self, title, description, address, date_of_creation, negotiable, price, area, agent_id):
        self.title = title
        self.description = description
        self.address = address
        self.date_of_creation = date_of_creation
        self.negotiable = negotiable
        self.price = price
        self.area = area
        self.agent_id = agent_id

    def __repr__(self):
        return "<RealEstateAd('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')>" % (self.id, self.title, self.description, self.address, self.date_of_creation, self.negotiable, self.price, self.area, self.agent_id)