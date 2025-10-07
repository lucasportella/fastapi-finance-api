from app.domain.repositories.user_repository import UserRepository


class GetAllUsers:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self):
        return self.user_repository.get_all()
