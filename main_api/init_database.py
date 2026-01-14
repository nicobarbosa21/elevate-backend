from sqlalchemy.orm import Session
from main_api.db import engine, Base, SessionLocal
from main_api.entities.employee import Employee
from main_api.entities.jobs import Job
from main_api.entities.nationality import Nationality
from main_api.entities.seniority import Seniority
from auth.models import User
from auth.helpers import hash_password


def init_database():
    """Initialize database with default data"""
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    try:
        if db.query(User).first() is not None:
            return
        
        users = [
            User(username="nicobarbosa", hashed_password=hash_password("Contraseña123")),
            User(username="admin", hashed_password=hash_password("Admin12345"))
        ]
        db.add_all(users)
        
        nationalities = [
            Nationality(country_name="Argentina", country_code="ARG"),
            Nationality(country_name="United States", country_code="USA"),
            Nationality(country_name="Colombia", country_code="COL"),
            Nationality(country_name="Brasil", country_code="BRA")
        ]
        db.add_all(nationalities)
        
        jobs = [
            Job(title="Developer", description="Python developer", salary=1800),
            Job(title="Tester", description="Manual tester", salary=1800),
            Job(title="Data Engineer", description="Data bricks engineer", salary=1800),
            Job(title="Data Analyst", description="PowerBI engineer", salary=1800)
        ]
        db.add_all(jobs)
        
        seniorities = [
            Seniority(level="Senior", description="Experienced professional with deep expertise"),
            Seniority(level="Junior", description="Entry-level professional building foundational skills"),
            Seniority(level="Semi Senior", description="Mid-level professional with growing expertise"),
            Seniority(level="Technician", description="Specialized technical professional"),
            Seniority(level="Senior Technician", description="Advanced technical specialist"),
            Seniority(level="Engineer", description="Professional engineer with technical expertise"),
            Seniority(level="Senior Engineer", description="Highly experienced engineering professional")
        ]
        db.add_all(seniorities)
        
        db.commit()
        
        employees = [
            Employee(
                name="Nicolas",
                last_name="Barbosa",
                age=22,
                dni="45213134",
                job_id=1,
                country_id=1,
                seniority_id=5
            ),
            Employee(
                name="Juan",
                last_name="Chiapero",
                age=43,
                dni="3456789",
                job_id=1,
                country_id=3,
                seniority_id=7
            ),
            Employee(
                name="Adolfo",
                last_name="Perez",
                age=32,
                dni="1233456",
                job_id=2,
                country_id=4,
                seniority_id=6
            ),
            Employee(
                name="Maria",
                last_name="Garcia",
                age=28,
                dni="9876543",
                job_id=3,
                country_id=2,
                seniority_id=3
            ),
            Employee(
                name="Carlos",
                last_name="Rodriguez",
                age=35,
                dni="5554321",
                job_id=4,
                country_id=1,
                seniority_id=1
            )
        ]
        db.add_all(employees)
        db.commit()
        
    except Exception as e:
        db.rollback()
        print(f"Error initializing database: {e}")
        raise
    finally:
        db.close()


if __name__ == "__main__":
    init_database()