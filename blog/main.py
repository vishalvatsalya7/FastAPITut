from fastapi import FastAPI
from . import models
from .database import engine
import uvicorn
from .routers import blog, users, authentication

models.Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(blog.router)
app.include_router(users.router)
app.include_router(authentication.router)

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
