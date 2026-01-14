import pytest
from unittest.mock import patch, MagicMock
from harry_potter_api import api_methods as harry_potter

@patch('harry_potter_api.api_methods.get')
def test_get_all_books(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = [{"id": 1, "title": "Philosopher's Stone"}]
    mock_get.return_value = mock_response
    result = harry_potter.get_all_books()
    assert isinstance(result, list)
    mock_get.assert_called_once_with("https://potterapi-fedeperin.vercel.app/en/books")

@patch('harry_potter_api.api_methods.get')
def test_search_books_by_title(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = [{"id": 1, "title": "Philosopher's Stone"}]
    mock_get.return_value = mock_response
    result = harry_potter.search_books_by_title("Philosopher")
    assert isinstance(result, list)
    mock_get.assert_called_once_with("https://potterapi-fedeperin.vercel.app/en/books?search=Philosopher")

@patch('harry_potter_api.api_methods.get')
def test_get_all_characters(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = [{"id": 1, "name": "Harry Potter"}]
    mock_get.return_value = mock_response
    result = harry_potter.get_all_characters()
    assert isinstance(result, list)
    mock_get.assert_called_once_with("https://potterapi-fedeperin.vercel.app/en/characters")

@patch('harry_potter_api.api_methods.get')
def test_search_characters_by_name(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = [{"id": 1, "name": "Harry Potter"}]
    mock_get.return_value = mock_response
    result = harry_potter.search_characters_by_name("Harry")
    assert isinstance(result, list)
    mock_get.assert_called_once_with("https://potterapi-fedeperin.vercel.app/en/characters?search=Harry")

@patch('harry_potter_api.api_methods.get')
def test_get_all_spells(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = [{"id": 1, "name": "Expelliarmus"}]
    mock_get.return_value = mock_response
    result = harry_potter.get_all_spells()
    assert isinstance(result, list)
    mock_get.assert_called_once_with("https://potterapi-fedeperin.vercel.app/en/spells")

@patch('harry_potter_api.api_methods.get')
def test_search_spells_by_name(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = [{"id": 1, "name": "Expelliarmus"}]
    mock_get.return_value = mock_response
    result = harry_potter.search_spells_by_name("Expelliarmus")
    assert isinstance(result, list)
    mock_get.assert_called_once_with("https://potterapi-fedeperin.vercel.app/en/spells?search=Expelliarmus")
