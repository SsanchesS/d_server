import sqlite3
import json
from src.base import base_worker
from src.models import usersM

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

def upd_user(id, user: usersM):
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

def del_user(id):
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