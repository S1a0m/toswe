from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# --- Client ---
class CustomerCreate(BaseModel):  # Mise à jour client
    name: Optional[str] = None
    surname: Optional[str] = None
    email: Optional[EmailStr] = None
    phone_number: Optional[str] = None
    password: Optional[str] = None  # Rendu optionnel
    address: Optional[str] = None
    subscribed: Optional[bool] = None
    subscription_date: Optional[datetime] = None

# --- Produit ---
class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    available_stock: int
    image_first: Optional[str] = None
    image_second: Optional[str] = None
    category: str

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int
    unit_price: float

class OrderCreate(BaseModel):
    customer_id: int
    total_amount: float
    items: List[OrderItemCreate]

# --- Alertes ---
class NotificationCreate(BaseModel):
    customer_id: int
    message: str
    is_read: Optional[bool] = False  

class PromoCreate(BaseModel):
    image: str
    message: str
    sent: Optional[bool] = False  
