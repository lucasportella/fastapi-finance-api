from app.use_cases.user.create_user import CreateUser
from app.infrastructure.database.mongo_user_repository import MongoUserRepository
from app.infrastructure.database.mongo import db
from app.use_cases.user.get_all_users import GetAllUsers

def get_create_user_case() -> CreateUser:
  user_repository = MongoUserRepository(db)
  return CreateUser(user_repository)

def get_all_user_case() -> GetAllUsers:
  user_repository = MongoUserRepository(db)
  return GetAllUsers(user_repository)