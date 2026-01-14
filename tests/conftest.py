from dotenv import load_dotenv
load_dotenv()

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker
from datetime import timedelta
from main_api.db import engine, get_db, Base
from main_api.entities.employee import Employee
from main_api.entities.jobs import Job
from main_api.entities.nationality import Nationality
from main_api.entities.seniority import Seniority
from auth.models import User
from auth.helpers import hash_password, create_access_token
from main import app


@pytest.fixture
def test_db():
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.query(Employee).delete()
    db.query(User).delete()
    db.query(Job).delete()
    db.query(Nationality).delete()
    db.query(Seniority).delete()
    db.commit()
    db.close()


@pytest.fixture
def test_user(test_db):
    user = User(username="testuser", hashed_password=hash_password("TestPass123"))
    test_db.add(user)
    test_db.commit()
    test_db.refresh(user)
    return user


@pytest.fixture
def access_token(test_user):
    access_token_expires = timedelta(minutes=60)
    token = create_access_token(
        sub=test_user.username,
        expires_delta=access_token_expires
    )
    return token


@pytest.fixture
def client(test_db, access_token):
    def override_get_db():
        try:
            yield test_db
        finally:
            pass
    app.dependency_overrides[get_db] = override_get_db
    client = TestClient(app)
    client.headers = {
        "Authorization": f"Bearer {access_token}"
    }
    yield client
    app.dependency_overrides.clear()
