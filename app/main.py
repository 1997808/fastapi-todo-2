from fastapi import FastAPI
from api.routes.todo import todo_router
from tortoise.contrib.fastapi import register_tortoise
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

DB_URL = f"postgres://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

app.include_router(todo_router)
register_tortoise(
    app=app,
    db_url=DB_URL,
    modules={"models": ["api.models.todo"]},
    generate_schemas=True,
    add_exception_handlers=True
)


@app.get("/")
def index():
    return {"status": "running"}
