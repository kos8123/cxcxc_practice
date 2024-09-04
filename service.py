from sqlalchemy.orm import Session
from dao import UserDao

class UserService:
    def __init__(self, db: Session):
        self.dao = UserDao(db)
    def list_allUser(self):
        return self.dao.get_allusers()
    def add_user(self, name: str, weight: float, height: float):
        return self.dao.create_user(name, weight, height)

