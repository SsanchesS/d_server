from typing import Optional,Union
from pydantic import BaseModel,constr,EmailStr
from datetime import date

class sneakersM(BaseModel):
    des: Optional[str] = None
    price: Optional[int] = None
    img: Optional[ Union[str, None] ] = None # file base64 str можно ли обойтись без Union?
    category_id: Optional[int] = None

class usersM(BaseModel):
    f_name: Optional[str] = None
    s_name: Optional[str] = None    
    password: Optional[constr(min_length=8, max_length=32)] = None
    email: Optional[EmailStr] = None
    role_id: Optional[int] = 0

class LoginM(BaseModel):
    password: constr(min_length=8, max_length=32)
    email: EmailStr

class categoriesM(BaseModel):
    name: Optional[str] = None
    des: Optional[str] = None

class promotionsM(BaseModel):
    name: Optional[str] = None
    des: Optional[str] = None    
    discount: Optional[int] = None

class delivery_methodsM(BaseModel):
    method_des: Optional[str] = None

class payment_methodsM(BaseModel):
    method_des: Optional[str] = None

class ordersM(BaseModel):
    user_id: Optional[int] = None
    order_date: Optional[str] = None # date 
    sum: Optional[int] = None
    status: Optional[str] = None
    delivery_method_id: Optional[int] = None
    payment_method_id: Optional[int] = None
    sneakers: Optional[str] = None

class rolesM(BaseModel):
    role: Optional[str] = None