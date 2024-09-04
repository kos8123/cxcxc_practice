from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from service import UserService
from model import SessionLocal
from pydantic import BaseModel
router = APIRouter()

class UserCreate(BaseModel):
    name: str
    height: float
    weight: float

def get_db():
    db = SessionLocal()  
    try:
        yield db        #https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/#sub-dependencies-with-yield
    finally:
        db.close()

@router.get("/api/user")
def get_allUsers(db: Session = Depends(get_db)):
    service = UserService(db)
    users = service.list_allUser()
    return [{"name":user.name, "height": user.height, "weight": user.weight} for user in users]

@router.post("/api/user")
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    service = UserService(db)
    try:
        service.add_user(user.name, user.height, user.height)
        return {"status": "successed"}
    except Exception as e:
        return {"status": "error"}


