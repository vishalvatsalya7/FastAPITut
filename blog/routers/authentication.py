from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from .. import schemas, database, models
from sqlalchemy.orm import Session
from ..repository import authentication

router = APIRouter(
    tags=['authentication']
)


@router.post('/login')
def login(request:  OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    return authentication.login(request, db)
