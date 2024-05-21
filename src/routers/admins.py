from fastapi import APIRouter
from src.models import usersM
# from src.resolvers.admins import get_admin,upd_admin,del_admin 

admins_router = APIRouter()

# @admins_router.get('/{id}')
# def f_get_admin(id: int):
#     admin = get_admin(id)
#     if admin == 500:
#         return {"code": 500, "message": "Ошибка сервера","admin":None}
#     if admin is None:
#         return {"code": 404, "message": f"Пользователь с таким id: {id} не найден","admin":None}
#     return {"code": 201, "message": "Успешно",'admin': admin}

# @admins_router.put('/{id}')
# def f_update_admin(id: int, admin: usersM):
#     admin = upd_admin(id, admin)
#     if admin == 500:
#         return {"code": 500, "message": "Ошибка сервера","admin":None}
#     if admin is None:
#         return {"code": 409, "message": f"Пользователь с таким email: уже существует","admin":None}
#     return {"code": 201, "message": "Успешно",'admin': admin}

# @admins_router.delete('/{id}')
# def f_delete_admin(id: int):
#     admin = del_admin(id)
#     if admin == 500:
#         return {"code": 500, "message": "Ошибка сервера","admin":None}
#     if admin is None:
#         return {"code": 404, "message": f"Пользователь с таким id: {id} не найден","admin":None}
#     return {"code": 201, "message": "Успешно",'admin': admin}