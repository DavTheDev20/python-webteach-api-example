from sqlalchemy.orm import Session

import models
import schemas

# CRUD Operations for database data


def get_student(db: Session, user_id: int):
    return db.query(models.Student).filter(models.Student.id == user_id).first()


def get_students(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()


def add_student(db: Session, student: schemas.StudentBase):
    db_student = models.Student(
        first_name=student.first_name,
        last_name=student.last_name,
        age=student.age,
        email=student.email,
        is_current_student=True
    )
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
