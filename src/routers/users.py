from fastapi import APIRouter
from src.models import usersM,ordersM
from src.resolvers.users import get_user,upd_user,del_user, get_orders,create_order,upd_order,del_order ,get_sneakers,get_methods

users_router = APIRouter()

@users_router.get('/{id}')
def f_get_user(id: int):
    user = get_user(id)
    if user == 500:
        return {"code": 500, "message": "Ошибка сервера","user":None}
    if user is None:
        return {"code": 404, "message": f"Пользователь с таким id: {id} не найден","user":None}
    return {"code": 201, "message": "Успешно",'user': user}

@users_router.put('/{id}')
def f_update_user(id: int, user: usersM):
    user = upd_user(id, user)
    if user == 500:
        return {"code": 500, "message": "Ошибка сервера","user":None}
    if user is None:
        return {"code": 409, "message": f"Пользователь с таким email: уже существует","user":None}
    return {"code": 201, "message": "Успешно",'user': user}

@users_router.delete('/{id}')
def f_delete_user(id: int):
    user = del_user(id)
    if user == 500:
        return {"code": 500, "message": "Ошибка сервера","user":None}
    if user is None:
        return {"code": 404, "message": f"Пользователь с таким id: {id} не найден","user":None}
    return {"code": 201, "message": "Успешно",'user': user}

###########
@users_router.get('/sneakers/')
def f_get_sneakers():
    sneakers = get_sneakers()
    if sneakers == 500:
        return {"code": 500, "message": "Ошибка сервера","sneakers":None}
    if sneakers is None:
        return {"code": 404, "message": f"Кроссовки не найдены","sneakers":None}
    return {"code": 201, "message": "Успешно",'sneakers': sneakers}
###########

@users_router.get('/orders/{user_id}')
def f_get_orders(user_id: int):
    orders = get_orders(user_id)
    if orders == 500:
        return {"code": 500, "message": "Ошибка сервера","orders":None}
    if orders is None:
        return {"code": 404, "message": f"Заказы не найдены","orders":None}
    return {"code": 201, "message": "Успешно",'orders': orders}

@users_router.post('/orders')
def f_create_order(order:ordersM):
    order = create_order(order)
    if order == 500:
        return {"code": 500, "message": "Ошибка сервера","order":None}
    return {"code": 201, "message": "Успешно",'order': order}

@users_router.put('/orders/{id}')
def f_update_order(id: int, order: ordersM):
    order = upd_order(id, order)
    if order == 500:
        return {"code": 500, "message": "Ошибка сервера","order":None}
    return {"code": 201, "message": "Успешно",'order': order}

@users_router.delete('/orders/{id}')
def f_delete_order(id: int):
    order = del_order(id)
    if order == 500:
        return {"code": 500, "message": "Ошибка сервера","order":None}
    if order is None:
        return {"code": 404, "message": f"Заказы не найдены","order":None}
    return {"code": 201, "message": "Успешно",'order': order}

###########
@users_router.get('/methods/')
def f_get_methods():
    methods = get_methods()
    if methods == 500:
        return {"code": 500, "message": "Ошибка сервера","methods":None}
    if methods is None:
        return {"code": 404, "message": f"Методы не найдены","methods":None}
    return {"code": 201, "message": "Успешно",'methods': methods}
###########