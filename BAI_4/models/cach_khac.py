from database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class EnrollmentModel(Base):
    __tablename__ = "enrollments" 
    
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
    student = relationship("StudentModel", back_populates="enrollments")
    course = relationship("CourseModel", back_populates="enrollments")





#  Bảng Học sinh 
class StudentModel(Base):
    __tablename__ = "students"
    
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    full_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    
    courses = relationship("CourseModel", secondary="enrollments", back_populates="students")
    enrollments = relationship("EnrollmentModel", back_populates="student")


# khoa hoc
class CourseModel(Base):
    __tablename__ = "courses"
    
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    students = relationship("StudentModel", secondary="enrollments", back_populates="courses")
    enrollments = relationship("EnrollmentModel", back_populates="course")