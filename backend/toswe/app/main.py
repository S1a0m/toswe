from fastapi import FastAPI
from app.routes import customers, products, orders, notifications
from app.database import engine
from app.models import Base

app = FastAPI(title="Toswe API")

# Création des tables si elles n'existent pas
Base.metadata.create_all(bind=engine)

# Inclusion des routes
app.include_router(customers.router, prefix="/customers", tags=["Customers"])
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])
app.include_router(notifications.router, prefix="/notifications", tags=["Notifications"])
