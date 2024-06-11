from fastapi import FastAPI, WebSocket
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
    "http://localhost:3000",
    "https://swfnhkr9-3000.euw.devtunnels.ms"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def main_page():
    return {"code": 200, "message": "Connection in correct",'user': None}

# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     while True:
#         data = await websocket.receive_text()
#         await websocket.send_text(f"Message text was: {data}")
    
app.include_router(auth_router, prefix='/auth')
app.include_router(registration_router, prefix='/registration')
app.include_router(users_router, prefix='/users')
app.include_router(admins_router, prefix='/admins')

PORT = 8000       # убрать это в файл засекреченный
HOST = "127.0.0.1"

if __name__ == "__main__":
    uvicorn.run("main:app", port=PORT, host=HOST, reload=True)