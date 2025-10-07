from fastapi import FastAPI

from app.presentation.routes.user_routes import router as user_router

app = FastAPI(title="Loan & Property API")

app.include_router(user_router, prefix="/user", tags=["users"])
