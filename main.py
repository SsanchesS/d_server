from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from src.routers.auth import auth_router
from src.routers.registration import registration_router
from src.routers.users import users_router
from src.routers.admins import admins_router

from src.routers.products import products_router
from src.routers.categories import categories_router
from src.routers.promotions import promotions_router
from src.routers.delivery_methods import delivery_methods_router
from src.routers.payment_methods import payment_methods_router
from src.routers.orders import orders_router

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
    "http://localhost:3000",  # адрес клиентского приложения
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
    return {'page': 'Connection in correct'}
    
app.include_router(auth_router, prefix='/auth')
app.include_router(registration_router, prefix='/registration')
app.include_router(users_router, prefix='/users')
app.include_router(admins_router, prefix='/admins')

app.include_router(products_router, prefix='/products')
app.include_router(categories_router, prefix='/categories')
app.include_router(promotions_router, prefix='/promotions')
app.include_router(delivery_methods_router, prefix='/delivery_methods')
app.include_router(payment_methods_router, prefix='/payment_methods')
app.include_router(orders_router, prefix='/orders')

PORT = 8000       # убрать это в файл засекреченный
HOST = "127.0.0.1"

if __name__ == "__main__":
    uvicorn.run("main:app", port=PORT, host=HOST, reload=True)