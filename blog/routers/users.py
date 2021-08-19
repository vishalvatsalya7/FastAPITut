from fastapi import APIRouter, status, Depends, HTTPException
from .. import schemas, models, database
from sqlalchemy.orm import Session
from ..repository import users

router = APIRouter(
    prefix="/user",
    tags=['users']
)


@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(database.get_db)):
    return users.create_user(request, db)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_user(id: int, db: Session = Depends(database.get_db)):
    return users.get_user(id, db)
