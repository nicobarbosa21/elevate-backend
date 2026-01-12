from sqlalchemy.orm import Session, joinedload
from main_api.entities.employee import Employee

def get_all_employees(db: Session):
    return db.query(Employee).options(
        joinedload(Employee.job),
        joinedload(Employee.nationality),
        joinedload(Employee.seniority)
    ).all()

def get_employee_by_id(db: Session, employee_id: int):
    return db.query(Employee).options(
        joinedload(Employee.job),
        joinedload(Employee.nationality),
        joinedload(Employee.seniority)
    ).filter(Employee.id == employee_id).first()

def get_employees_by_name(db: Session, name: str):
    return db.query(Employee).options(
        joinedload(Employee.job),
        joinedload(Employee.nationality),
        joinedload(Employee.seniority)
    ).filter(Employee.name.ilike(f"%{name}%")).all()

def get_employees_by_last_name(db: Session, last_name: str):
    return db.query(Employee).options(
        joinedload(Employee.job),
        joinedload(Employee.nationality),
        joinedload(Employee.seniority)
    ).filter(Employee.last_name.ilike(f"%{last_name}%")).all()

def create_employee(db: Session, name: str, last_name: str, age: int, dni: str, job_id: int, country_id: int, seniority_id: int):
    new_employee = Employee(
        name=name,
        last_name=last_name,
        age=age,
        dni=dni,
        job_id=job_id,
        country_id=country_id,
        seniority_id=seniority_id
    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

def update_employee(db: Session, employee_id: int, name: str = None, last_name: str = None, age: int = None, dni: str = None, job_id: int = None, country_id: int = None, seniority_id: int = None):
    employee = get_employee_by_id(db, employee_id)
    if employee:
        if name is not None:
            employee.name = name
        if last_name is not None:
            employee.last_name = last_name
        if age is not None:
            employee.age = age
        if dni is not None:
            employee.dni = dni
        if job_id is not None:
            employee.job_id = job_id
        if country_id is not None:
            employee.country_id = country_id
        if seniority_id is not None:
            employee.seniority_id = seniority_id
        db.commit()
        db.refresh(employee)
    return employee

def delete_employee(db: Session, employee_id: int):
    employee = get_employee_by_id(db, employee_id)
    if employee:
        db.delete(employee)
        db.commit()
        return True
    return False
