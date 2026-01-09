import pytest
from sqlalchemy.orm import sessionmaker
from main_api.db import engine
from main_api.entities.employee import Employee
from main_api.services import employee_services


@pytest.fixture
def test_db():
    """Use existing SQLite database for testing with cleanup"""
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = TestingSessionLocal()
    yield db
    
    # Cleanup: delete all employees after test
    db.query(Employee).delete()
    db.commit()
    db.close()


def test_get_all_employees_empty(test_db):
    employees = employee_services.get_all_employees(test_db)
    assert employees == []


def test_create_employee(test_db):
    employee = employee_services.create_employee(
        test_db, "John", "Doe", 30, "12345678", 1, 1, 1
    )
    assert employee.name == "John"
    assert employee.last_name == "Doe"
    assert employee.age == 30
    assert employee.dni == "12345678"
    assert employee.job_id == 1
    assert employee.country_id == 1
    assert employee.seniority_id == 1
    assert employee.id is not None


def test_get_all_employees(test_db):
    employee_services.create_employee(test_db, "John", "Doe", 30, "12345678", 1, 1, 1)
    employee_services.create_employee(test_db, "Jane", "Smith", 28, "87654321", 1, 1, 1)
    
    employees = employee_services.get_all_employees(test_db)
    assert len(employees) == 2
    assert employees[0].name == "John"
    assert employees[1].name == "Jane"


def test_get_employee_by_id(test_db):
    created_employee = employee_services.create_employee(
        test_db, "John", "Doe", 30, "12345678", 1, 1, 1
    )
    
    employee = employee_services.get_employee_by_id(test_db, created_employee.id)
    assert employee is not None
    assert employee.name == "John"
    assert employee.id == created_employee.id


def test_get_employee_by_id_not_found(test_db):
    employee = employee_services.get_employee_by_id(test_db, 999)
    assert employee is None


def test_update_employee(test_db):
    created_employee = employee_services.create_employee(
        test_db, "John", "Doe", 30, "12345678", 1, 1, 1
    )
    
    updated_employee = employee_services.update_employee(
        test_db, created_employee.id, name="Jane", age=35
    )
    
    assert updated_employee.name == "Jane"
    assert updated_employee.age == 35
    assert updated_employee.last_name == "Doe"


def test_update_employee_not_found(test_db):
    result = employee_services.update_employee(test_db, 999, name="Jane")
    assert result is None


def test_delete_employee(test_db):
    created_employee = employee_services.create_employee(
        test_db, "John", "Doe", 30, "12345678", 1, 1, 1
    )
    
    success = employee_services.delete_employee(test_db, created_employee.id)
    assert success is True
    
    employee = employee_services.get_employee_by_id(test_db, created_employee.id)
    assert employee is None


def test_delete_employee_not_found(test_db):
    success = employee_services.delete_employee(test_db, 999)
    assert success is False
