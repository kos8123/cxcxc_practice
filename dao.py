from sqlalchemy.orm import Session
from fastapi import Depends
from model import User

class UserDao:
    def __init__(self, db: Session):
        self.db = db
    
    def get_allusers(self):
        return self.db.query(User).all()

    def create_user(self, name: str, height: float, weight:float):
        db_user = User(name=name, height=height, weight=weight)
        self.db.add(db_user) 
        self.db.commit()            #提交
        self.db.refresh(db_user)    #刷新
        return db_user
