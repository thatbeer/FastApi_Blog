from fastapi import APIRouter , Depends , UploadFile , File
from routes.schemas import PostBase
from db.database import get_db
from sqlalchemy.orm import Session
from db import db_post
import string
import random
import shutil

router = APIRouter(
    prefix='/post',
    tags=['post']
)

@router.post('/')
def create_post(request: PostBase, db: Session = Depends(get_db)):
    return db_post.create(db, request)


@router.get("/all")
def posts(db: Session = Depends(get_db)):
    return db_post.get_all(db)

@router.delete('/{id}')
def delete(id: int , db: Session = Depends(get_db)):
    return db_post.delete(id,db)

@router.post('/image')
def upload_image(image: UploadFile= File(...)):
    letter = string.ascii_letters
    rand_str = ' '.join(random.choice(letter) for i in range(6))
    new = f'_{rand_str}.'
    filename = new.join(image.filename.split('.', 1))
    path = f'image/{filename}'

    with open(path,'w+b') as buffer:
        shutil.copyfileobj(image.file, buffer)
    
    return {'filename' : path}
