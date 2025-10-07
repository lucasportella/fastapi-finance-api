from dataclasses import asdict
from typing import List

from bson import ObjectId
from pymongo.database import Database

from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from app.infrastructure.repositories.helpers import docs_to_users
from app.presentation.dtos.user_dto import UserCreateDTO


class MongoUserRepository(UserRepository):
    def __init__(self, db: Database):
        self.db = db

    def add(self, user: UserCreateDTO) -> User:
        result = self.db.users.insert_one(asdict(user))
        user.id = str(result.inserted_id)
        return user

    def get_by_id(self, user_id: str) -> User:
        return self.db.users.find_one({"_id": ObjectId(user_id)})

    def get_all(self) -> List[User]:
        return docs_to_users(self.db.users.find())

    def update(self, user: User) -> User:
        return self.db.users.update_one(
            {"_id": ObjectId(user.id)}, {"$set": asdict(user)}
        )

    def delete(self, user_id: str) -> bool:
        result = self.db.users.delete_one({"_id": ObjectId(user_id)})
        return result.deleted_count == 1
