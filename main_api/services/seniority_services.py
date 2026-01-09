from sqlalchemy.orm import Session
from main_api.entities.seniority import Seniority

def get_all_seniorities(db: Session):
    return db.query(Seniority).all()

def get_seniority_by_id(db: Session, seniority_id: int):
    return db.query(Seniority).filter(Seniority.id == seniority_id).first()

def create_seniority(db: Session, level: str, description: str = None):
    new_seniority = Seniority(level=level, description=description)
    db.add(new_seniority)
    db.commit()
    db.refresh(new_seniority)
    return new_seniority

def update_seniority(db: Session, seniority_id: int, level: str = None, description: str = None):
    seniority = get_seniority_by_id(db, seniority_id)
    if seniority:
        if level is not None:
            seniority.level = level
        if description is not None:
            seniority.description = description
        db.commit()
        db.refresh(seniority)
    return seniority

def delete_seniority(db: Session, seniority_id: int):
    seniority = get_seniority_by_id(db, seniority_id)
    if seniority:
        db.delete(seniority)
        db.commit()
        return True
    return False
