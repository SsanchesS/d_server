import sqlite3
from src.base import base_worker
from src.models import usersM,rolesM,sneakersM,categoriesM,promotionsM,delivery_methodsM,payment_methodsM,ordersM

def get_user(id):
    try:
        user = base_worker.insert_data(f"SELECT * FROM users WHERE id = {id}",())
        if not user:
            return None
        user = user[0]
            
        user = {"id":user[0],"f_name":user[1],"s_name":user[2],"password":user[3],"email":user[4],"role_id":user[5]}
        return user  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

def create_user(user:usersM):
    try:
        insert_fields = ["f_name", "s_name", "password","email","role_id"]
        insert_values = [f"'{user.f_name}'",f"'{user.s_name}'",f"'{user.password}'",f"'{user.email}'",f"'{user.role_id}'"]

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

        if user.role_id is not None and user.role_id != 0:
            update_fields.append(f"role_id = '{user.role_id}'")

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
        user = {"id":user_id[0],"f_name":None,"s_name":None,"password":None,"email":None,"role_id":None}
        return user  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

def del_user(id):
    try:
        user_id = base_worker.insert_data(f"DELETE FROM users WHERE id = {id} RETURNING id;",())
        if not user_id:
            return None
        else:
            user_id = user_id[0]
            user = {"id":user_id[0],"f_name":None,"s_name":None,"password":None,"email":None,"role_id":None}
            return user  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500
#
def get_role(id):
    try:
        role = base_worker.insert_data(f"SELECT * FROM roles WHERE id = {id}",())
        if not role:
            return None
        role = role[0]
            
        role = {"id":role[0],"role":role[1]}
        return role  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

def create_role(role:rolesM):
    try:
        insert_fields = ["role"]
        insert_values = [f"'{role.role}'"]

        fields_str = ', '.join(insert_fields)
        values_str = ', '.join(insert_values)
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

    try:
        new_id = base_worker.insert_data(f"""
        INSERT INTO roles ({fields_str})
        VALUES ({values_str})
        RETURNING id;                                                                                                 
        """, ())            
        if not new_id:
            return None     
        new_id = new_id[0]                                                                                               
        role = {"id":new_id[0],"role":role.role}
        return role   
    except Exception as e:
        print(f"Ошибка: {e}")
        return None
    
def upd_role(id, role: rolesM):
    try:
        update_fields = []

        if role.role is not None and role.role != '':
            update_fields.append(f"role = '{role.role}'")

        update_fields_str = ', '.join(update_fields)
        try:
            role_id = base_worker.insert_data(f"""
            UPDATE roles
            SET {update_fields_str}
            WHERE id = {id} 
            RETURNING id;
            """, ())
        except Exception as e:
            print(f"Ошибка: {e}")
            return None
        if not role_id:
            return None
        role_id = role_id[0]
        role = {"id":role_id[0],"role":None}
        return role  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

def del_role(id):
    try:
        role_id = base_worker.insert_data(f"DELETE FROM roles WHERE id = {id} RETURNING id;",())
        if not role_id:
            return None
        else:
            role_id = role_id[0]
            role = {"id":role_id[0],"role":None}
            return role  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500
#
def get_sneaker(id):
    try:
        sneaker = base_worker.insert_data(f"SELECT * FROM sneakers WHERE id = {id}",())
        if not sneaker:
            return None
        sneaker = sneaker[0]
            
        sneaker = {"id":sneaker[0],"des":sneaker[1],"price":sneaker[2],"img":sneaker[3],"category_id":sneaker[4]}
        return sneaker  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

def create_sneaker(sneaker:sneakersM):
    try:
        insert_fields = ["des","price","img","category_id"]
        insert_values = [f"'{sneaker.des}'",f"'{sneaker.price}'",f"'{sneaker.img}'",f"'{sneaker.category_id}'"]

        fields_str = ', '.join(insert_fields)
        values_str = ', '.join(insert_values)
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

    try:
        new_id = base_worker.insert_data(f"""
        INSERT INTO sneakers ({fields_str})
        VALUES ({values_str})
        RETURNING id;                                                                                                 
        """, ())            
        if not new_id:
            return None     
        new_id = new_id[0]                               
        sneaker = {"id":new_id[0],"des":sneaker.des,"price":sneaker.price,"img":sneaker.img,"category_id":sneaker.category_id}                                                                
        return sneaker   
    except Exception as e:
        print(f"Ошибка: {e}")
        return None
    
def upd_sneaker(id, sneaker: sneakersM):
    try:
        update_fields = []

        if sneaker.des is not None and sneaker.des != '':
            update_fields.append(f"des = '{sneaker.des}'")
        
        if sneaker.price is not None and sneaker.price != 0:
            update_fields.append(f"price = '{sneaker.price}'")

        if sneaker.img is not None and sneaker.img != '':
            update_fields.append(f"img = '{sneaker.img}'")

        if sneaker.category_id is not None and sneaker.category_id != 0:
            update_fields.append(f"category_id = '{sneaker.category_id}'")

        update_fields_str = ', '.join(update_fields)
        try:
            sneaker_id = base_worker.insert_data(f"""
            UPDATE sneakers
            SET {update_fields_str}
            WHERE id = {id} 
            RETURNING id;
            """, ())
        except Exception as e:
            print(f"Ошибка: {e}")
            return None
        if not sneaker_id:
            return None
        sneaker_id = sneaker_id[0]
        sneaker = {"id":sneaker_id[0],"des":None,"price":None,"img":None,"category_id":None} 
        return sneaker  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

def del_sneaker(id):
    try:
        sneaker_id = base_worker.insert_data(f"DELETE FROM sneakers WHERE id = {id} RETURNING id;",())
        if not sneaker_id:
            return None
        else:
            sneaker_id = sneaker_id[0]
            sneaker = {"id":sneaker_id[0],"des":None,"price":None,"img":None,"category_id":None}
            return sneaker  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500
#
def get_category(id):
    try:
        category = base_worker.insert_data(f"SELECT * FROM categories WHERE id = {id}",())
        if not category:
            return None
        category = category[0]
            
        category = {"id":category[0],"name":category[1],"des":category[2]}
        return category  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

def create_category(category:categoriesM):
    try:
        insert_fields = ["name","des"]
        insert_values = [f"'{category.name}'",f"'{category.des}'"]

        fields_str = ', '.join(insert_fields)
        values_str = ', '.join(insert_values)
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

    try:
        new_id = base_worker.insert_data(f"""
        INSERT INTO categories ({fields_str})
        VALUES ({values_str})
        RETURNING id;                                                                                                 
        """, ())            
        if not new_id:
            return None     
        new_id = new_id[0]                               
        category = {"id":new_id[0],"name":category.name,"des":category.des}                                                                
        return category   
    except Exception as e:
        print(f"Ошибка: {e}")
        return None
    
def upd_category(id, category: categoriesM):
    try:
        update_fields = []

        if category.name is not None and category.name != '':
            update_fields.append(f"name = '{category.name}'")
        
        if category.des is not None and category.des != '':
            update_fields.append(f"des = '{category.des}'")

        update_fields_str = ', '.join(update_fields)
        try:
            category_id = base_worker.insert_data(f"""
            UPDATE categories
            SET {update_fields_str}
            WHERE id = {id} 
            RETURNING id;
            """, ())
        except Exception as e:
            print(f"Ошибка: {e}")
            return None
        if not category_id:
            return None
        category_id = category_id[0]
        category = {"id":category_id[0],"name":None,"des":None} 
        return category  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

def del_category(id):
    try:
        category_id = base_worker.insert_data(f"DELETE FROM categories WHERE id = {id} RETURNING id;",())
        if not category_id:
            return None
        else:
            category_id = category_id[0]
            category = {"id":category_id[0],"name":None,"des":None}
            return category  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500
#
def get_promotion(id):
    try:
        promotion = base_worker.insert_data(f"SELECT * FROM promotions WHERE id = {id}",())
        if not promotion:
            return None
        promotion = promotion[0]
            
        promotion = {"id":promotion[0],"name":promotion[1],"des":promotion[2],"discount":promotion[3]}
        return promotion  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

def create_promotion(promotion:promotionsM):
    try:
        insert_fields = ["name","des","discount"]
        insert_values = [f"'{promotion.name}'",f"'{promotion.des}'",f"'{promotion.discount}'"]

        fields_str = ', '.join(insert_fields)
        values_str = ', '.join(insert_values)
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

    try:
        new_id = base_worker.insert_data(f"""
        INSERT INTO promotions ({fields_str})
        VALUES ({values_str})
        RETURNING id;                                                                                                 
        """, ())            
        if not new_id:
            return None     
        new_id = new_id[0]                               
        promotion = {"id":new_id[0],"name":promotion.name,"des":promotion.des,"discount":promotion.discount}                                                                
        return promotion   
    except Exception as e:
        print(f"Ошибка: {e}")
        return None
    
def upd_promotion(id, promotion: promotionsM):
    try:
        update_fields = []
        if promotion.name is not None and promotion.name != '':
            update_fields.append(f"name = '{promotion.name}'")
        
        if promotion.des is not None and promotion.des != '':
            update_fields.append(f"des = '{promotion.des}'")

        if promotion.discount is not None and promotion.discount != 0:
            update_fields.append(f"discount = '{promotion.discount}'")

        update_fields_str = ', '.join(update_fields)
        print(update_fields_str)
        try:
            promotion_id = base_worker.insert_data(f"""
            UPDATE promotions
            SET {update_fields_str}
            WHERE id = {id} 
            RETURNING id;
            """, ())
        except Exception as e:
            print(f"Ошибка: {e}")
            return None
        if not promotion_id:
            return None
        promotion_id = promotion_id[0]
        promotion = {"id":promotion_id[0],"name":None,"des":None,"discount":None} 
        return promotion  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

def del_promotion(id):
    try:
        promotion_id = base_worker.insert_data(f"DELETE FROM promotions WHERE id = {id} RETURNING id;",())
        if not promotion_id:
            return None
        else:
            promotion_id = promotion_id[0]
            promotion = {"id":promotion_id[0],"name":None,"des":None,"discount":None}
            return promotion  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500
#
def get_delivery_method(id):
    try:
        delivery_method = base_worker.insert_data(f"SELECT * FROM delivery_methods WHERE id = {id}",())
        if not delivery_method:
            return None
        delivery_method = delivery_method[0]
            
        delivery_method = {"id":delivery_method[0],"method_des":delivery_method[1]}
        return delivery_method  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

def create_delivery_method(delivery_method:delivery_methodsM):
    try:
        insert_fields = ["method_des"]
        insert_values = [f"'{delivery_method.method_des}'"]

        fields_str = ', '.join(insert_fields)
        values_str = ', '.join(insert_values)
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

    try:
        new_id = base_worker.insert_data(f"""
        INSERT INTO delivery_methods ({fields_str})
        VALUES ({values_str})
        RETURNING id;                                                                                                 
        """, ())            
        if not new_id:
            return None     
        new_id = new_id[0]                               
        delivery_method = {"id":new_id[0],"method_des":delivery_method.method_des}                                                                
        return delivery_method   
    except Exception as e:
        print(f"Ошибка: {e}")
        return None
    
def upd_delivery_method(id, delivery_method: delivery_methodsM):
    try:
        update_fields = []
        
        if delivery_method.method_des is not None and delivery_method.method_des != '':
            update_fields.append(f"method_des = '{delivery_method.method_des}'")

        update_fields_str = ', '.join(update_fields)
        try:
            delivery_method_id = base_worker.insert_data(f"""
            UPDATE delivery_methods
            SET {update_fields_str}
            WHERE id = {id} 
            RETURNING id;
            """, ())
        except Exception as e:
            print(f"Ошибка: {e}")
            return None
        if not delivery_method_id:
            return None
        delivery_method_id = delivery_method_id[0]
        delivery_method = {"id":delivery_method_id[0],"method_des":None} 
        return delivery_method  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

def del_delivery_method(id):
    try:
        delivery_method_id = base_worker.insert_data(f"DELETE FROM delivery_methods WHERE id = {id} RETURNING id;",())
        if not delivery_method_id:
            return None
        else:
            delivery_method_id = delivery_method_id[0]
            delivery_method = {"id":delivery_method_id[0],"method_des":None}
            return delivery_method  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500
#
def get_payment_method(id):
    try:
        payment_method = base_worker.insert_data(f"SELECT * FROM payment_methods WHERE id = {id}",())
        if not payment_method:
            return None
        payment_method = payment_method[0]
            
        payment_method = {"id":payment_method[0],"method_des":payment_method[1]}
        return payment_method  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

def create_payment_method(payment_method:payment_methodsM):
    try:
        insert_fields = ["method_des"]
        insert_values = [f"'{payment_method.method_des}'"]

        fields_str = ', '.join(insert_fields)
        values_str = ', '.join(insert_values)
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

    try:
        new_id = base_worker.insert_data(f"""
        INSERT INTO payment_methods ({fields_str})
        VALUES ({values_str})
        RETURNING id;                                                                                                 
        """, ())            
        if not new_id:
            return None     
        new_id = new_id[0]                               
        payment_method = {"id":new_id[0],"method_des":payment_method.method_des}                                                                
        return payment_method   
    except Exception as e:
        print(f"Ошибка: {e}")
        return None
    
def upd_payment_method(id, payment_method: payment_methodsM):
    try:
        update_fields = []
        
        if payment_method.method_des is not None and payment_method.method_des != '':
            update_fields.append(f"method_des = '{payment_method.method_des}'")

        update_fields_str = ', '.join(update_fields)
        try:
            payment_method_id = base_worker.insert_data(f"""
            UPDATE payment_methods
            SET {update_fields_str}
            WHERE id = {id} 
            RETURNING id;
            """, ())
        except Exception as e:
            print(f"Ошибка: {e}")
            return None
        if not payment_method_id:
            return None
        payment_method_id = payment_method_id[0]
        payment_method = {"id":payment_method_id[0],"method_des":None} 
        return payment_method  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

def del_payment_method(id):
    try:
        payment_method_id = base_worker.insert_data(f"DELETE FROM payment_methods WHERE id = {id} RETURNING id;",())
        if not payment_method_id:
            return None
        else:
            payment_method_id = payment_method_id[0]
            payment_method = {"id":payment_method_id[0],"method_des":None}
            return payment_method  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500
#
def get_order(id):
    try:
        order = base_worker.insert_data(f"SELECT * FROM orders WHERE id = {id}",())
        if not order:
            return None
        order = order[0]
            
        order = {"id":order[0],"user_id":order[1],"order_date":order[2],"sum":order[3],"status":order[4],"delivery_method_id":order[5],"payment_method_id":order[6],"sneakers":order[7]}
        return order  
    except Exception as e:
        print(f"Ошибка {e}")
        return 500
    
def upd_order(id, order: ordersM):
    try:
        update_fields = []

        if order.order_date is not None and order.order_date != '':
            update_fields.append(f"order_date = '{order.order_date}'")

        if order.sum is not None and order.sum != 0:
            update_fields.append(f"sum = '{order.sum}'")

        if order.status is not None and order.status != '':
            update_fields.append(f"status = '{order.status}'")

        if order.delivery_method_id is not None and order.delivery_method_id != 0:
            update_fields.append(f"delivery_method_id = '{order.delivery_method_id}'")

        if order.payment_method_id is not None and order.payment_method_id != 0:
            update_fields.append(f"payment_method_id = '{order.payment_method_id}'")
        
        if order.sneakers is not None and order.sneakers != '':
            update_fields.append(f"sneakers = '{order.sneakers}'")

        update_fields_str = ', '.join(update_fields)
        try:
            order_id = base_worker.insert_data(f"""
            UPDATE orders
            SET {update_fields_str}
            WHERE id = {id} 
            RETURNING id;
            """, ())
        except Exception as e:
            print(f"Ошибка: {e}")
            return None
        if not order_id:
            return None
        order_id = order_id[0]
        order = {"id":order_id[0],"user_id":None,"order_date":None,"sum":None,"status":None,"delivery_method_id":None,"payment_method_id":None,"sneakers":None}
        return order
    except Exception as e:
        print(f"Ошибка {e}")
        return 500

def del_order(id):
    try:
        order_id = base_worker.insert_data(f"DELETE FROM orders WHERE id = {id} RETURNING id;",())
        if not order_id:
            return None
        else:
            order_id = order_id[0]
            order = {"id":order_id[0],"user_id":None,"order_date":None,"sum":None,"status":None,"delivery_method_id":None,"payment_method_id":None,"sneakers":None}
            return order
    except Exception as e:
        print(f"Ошибка {e}")
        return 500