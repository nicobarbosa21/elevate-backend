import pytest
from sqlalchemy.orm import sessionmaker
from main_api.db import engine
from main_api.entities.seniority import Seniority
from main_api.services import seniority_services


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


def test_get_all_seniorities_empty(test_db):
    seniorities = seniority_services.get_all_seniorities(test_db)
    assert seniorities == []


def test_create_seniority(test_db):
    seniority = seniority_services.create_seniority(
        test_db, "Senior", "Senior Developer"
    )
    assert seniority.level == "Senior"
    assert seniority.description == "Senior Developer"
    assert seniority.id is not None


def test_get_all_seniorities(test_db):
    seniority_services.create_seniority(test_db, "Senior", "Senior Developer")
    seniority_services.create_seniority(test_db, "Junior", "Junior Developer")
    
    seniorities = seniority_services.get_all_seniorities(test_db)
    assert len(seniorities) == 2
    assert seniorities[0].level == "Senior"
    assert seniorities[1].level == "Junior"


def test_get_seniority_by_id(test_db):
    created_seniority = seniority_services.create_seniority(
        test_db, "Senior", "Senior Developer"
    )
    
    seniority = seniority_services.get_seniority_by_id(test_db, created_seniority.id)
    assert seniority is not None
    assert seniority.level == "Senior"
    assert seniority.id == created_seniority.id


def test_get_seniority_by_id_not_found(test_db):
    seniority = seniority_services.get_seniority_by_id(test_db, 999)
    assert seniority is None


def test_update_seniority(test_db):
    created_seniority = seniority_services.create_seniority(
        test_db, "Senior", "Senior Developer"
    )
    
    updated_seniority = seniority_services.update_seniority(
        test_db, created_seniority.id, level="Lead", description="Lead Developer"
    )
    
    assert updated_seniority.level == "Lead"
    assert updated_seniority.description == "Lead Developer"


def test_update_seniority_not_found(test_db):
    result = seniority_services.update_seniority(test_db, 999, level="Lead")
    assert result is None


def test_delete_seniority(test_db):
    created_seniority = seniority_services.create_seniority(
        test_db, "Senior", "Senior Developer"
    )
    
    success = seniority_services.delete_seniority(test_db, created_seniority.id)
    assert success is True
    
    seniority = seniority_services.get_seniority_by_id(test_db, created_seniority.id)
    assert seniority is None


def test_delete_seniority_not_found(test_db):
    success = seniority_services.delete_seniority(test_db, 999)
    assert success is False
