from main_api.services import nationality_services


def test_get_all_nationalities_empty(test_db):
    nationalities = nationality_services.get_all_nationalities(test_db)
    assert nationalities == []


def test_create_nationality(test_db):
    nationality = nationality_services.create_nationality(
        test_db, "Spain", "ES"
    )
    assert nationality.country_name == "Spain"
    assert nationality.country_code == "ES"
    assert nationality.id is not None


def test_get_all_nationalities(test_db):
    nationality_services.create_nationality(test_db, "Spain", "ES")
    nationality_services.create_nationality(test_db, "France", "FR")
    
    nationalities = nationality_services.get_all_nationalities(test_db)
    assert len(nationalities) == 2
    assert nationalities[0].country_name == "Spain"
    assert nationalities[1].country_name == "France"


def test_get_nationality_by_id(test_db):
    created_nationality = nationality_services.create_nationality(
        test_db, "Spain", "ES"
    )
    
    nationality = nationality_services.get_nationality_by_id(test_db, created_nationality.id)
    assert nationality is not None
    assert nationality.country_name == "Spain"
    assert nationality.id == created_nationality.id


def test_get_nationality_by_id_not_found(test_db):
    nationality = nationality_services.get_nationality_by_id(test_db, 999)
    assert nationality is None


def test_update_nationality(test_db):
    created_nationality = nationality_services.create_nationality(
        test_db, "Spain", "ES"
    )
    
    updated_nationality = nationality_services.update_nationality(
        test_db, created_nationality.id, country_name="Portugal", country_code="PT"
    )
    
    assert updated_nationality.country_name == "Portugal"
    assert updated_nationality.country_code == "PT"


def test_update_nationality_not_found(test_db):
    result = nationality_services.update_nationality(test_db, 999, country_name="Portugal")
    assert result is None


def test_delete_nationality(test_db):
    created_nationality = nationality_services.create_nationality(
        test_db, "Spain", "ES"
    )
    
    success = nationality_services.delete_nationality(test_db, created_nationality.id)
    assert success is True
    
    nationality = nationality_services.get_nationality_by_id(test_db, created_nationality.id)
    assert nationality is None


def test_delete_nationality_not_found(test_db):
    success = nationality_services.delete_nationality(test_db, 999)
    assert success is False
