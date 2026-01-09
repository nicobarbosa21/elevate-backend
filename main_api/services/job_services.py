from sqlalchemy.orm import Session
from main_api.entities.jobs import Job

def get_all_jobs(db: Session):
    return db.query(Job).all()

def get_job_by_id(db: Session, job_id: int):
    return db.query(Job).filter(Job.id == job_id).first()

def create_job(db: Session, title: str, description: str, salary: int):
    new_job = Job(title=title, description=description, salary=salary)
    db.add(new_job)
    db.commit()
    db.refresh(new_job)
    return new_job

def update_job(db: Session, job_id: int, title: str = None, description: str = None, salary: int = None):
    job = get_job_by_id(db, job_id)
    if job:
        if title is not None:
            job.title = title
        if description is not None:
            job.description = description
        if salary is not None:
            job.salary = salary
        db.commit()
        db.refresh(job)
    return job

def delete_job(db: Session, job_id: int):
    job = get_job_by_id(db, job_id)
    if job:
        db.delete(job)
        db.commit()
        return True
    return False