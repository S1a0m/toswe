from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, dependencies

router = APIRouter()

@router.post("/", response_model=schemas.NotificationCreate)
async def create_notification(notification: schemas.NotificationCreate, db: Session = Depends(dependencies.get_db)):
    db_notification = models.Notification(**notification.dict())
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification

@router.get("/{customer_id}")
async def get_notifications(customer_id: int, db: Session = Depends(dependencies.get_db)):
    return db.query(models.Notification).filter(models.Notification.customer_id == customer_id).all()
