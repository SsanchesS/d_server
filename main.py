from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from src.routers.auth import auth_router
from src.routers.registration import registration_router
from src.routers.users import users_router
from src.routers.admins import admins_router

from src.base import base_worker

BASE_PATH = 'db.db'
base_worker.set_base_path(BASE_PATH)

if not base_worker.check_base():
    print("БД не существует")
    base_worker.create_base('src/sql/base.sql')
else:
    print("БД существует")
    
app = FastAPI()

# CORS
origins = [
    # адрес клиентского приложения
    "http://localhost:3000"
    # "https://swfnhkr9-3000.euw.devtunnels.ms"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]

    # allow_methods=["GET","POST","OPTIONS","DELETE","PATCH","PUT"],
    # allow_headers=["Content-Type","Set-Cookie","Access-Control-Allow-Headers",
    #                "Authorization","Access-Control-Allow-Origin","Access-Control-Allow-Methods"]
)

# @app.middleware("https")
# async def add_cors_headers(request, call_next):
#     response = await call_next(request)
#     response.headers["Access-Control-Allow-Origin"] = origins[0]
#     response.headers["Access-Control-Allow-Headers"] = "*"
#     response.headers["Access-Control-Allow-Methods"] = "*"
#     return response

@app.get("/")
def main_page():
    return {"code": 200, "message": "Connection in correct",'user': None}
    
app.include_router(auth_router, prefix='/auth')
app.include_router(registration_router, prefix='/registration')
app.include_router(users_router, prefix='/users')
app.include_router(admins_router, prefix='/admins')

PORT = 8000       # убрать это в файл засекреченный
# HOST = "127.0.0.1"
HOST = "0.0.0.0"

if __name__ == "__main__":
    uvicorn.run("main:app", port=PORT, host=HOST, reload=True)