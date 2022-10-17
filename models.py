from sqlalchemy import Column, String, Boolean, Integer
from database import Base

# SQL Student Model/Schema


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    email = Column(String)
    is_current_student = Column(Boolean)
