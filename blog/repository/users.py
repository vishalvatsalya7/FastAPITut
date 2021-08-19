from ..hashing import Hashing
from .. import models, schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException


def create_user(request: schemas.User, db: Session):
    hashedObj = Hashing()
    hashedPassword = hashedObj.bcrypt(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")
    return user
