import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker
from main_api.db import engine, get_db
from main_api.entities.nationality import Nationality
from main import app


@pytest.fixture
def test_db():
    """Use existing SQLite database for testing with cleanup"""
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = TestingSessionLocal()
    yield db
    
    # Cleanup: delete all nationalities after test
    db.query(Nationality).delete()
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


def test_get_all_nationalities(client):
    response = client.get("/nationalities/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_nationality(client):
    response = client.post(
        "/nationalities/",
        params={
            "country_name": "Spain",
            "country_code": "ES"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["country_name"] == "Spain"
    assert data["country_code"] == "ES"


def test_get_nationality_by_id(client):
    # Create nationality
    create_response = client.post(
        "/nationalities/",
        params={
            "country_name": "Spain",
            "country_code": "ES"
        }
    )
    nationality_id = create_response.json()["id"]
    
    # Get nationality
    response = client.get(f"/nationalities/{nationality_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["country_name"] == "Spain"
    assert data["id"] == nationality_id


def test_get_nationality_by_id_not_found(client):
    response = client.get("/nationalities/999")
    assert response.status_code == 200
    assert response.json() is None


def test_update_nationality(client):
    # Create nationality
    create_response = client.post(
        "/nationalities/",
        params={
            "country_name": "Spain",
            "country_code": "ES"
        }
    )
    nationality_id = create_response.json()["id"]
    
    # Update nationality
    response = client.put(
        f"/nationalities/{nationality_id}",
        params={
            "country_name": "Portugal",
            "country_code": "PT"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["country_name"] == "Portugal"
    assert data["country_code"] == "PT"


def test_delete_nationality(client):
    # Create nationality
    create_response = client.post(
        "/nationalities/",
        params={
            "country_name": "Spain",
            "country_code": "ES"
        }
    )
    nationality_id = create_response.json()["id"]
    
    # Delete nationality
    response = client.delete(f"/nationalities/{nationality_id}")
    assert response.status_code == 200
    assert response.json()["success"] is True
    
    # Verify deletion
    get_response = client.get(f"/nationalities/{nationality_id}")
    assert get_response.json() is None
