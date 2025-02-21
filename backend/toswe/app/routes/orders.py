from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, dependencies

router = APIRouter()

@router.post("/", response_model=schemas.OrderCreate)
async def create_order(order: schemas.OrderCreate, db: Session = Depends(dependencies.get_db)):
    db_order = models.Order(**order.dict())
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@router.get("/{order_id}")
async def get_order(order_id: int, db: Session = Depends(dependencies.get_db)):
    return db.query(models.Order).filter(models.Order.id == order_id).first()
