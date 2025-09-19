from typing import List
from core.domain.repositories.user_repository import UserRepository
from core.domain.entities.user import User
from pymongo.database import Database
from dataclasses import asdict

class MongoUserRepository(UserRepository):
  def __init__(self, db: Database):
    self.db = db
    
  def add(self, user: User) -> User:
    return self.db.users.insert_one(asdict(user))
  
  def get_by_id(self, user_id: str) -> User:
    return self.db.users.find_one({"_id": user_id})
  
  def get_all(self) -> List[User]:
    return self.db.users.find()
  
  def update(self, user: User) -> User:
    return self.db.users.update_one({"_id": user.id}, {"$set": asdict(user)}) # pydantic .dict() method converts class to dict
  
  def delete(self, user_id: str) -> bool:
    return self.db.users.delete_one({"_id": user_id})
    