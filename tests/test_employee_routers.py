import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker
from main_api.db import engine, get_db
from main_api.entities.employee import Employee
from main import app


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


@pytest.fixture
def client(test_db):
    """Create a test client with overridden get_db dependency"""
    def override_get_db():
        try:
            yield test_db
        finally:
            pass
    
    app.dependency_overrides[get_db] = override_get_db
    
    with TestClient(app) as test_client:
        yield test_client
    
    app.dependency_overrides.clear()


def test_get_all_employees(client):
    response = client.get("/employees/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_employee(client):
    response = client.post(
        "/employees/",
        params={
            "name": "John",
            "last_name": "Doe",
            "age": 30,
            "dni": "12345678",
            "job_id": 1,
            "country_id": 1,
            "seniority_id": 1
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John"
    assert data["last_name"] == "Doe"
    assert data["age"] == 30


def test_get_employee_by_id(client):
    # Create employee
    create_response = client.post(
        "/employees/",
        params={
            "name": "John",
            "last_name": "Doe",
            "age": 30,
            "dni": "12345678",
            "job_id": 1,
            "country_id": 1,
            "seniority_id": 1
        }
    )
    employee_id = create_response.json()["id"]
    
    # Get employee
    response = client.get(f"/employees/{employee_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John"
    assert data["id"] == employee_id


def test_get_employee_by_id_not_found(client):
    response = client.get("/employees/999")
    assert response.status_code == 200
    assert response.json() is None


def test_update_employee(client):
    # Create employee
    create_response = client.post(
        "/employees/",
        params={
            "name": "John",
            "last_name": "Doe",
            "age": 30,
            "dni": "12345678",
            "job_id": 1,
            "country_id": 1,
            "seniority_id": 1
        }
    )
    employee_id = create_response.json()["id"]
    
    # Update employee
    response = client.put(
        f"/employees/{employee_id}",
        params={
            "name": "Jane",
            "age": 35
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Jane"
    assert data["age"] == 35


def test_delete_employee(client):
    # Create employee
    create_response = client.post(
        "/employees/",
        params={
            "name": "John",
            "last_name": "Doe",
            "age": 30,
            "dni": "12345678",
            "job_id": 1,
            "country_id": 1,
            "seniority_id": 1
        }
    )
    employee_id = create_response.json()["id"]
    
    # Delete employee
    response = client.delete(f"/employees/{employee_id}")
    assert response.status_code == 200
    assert response.json()["success"] is True
    
    # Verify deletion
    get_response = client.get(f"/employees/{employee_id}")
    assert get_response.json() is None
