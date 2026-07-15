from database import Base
from sqlalchemy import Column , Integer , String  , ForeignKey
from sqlalchemy.orm import relationship  

class EnrollmentModel(Base):
    __tablename_ = "enrollments"
    id = Column(Integer , nullable= False , primary_key= True , autoincrement=True )
    student_id = Column(Integer , ForeignKey('students.id') , nullable= False)
    course_id = Column(Integer , ForeignKey('courses.id') , nullable= False)
    

    