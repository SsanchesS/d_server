from fastapi import APIRouter
from src.models import usersM,rolesM,sneakersM,categoriesM,promotionsM,delivery_methodsM,payment_methodsM,ordersM
from src.resolvers.admins import get_user,upd_user,del_user,create_user
from src.resolvers.admins import get_role,upd_role,del_role,create_role
from src.resolvers.admins import get_sneaker,upd_sneaker,del_sneaker,create_sneaker
from src.resolvers.admins import get_category,upd_category,del_category,create_category
from src.resolvers.admins import get_promotion,upd_promotion,del_promotion,create_promotion
from src.resolvers.admins import get_delivery_method,upd_delivery_method,del_delivery_method,create_delivery_method
from src.resolvers.admins import get_payment_method,upd_payment_method,del_payment_method,create_payment_method
from src.resolvers.admins import get_order,upd_order,del_order

admins_router = APIRouter()

@admins_router.get('/{id}')
def f_get_user(id: int):
   user = get_user(id)
   if user == 500:
      return {"code": 500, "message": "Ошибка сервера","user":None}
   if user is None:
      return {"code": 404, "message": f"Пользователь с таким id: {id} не найден или ошибка","user":None}
   return {"code": 201, "message": "Успешно",'user': user}

@admins_router.post('/')
def f_create_user(user:usersM):
   user = create_user(user)
   if user == 500:
      return {"code": 500, "message": "Ошибка сервера","user":None}
   if user is None:
      return {"code": 401, "message": "Этот email уже занят","user":None}
   return {"code": 201, "message": "Успешно",'user': user}

@admins_router.put('/{id}')
def f_update_user(id: int, user: usersM):
   user = upd_user(id, user)
   if user == 500:
      return {"code": 500, "message": "Ошибка сервера","user":None}
   if user is None:
      return {"code": 404, "message": f"Пользователь с таким id: {id} не найден или ошибка","user":None}
   return {"code": 201, "message": "Успешно",'user': user}

@admins_router.delete('/{id}')
def f_delete_user(id: int):
   user = del_user(id)
   if user == 500:
      return {"code": 500, "message": "Ошибка сервера","user":None}
   if user is None:
      return {"code": 404, "message": f"Пользователь с таким id: {id} не найден или ошибка","user":None}
   return {"code": 201, "message": "Успешно",'user': user}
#
@admins_router.get('/role/{id}')
def f_get_role(id: int):
   role = get_role(id)
   if role == 500:
      return {"code": 500, "message": "Ошибка сервера","role":None}
   if role is None:
      return {"code": 404, "message": f"Роль с таким id: {id} не найден или ошибка","role":None}
   return {"code": 201, "message": "Успешно",'role': role}

@admins_router.post('/role/')
def f_create_role(role:rolesM):
   role = create_role(role)
   if role == 500:
      return {"code": 500, "message": "Ошибка сервера","role":None}
   return {"code": 201, "message": "Успешно",'role': role}

@admins_router.put('/role/{id}')
def f_update_role(id: int, role: rolesM):
   role = upd_role(id, role)
   if role == 500:
      return {"code": 500, "message": "Ошибка сервера","role":None}
   if role is None:
      return {"code": 404, "message": f"Роль с таким id: {id} не найден или ошибка","role":None}
   return {"code": 201, "message": "Успешно",'role': role}

@admins_router.delete('/role/{id}')
def f_delete_role(id: int):
   role = del_role(id)
   if role == 500:
      return {"code": 500, "message": "Ошибка сервера","role":None}
   if role is None:
      return {"code": 404, "message": f"Роль с таким id: {id} не найден или ошибка","role":None}
   return {"code": 201, "message": "Успешно",'role': role}
#
@admins_router.get('/sneaker/{id}')
def f_get_sneaker(id: int):
   sneaker = get_sneaker(id)
   if sneaker == 500:
      return {"code": 500, "message": "Ошибка сервера","sneaker":None}
   if sneaker is None:
      return {"code": 404, "message": f"Кроссовки с таким id: {id} не найден или ошибка","sneaker":None}
   return {"code": 201, "message": "Успешно",'sneaker': sneaker}

@admins_router.post('/sneaker/')
def f_create_sneaker(sneaker:sneakersM):
   sneaker = create_sneaker(sneaker)
   if sneaker == 500:
      return {"code": 500, "message": "Ошибка сервера","sneaker":None}
   return {"code": 201, "message": "Успешно",'sneaker': sneaker}

@admins_router.put('/sneaker/{id}')
def f_update_sneaker(id: int, sneaker: sneakersM):
   sneaker = upd_sneaker(id, sneaker)
   if sneaker == 500:
      return {"code": 500, "message": "Ошибка сервера","sneaker":None}
   if sneaker is None:
      return {"code": 404, "message": f"Кроссовки с таким id: {id} не найден или ошибка","sneaker":None}
   return {"code": 201, "message": "Успешно",'sneaker': sneaker}

@admins_router.delete('/sneaker/{id}')
def f_delete_sneaker(id: int):
   sneaker = del_sneaker(id)
   if sneaker == 500:
      return {"code": 500, "message": "Ошибка сервера","sneaker":None}
   if sneaker is None:
      return {"code": 404, "message": f"Пользователь с таким id: {id} не найден или ошибка","sneaker":None}
   return {"code": 201, "message": "Успешно",'sneaker': sneaker}
# 
@admins_router.get('/category/{id}')
def f_get_category(id: int):
   category = get_category(id)
   if category == 500:
      return {"code": 500, "message": "Ошибка сервера","category":None}
   if category is None:
      return {"code": 404, "message": f"Категория с таким id: {id} не найден или ошибка","category":None}
   return {"code": 201, "message": "Успешно",'category': category}

@admins_router.post('/category/')
def f_create_category(category:categoriesM):
   category = create_category(category)
   if category == 500:
      return {"code": 500, "message": "Ошибка сервера","category":None}
   return {"code": 201, "message": "Успешно",'category': category}

@admins_router.put('/category/{id}')
def f_update_category(id: int, category: categoriesM):
   category = upd_category(id, category)
   if category == 500:
      return {"code": 500, "message": "Ошибка сервера","category":None}
   if category is None:
      return {"code": 404, "message": f"Категория с таким id: {id} не найден или ошибка","category":None}
   return {"code": 201, "message": "Успешно",'category': category}

@admins_router.delete('/category/{id}')
def f_delete_category(id: int):
   category = del_category(id)
   if category == 500:
      return {"code": 500, "message": "Ошибка сервера","category":None}
   if category is None:
      return {"code": 404, "message": f"Пользователь с таким id: {id} не найден или ошибка","category":None}
   return {"code": 201, "message": "Успешно",'category': category}
# 
@admins_router.get('/promotion/{id}')
def f_get_promotion(id: int):
   promotion = get_promotion(id)
   if promotion == 500:
      return {"code": 500, "message": "Ошибка сервера","promotion":None}
   if promotion is None:
      return {"code": 404, "message": f"Акция с таким id: {id} не найден или ошибка","promotion":None}
   return {"code": 201, "message": "Успешно",'promotion': promotion}

@admins_router.post('/promotion/')
def f_create_promotion(promotion:promotionsM):
   promotion = create_promotion(promotion)
   if promotion == 500:
      return {"code": 500, "message": "Ошибка сервера","promotion":None}
   return {"code": 201, "message": "Успешно",'promotion': promotion}

@admins_router.put('/promotion/{id}')
def f_update_promotion(id: int, promotion: promotionsM):
   promotion = upd_promotion(id, promotion)
   if promotion == 500:
      return {"code": 500, "message": "Ошибка сервера","promotion":None}
   if promotion is None:
      return {"code": 404, "message": f"Акция с таким id: {id} не найден или ошибка","promotion":None}
   return {"code": 201, "message": "Успешно",'promotion': promotion}

@admins_router.delete('/promotion/{id}')
def f_delete_promotion(id: int):
   promotion = del_promotion(id)
   if promotion == 500:
      return {"code": 500, "message": "Ошибка сервера","promotion":None}
   if promotion is None:
      return {"code": 404, "message": f"Пользователь с таким id: {id} не найден или ошибка","promotion":None}
   return {"code": 201, "message": "Успешно",'promotion': promotion}
# 
@admins_router.get('/delivery_method/{id}')
def f_get_delivery_method(id: int):
   delivery_method = get_delivery_method(id)
   if delivery_method == 500:
      return {"code": 500, "message": "Ошибка сервера","delivery_method":None}
   if delivery_method is None:
      return {"code": 404, "message": f"Способ доставки с таким id: {id} не найден или ошибка","delivery_method":None}
   return {"code": 201, "message": "Успешно",'delivery_method': delivery_method}

@admins_router.post('/delivery_method/')
def f_create_delivery_method(delivery_method:delivery_methodsM):
   delivery_method = create_delivery_method(delivery_method)
   if delivery_method == 500:
      return {"code": 500, "message": "Ошибка сервера","delivery_method":None}
   return {"code": 201, "message": "Успешно",'delivery_method': delivery_method}

@admins_router.put('/delivery_method/{id}')
def f_update_delivery_method(id: int, delivery_method: delivery_methodsM):
   delivery_method = upd_delivery_method(id, delivery_method)
   if delivery_method == 500:
      return {"code": 500, "message": "Ошибка сервера","delivery_method":None}
   if delivery_method is None:
      return {"code": 404, "message": f"Способ доставки с таким id: {id} не найден или ошибка","delivery_method":None}
   return {"code": 201, "message": "Успешно",'delivery_method': delivery_method}

@admins_router.delete('/delivery_method/{id}')
def f_delete_delivery_method(id: int):
   delivery_method = del_delivery_method(id)
   if delivery_method == 500:
      return {"code": 500, "message": "Ошибка сервера","delivery_method":None}
   if delivery_method is None:
      return {"code": 404, "message": f"Пользователь с таким id: {id} не найден или ошибка","delivery_method":None}
   return {"code": 201, "message": "Успешно",'delivery_method': delivery_method}
# 
@admins_router.get('/payment_method/{id}')
def f_get_payment_method(id: int):
   payment_method = get_payment_method(id)
   if payment_method == 500:
      return {"code": 500, "message": "Ошибка сервера","payment_method":None}
   if payment_method is None:
      return {"code": 404, "message": f"Способ оплаты с таким id: {id} не найден или ошибка","payment_method":None}
   return {"code": 201, "message": "Успешно",'payment_method': payment_method}

@admins_router.post('/payment_method/')
def f_create_payment_method(payment_method:payment_methodsM):
   payment_method = create_payment_method(payment_method)
   if payment_method == 500:
      return {"code": 500, "message": "Ошибка сервера","payment_method":None}
   return {"code": 201, "message": "Успешно",'payment_method': payment_method}

@admins_router.put('/payment_method/{id}')
def f_update_payment_method(id: int, payment_method: payment_methodsM):
   payment_method = upd_payment_method(id, payment_method)
   if payment_method == 500:
      return {"code": 500, "message": "Ошибка сервера","payment_method":None}
   if payment_method is None:
      return {"code": 404, "message": f"Способ оплаты с таким id: {id} не найден или ошибка","payment_method":None}
   return {"code": 201, "message": "Успешно",'payment_method': payment_method}

@admins_router.delete('/payment_method/{id}')
def f_delete_payment_method(id: int):
   payment_method = del_payment_method(id)
   if payment_method == 500:
      return {"code": 500, "message": "Ошибка сервера","payment_method":None}
   if payment_method is None:
      return {"code": 404, "message": f"Пользователь с таким id: {id} не найден или ошибка","payment_method":None}
   return {"code": 201, "message": "Успешно",'payment_method': payment_method}
# 
@admins_router.get('/order/{id}')
def f_get_order(id: int):
   order = get_order(id)
   if order == 500:
      return {"code": 500, "message": "Ошибка сервера","order":None}
   if order is None:
      return {"code": 404, "message": f"Заказ с таким id: {id} не найден или ошибка","order":None}
   return {"code": 201, "message": "Успешно",'order': order}

@admins_router.put('/order/{id}')
def f_update_order(id: int, order: ordersM):
   order = upd_order(id, order)
   if order == 500:
      return {"code": 500, "message": "Ошибка сервера","order":None}
   if order is None:
      return {"code": 404, "message": f"Заказ с таким id: {id} не найден или ошибка","order":None}
   return {"code": 201, "message": "Успешно",'order': order}

@admins_router.delete('/order/{id}')
def f_delete_order(id: int):
   order = del_order(id)
   if order == 500:
      return {"code": 500, "message": "Ошибка сервера","order":None}
   if order is None:
      return {"code": 404, "message": f"Пользователь с таким id: {id} не найден или ошибка","order":None}
   return {"code": 201, "message": "Успешно",'order': order}