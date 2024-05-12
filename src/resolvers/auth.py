from src.models import LoginM 
from src.base import base_worker

def check_login_request(user: LoginM):
    try:
        get_user = base_worker.insert_data(f"SELECT * FROM users WHERE email = ? AND password = ?",(user.email,user.password))
        if get_user is None:
            return None
        user = {"id":get_user[0],"f_name":get_user[1],"s_name":get_user[2],"password":None,"email":get_user[4]}     
        return user 
    except Exception as e:
        print(f"Ошибка {e}")
        return 500