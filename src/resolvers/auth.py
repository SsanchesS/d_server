import json
from src.models import LoginM 
from src.base import base_worker
from src.resolvers.users import get_orders,get_sneaker
def check_login_request(user: LoginM):
    try:
        get_user = base_worker.insert_data(f"SELECT * FROM users WHERE email = ? AND password = ?",(user.email,user.password))
        if not get_user:
            return None
        get_user = get_user[0]   

        if get_user[6] is not None:            
            sneakers_basket = []
            mas_sneakers_basket = json.loads(get_user[6])
            for item in mas_sneakers_basket:
                id = item
                sneaker = get_sneaker(id)
                if (sneaker == 500):
                    return 500
                sneakers_basket.append(sneaker)     
        else:
            sneakers_basket= []

        if get_user[7] is not None:
            sneakers_orders = []
            mas_sneakers_orders = json.loads(get_user[7])
            sneakers_orders=get_orders(get_user[0])
            if (sneakers_orders == 500):
                return 500   
        else:
            sneakers_orders= []
        
        user = {"id":get_user[0],"f_name":get_user[1],"s_name":get_user[2],"password":get_user[3],"email":get_user[4],"role_id":get_user[5],"sneakers_basket":sneakers_basket,"sneakers_orders":sneakers_orders}    
        return user 
    except Exception as e:
        print(f"Ошибка {e}")
        return 500