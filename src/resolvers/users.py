import sqlite3
from src.base import base_worker
from src.models import usersM,ordersM

def get_user(id):
    try:
        user = base_worker.insert_data(f"SELECT * FROM users WHERE id = {id}",())
        if not user:
            return None
        user = user[0]

        sneakers_basket = []
        for item in user[7]:
            id = item[0]
            sneaker = get_sneaker(id)
            if (sneaker == 500):
                return 500
            sneakers_basket.append(sneaker)

        sneakers_orders=get_orders(user[0])
        if (sneakers_orders == 500):
            return 500

        user = {"id":user[0],"f_name":user[1],"s_name":user[2],"password":None,"email":user[4],"role_id":user[5],"itemsPrice":user[6],"sneakers_basket":sneakers_basket,"sneakers_orders":sneakers_orders}
        return user  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

def upd_user(id, user: usersM): # сюда свой id из клинтка пихаем из обьекта
    try:
        update_fields = []

        if user.f_name is not None and user.f_name != '':
            update_fields.append(f"f_name = '{user.f_name}'")

        if user.s_name is not None and user.s_name != '':
            update_fields.append(f"s_name = '{user.s_name}'")

        if user.password is not None and user.password != '':
            update_fields.append(f"password = '{user.password}'")

        if user.email is not None and user.email != '':
            update_fields.append(f"email = '{user.email}'")

        if user.itemsPrice is not None and user.itemsPrice != '':
            update_fields.append(f"itemsPrice = '{user.itemsPrice}'")

        if user.sneakers_basket is not None and user.sneakers_basket != '':
            update_fields.append(f"sneakers_basket = '{user.sneakers_basket}'")

        if user.sneakers_orders is not None and user.sneakers_orders != '':
            update_fields.append(f"sneakers_orders = '{user.sneakers_orders}'")

        update_fields_str = ', '.join(update_fields)

        try:
            user_id = base_worker.insert_data(f"""
            UPDATE users
            SET {update_fields_str}
            WHERE id = {id} 
            RETURNING id;
            """, ())
        except sqlite3.IntegrityError as e:
            print(f"Ошибка: {e}")
            return None
        if not user_id:
            return None
        user_id = user_id[0]
        user = {"id":user_id[0],"f_name":None,"s_name":None,"password":None,"email":None,"role_id":None,"itemsPrice":None,"sneakers_basket":None,"sneakers_orders":None}
        return user  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

def del_user(id): # сюда свой id из клинтка пихаем из обьекта
    try:
        user_id = base_worker.insert_data(f"DELETE FROM users WHERE id = {id} RETURNING id;",())
        if not user_id:
            return None
        else:
            user_id = user_id[0]
            user = {"id":user_id[0],"f_name":None,"s_name":None,"password":None,"email":None,"role_id":None,"itemsPrice":None,"sneakers_basket":None,"sneakers_orders":None}
            return user  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500
    
##########
def get_sneakers():
    try:
        get_sneakers = base_worker.insert_data(f"SELECT * FROM sneakers",())
        if not get_sneakers:
            return None
        
        sneakers = []
        for item in get_sneakers:
            sneaker = {"id":item[0],"des":item[1],"price":item[2],"img":item[3],"category_id":item[4]}
            sneakers.append(sneaker)
        return sneakers
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

def get_sneaker(id):
    try:
        get_sneaker = base_worker.insert_data(f"SELECT * FROM sneakers WHERE id = {id}",())
        if not get_sneaker:
            return None
        
        sneaker = {"id":get_sneaker[0],"des":get_sneaker[1],"price":get_sneaker[2],"img":get_sneaker[3],"category_id":get_sneaker[4]}
        return sneaker
    
    except Exception as e:
        print(f"Ошибка {e}")
        return 500
##########
def get_orders(user_id):
    try:
        get_orders = base_worker.insert_data(f"SELECT * FROM orders WHERE user_id = {user_id}",())
        if not get_orders:
            return None
        
        orders = []
        for item in get_orders:
            order = {"id":item[0],"user_id":None,"order_date":item[2],"sum":item[3],"status":item[4],"delivery_method_id":item[5],"payment_method_id":item[6]}
            orders.append(order)
        return orders
    
    except Exception as e:
        print(f"Ошибка {e}")
        return 500
    
def create_order(order:ordersM):
    try:
        insert_fields = ["user_id", "order_date", "sum","status","delivery_method_id","payment_method_id"]
        insert_values = [f"'{order.user_id}'",f"'{order.order_date}'",f"'{order.sum}'",f"'{order.status}'",f"'{order.delivery_method_id}'",f"'{order.payment_method_id}'"]

        fields_str = ', '.join(insert_fields)
        values_str = ', '.join(insert_values)
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

    try:
        new_id = base_worker.insert_data(f"""
        INSERT INTO orders ({fields_str})
        VALUES ({values_str})
        RETURNING id;                                                                                                 
        """, ())            
        if not new_id:
            return None    
        new_id = new_id[0]                                                                                                
        order = {"id":new_id[0],"user_id":None,"order_date":order.order_date,"sum":order.sum,"status":order.status,"delivery_method_id":order.delivery_method_id,"payment_method_id":order.payment_method_id}
        return order   
    except sqlite3.IntegrityError as e:
        print(f"Ошибка: {e}")
        return None
    
def del_order(user_id, id):
    try:
        order_id = base_worker.insert_data(f"DELETE FROM orders WHERE user_id = ? AND id = ? RETURNING id;",(user_id,id))
        if not order_id:
            return None
        else:
            order_id = order_id[0]
            order = {"id":order_id[0],"user_id":None,"order_date":None,"sum":None,"status":None,"delivery_method_id":None,"payment_method_id":None}
            return order  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500