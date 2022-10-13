from fastapi import FastAPI
from db import models
from db.database import engine
from routes import post
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.include_router(post.router)


@app.get("/")
def hi():
    return "hello world"


models.Base.metadata.create_all(engine)


## mount the local server to hold the image files
app.mount('/images', StaticFiles(directory='images'), name= 'images')


## CORS SETTING
origins = [
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)