from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from main_api.db import get_db
from main_api.services.seniority_services import (
    get_all_seniorities,
    get_seniority_by_id,
    create_seniority,
    update_seniority,
    delete_seniority
)

router = APIRouter(
    prefix="/seniorities",
    tags=["seniorities"]
)

@router.get("/")
def get_seniorities(db: Session = Depends(get_db)):
    return get_all_seniorities(db)

@router.get("/{seniority_id}")
def get_seniority(seniority_id: int, db: Session = Depends(get_db)):
    return get_seniority_by_id(db, seniority_id)

@router.post("/")
def add_seniority(
    level: str,
    description: str = None,
    db: Session = Depends(get_db)
):
    return create_seniority(db, level, description)

@router.put("/{seniority_id}")
def modify_seniority(
    seniority_id: int,
    level: str = None,
    description: str = None,
    db: Session = Depends(get_db)
):
    return update_seniority(db, seniority_id, level, description)

@router.delete("/{seniority_id}")
def remove_seniority(seniority_id: int, db: Session = Depends(get_db)):
    success = delete_seniority(db, seniority_id)
    return {"success": success}
