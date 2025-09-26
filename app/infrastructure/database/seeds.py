from datetime import datetime
from app.domain.entities.user import User
from app.infrastructure.repositories.mongo_user_repository import MongoUserRepository
from app.infrastructure.database.mongo import db


def seed_users():
    user1 = User(
        first_name="Lucas",
        last_name="Portella",
        date_of_birth=datetime(1995, 7, 15),
        email="lucas@example.com",
        address="123 Main St, Porto Alegre, Brazil",
        phone="+55 51 91234-5678",
        hashed_password="hashed_password_1",
        id=None
    )

    user1.add_asset({"type": "Property", "value": 350000.0, "description": "Apartment in Porto Alegre", "year": 2018, "id": 1})
    user1.add_asset({"type": "Vehicle", "value": 45000.0, "description": "Used car", "year": 2020, "id": 2})

    user1.add_debt({"total_value": 50000.0, "interest_rate": 5.0, "total_installments": 24, "principal_paid": 12000.0, "remaining": 38000.0})

    user1.add_income({"type": "Salary", "netIncome": 3500.0})
    user1.add_income({"type": "Freelance", "netIncome": 800.0})

    user1.add_expense({"type": "Rent", "net_expense": 1200.0})
    user1.add_expense({"type": "Food", "net_expense": 600.0})

    user2 = User(
        first_name="Alice",
        last_name="Santos",
        date_of_birth=datetime(1990, 3, 22),
        email="alice@example.com",
        address="456 Elm St, São Paulo, Brazil",
        phone="+55 11 98765-4321",
        hashed_password="hashed_password_2",
        id=None
    )

    user2.add_asset({"type": "Savings Account", "value": 15000.0, "description": "Bank savings", "year": None, "id": 1})
    user2.add_debt({"total_value": 10000.0, "interest_rate": 7.0, "total_installments": 12, "principal_paid": 2000.0, "remaining": 8000.0})
    user2.add_income({"type": "Salary", "netIncome": 4500.0})
    user2.add_expense({"type": "Utilities", "net_expense": 300.0})
    user2.add_expense({"type": "Transport", "net_expense": 200.0})

    seed_users = [user1, user2]

    return [MongoUserRepository(db).add(u) for u in seed_users]

if __name__ == "__main__":
    # run with "python -m app.infrastructure.database.seeds"
    results = seed_users()
    print(results)
    db.client.close()