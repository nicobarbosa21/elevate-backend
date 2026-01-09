from sqlalchemy.orm import Session
from main_api.entities.nationality import Nationality

def get_all_nationalities(db: Session):
    return db.query(Nationality).all()

def get_nationality_by_id(db: Session, nationality_id: int):
    return db.query(Nationality).filter(Nationality.id == nationality_id).first()

def create_nationality(db: Session, country_name: str, country_code: str):
    new_nationality = Nationality(country_name=country_name, country_code=country_code)
    db.add(new_nationality)
    db.commit()
    db.refresh(new_nationality)
    return new_nationality

def update_nationality(db: Session, nationality_id: int, country_name: str = None, country_code: str = None):
    nationality = get_nationality_by_id(db, nationality_id)
    if nationality:
        if country_name is not None:
            nationality.country_name = country_name
        if country_code is not None:
            nationality.country_code = country_code
        db.commit()
        db.refresh(nationality)
    return nationality

def delete_nationality(db: Session, nationality_id: int):
    nationality = get_nationality_by_id(db, nationality_id)
    if nationality:
        db.delete(nationality)
        db.commit()
        return True
    return False
