from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from main_api.db import get_db
from main_api.services.job_services import (
    get_all_jobs,
    get_job_by_id,
    create_job,
    update_job,
    delete_job
)

router = APIRouter(
    prefix="/jobs",
    tags=["jobs"]
)

@router.get("/")
def get_jobs(db: Session = Depends(get_db)):
    return get_all_jobs(db)

@router.get("/{job_id}")
def get_job(job_id: int, db: Session = Depends(get_db)):
    return get_job_by_id(db, job_id)

@router.post("/")
def add_job(
    title: str,
    description: str,
    salary: int,
    db: Session = Depends(get_db)
):
    return create_job(db, title, description, salary)

@router.put("/{job_id}")
def modify_job(
    job_id: int,
    title: str = None,
    description: str = None,
    salary: int = None,
    db: Session = Depends(get_db)
):
    return update_job(db, job_id, title, description, salary)

@router.delete("/{job_id}")
def remove_job(job_id: int, db: Session = Depends(get_db)):
    success = delete_job(db, job_id)
    return {"success": success}
