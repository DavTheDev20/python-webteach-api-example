from pydantic import BaseModel

# Pydantic Schemas


class StudentBase(BaseModel):
    first_name: str
    last_name: str
    age: int
    email: str


class Student(StudentBase):
    id: int
    is_current_student: bool

    class Config:
        orm_mode = True
