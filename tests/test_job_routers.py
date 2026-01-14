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
    create_response = client.post(
        "/jobs/",
        params={
            "title": "Developer",
            "description": "Software Developer",
            "salary": 50000
        }
    )
    job_id = create_response.json()["id"]
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
    create_response = client.post(
        "/jobs/",
        params={
            "title": "Developer",
            "description": "Software Developer",
            "salary": 50000
        }
    )
    job_id = create_response.json()["id"]
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
    create_response = client.post(
        "/jobs/",
        params={
            "title": "Developer",
            "description": "Software Developer",
            "salary": 50000
        }
    )
    job_id = create_response.json()["id"]
    response = client.delete(f"/jobs/{job_id}")
    assert response.status_code == 200
    assert response.json()["success"] is True
    get_response = client.get(f"/jobs/{job_id}")
    assert get_response.json() is None
