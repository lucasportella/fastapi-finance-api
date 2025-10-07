from typing import List

from app.domain.entities.user import User


def doc_to_user(doc) -> User:
    doc["id"] = str(doc["_id"])
    doc.pop("_id")
    return User(**doc)


def docs_to_users(docs) -> List[User]:
    return [doc_to_user(doc) for doc in docs]
