from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from main_api.db import get_db
from main_api.services.employee_services import (
    get_all_employees,
    get_employee_by_id,
    create_employee,
    update_employee,
    delete_employee
)

router = APIRouter(
    prefix="/employees",
    tags=["employees"]
)

@router.get("/")
def get_employees(db: Session = Depends(get_db)):
    return get_all_employees(db)

@router.get("/{employee_id}")
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    return get_employee_by_id(db, employee_id)

@router.post("/")
def add_employee(
    name: str,
    last_name: str,
    age: int,
    dni: str,
    job_id: int,
    country_id: int,
    seniority_id: int,
    db: Session = Depends(get_db)
):
    return create_employee(db, name, last_name, age, dni, job_id, country_id, seniority_id)

@router.put("/{employee_id}")
def modify_employee(
    employee_id: int,
    name: str = None,
    last_name: str = None,
    age: int = None,
    dni: str = None,
    job_id: int = None,
    country_id: int = None,
    seniority_id: int = None,
    db: Session = Depends(get_db)
):
    return update_employee(db, employee_id, name, last_name, age, dni, job_id, country_id, seniority_id)

@router.delete("/{employee_id}")
def remove_employee(employee_id: int, db: Session = Depends(get_db)):
    success = delete_employee(db, employee_id)
    return {"success": success}