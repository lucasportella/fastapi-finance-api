from typing import List
from core.domain.repositories.user_repository import UserRepository
from core.domain.entities.user import User
from core.infrastructure.database.mongo import db
from pymongo.database import Database

class MongoUserRepository(UserRepository):
  def __init__(self, db: Database):
    self.db = db
    
  def add(self, user: User) -> User:
    return db.users.insert_one(user.dict())
  
  def find_by_id(self, user_id: str) -> User:
    return db.users.find_one({"_id": user_id})
  
  def get_all(self) -> List[User]:
    return db.users.find()
  
  def update(self, user: User) -> User:
    return db.users.update_one({"_id": user.id}, {"$set": user.dict()}) # pydantic .dict() method converts class to dict
  
  def delete(self, user_id: str) -> bool:
    return db.users.delete_one({"_id": user_id})
    