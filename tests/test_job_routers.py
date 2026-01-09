import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker
from main_api.db import engine, get_db
from main_api.entities.jobs import Job
from main import app


@pytest.fixture
def test_db():
    """Use existing SQLite database for testing with cleanup"""
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = TestingSessionLocal()
    yield db
    
    # Cleanup: delete all jobs after test
    db.query(Job).delete()
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


def test_get_all_jobs(client):
    response = client.get("/jobs/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_job(client):
    response = client.post(
        "/jobs/",
        params={
            "title": "Developer",
            "description": "Software Developer",
            "salary": 50000
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Developer"
    assert data["description"] == "Software Developer"
    assert data["salary"] == 50000


def test_get_job_by_id(client):
    # Create job
    create_response = client.post(
        "/jobs/",
        params={
            "title": "Developer",
            "description": "Software Developer",
            "salary": 50000
        }
    )
    job_id = create_response.json()["id"]
    
    # Get job
    response = client.get(f"/jobs/{job_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Developer"
    assert data["id"] == job_id


def test_get_job_by_id_not_found(client):
    response = client.get("/jobs/999")
    assert response.status_code == 200
    assert response.json() is None


def test_update_job(client):
    # Create job
    create_response = client.post(
        "/jobs/",
        params={
            "title": "Developer",
            "description": "Software Developer",
            "salary": 50000
        }
    )
    job_id = create_response.json()["id"]
    
    # Update job
    response = client.put(
        f"/jobs/{job_id}",
        params={
            "title": "Senior Developer",
            "salary": 70000
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Senior Developer"
    assert data["salary"] == 70000


def test_delete_job(client):
    # Create job
    create_response = client.post(
        "/jobs/",
        params={
            "title": "Developer",
            "description": "Software Developer",
            "salary": 50000
        }
    )
    job_id = create_response.json()["id"]
    
    # Delete job
    response = client.delete(f"/jobs/{job_id}")
    assert response.status_code == 200
    assert response.json()["success"] is True
    
    # Verify deletion
    get_response = client.get(f"/jobs/{job_id}")
    assert get_response.json() is None
