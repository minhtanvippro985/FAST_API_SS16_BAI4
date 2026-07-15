from database import Base
from sqlalchemy import Column , Integer , String 
from sqlalchemy.orm import relationship 

class StudentModel(Base):
    __tablename__ = "students"
    id = Column(Integer , nullable= False , primary_key= True , autoincrement=True )
    full_name = Column(String(255) , nullable= False)
    email = Column(String(255) , nullable= False)