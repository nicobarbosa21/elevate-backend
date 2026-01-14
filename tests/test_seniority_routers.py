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
    create_response = client.post(
        "/seniorities/",
        params={
            "level": "Senior",
            "description": "Senior Developer"
        }
    )
    seniority_id = create_response.json()["id"]
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
    create_response = client.post(
        "/seniorities/",
        params={
            "level": "Senior",
            "description": "Senior Developer"
        }
    )
    seniority_id = create_response.json()["id"]
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
    create_response = client.post(
        "/seniorities/",
        params={
            "level": "Senior",
            "description": "Senior Developer"
        }
    )
    seniority_id = create_response.json()["id"]
    response = client.delete(f"/seniorities/{seniority_id}")
    assert response.status_code == 200
    assert response.json()["success"] is True
    get_response = client.get(f"/seniorities/{seniority_id}")
    assert get_response.json() is None
