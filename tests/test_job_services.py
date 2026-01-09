import pytest
from sqlalchemy.orm import sessionmaker
from main_api.db import engine
from main_api.entities.jobs import Job
from main_api.services import job_services


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


def test_get_all_jobs_empty(test_db):
    jobs = job_services.get_all_jobs(test_db)
    assert jobs == []


def test_create_job(test_db):
    job = job_services.create_job(
        test_db, "Developer", "Software Developer", 50000
    )
    assert job.title == "Developer"
    assert job.description == "Software Developer"
    assert job.salary == 50000
    assert job.id is not None


def test_get_all_jobs(test_db):
    job_services.create_job(test_db, "Developer", "Software Developer", 50000)
    job_services.create_job(test_db, "Manager", "Project Manager", 60000)
    
    jobs = job_services.get_all_jobs(test_db)
    assert len(jobs) == 2
    assert jobs[0].title == "Developer"
    assert jobs[1].title == "Manager"


def test_get_job_by_id(test_db):
    created_job = job_services.create_job(
        test_db, "Developer", "Software Developer", 50000
    )
    
    job = job_services.get_job_by_id(test_db, created_job.id)
    assert job is not None
    assert job.title == "Developer"
    assert job.id == created_job.id


def test_get_job_by_id_not_found(test_db):
    job = job_services.get_job_by_id(test_db, 999)
    assert job is None


def test_update_job(test_db):
    created_job = job_services.create_job(
        test_db, "Developer", "Software Developer", 50000
    )
    
    updated_job = job_services.update_job(
        test_db, created_job.id, title="Senior Developer", salary=70000
    )
    
    assert updated_job.title == "Senior Developer"
    assert updated_job.salary == 70000
    assert updated_job.description == "Software Developer"


def test_update_job_not_found(test_db):
    result = job_services.update_job(test_db, 999, title="Senior Developer")
    assert result is None


def test_delete_job(test_db):
    created_job = job_services.create_job(
        test_db, "Developer", "Software Developer", 50000
    )
    
    success = job_services.delete_job(test_db, created_job.id)
    assert success is True
    
    job = job_services.get_job_by_id(test_db, created_job.id)
    assert job is None


def test_delete_job_not_found(test_db):
    success = job_services.delete_job(test_db, 999)
    assert success is False
