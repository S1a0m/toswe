from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import models, schemas, dependencies

router = APIRouter()

@router.post("/", response_model=schemas.ProductCreate)
async def create_product(product: schemas.ProductCreate, db: Session = Depends(dependencies.get_db)):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@router.get("/{product_id}")
async def get_product(product_id: int, db: Session = Depends(dependencies.get_db)):
    return db.query(models.Product).filter(models.Product.id == product_id).first()
