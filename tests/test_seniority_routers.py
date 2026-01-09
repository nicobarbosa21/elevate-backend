import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker
from main_api.db import engine, get_db
from main_api.entities.seniority import Seniority
from main import app


@pytest.fixture
def test_db():
    """Use existing SQLite database for testing with cleanup"""
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = TestingSessionLocal()
    yield db
    
    # Cleanup: delete all seniorities after test
    db.query(Seniority).delete()
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


def test_get_all_seniorities(client):
    response = client.get("/seniorities/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_seniority(client):
    response = client.post(
        "/seniorities/",
        params={
            "level": "Senior",
            "description": "Senior Developer"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["level"] == "Senior"
    assert data["description"] == "Senior Developer"


def test_get_seniority_by_id(client):
    # Create seniority
    create_response = client.post(
        "/seniorities/",
        params={
            "level": "Senior",
            "description": "Senior Developer"
        }
    )
    seniority_id = create_response.json()["id"]
    
    # Get seniority
    response = client.get(f"/seniorities/{seniority_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["level"] == "Senior"
    assert data["id"] == seniority_id


def test_get_seniority_by_id_not_found(client):
    response = client.get("/seniorities/999")
    assert response.status_code == 200
    assert response.json() is None


def test_update_seniority(client):
    # Create seniority
    create_response = client.post(
        "/seniorities/",
        params={
            "level": "Senior",
            "description": "Senior Developer"
        }
    )
    seniority_id = create_response.json()["id"]
    
    # Update seniority
    response = client.put(
        f"/seniorities/{seniority_id}",
        params={
            "level": "Lead",
            "description": "Lead Developer"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["level"] == "Lead"
    assert data["description"] == "Lead Developer"


def test_delete_seniority(client):
    # Create seniority
    create_response = client.post(
        "/seniorities/",
        params={
            "level": "Senior",
            "description": "Senior Developer"
        }
    )
    seniority_id = create_response.json()["id"]
    
    # Delete seniority
    response = client.delete(f"/seniorities/{seniority_id}")
    assert response.status_code == 200
    assert response.json()["success"] is True
    
    # Verify deletion
    get_response = client.get(f"/seniorities/{seniority_id}")
    assert get_response.json() is None
