from app.domain.repositories.user_repository import UserRepository


class DeleteUser:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_id: str):
        return self.user_repository.delete(user_id)
