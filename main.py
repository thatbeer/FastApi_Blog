from xml.etree.ElementInclude import FatalIncludeError
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def hi():
    return "hello world"