from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.settings import get_settings
from app.api import chat, billing, cv


settings = get_settings()
app = FastAPI(title="CVia API")


app.add_middleware(
CORSMiddleware,
allow_origins=settings.allowed_origins,
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)


app.include_router(chat.router, prefix=settings.api_v1_prefix + "/chat")
app.include_router(cv.router, prefix=settings.api_v1_prefix + "/cv")
app.include_router(billing.router, prefix=settings.api_v1_prefix + "/billing")