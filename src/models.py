from typing import Optional,Union
from pydantic import BaseModel,constr,EmailStr
from datetime import date

class SneakerM(BaseModel):
    img: Optional[ Union[str, None] ] = None # file base64 str можно ли обойтись без Union?
    des: Optional[str] = None
    price: Optional[int] = None
    category_id: Optional[int] = None

class usersM(BaseModel):
    f_name: Optional[str] = None
    s_name: Optional[str] = None    
    password: Optional[constr(min_length=8, max_length=32)] = None
    email: Optional[EmailStr] = None
    role_id: Optional[int] = 0

    itemsPrice: Optional[int] = 0                             # or None
    sneakers_basket: Optional[str] = None

class LoginM(BaseModel):
    password: constr(min_length=8, max_length=32)
    email: EmailStr

class categoriesM(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None

class promotionsM(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None    
    discount: Optional[int] = None

class delivery_methodsM(BaseModel):
    name: Optional[str] = None
    method_description: Optional[str] = None

class payment_methodsM(BaseModel):
    name: Optional[str] = None
    method_description: Optional[str] = None

class ordersM(BaseModel):
    user_id: Optional[int] = None
    order_date: Optional[date] = None    
    sum: Optional[int] = None
    status: Optional[str] = None
    delivery_method_id: Optional[int] = None
    payment_method_id: Optional[int] = None