from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from main_api.db import get_db
from main_api.services.nationality_services import (
    get_all_nationalities,
    get_nationality_by_id,
    create_nationality,
    update_nationality,
    delete_nationality
)

router = APIRouter(
    prefix="/nationalities",
    tags=["nationalities"]
)

@router.get("/")
def get_nationalities(db: Session = Depends(get_db)):
    return get_all_nationalities(db)

@router.get("/{nationality_id}")
def get_nationality(nationality_id: int, db: Session = Depends(get_db)):
    return get_nationality_by_id(db, nationality_id)

@router.post("/")
def add_nationality(
    country_name: str,
    country_code: str,
    db: Session = Depends(get_db)
):
    return create_nationality(db, country_name, country_code)

@router.put("/{nationality_id}")
def modify_nationality(
    nationality_id: int,
    country_name: str = None,
    country_code: str = None,
    db: Session = Depends(get_db)
):
    return update_nationality(db, nationality_id, country_name, country_code)

@router.delete("/{nationality_id}")
def remove_nationality(nationality_id: int, db: Session = Depends(get_db)):
    success = delete_nationality(db, nationality_id)
    return {"success": success}
