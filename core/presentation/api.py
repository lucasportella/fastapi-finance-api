from fastapi import FastAPI
from core.presentation.routes.user_routes import router as user_router

app = FastAPI(title="Loan & Property API")

app.include_router(user_router, prefix="/users", tags=["users"])