import sqlite3
from src.models import usersM 
from src.base import base_worker

def create_user(user:usersM):
    try:
        insert_fields = ["f_name", "s_name", "password","email"]
        insert_values = [f"'{user.f_name}'",f"'{user.s_name}'",f"'{user.password}'",f"'{user.email}'"]

        fields_str = ', '.join(insert_fields)
        values_str = ', '.join(insert_values)
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

    try:
        new_id = base_worker.insert_data(f"""
        INSERT INTO users ({fields_str})
        VALUES ({values_str})
        RETURNING id;                                                                                                 
        """, ())            
        if not new_id:
            return None     
        new_id = new_id[0]                                                                                               
        user = {"id":new_id[0],"f_name":user.f_name,"s_name":user.s_name,"password":user.password,"email":user.email,"role_id":user.role_id}
        return user   
    except sqlite3.IntegrityError as e:
        print(f"Ошибка: {e}")
        return None