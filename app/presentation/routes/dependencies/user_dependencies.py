from app.infrastructure.database.mongo import db
from app.infrastructure.repositories.mongo_user_repository import MongoUserRepository
from app.use_cases.user.create_user import CreateUser
from app.use_cases.user.delete_user import DeleteUser
from app.use_cases.user.get_all_users import GetAllUsers

user_repository = MongoUserRepository(db)


def create_user_case() -> CreateUser:
    return CreateUser(user_repository)


def get_all_user_case() -> GetAllUsers:
    return GetAllUsers(user_repository)


def delete_user_case() -> DeleteUser:
    return DeleteUser(user_repository)
