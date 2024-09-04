from sqlalchemy.orm import Session
from fastapi import Depends
from model import user

class UserDao:
    def __init__(self, db: Session):
        self.db = db
    
    def get_allusers(self):
        return self.db.query(user).all()

    def create_user(self, name: str, height: float, weight:float, db: Session):
        self.db.add(user) 
        self.db.commit()    #提交
        self.db.refresh(user)   #刷新
        return user
