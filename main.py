from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from controller import users, health, unicorn_basket, unicorns
from app.core.config import settings


def get_application():
    _app = FastAPI(title=settings.PROJECT_NAME)

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()
app.include_router(users.router)
app.include_router(unicorns.router)
app.include_router(health.router)
app.include_router(unicorn_basket.router)
