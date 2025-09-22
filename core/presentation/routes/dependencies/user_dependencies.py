from core.use_cases.create_user import CreateUser
from core.infrastructure.database.mongo_user_repository import MongoUserRepository
from core.infrastructure.database.mongo import db

def get_create_user_case() -> CreateUser:
  user_repository = MongoUserRepository(db)
  return CreateUser(user_repository)