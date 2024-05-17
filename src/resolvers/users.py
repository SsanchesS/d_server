import sqlite3
from src.base import base_worker
from src.models import usersM,ordersM

def get_user(id):
    try:
        user = base_worker.insert_data(f"SELECT * FROM users WHERE id = {id}",())
        if user is None:
            return None
        user = {"id":user[0],"f_name":user[1],"s_name":user[2],"password":None,"email":user[4]}
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

        user = {"id":user_id[0],"f_name":None,"s_name":None,"password":None,"email":None}
        return user  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

def del_user(id): # сюда свой id из клинтка пихаем из обьекта
    try:
        user_id = base_worker.insert_data(f"DELETE FROM users WHERE id = {id} RETURNING id;",())
        if user_id is None:
            return None
        else:
            user = {"id":user_id[0],"f_name":None,"s_name":None,"password":None,"email":None}
            return user  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500
##########
def get_orders(user_id):
    try:
        orders = base_worker.insert_data(f"SELECT * FROM orders WHERE user_id = {user_id}",())
        if orders is None:
            return None
        print(orders)
        # order = {"id":order[0],"user_id":None,"order_date":order[2],"sum":order[3],"status":order[4],"delivery_method_id":order[5],"payment_method_id":order[6]}
        # return orders
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
        if new_id is None:
            return None                                                                                                    
        order = {"id":new_id[0],"user_id":None,"order_date":order.order_date,"sum":order.sum,"status":order.status,"delivery_method_id":order.delivery_method_id,"payment_method_id":order.payment_method_id}
        return order   
    except sqlite3.IntegrityError as e:
        print(f"Ошибка: {e}")
        return None
    
def del_order(user_id, id):
    try:
        order_id = base_worker.insert_data(f"DELETE FROM orders WHERE user_id = ? AND id = ? RETURNING id;",(user_id,id))
        if order_id is None:
            return None
        else:
            order = {"id":order_id[0],"user_id":None,"order_date":None,"sum":None,"status":None,"delivery_method_id":None,"payment_method_id":None}
            return order  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500