from xml.etree.ElementInclude import FatalIncludeError
from fastapi import FastAPI
from db import models
from db.database import engine

app = FastAPI()


@app.get("/")
def hi():
    return "hello world"


models.Base.metadata.create_all(engine)