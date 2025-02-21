from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base  # Base SQLAlchemy

# --- CUSTOMER ---
class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=True)  # Nullable pour les non abonnés
    phone_number = Column(String, nullable=False)
    address = Column(String, nullable=False)
    subscribed = Column(Boolean, default=False)
    subscription_date = Column(DateTime, default=None, nullable=True)  # Peut être NULL

    orders = relationship("Order", back_populates="customer")
    notifications = relationship("Notification", back_populates="customer")

# --- PRODUCT ---
class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    available_stock = Column(Integer, default=0)
    image_first = Column(String)  # URL de l'image
    image_second = Column(String)  
    category = Column(String)

# --- ORDER --- Reçu de la commande
class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    date_order = Column(DateTime, default=datetime.now)
    status = Column(String, default="pending")
    total_amount = Column(Float, default=0.0)
    payment_method = Column(String, nullable=False)
    transaction_id = Column(String, unique=True)

    customer = relationship("Customer", back_populates="orders")
    order_items = relationship("OrderItem", back_populates="order")

# --- ORDER ITEM --- Produit commandé
class OrderItem(Base):
    __tablename__ = "order_items"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("products.id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Float, nullable=False)

    order = relationship("Order", back_populates="order_items")
    product = relationship("Product")

# --- NOTIFICATION --- suivi de commandes ou autres
class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.id"), nullable=False)
    message = Column(String, nullable=False)
    is_read = Column(Boolean, default=False)  # 0 = non lu, 1 = lu
    creation_date = Column(DateTime, default=datetime.now)

    customer = relationship("Customer", back_populates="notifications")

# --- PROMO --- offres promotionnelles
class Promo(Base):
    __tablename__ = "promos"
    id = Column(Integer, primary_key=True, index=True)
    image = Column(String)
    message = Column(String, nullable=False)
    sent = Column(Boolean, default=False)  # 0 = non envoyé, 1 = envoyé
    creation_date = Column(DateTime, default=datetime.now)
