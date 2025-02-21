from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, dependencies, models

router = APIRouter()

@router.post("/", response_model=schemas.CustomerCreate)
async def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(dependencies.get_db)):
    db_customer = models.Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer


