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
    response = client.get(f"/employees/id/{employee_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "John"
    assert data["id"] == employee_id

def test_get_employee_by_id_not_found(client):
    response = client.get("/employees/id/999")
    assert response.status_code == 200
    assert response.json() is None

def test_update_employee(client):
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
    response = client.delete(f"/employees/{employee_id}")
    assert response.status_code == 200
    assert response.json()["success"] is True
    get_response = client.get(f"/employees/id/{employee_id}")
    assert get_response.json() is None
