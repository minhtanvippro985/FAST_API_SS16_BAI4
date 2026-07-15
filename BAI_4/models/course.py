from database import Base
from sqlalchemy import Column , Integer , String 
from sqlalchemy.orm import relationship 

class CourseModel(Base):
    __tablename__ = "courses"
    id = Column(Integer , nullable= False , primary_key= True , autoincrement=True )
    name = Column(String(255) , nullable= False)
    